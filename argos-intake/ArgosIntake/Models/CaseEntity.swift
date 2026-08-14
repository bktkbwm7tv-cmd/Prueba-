import Foundation
import SwiftData
import ArgosCore

/// Ficha maestra de caso (sección 8). `argosCaseCode` es el token `[CASO]`
/// usado en cada `ArgosIdentifier` de sus ítems (sección 9) — corto,
/// estable, y distinto del `id` interno (UUID) que SwiftData administra.
@Model
final class CaseEntity {
    @Attribute(.unique) var id: UUID
    /// Token corto usado en los IDs ARGOS de este caso, p. ej. "CFE".
    @Attribute(.unique) var argosCaseCode: String

    var name: String
    var folioInvestigacion: String?
    var fechaApertura: Date
    var institucion: String?
    var unidad: String?
    var responsable: String?
    var analistasAsignados: [String]
    var victimas: [String]
    var personasDeInteres: [String]
    var objetivos: String?
    var telefonosRelacionados: [String]
    var vehiculosRelacionados: [String]
    var domiciliosRelacionados: [String]
    var municipios: [String]
    var estados: [String]
    var estatusRaw: String
    var prioridadRaw: String
    var descripcionBreve: String?
    var etiquetas: [String]
    /// Imagen representativa del caso (sección 8), guardada como derivado —
    /// nunca sustituye a un ITEM de tipo imagen con su propio hash.
    @Attribute(.externalStorage) var imagenRepresentativa: Data?

    var createdAt: Date
    var updatedAt: Date

    @Relationship(deleteRule: .cascade, inverse: \ItemEntity.caseRef)
    var items: [ItemEntity] = []

    @Relationship(deleteRule: .nullify, inverse: \TagEntity.cases)
    var tags: [TagEntity] = []

    var estatus: CaseStatus {
        get { CaseStatus(rawValue: estatusRaw) ?? .abierto }
        set { estatusRaw = newValue.rawValue }
    }

    var prioridad: PriorityLevel {
        get { PriorityLevel(rawValue: prioridadRaw) ?? .media }
        set { prioridadRaw = newValue.rawValue }
    }

    init(
        argosCaseCode: String,
        name: String,
        folioInvestigacion: String? = nil,
        institucion: String? = nil,
        unidad: String? = nil,
        responsable: String? = nil,
        estatus: CaseStatus = .abierto,
        prioridad: PriorityLevel = .media,
        descripcionBreve: String? = nil
    ) {
        self.id = UUID()
        self.argosCaseCode = argosCaseCode.uppercased()
        self.name = name
        self.folioInvestigacion = folioInvestigacion
        self.fechaApertura = Date()
        self.institucion = institucion
        self.unidad = unidad
        self.responsable = responsable
        self.analistasAsignados = []
        self.victimas = []
        self.personasDeInteres = []
        self.objetivos = nil
        self.telefonosRelacionados = []
        self.vehiculosRelacionados = []
        self.domiciliosRelacionados = []
        self.municipios = []
        self.estados = []
        self.estatusRaw = estatus.rawValue
        self.prioridadRaw = prioridad.rawValue
        self.descripcionBreve = descripcionBreve
        self.etiquetas = []
        self.imagenRepresentativa = nil
        self.createdAt = Date()
        self.updatedAt = Date()
    }
}

/// Bandeja de entrada especial (sección 24): caso lógico reservado para
/// ítems sin caso asignado todavía. No es un CaseEntity real — este código
/// es la constante compartida que las vistas y el servicio de ingesta usan
/// para reconocerlo sin comparar cadenas mágicas dispersas por el código.
enum InboxCaseCode {
    static let value = "INBOX"
}
