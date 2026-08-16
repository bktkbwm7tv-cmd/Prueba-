import Foundation
import SwiftData
import ArgosCore

/// Orquesta ARGOS EXTRACT (sección 13) sobre un ítem: corre los
/// detectores de patrón (`ArgosCore.EntityExtractor`) y de nombres
/// (`PersonNameExtractor`) sobre cada fuente de texto disponible — texto
/// OCR y notas del analista — y crea una propuesta (`EntityCandidateEntity`)
/// por cada hallazgo nuevo. No reevalúa duplicados ya propuestos para el
/// mismo ítem, para que volver a correr la extracción no reviva algo que
/// el analista ya descartó ni duplique lo que ya confirmó.
///
/// El resultado siempre entra como propuesta (`VerificationStatus.recibido`)
/// — nunca como hecho. Confirmar o rechazar es una acción humana separada.
struct EntityExtractionService {
    let context: ModelContext
    let currentUser: String

    @discardableResult
    func extractEntities(for item: ItemEntity) -> [EntityCandidateEntity] {
        var sources: [(text: String, label: String)] = []
        if let ocrText = item.ocrText, !ocrText.isEmpty { sources.append((ocrText, "Texto OCR")) }
        if let notes = item.notes, !notes.isEmpty { sources.append((notes, "Nota")) }
        guard !sources.isEmpty else { return [] }

        let nameExtractor = PersonNameExtractor()
        var seenKeys = Set(item.entityCandidates.map(Self.dedupeKey))

        var created: [EntityCandidateEntity] = []
        for source in sources {
            let candidates = EntityExtractor.extract(from: source.text) + nameExtractor.extract(from: source.text)
            for candidate in candidates {
                let key = "\(candidate.category.rawValue):\(candidate.label):\(candidate.value.lowercased())"
                guard !seenKeys.contains(key) else { continue }
                seenKeys.insert(key)

                let entity = EntityCandidateEntity(
                    caseArgosCode: item.caseArgosCode, candidate: candidate, sourceLabel: source.label
                )
                entity.itemRef = item
                context.insert(entity)
                created.append(entity)
            }
        }

        if !created.isEmpty {
            AuditLogService(context: context).record(
                user: currentUser,
                action: .extraccionDeTexto,
                caseCode: item.caseArgosCode,
                itemFilename: item.originalFilename,
                sha256: item.sha256,
                detail: "ARGOS EXTRACT: \(created.count) entidad(es) propuesta(s), pendientes de validación"
            )
        }

        return created
    }

    private static func dedupeKey(_ entity: EntityCandidateEntity) -> String {
        "\(entity.categoryRaw):\(entity.label):\(entity.value.lowercased())"
    }
}
