import Foundation

/// Un documento indexable para el buscador global (sección 18). El servicio
/// de la app construye uno de estos por ITEM a partir de sus campos
/// (nombre, notas, etiquetas, texto OCR, entidades) — este tipo no conoce
/// SwiftData, solo texto, para poder probarse de forma aislada.
public struct SearchDocument: Sendable {
    public let id: String
    public let caseCode: String
    public let argosId: String
    public let fields: [String]

    public init(id: String, caseCode: String, argosId: String, fields: [String]) {
        self.id = id
        self.caseCode = caseCode
        self.argosId = argosId
        self.fields = fields
    }

    fileprivate var normalizedFields: [String] {
        fields.map(SearchIndex.normalize)
    }
}

public struct SearchMatch: Sendable {
    public let document: SearchDocument
    /// Número de campos distintos en los que hubo coincidencia; usado para
    /// ordenar resultados sin pretender ser un score de relevancia real.
    public let matchedFieldCount: Int
}

/// Búsqueda simple por substring, insensible a mayúsculas y acentos, sobre
/// nombres, texto OCR, metadatos, etiquetas, notas y entidades extraídas
/// (sección 18). No es un motor de relevancia — es deliberadamente literal
/// y auditable: lo que coincide es exactamente lo que el analista ve.
public enum SearchIndex {
    public static func normalize(_ text: String) -> String {
        text.folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current)
    }

    public static func search(query: String, in documents: [SearchDocument]) -> [SearchMatch] {
        let needle = normalize(query).trimmingCharacters(in: .whitespacesAndNewlines)
        guard !needle.isEmpty else { return [] }

        var matches: [SearchMatch] = []
        for document in documents {
            let hitCount = document.normalizedFields.filter { $0.contains(needle) }.count
            if hitCount > 0 {
                matches.append(SearchMatch(document: document, matchedFieldCount: hitCount))
            }
        }
        return matches.sorted { $0.matchedFieldCount > $1.matchedFieldCount }
    }
}
