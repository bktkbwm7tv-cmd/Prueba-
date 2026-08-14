import Foundation
import SwiftData
import ArgosCore

/// Buscador global (sección 18). Recorre todos los ítems de todos los casos
/// autorizados e indexa nombre, notas, etiquetas, texto OCR (cuando exista)
/// y metadatos — la lógica de coincidencia en sí vive en
/// `ArgosCore.SearchIndex` para poder probarse sin SwiftData.
struct SearchService {
    let context: ModelContext

    func search(query: String) throws -> [SearchMatch] {
        guard !query.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else { return [] }

        let items = try context.fetch(FetchDescriptor<ItemEntity>())
        let documents = items.map(Self.document(for:))
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
            id: item.itemId.uuidString,
            caseCode: item.caseArgosCode,
            argosId: item.argosIdentifier,
            fields: fields
        )
    }
}
