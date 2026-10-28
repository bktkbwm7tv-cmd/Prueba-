import Foundation
import SwiftData
import ArgosCore

/// Persistencia SwiftData de la bitácora de auditoría (sección 12). Cada
/// instancia se crea a partir de un `AuditLogEntry` (ArgosCore) y nunca se
/// muta después de guardarse — `AuditLogService` solo inserta, no edita.
@Model
final class AuditLogEntity {
    @Attribute(.unique) var id: UUID
    var timestamp: Date
    var user: String
    var actionRaw: String
    var caseCode: String?
    var itemFilename: String?
    var sha256: String?
    var detail: String?

    var action: AuditAction {
        AuditAction(rawValue: actionRaw) ?? .cambioDeMetadatosAdministrativos
    }

    init(entry: AuditLogEntry) {
        self.id = entry.id
        self.timestamp = entry.timestamp
        self.user = entry.user
        self.actionRaw = entry.action.rawValue
        self.caseCode = entry.caseCode
        self.itemFilename = entry.itemFilename
        self.sha256 = entry.sha256
        self.detail = entry.detail
    }

    var asAuditLogEntry: AuditLogEntry {
        AuditLogEntry(
            id: id, timestamp: timestamp, user: user, action: action,
            caseCode: caseCode, itemFilename: itemFilename, sha256: sha256, detail: detail
        )
    }
}
