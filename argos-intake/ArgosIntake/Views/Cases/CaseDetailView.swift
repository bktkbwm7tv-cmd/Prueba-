import SwiftUI
import SwiftData
import ArgosCore

/// Expediente de un caso: ficha maestra (sección 8) + sus ítems agrupados
/// por la estructura lógica de la sección 7. Esa estructura es virtual —
/// se deriva agrupando `ItemEntity.type`, no carpetas físicas separadas.
struct CaseDetailView: View {
    @Bindable var caseEntity: CaseEntity

    private var itemsByType: [(ItemType, [ItemEntity])] {
        Dictionary(grouping: caseEntity.items, by: \.type)
            .sorted { $0.key.rawValue < $1.key.rawValue }
    }

    var body: some View {
        List {
            Section("Ficha del caso") {
                LabeledContent("Código ARGOS", value: caseEntity.argosCaseCode)
                LabeledContent("Estatus", value: caseEntity.estatus.rawValue)
                LabeledContent("Prioridad", value: caseEntity.prioridad.rawValue)
                if let folio = caseEntity.folioInvestigacion {
                    LabeledContent("Folio de investigación", value: folio)
                }
                if let responsable = caseEntity.responsable {
                    LabeledContent("Responsable", value: responsable)
                }
                if let descripcion = caseEntity.descripcionBreve, !descripcion.isEmpty {
                    Text(descripcion).foregroundStyle(ArgosTheme.textSecondary)
                }
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Herramientas") {
                NavigationLink {
                    CaseMapView(caseEntity: caseEntity)
                } label: {
                    Label("Mapa del caso", systemImage: "map")
                }
                NavigationLink {
                    CaseTimelineView(caseEntity: caseEntity)
                } label: {
                    Label("Timeline ARGOS", systemImage: "clock.arrow.circlepath")
                }
            }
            .listRowBackground(ArgosTheme.surface)

            if !caseEntity.chatImports.isEmpty {
                Section("Conversaciones importadas (\(caseEntity.chatImports.count))") {
                    ForEach(caseEntity.chatImports.sorted(by: { $0.importedAt > $1.importedAt }), id: \.persistentModelID) { chat in
                        NavigationLink {
                            ChatDetailView(chat: chat)
                        } label: {
                            VStack(alignment: .leading) {
                                Text(chat.chatName).foregroundStyle(ArgosTheme.textPrimary)
                                Text("\(chat.messageCount) mensajes · \(chat.participants.count) participantes")
                                    .font(.caption).foregroundStyle(ArgosTheme.textSecondary)
                            }
                        }
                    }
                }
                .listRowBackground(ArgosTheme.surface)
            }

            ForEach(itemsByType, id: \.0) { type, items in
                Section("\(type.logicalFolder) (\(items.count))") {
                    ForEach(items.sorted(by: { $0.importedAt > $1.importedAt })) { item in
                        NavigationLink {
                            ItemDetailView(item: item)
                        } label: {
                            VStack(alignment: .leading) {
                                Text(item.originalFilename).foregroundStyle(ArgosTheme.textPrimary)
                                Text(item.argosIdentifier)
                                    .font(.caption).foregroundStyle(ArgosTheme.textSecondary)
                            }
                        }
                    }
                }
                .listRowBackground(ArgosTheme.surface)
            }

            if caseEntity.items.isEmpty && caseEntity.chatImports.isEmpty {
                Text("Este caso aún no tiene elementos. Usa \"Guardar en ARGOS\" desde WhatsApp, importa un chat, o la Captura Rápida.")
                    .foregroundStyle(ArgosTheme.textSecondary)
                    .listRowBackground(ArgosTheme.surface)
            }
        }
        .scrollContentBackground(.hidden)
        .navigationTitle(caseEntity.name)
    }
}
