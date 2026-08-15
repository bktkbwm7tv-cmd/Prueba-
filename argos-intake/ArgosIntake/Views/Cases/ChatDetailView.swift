import SwiftUI
import SwiftData
import ArgosCore

/// Reconstrucción de una conversación importada (sección 5): mensajes en
/// orden, con remitente, fecha/hora y adjuntos vinculados a su propia
/// ficha de archivo cuando el paquete los incluía.
struct ChatDetailView: View {
    @Bindable var chat: ChatImportEntity

    private var orderedMessages: [MessageEntity] {
        chat.messages.sorted { $0.sequenceIndex < $1.sequenceIndex }
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
