import SwiftUI
import SwiftData
import ArgosCore

/// Buscador global (sección 18): localiza coincidencias en nombre, notas,
/// etiquetas, texto OCR, metadatos y mensajes de chats importados, en
/// todos los casos autorizados.
struct SearchView: View {
    @Environment(\.modelContext) private var context
    @State private var query = ""
    @State private var results: [SearchMatch] = []
    @State private var itemsByID: [String: ItemEntity] = [:]
    @State private var messagesByID: [String: MessageEntity] = [:]

    var body: some View {
        VStack {
            HStack {
                Image(systemName: "magnifyingglass").foregroundStyle(ArgosTheme.textSecondary)
                TextField("Buscar en ARGOS — nombre, teléfono, placa, persona…", text: $query)
                    .textFieldStyle(.plain)
                    .foregroundStyle(ArgosTheme.textPrimary)
                    .onSubmit(runSearch)
                    .onChange(of: query) { _, _ in runSearch() }
            }
            .padding(10)
            .background(ArgosTheme.surfaceElevated, in: RoundedRectangle(cornerRadius: 10))
            .padding()

            if query.isEmpty {
                Spacer()
            } else if results.isEmpty {
                ContentUnavailableView.search(text: query)
                    .foregroundStyle(ArgosTheme.textSecondary)
                Spacer()
            } else {
                List {
                    Section("\(results.count) coincidencias") {
                        ForEach(results, id: \.document.id) { match in
                            resultLink(for: match)
                        }
                    }
                    .listRowBackground(ArgosTheme.surface)
                }
                .scrollContentBackground(.hidden)
            }
        }
        .navigationTitle("Buscar en ARGOS")
        .argosBackground()
    }

    @ViewBuilder
    private func resultLink(for match: SearchMatch) -> some View {
        if let item = itemsByID[match.document.id] {
            NavigationLink {
                ItemDetailView(item: item)
            } label: {
                itemRow(item: item)
            }
        } else if let message = messagesByID[match.document.id] {
            if let chat = message.chatRef {
                NavigationLink {
                    ChatDetailView(chat: chat)
                } label: {
                    messageRow(message: message)
                }
            } else {
                messageRow(message: message)
            }
        }
    }

    private func itemRow(item: ItemEntity) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text("Caso \(item.caseArgosCode)")
                .font(.caption).foregroundStyle(ArgosTheme.cyan)
            Text(item.originalFilename).foregroundStyle(ArgosTheme.textPrimary)
            Text(item.argosIdentifier)
                .font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
        }
    }

    private func messageRow(message: MessageEntity) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text("Caso \(message.caseArgosCode) · \(message.chatRef?.chatName ?? "Mensaje")")
                .font(.caption).foregroundStyle(ArgosTheme.cyan)
            Text(message.body ?? "(sin texto)")
                .foregroundStyle(ArgosTheme.textPrimary)
                .lineLimit(2)
            Text(message.sender ?? "Sistema")
                .font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
        }
    }

    private func runSearch() {
        do {
            let service = SearchService(context: context)
            results = try service.search(query: query)
            let items = try context.fetch(FetchDescriptor<ItemEntity>())
            itemsByID = Dictionary(uniqueKeysWithValues: items.map { (SearchService.itemDocumentID($0), $0) })
            let messages = try context.fetch(FetchDescriptor<MessageEntity>())
            messagesByID = Dictionary(uniqueKeysWithValues: messages.map { (SearchService.messageDocumentID($0), $0) })
        } catch {
            results = []
        }
    }
}
