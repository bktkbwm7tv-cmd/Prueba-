import Foundation

/// Top-level classification of an ingested item.
/// Mirrors "6. Clasificación automática por tipo de archivo" and the
/// identifier tokens in "9. Identificador único" of the master instruction.
public enum ItemType: String, Codable, CaseIterable, Sendable, Hashable {
    case image = "IMG"
    case video = "VID"
    case audio = "AUD"
    case document = "DOC"
    case message = "MSG"
    case location = "LOC"
    case phone = "TEL"
    case vehicle = "VEH"
    case person = "PER"
    case financial = "FIN"
    case other = "OTR"

    /// Nombre de carpeta lógica (sección 6).
    public var logicalFolder: String {
        switch self {
        case .image: return "03_IMÁGENES"
        case .video: return "04_VIDEO"
        case .audio: return "05_AUDIO"
        case .document: return "06_DOCUMENTOS"
        case .message: return "02_WHATSAPP"
        case .location: return "10_GEOGRAFÍA"
        case .phone: return "09_TELEFONÍA"
        case .vehicle: return "08_VEHÍCULOS"
        case .person: return "07_PERSONAS"
        case .financial: return "11_FINANCIERO"
        case .other: return "01_ORIGINALES"
        }
    }

    public var displayName: String {
        switch self {
        case .image: return "Imagen"
        case .video: return "Video"
        case .audio: return "Audio"
        case .document: return "Documento"
        case .message: return "Mensaje"
        case .location: return "Ubicación"
        case .phone: return "Teléfono"
        case .vehicle: return "Vehículo"
        case .person: return "Persona"
        case .financial: return "Financiero"
        case .other: return "Otro"
        }
    }

    /// Nombre de SF Symbol para representar el tipo en listas, bandeja de
    /// entrada y timeline — un solo lugar para que todas las vistas usen
    /// el mismo glifo por tipo.
    public var symbolName: String {
        switch self {
        case .image: return "photo"
        case .video: return "video"
        case .audio: return "waveform"
        case .document: return "doc.text"
        case .message: return "message"
        case .location: return "mappin.circle"
        case .phone: return "phone"
        case .vehicle: return "car"
        case .person: return "person"
        case .financial: return "banknote"
        case .other: return "questionmark.folder"
        }
    }
}

/// Subclasificaciones sugeridas por tipo (sección 6). No exhaustivo: el
/// analista siempre puede corregir con texto libre, por lo que ItemEntity
/// guarda el subtipo como String — este enum es la fuente de las opciones
/// sugeridas en la interfaz.
public enum ItemSubtype: String, Codable, CaseIterable, Sendable, Hashable {
    // Imágenes
    case personas, vehiculos, documentosFotografiados, domicilios, lugares
    case capturasDePantalla, evidencia

    // Audio
    case notaDeVoz, entrevista, llamada, grabacionAmbiental

    // Documentos
    case oficio, iph, fichaDeBusqueda, denuncia, dictamen, informe
    case registroTelefonico, documentoFinanciero, identificacion

    case otros

    public var displayName: String {
        switch self {
        case .personas: return "Personas"
        case .vehiculos: return "Vehículos"
        case .documentosFotografiados: return "Documentos fotografiados"
        case .domicilios: return "Domicilios"
        case .lugares: return "Lugares"
        case .capturasDePantalla: return "Capturas de pantalla"
        case .evidencia: return "Evidencia"
        case .notaDeVoz: return "Nota de voz"
        case .entrevista: return "Entrevista"
        case .llamada: return "Llamada"
        case .grabacionAmbiental: return "Grabación ambiental"
        case .oficio: return "Oficio"
        case .iph: return "IPH"
        case .fichaDeBusqueda: return "Ficha de búsqueda"
        case .denuncia: return "Denuncia"
        case .dictamen: return "Dictamen"
        case .informe: return "Informe"
        case .registroTelefonico: return "Registro telefónico"
        case .documentoFinanciero: return "Documento financiero"
        case .identificacion: return "Identificación"
        case .otros: return "Otros"
        }
    }
}
