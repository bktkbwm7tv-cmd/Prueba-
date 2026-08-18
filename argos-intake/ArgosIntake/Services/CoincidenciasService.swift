import Foundation
import SwiftData
import ArgosCore

/// Una entidad (mismo valor, misma categoría) que aparece en más de un
/// caso. Es exactamente lo que pide la sección 19: "coincidencia de
/// información susceptible de análisis" — nunca una vinculación
/// declarada. Este tipo no se persiste: se recalcula cada vez que se abre
/// `CoincidenciasView`, para que nunca pueda quedar desactualizado
/// respecto al estado real de los `EntityCandidateEntity`.
struct CoincidenceGroup: Identifiable {
    let category: EntityCategory
    let value: String
    /// Casos donde aparece, con las propuestas correspondientes en cada
    /// uno (puede haber más de una por caso: p. ej. detectada en dos
    /// ítems distintos).
    let occurrencesByCase: [(caseEntity: CaseEntity, candidates: [EntityCandidateEntity])]

    var id: String { "\(category.rawValue):\(value.lowercased())" }
    var caseCount: Int { occurrencesByCase.count }
}

/// Módulo de Coincidencias ARGOS (sección 19). Cruza las entidades ya
/// propuestas por ARGOS EXTRACT entre todos los casos autorizados — nunca
/// asegura que una coincidencia implique una vinculación criminal, eso lo
/// decide el análisis humano después de ver la lista.
///
/// Se excluyen las propuestas `DESCARTADO`: si un analista ya determinó
/// que un valor detectado no era correcto en un caso, no tiene sentido que
/// siga alimentando coincidencias en otros. `RECIBIDO` y `VERIFICADO` sí
/// se incluyen — ambos son "información", solo con distinto nivel de
/// revisión, y la sección 19 no exige que una coincidencia esté
/// previamente confirmada para mostrarse, solo que se presente como tal.
struct CoincidenciasService {
    let context: ModelContext

    func findCoincidences() throws -> [CoincidenceGroup] {
        let candidates = try context.fetch(FetchDescriptor<EntityCandidateEntity>())
            .filter { $0.status != .descartado }
        guard !candidates.isEmpty else { return [] }

        let cases = try context.fetch(FetchDescriptor<CaseEntity>())
        let caseByCode = Dictionary(uniqueKeysWithValues: cases.map { ($0.argosCaseCode, $0) })

        let normalizedKey: (EntityCandidateEntity) -> String = {
            "\($0.categoryRaw):\($0.value.lowercased().trimmingCharacters(in: .whitespaces))"
        }
        let grouped = Dictionary(grouping: candidates, by: normalizedKey)

        var groups: [CoincidenceGroup] = []
        for (_, items) in grouped {
            let byCase = Dictionary(grouping: items, by: \.caseArgosCode)
            guard byCase.keys.count > 1 else { continue }

            let occurrences: [(caseEntity: CaseEntity, candidates: [EntityCandidateEntity])] = byCase
                .compactMap { code, candidatesInCase in
                    guard let caseEntity = caseByCode[code] else { return nil }
                    return (caseEntity, candidatesInCase)
                }
                .sorted { $0.caseEntity.name < $1.caseEntity.name }

            guard occurrences.count > 1, let first = items.first else { continue }
            groups.append(CoincidenceGroup(category: first.category, value: first.value, occurrencesByCase: occurrences))
        }

        return groups.sorted { lhs, rhs in
            lhs.caseCount != rhs.caseCount ? lhs.caseCount > rhs.caseCount : lhs.value < rhs.value
        }
    }
}
