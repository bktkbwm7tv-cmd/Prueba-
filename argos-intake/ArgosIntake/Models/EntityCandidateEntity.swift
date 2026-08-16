import Foundation
import SwiftData
import ArgosCore

/// Una entidad propuesta por ARGOS EXTRACT (sección 13) — nunca un hecho.
/// El estado de verificación es el mismo vocabulario de la sección 30
/// (RECIBIDO / VERIFICADO / NO VERIFICADO / DESCARTADO): así una entidad
/// "detectada" y una "confirmada por el analista" son, explícitamente,
/// dos cosas distintas en el modelo — la separación EXTRACCIÓN AUTOMÁTICA
/// vs. VALIDACIÓN HUMANA de la sección 29 no depende de que la interfaz lo
/// recuerde, está en el dato.
@Model
final class EntityCandidateEntity {
    @Attribute(.unique) var id: UUID

    var caseArgosCode: String
    var itemRef: ItemEntity?

    var categoryRaw: String
    /// Etiqueta específica ("RFC", "Teléfono", "Nombre de persona"...).
    var label: String
    var value: String
    var context: String

    /// De dónde salió el texto analizado: "Texto OCR", "Nota", etc. —
    /// trazabilidad de la fuente, no solo del archivo (sección 13/30).
    var sourceLabel: String

    var statusRaw: String
    var detectedAt: Date
    var reviewedAt: Date?
    var reviewedBy: String?

    var category: EntityCategory {
        get { EntityCategory(rawValue: categoryRaw) ?? .identificador }
        set { categoryRaw = newValue.rawValue }
    }

    var status: VerificationStatus {
        get { VerificationStatus(rawValue: statusRaw) ?? .recibido }
        set { statusRaw = newValue.rawValue }
    }

    init(caseArgosCode: String, candidate: ExtractedEntityCandidate, sourceLabel: String) {
        self.id = UUID()
        self.caseArgosCode = caseArgosCode.uppercased()
        self.categoryRaw = candidate.category.rawValue
        self.label = candidate.label
        self.value = candidate.value
        self.context = candidate.context
        self.sourceLabel = sourceLabel
        self.statusRaw = VerificationStatus.recibido.rawValue
        self.detectedAt = Date()
        self.reviewedAt = nil
        self.reviewedBy = nil
    }
}
