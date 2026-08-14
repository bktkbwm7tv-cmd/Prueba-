import SwiftUI
import SwiftData
import ArgosCore

/// Buscador global (sección 18): localiza coincidencias en nombre, notas,
/// etiquetas, texto OCR y metadatos de todos los casos autorizados.
struct SearchView: View {
    @Environment(\.modelContext) private var context
    @State private var query = ""
    @State private var results: [SearchMatch] = []
    @State private var itemsByID: [String: ItemEntity] = [:]

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
                            if let item = itemsByID[match.document.id] {
                                NavigationLink {
                                    ItemDetailView(item: item)
                                } label: {
                                    resultRow(match: match, item: item)
                                }
                            }
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

    private func resultRow(match: SearchMatch, item: ItemEntity) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text("Caso \(item.caseArgosCode)")
                .font(.caption).foregroundStyle(ArgosTheme.cyan)
            Text(item.originalFilename).foregroundStyle(ArgosTheme.textPrimary)
            Text(match.document.argosId)
                .font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
        }
    }

    private func runSearch() {
        do {
            let service = SearchService(context: context)
            results = try service.search(query: query)
            let items = try context.fetch(FetchDescriptor<ItemEntity>())
            itemsByID = Dictionary(uniqueKeysWithValues: items.map { ($0.itemId.uuidString, $0) })
        } catch {
            results = []
        }
    }
}
