import SwiftUI
import SwiftData
import ArgosCore

/// Timeline ARGOS (sección 17): mezcla cronológicamente ítems y mensajes de
/// chats importados de un caso, agrupados por día. Los ítems usan
/// `importedAt` como fecha del evento — es la mejor aproximación
/// disponible sin metadatos EXIF/de captura, que MVP2 todavía no lee. Los
/// mensajes usan su propio `timestamp` (la fecha real de envío en
/// WhatsApp), que es más preciso. Un mensaje cuya fecha no pudo
/// interpretarse (ver `WhatsAppChatParser`) no aparece — omitirlo es mejor
/// que inventarle una fecha.
struct CaseTimelineView: View {
    let caseEntity: CaseEntity

    @State private var typeFilter: TypeFilter = .todos
    @State private var tagCategoryFilter: TagCategory?
    @State private var sourceFilter: String = ""

    private enum TypeFilter: Hashable {
        case todos
        case soloMensajes
        case tipo(ItemType)
    }

    private struct Entry: Identifiable {
        let id: String
        let date: Date
        let title: String
        let subtitle: String
        let symbolName: String
        let destination: Destination
    }

    private enum Destination {
        case item(ItemEntity)
        case message(MessageEntity, ChatImportEntity)
    }

    private var allEntries: [Entry] {
        let itemEntries: [Entry] = caseEntity.items.map { item in
            Entry(
                id: "item-\(item.itemId.uuidString)",
                date: item.importedAt,
                title: item.originalFilename,
                subtitle: "\(item.type.displayName) · \(item.source)",
                symbolName: item.type.symbolName,
                destination: .item(item)
            )
        }

        let messageEntries: [Entry] = caseEntity.chatImports.flatMap { chat in
            chat.messages.compactMap { message -> Entry? in
                guard let timestamp = message.timestamp else { return nil }
                let sender = message.isSystemEvent ? "Sistema" : (message.sender ?? "Desconocido")
                return Entry(
                    id: "msg-\(message.id.uuidString)",
                    date: timestamp,
                    title: message.body ?? message.attachmentFilename ?? "(sin texto)",
                    subtitle: "\(sender) · \(chat.chatName)",
                    symbolName: "message",
                    destination: .message(message, chat)
                )
            }
        }

        return itemEntries + messageEntries
    }

    private var filteredEntries: [Entry] {
        allEntries.filter { entry in
            guard matchesType(entry) else { return false }
            guard matchesTagCategory(entry) else { return false }
            guard matchesSource(entry) else { return false }
            return true
        }
        .sorted { $0.date < $1.date }
    }

    private func matchesType(_ entry: Entry) -> Bool {
        switch typeFilter {
        case .todos: return true
        case .soloMensajes:
            if case .message = entry.destination { return true }
            return false
        case .tipo(let type):
            if case .item(let item) = entry.destination { return item.type == type }
            return false
        }
    }

    /// Los mensajes no llevan etiquetas (sección 4 solo las define para
    /// ítems), así que un filtro de etiqueta activo los excluye — no hay
    /// forma honesta de evaluarlos contra ese criterio.
    private func matchesTagCategory(_ entry: Entry) -> Bool {
        guard let tagCategoryFilter else { return true }
        guard case .item(let item) = entry.destination else { return false }
        return item.tags.contains { $0.category == tagCategoryFilter }
    }

    private func matchesSource(_ entry: Entry) -> Bool {
        guard !sourceFilter.trimmingCharacters(in: .whitespaces).isEmpty else { return true }
        let needle = sourceFilter.lowercased()
        switch entry.destination {
        case .item(let item): return item.source.lowercased().contains(needle)
        case .message: return "importación de chat".contains(needle)
        }
    }

    private var entriesByDay: [(Date, [Entry])] {
        let grouped = Dictionary(grouping: filteredEntries) { Calendar.current.startOfDay(for: $0.date) }
        return grouped.sorted { $0.key < $1.key }
    }

    private let dayFormatter: DateFormatter = {
        let f = DateFormatter()
        f.locale = Locale(identifier: "es_MX")
        f.dateFormat = "d MMM yyyy"
        return f
    }()

    private let timeFormatter: DateFormatter = {
        let f = DateFormatter()
        f.dateFormat = "HH:mm"
        return f
    }()

    var body: some View {
        VStack(spacing: 0) {
            filterBar

            if filteredEntries.isEmpty {
                ContentUnavailableView(
                    "Sin eventos",
                    systemImage: "clock",
                    description: Text("No hay elementos o mensajes con fecha que coincidan con estos filtros.")
                )
                .foregroundStyle(ArgosTheme.textSecondary)
            } else {
                List {
                    ForEach(entriesByDay, id: \.0) { day, entries in
                        Section(dayFormatter.string(from: day).uppercased()) {
                            ForEach(entries) { entry in
                                NavigationLink {
                                    destinationView(for: entry)
                                } label: {
                                    HStack(alignment: .top, spacing: 10) {
                                        Text(timeFormatter.string(from: entry.date))
                                            .font(.caption.monospaced())
                                            .foregroundStyle(ArgosTheme.cyan)
                                            .frame(width: 44, alignment: .leading)
                                        Image(systemName: entry.symbolName)
                                            .foregroundStyle(ArgosTheme.textSecondary)
                                            .frame(width: 18)
                                        VStack(alignment: .leading, spacing: 2) {
                                            Text(entry.title).foregroundStyle(ArgosTheme.textPrimary).lineLimit(2)
                                            Text(entry.subtitle).font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
                                        }
                                    }
                                }
                            }
                        }
                        .listRowBackground(ArgosTheme.surface)
                    }
                }
                .scrollContentBackground(.hidden)
            }
        }
        .navigationTitle("Timeline — \(caseEntity.name)")
        .argosBackground()
    }

    @ViewBuilder
    private func destinationView(for entry: Entry) -> some View {
        switch entry.destination {
        case .item(let item): ItemDetailView(item: item)
        case .message(_, let chat): ChatDetailView(chat: chat)
        }
    }

    private var filterBar: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Menu {
                    Button("Todos") { typeFilter = .todos }
                    Button("Solo mensajes") { typeFilter = .soloMensajes }
                    ForEach(ItemType.allCases, id: \.self) { type in
                        Button(type.displayName) { typeFilter = .tipo(type) }
                    }
                } label: {
                    Label(typeFilterLabel, systemImage: "line.3.horizontal.decrease.circle")
                }

                Menu {
                    Button("Todas") { tagCategoryFilter = nil }
                    ForEach([TagCategory.persona, .telefono, .vehiculo, .ubicacion], id: \.self) { category in
                        Button(category.displayName) { tagCategoryFilter = category }
                    }
                } label: {
                    Label(tagCategoryFilter?.displayName ?? "Etiqueta", systemImage: "tag")
                }

                Spacer()
            }
            .font(.caption)

            TextField("Filtrar por fuente…", text: $sourceFilter)
                .textFieldStyle(.roundedBorder)
                .font(.caption)
        }
        .padding()
    }

    private var typeFilterLabel: String {
        switch typeFilter {
        case .todos: return "Todos"
        case .soloMensajes: return "Solo mensajes"
        case .tipo(let type): return type.displayName
        }
    }
}
