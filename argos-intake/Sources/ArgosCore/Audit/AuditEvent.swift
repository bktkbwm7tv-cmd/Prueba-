import Foundation

/// Catálogo cerrado de acciones auditables (sección 11). Usar un enum en
/// lugar de String evita que la bitácora acumule variantes de redacción
/// libre a lo largo del tiempo, lo que rompería la consultabilidad exigida
/// en la sección 12.
public enum AuditAction: String, Codable, CaseIterable, Sendable {
    case importacion = "IMPORTACIÓN"
    case apertura = "APERTURA"
    case clasificacion = "CLASIFICACIÓN"
    case cambioDeCategoria = "CAMBIO DE CATEGORÍA"
    case generacionDeCopia = "GENERACIÓN DE COPIA"
    case extraccionDeTexto = "EXTRACCIÓN DE TEXTO"
    case transcripcion = "TRANSCRIPCIÓN"
    case exportacion = "EXPORTACIÓN"
    case eliminacionAutorizada = "ELIMINACIÓN AUTORIZADA"
    case cambioDeMetadatosAdministrativos = "CAMBIO DE METADATOS ADMINISTRATIVOS"
}

/// Un renglón inmutable de la bitácora (sección 12). Cada entrada, una vez
/// escrita, no se edita: correcciones posteriores se registran como una
/// nueva entrada, nunca sobrescribiendo la anterior.
public struct AuditLogEntry: Codable, Hashable, Sendable, Identifiable {
    public let id: UUID
    public let timestamp: Date
    public let user: String
    public let action: AuditAction
    public let caseCode: String?
    public let itemFilename: String?
    public let sha256: String?
    public let detail: String?

    public init(
        id: UUID = UUID(),
        timestamp: Date = Date(),
        user: String,
        action: AuditAction,
        caseCode: String? = nil,
        itemFilename: String? = nil,
        sha256: String? = nil,
        detail: String? = nil
    ) {
        self.id = id
        self.timestamp = timestamp
        self.user = user
        self.action = action
        self.caseCode = caseCode
        self.itemFilename = itemFilename
        self.sha256 = sha256
        self.detail = detail
    }

    /// Formato de línea legible tal como lo ilustra la sección 12 del
    /// instructivo (fecha/hora, usuario, acción, caso, archivo, hash).
    public func formattedLine(dateFormatter: DateFormatter) -> String {
        var lines = [dateFormatter.string(from: timestamp)]
        lines.append("Usuario: \(user)")
        lines.append("Acción: \(action.rawValue)")
        if let caseCode { lines.append("Caso: \(caseCode)") }
        if let itemFilename { lines.append("Archivo: \(itemFilename)") }
        if let sha256 { lines.append("Hash: \(sha256)") }
        if let detail { lines.append(detail) }
        return lines.joined(separator: "\n")
    }
}
