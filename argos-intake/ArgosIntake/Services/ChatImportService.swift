import Foundation
import SwiftData
import ZIPFoundation
import ArgosCore

enum ChatImportError: Error {
    case archiveUnreadable
    case noChatTextFound
}

/// Segunda modalidad de ingesta (sección 5): "Importar chat de WhatsApp".
/// El usuario exporta un chat desde WhatsApp, con o sin multimedia
/// (`.txt` suelto o `.zip`), y este servicio:
///
/// 1. preserva el paquete original tal como llegó;
/// 2. si es `.zip`, lo extrae a un directorio de trabajo temporal para leer
///    el `.txt` y localizar los adjuntos — la extracción no es una
///    modificación del original: el `.zip` preservado en el paso 1 sigue
///    intacto y es la evidencia de referencia;
/// 3. parsea el texto con `ArgosCore.WhatsAppChatParser`;
/// 4. crea la conversación (`ChatImportEntity`) y un `MessageEntity` por
///    mensaje, vinculando cada adjunto localizado a su propio `ItemEntity`
///    — con hash e ID ARGOS independientes — a través del mismo
///    `IngestionService` que usa el resto de la app, para que la cadena
///    archivo → mensaje → conversación → importación → caso sea completa
///    y auditable.
struct ChatImportService {
    let context: ModelContext
    let storage: FileStorageService
    let currentUser: String

    init(context: ModelContext, storage: FileStorageService = FileStorageService(), currentUser: String) {
        self.context = context
        self.storage = storage
        self.currentUser = currentUser
    }

    @discardableResult
    func importChat(
        fileAt sourceURL: URL,
        originalFilename: String,
        into caseEntity: CaseEntity,
        chatNameOverride: String? = nil
    ) throws -> ChatImportEntity {
        let ingestion = IngestionService(context: context, storage: storage, currentUser: currentUser)

        // 1. Preservar el paquete tal como llegó, antes de tocar su contenido.
        let packageItem = try ingestion.ingest(
            fileAt: sourceURL, originalFilename: originalFilename, into: caseEntity,
            source: "Importación de chat", userSuppliedType: .message
        )

        // 2. Texto + adjuntos disponibles, según sea .txt suelto o .zip.
        let ext = (originalFilename as NSString).pathExtension.lowercased()
        let chatText: String
        var mediaFiles: [String: URL] = [:]
        var extractionWorkDir: URL?

        if ext == "zip" {
            let extracted = try Self.extractZip(at: sourceURL)
            chatText = extracted.text
            mediaFiles = extracted.media
            extractionWorkDir = extracted.workDir
        } else {
            chatText = try String(contentsOf: sourceURL, encoding: .utf8)
        }
        defer { if let extractionWorkDir { try? FileManager.default.removeItem(at: extractionWorkDir) } }

        // 3. Parsear.
        let parsed = WhatsAppChatParser.parse(chatText)

        let chatName = chatNameOverride ?? (originalFilename as NSString).deletingPathExtension
        let chat = ChatImportEntity(
            caseArgosCode: caseEntity.argosCaseCode, chatName: chatName, participants: parsed.participants
        )
        chat.caseRef = caseEntity
        chat.originalItem = packageItem
        if let range = parsed.dateRange {
            chat.dateRangeStart = range.start
            chat.dateRangeEnd = range.end
        }
        context.insert(chat)

        // 4. Materializar mensajes, vinculando adjuntos cuando el archivo
        // referenciado sí está presente en el paquete (sección 5, puntos 8 y 10).
        for (index, message) in parsed.messages.enumerated() {
            let entity = MessageEntity(
                caseArgosCode: caseEntity.argosCaseCode,
                sequenceIndex: index,
                timestamp: message.date,
                sender: message.sender,
                isSystemEvent: message.isSystemEvent,
                body: message.body.isEmpty ? nil : message.body,
                attachmentFilename: message.attachmentFilename,
                rawLine: message.rawLine
            )
            entity.chatRef = chat

            if let attachmentName = message.attachmentFilename, let mediaURL = mediaFiles[attachmentName] {
                entity.linkedItem = try? ingestion.ingest(
                    fileAt: mediaURL, originalFilename: attachmentName, into: caseEntity,
                    source: "Importación de chat", sourceChat: chatName, sourceSender: message.sender
                )
            }

            context.insert(entity)
        }

        AuditLogService(context: context).record(
            user: currentUser,
            action: .importacion,
            caseCode: caseEntity.argosCaseCode,
            itemFilename: originalFilename,
            detail: "Chat importado \"\(chatName)\": \(parsed.messages.count) mensajes, "
                + "\(parsed.participants.count) participantes, \(mediaFiles.count) adjuntos en el paquete"
        )

        return chat
    }

    private static func extractZip(at zipURL: URL) throws -> (text: String, media: [String: URL], workDir: URL) {
        guard let archive = Archive(url: zipURL, accessMode: .read) else {
            throw ChatImportError.archiveUnreadable
        }
        let workDir = FileManager.default.temporaryDirectory
            .appendingPathComponent("argos-chat-extract-\(UUID().uuidString)", isDirectory: true)
        try FileManager.default.createDirectory(at: workDir, withIntermediateDirectories: true)

        var chatText: String?
        var media: [String: URL] = [:]

        for entry in archive {
            let basename = (entry.path as NSString).lastPathComponent
            let destination = workDir.appendingPathComponent(basename)
            _ = try? archive.extract(entry, to: destination)

            if basename.lowercased().hasSuffix(".txt") {
                chatText = try? String(contentsOf: destination, encoding: .utf8)
            } else {
                media[basename] = destination
            }
        }

        guard let text = chatText else { throw ChatImportError.noChatTextFound }
        return (text, media, workDir)
    }
}
