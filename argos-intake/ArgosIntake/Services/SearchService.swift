import Foundation
import SwiftData
import ArgosCore

/// Buscador global (sección 18). Recorre todos los ítems y mensajes de
/// chats importados de todos los casos autorizados, e indexa nombre,
/// notas, etiquetas, texto OCR (cuando exista) y el cuerpo de los mensajes
/// — la lógica de coincidencia en sí vive en `ArgosCore.SearchIndex` para
/// poder probarse sin SwiftData.
///
/// `SearchDocument.id` se prefija con `"item:"` o `"msg:"` porque los
/// resultados pueden apuntar a un `ItemEntity` o a un `MessageEntity`
/// dentro de una conversación — la vista de búsqueda usa el prefijo para
/// saber a qué ficha navegar.
struct SearchService {
    let context: ModelContext

    static func itemDocumentID(_ item: ItemEntity) -> String { "item:\(item.itemId.uuidString)" }
    static func messageDocumentID(_ message: MessageEntity) -> String { "msg:\(message.id.uuidString)" }

    func search(query: String) throws -> [SearchMatch] {
        guard !query.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else { return [] }

        let items = try context.fetch(FetchDescriptor<ItemEntity>())
        let messages = try context.fetch(FetchDescriptor<MessageEntity>())
        let documents = items.map(Self.document(for:)) + messages.map(Self.document(for:))
        return SearchIndex.search(query: query, in: documents)
    }

    static func document(for item: ItemEntity) -> SearchDocument {
        var fields: [String] = [
            item.originalFilename,
            item.argosIdentifier,
            item.caseArgosCode,
            item.type.displayName
        ]
        if let subtype = item.subtype { fields.append(subtype.displayName) }
        if let notes = item.notes { fields.append(notes) }
        if let ocrText = item.ocrText { fields.append(ocrText) }
        if let sourceChat = item.sourceChat { fields.append(sourceChat) }
        if let sourceSender = item.sourceSender { fields.append(sourceSender) }
        fields.append(contentsOf: item.tags.map(\.name))

        return SearchDocument(
            id: itemDocumentID(item),
            caseCode: item.caseArgosCode,
            argosId: item.argosIdentifier,
            fields: fields
        )
    }

    static func document(for message: MessageEntity) -> SearchDocument {
        var fields: [String] = [message.caseArgosCode]
        if let sender = message.sender { fields.append(sender) }
        if let body = message.body { fields.append(body) }
        if let chatName = message.chatRef?.chatName { fields.append(chatName) }
        if let attachmentFilename = message.attachmentFilename { fields.append(attachmentFilename) }

        return SearchDocument(
            id: messageDocumentID(message),
            caseCode: message.caseArgosCode,
            argosId: message.chatRef?.chatName ?? "Mensaje",
            fields: fields
        )
    }
}
