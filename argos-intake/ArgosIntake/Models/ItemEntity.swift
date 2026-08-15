import Foundation
import SwiftData
import ArgosCore

/// Un elemento incorporado a ARGOS (sección 39 — ITEM). Los nombres de
/// propiedad siguen el modelo mínimo del instructivo (item_id, case_id,
/// type, subtype, original_filename, ...) traducido a camelCase de Swift.
///
/// Regla de arquitectura (sección 40): `originalRelativePath` apunta
/// siempre al archivo intacto tal como se importó; cualquier derivado
/// (preview, OCR, miniatura) vive en una ruta distinta y nunca sobrescribe
/// el original ni su hash.
@Model
final class ItemEntity {
    @Attribute(.unique) var itemId: UUID

    /// Identificador ARGOS legible y trazable, p. ej. "ARGOS-CFE-2026-IMG-000123".
    @Attribute(.unique) var argosIdentifier: String
    var sequenceInCaseTypeYear: Int

    var caseArgosCode: String
    var typeRaw: String
    var subtypeRaw: String?

    var originalFilename: String
    var storedFilename: String
    var fileExtension: String
    var mimeType: String?
    var sizeBytes: Int64
    var sha256: String

    var createdAt: Date
    var importedAt: Date

    /// Fuente de ingesta: "Share Extension", "Importación de chat",
    /// "Captura rápida", "Importación manual", etc.
    var source: String
    var sourceChat: String?
    var sourceSender: String?

    var notes: String?

    var verificationStatusRaw: String
    var classificationStatusRaw: String
    var inboxStatusRaw: String

    /// Ruta relativa (dentro del contenedor de la app) al archivo original
    /// preservado — nunca al derivado.
    var originalRelativePath: String
    var previewRelativePath: String?

    /// Texto extraído por OCR (sección 14), cacheado aquí para que
    /// `SearchService` lo indexe sin releer el derivado en cada búsqueda.
    /// El derivado en sí (la fuente de verdad, auditable) vive en
    /// `ocrRelativePath` — nunca se escribe sobre el original.
    var ocrText: String?
    var ocrRelativePath: String?
    /// Confianza promedio que reporta Vision, 0.0–1.0. `nil` cuando el
    /// texto vino de la capa de texto embebida de un PDF (no hay
    /// "confianza" que reportar ahí: es texto exacto, no reconocido).
    var ocrConfidence: Double?

    var latitude: Double?
    var longitude: Double?

    var caseRef: CaseEntity?

    @Relationship(deleteRule: .nullify, inverse: \TagEntity.items)
    var tags: [TagEntity] = []

    var type: ItemType {
        get { ItemType(rawValue: typeRaw) ?? .other }
        set { typeRaw = newValue.rawValue }
    }

    var subtype: ItemSubtype? {
        get { subtypeRaw.flatMap(ItemSubtype.init(rawValue:)) }
        set { subtypeRaw = newValue?.rawValue }
    }

    var verificationStatus: VerificationStatus {
        get { VerificationStatus(rawValue: verificationStatusRaw) ?? .recibido }
        set { verificationStatusRaw = newValue.rawValue }
    }

    var classificationStatus: ClassificationStatus {
        get { ClassificationStatus(rawValue: classificationStatusRaw) ?? .sinClasificar }
        set { classificationStatusRaw = newValue.rawValue }
    }

    var inboxStatus: InboxStatus {
        get { InboxStatus(rawValue: inboxStatusRaw) ?? .pendiente }
        set { inboxStatusRaw = newValue.rawValue }
    }

    init(
        argosIdentifier: ArgosIdentifier,
        caseArgosCode: String,
        type: ItemType,
        subtype: ItemSubtype?,
        originalFilename: String,
        storedFilename: String,
        fileExtension: String,
        mimeType: String?,
        sizeBytes: Int64,
        sha256: String,
        source: String,
        originalRelativePath: String
    ) {
        self.itemId = UUID()
        self.argosIdentifier = argosIdentifier.description
        self.sequenceInCaseTypeYear = argosIdentifier.sequence
        self.caseArgosCode = caseArgosCode.uppercased()
        self.typeRaw = type.rawValue
        self.subtypeRaw = subtype?.rawValue
        self.originalFilename = originalFilename
        self.storedFilename = storedFilename
        self.fileExtension = fileExtension
        self.mimeType = mimeType
        self.sizeBytes = sizeBytes
        self.sha256 = sha256
        self.createdAt = Date()
        self.importedAt = Date()
        self.source = source
        self.sourceChat = nil
        self.sourceSender = nil
        self.notes = nil
        self.verificationStatusRaw = VerificationStatus.recibido.rawValue
        self.classificationStatusRaw = ClassificationStatus.autoClasificado.rawValue
        self.inboxStatusRaw = InboxStatus.pendiente.rawValue
        self.originalRelativePath = originalRelativePath
        self.previewRelativePath = nil
        self.ocrText = nil
        self.ocrRelativePath = nil
        self.ocrConfidence = nil
        self.latitude = nil
        self.longitude = nil
    }
}
