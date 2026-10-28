import SwiftUI
import SwiftData
import UniformTypeIdentifiers
import ArgosCore

/// "Importar chat de WhatsApp" (sección 5): segunda modalidad de ingesta,
/// junto a la Share Extension. El usuario elige el `.txt` o `.zip` que
/// exportó desde WhatsApp y el caso destino; `ChatImportService` hace el
/// resto (preservar, extraer, parsear, vincular adjuntos).
struct ImportChatView: View {
    @Environment(\.modelContext) private var context
    @Environment(\.dismiss) private var dismiss
    @EnvironmentObject private var session: AppSession
    @Query(sort: \CaseEntity.name) private var cases: [CaseEntity]

    let preselectedCase: CaseEntity?

    @State private var targetCase: CaseEntity?
    @State private var showingFileImporter = false
    @State private var chatNameOverride = ""
    @State private var isImporting = false
    @State private var errorMessage: String?
    @State private var importedChat: ChatImportEntity?

    private static let allowedTypes: [UTType] = [.zip, .plainText]

    var body: some View {
        NavigationStack {
            Form {
                Section("Caso destino") {
                    Picker("Caso", selection: $targetCase) {
                        Text("Selecciona un caso").tag(CaseEntity?.none)
                        ForEach(cases.filter { $0.argosCaseCode != InboxCaseCode.value }) { c in
                            Text("\(c.name) (\(c.argosCaseCode))").tag(CaseEntity?.some(c))
                        }
                    }
                }

                Section("Archivo exportado de WhatsApp") {
                    Text("Desde WhatsApp: abre el chat → Más → Exportar chat → con o sin multimedia.")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Button {
                        showingFileImporter = true
                    } label: {
                        Label("Elegir archivo (.txt o .zip)", systemImage: "square.and.arrow.down")
                    }
                    TextField("Nombre del chat (opcional)", text: $chatNameOverride)
                }

                if let importedChat {
                    Section("Resultado") {
                        LabeledContent("Mensajes", value: "\(importedChat.messageCount)")
                        LabeledContent("Participantes", value: "\(importedChat.participants.count)")
                        NavigationLink("Ver conversación") {
                            ChatDetailView(chat: importedChat)
                        }
                    }
                }

                if let errorMessage {
                    Text(errorMessage).foregroundStyle(ArgosTheme.alertRed)
                }
            }
            .navigationTitle("Importar chat")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(importedChat == nil ? "Cancelar" : "Cerrar") { dismiss() }
                }
            }
            .disabled(isImporting)
            .onAppear { targetCase = preselectedCase }
            .fileImporter(isPresented: $showingFileImporter, allowedContentTypes: Self.allowedTypes) { result in
                handlePickedFile(result)
            }
        }
    }

    private func handlePickedFile(_ result: Result<URL, Error>) {
        guard let caseEntity = targetCase else {
            errorMessage = "Selecciona primero un caso destino."
            return
        }
        guard case .success(let url) = result else {
            errorMessage = "No se pudo leer el archivo seleccionado."
            return
        }

        let accessed = url.startAccessingSecurityScopedResource()
        defer { if accessed { url.stopAccessingSecurityScopedResource() } }

        isImporting = true
        errorMessage = nil
        let service = ChatImportService(context: context, currentUser: session.currentAnalyst)
        do {
            importedChat = try service.importChat(
                fileAt: url,
                originalFilename: url.lastPathComponent,
                into: caseEntity,
                chatNameOverride: chatNameOverride.isEmpty ? nil : chatNameOverride
            )
        } catch {
            errorMessage = "Error al importar el chat: \(error.localizedDescription)"
        }
        isImporting = false
    }
}
