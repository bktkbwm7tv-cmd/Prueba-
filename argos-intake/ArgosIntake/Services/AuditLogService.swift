import Foundation
import SwiftData
import ArgosCore

/// Escribe y consulta la bitácora de auditoría (secciones 11-12). Solo
/// inserta — nunca hay una operación de edición sobre un `AuditLogEntity`
/// existente, para que la bitácora sea "resistente a modificación
/// accidental" tal como exige el instructivo.
struct AuditLogService {
    let context: ModelContext

    @discardableResult
    func record(
        user: String,
        action: AuditAction,
        caseCode: String? = nil,
        itemFilename: String? = nil,
        sha256: String? = nil,
        detail: String? = nil
    ) -> AuditLogEntity {
        let entry = AuditLogEntry(
            user: user, action: action, caseCode: caseCode,
            itemFilename: itemFilename, sha256: sha256, detail: detail
        )
        let entity = AuditLogEntity(entry: entry)
        context.insert(entity)
        return entity
    }

    func recentEvents(limit: Int = 200) throws -> [AuditLogEntity] {
        var descriptor = FetchDescriptor<AuditLogEntity>(
            sortBy: [SortDescriptor(\.timestamp, order: .reverse)]
        )
        descriptor.fetchLimit = limit
        return try context.fetch(descriptor)
    }

    func events(forCaseCode caseCode: String) throws -> [AuditLogEntity] {
        let code = caseCode.uppercased()
        let descriptor = FetchDescriptor<AuditLogEntity>(
            predicate: #Predicate { $0.caseCode == code },
            sortBy: [SortDescriptor(\.timestamp, order: .reverse)]
        )
        return try context.fetch(descriptor)
    }
}
