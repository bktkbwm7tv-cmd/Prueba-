import SwiftUI
import SwiftData
import ArgosCore

/// Reconstrucción de una conversación importada (sección 5): mensajes en
/// orden, con remitente, fecha/hora y adjuntos vinculados a su propia
/// ficha de archivo cuando el paquete los incluía.
struct ChatDetailView: View {
    @Bindable var chat: ChatImportEntity
    @Environment(\.modelContext) private var context
    @EnvironmentObject private var session: AppSession

    @State private var isRunningExtraction = false
    @State private var extractionMessage: String?

    private var orderedMessages: [MessageEntity] {
        chat.messages.sorted { $0.sequenceIndex < $1.sequenceIndex }
    }

    private var allCandidates: [EntityCandidateEntity] {
        chat.messages.flatMap(\.entityCandidates)
    }

    private let timeFormatter: DateFormatter = {
        let f = DateFormatter()
        f.dateFormat = "dd/MM/yyyy HH:mm"
        return f
    }()

    var body: some View {
        List {
            Section("Conversación") {
                LabeledContent("Participantes", value: chat.participants.isEmpty ? "No detectados" : chat.participants.joined(separator: ", "))
                LabeledContent("Mensajes", value: "\(chat.messageCount)")
                if let start = chat.dateRangeStart, let end = chat.dateRangeEnd {
                    LabeledContent("Rango", value: "\(timeFormatter.string(from: start)) – \(timeFormatter.string(from: end))")
                }
                if let originalItem = chat.originalItem {
                    NavigationLink("Ver paquete original (\(originalItem.argosIdentifier))") {
                        ItemDetailView(item: originalItem)
                    }
                }
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Entidades detectadas (ARGOS EXTRACT)") {
                Text("Propuestas automáticas sobre el texto de los mensajes — ninguna se trata como hecho confirmado hasta que la revises.")
                    .font(.caption)
                    .foregroundStyle(ArgosTheme.textSecondary)

                EntityCandidateGroupedList(candidates: allCandidates, onConfirm: confirm, onReject: reject)

                Button {
                    Task { await runEntityExtraction() }
                } label: {
                    Label(
                        isRunningExtraction ? "Analizando…" : "Detectar entidades en la conversación",
                        systemImage: "sparkle.magnifyingglass"
                    )
                }
                .disabled(isRunningExtraction || chat.messages.isEmpty)

                if let extractionMessage {
                    Text(extractionMessage).font(.caption).foregroundStyle(ArgosTheme.textSecondary)
                }
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Mensajes") {
                ForEach(orderedMessages, id: \.persistentModelID) { message in
                    MessageRow(message: message, timeFormatter: timeFormatter)
                }
                .listRowBackground(ArgosTheme.surface)
            }
        }
        .scrollContentBackground(.hidden)
        .navigationTitle(chat.chatName)
    }

    private func runEntityExtraction() async {
        isRunningExtraction = true
        extractionMessage = nil
        defer { isRunningExtraction = false }

        let service = EntityExtractionService(context: context, currentUser: session.currentAnalyst)
        let created = service.extractEntities(forChat: chat)
        extractionMessage = created.isEmpty
            ? "No se detectaron entidades nuevas."
            : "\(created.count) entidad(es) nueva(s) propuesta(s)."
    }

    private func confirm(_ candidate: EntityCandidateEntity) {
        candidate.status = .verificado
        candidate.reviewedAt = Date()
        candidate.reviewedBy = session.currentAnalyst
        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: chat.caseArgosCode,
            itemFilename: chat.chatName,
            detail: "Entidad confirmada: \(candidate.label) \"\(candidate.value)\""
        )
    }

    private func reject(_ candidate: EntityCandidateEntity) {
        candidate.status = .descartado
        candidate.reviewedAt = Date()
        candidate.reviewedBy = session.currentAnalyst
        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: chat.caseArgosCode,
            itemFilename: chat.chatName,
            detail: "Entidad descartada: \(candidate.label) \"\(candidate.value)\""
        )
    }
}

private struct MessageRow: View {
    let message: MessageEntity
    let timeFormatter: DateFormatter

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                Text(message.isSystemEvent ? "Sistema" : (message.sender ?? "Desconocido"))
                    .font(.caption.bold())
                    .foregroundStyle(message.isSystemEvent ? ArgosTheme.textSecondary : ArgosTheme.cyan)
                Spacer()
                if let timestamp = message.timestamp {
                    Text(timeFormatter.string(from: timestamp))
                        .font(.caption2)
                        .foregroundStyle(ArgosTheme.textSecondary)
                }
            }

            if let body = message.body, !body.isEmpty {
                Text(body)
                    .font(.subheadline)
                    .foregroundStyle(message.isSystemEvent ? ArgosTheme.textSecondary : ArgosTheme.textPrimary)
                    .italic(message.isSystemEvent)
            }

            if let attachmentFilename = message.attachmentFilename {
                if let linkedItem = message.linkedItem {
                    NavigationLink {
                        ItemDetailView(item: linkedItem)
                    } label: {
                        Label(attachmentFilename, systemImage: "paperclip")
                            .font(.caption)
                    }
                } else {
                    Label("\(attachmentFilename) — no incluido en el paquete importado", systemImage: "paperclip")
                        .font(.caption)
                        .foregroundStyle(ArgosTheme.pendingYellow)
                }
            }
        }
        .padding(.vertical, 2)
    }
}
