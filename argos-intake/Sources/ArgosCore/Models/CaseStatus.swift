import Foundation

public enum CaseStatus: String, Codable, CaseIterable, Sendable, Hashable {
    case abierto = "Abierto"
    case enAnalisis = "En análisis"
    case suspendido = "Suspendido"
    case cerrado = "Cerrado"
    case archivado = "Archivado"
}

public enum PriorityLevel: String, Codable, CaseIterable, Sendable, Comparable, Hashable {
    case baja = "Baja"
    case media = "Media"
    case alta = "Alta"
    case critica = "Crítica"

    private var rank: Int {
        switch self {
        case .baja: return 0
        case .media: return 1
        case .alta: return 2
        case .critica: return 3
        }
    }

    public static func < (lhs: PriorityLevel, rhs: PriorityLevel) -> Bool {
        lhs.rank < rhs.rank
    }
}

/// Estado dentro de la Bandeja de Entrada (sección 24).
public enum InboxStatus: String, Codable, CaseIterable, Sendable, Hashable {
    case pendiente = "Pendiente"
    case revisado = "Revisado"
    case clasificado = "Clasificado"
    case asignado = "Asignado"
}

/// Estado de validación de una entidad extraída o de un elemento en general
/// (sección 30). Nunca se mezcla con VerificationStatus del archivo fuente.
public enum VerificationStatus: String, Codable, CaseIterable, Sendable, Hashable {
    case recibido = "RECIBIDO"
    case verificado = "VERIFICADO"
    case noVerificado = "NO VERIFICADO"
    case descartado = "DESCARTADO"
}

/// Estado de clasificación de un ITEM dentro del flujo de ingesta.
public enum ClassificationStatus: String, Codable, CaseIterable, Sendable, Hashable {
    case sinClasificar = "Sin clasificar"
    case autoClasificado = "Auto-clasificado"
    case confirmadoPorAnalista = "Confirmado por analista"
    case corregido = "Corregido"
}

/// Categorías de etiqueta libre (sección 4).
public enum TagCategory: String, Codable, CaseIterable, Sendable, Hashable {
    case persona, vehiculo, telefono, domicilio, ubicacion, documento
    case fotografia, audio, video, financiero, telefonia, entrevista
    case vigilancia, investigacion, inteligencia, evidencia, otros

    public var displayName: String {
        switch self {
        case .persona: return "Persona"
        case .vehiculo: return "Vehículo"
        case .telefono: return "Teléfono"
        case .domicilio: return "Domicilio"
        case .ubicacion: return "Ubicación"
        case .documento: return "Documento"
        case .fotografia: return "Fotografía"
        case .audio: return "Audio"
        case .video: return "Video"
        case .financiero: return "Financiero"
        case .telefonia: return "Telefonía"
        case .entrevista: return "Entrevista"
        case .vigilancia: return "Vigilancia"
        case .investigacion: return "Investigación"
        case .inteligencia: return "Inteligencia"
        case .evidencia: return "Evidencia"
        case .otros: return "Otros"
        }
    }
}
