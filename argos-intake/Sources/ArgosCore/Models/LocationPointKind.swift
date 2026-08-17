import Foundation

/// Iconografía del Mapa del Caso (sección 16): diferencia el tipo de punto,
/// nunca infiere uno — un `ItemEntity` de tipo `.location` sin este dato
/// se muestra como `.puntoDeInteres` (genérico) hasta que el analista lo
/// corrija, nunca se adivina la categoría a partir de otro campo.
public enum LocationPointKind: String, Codable, CaseIterable, Sendable, Hashable {
    case domicilio, avistamiento, vehiculo, camara, banco, cajero, antena
    case evento, hallazgo, puntoDeInteres

    public var displayName: String {
        switch self {
        case .domicilio: return "Domicilio"
        case .avistamiento: return "Avistamiento"
        case .vehiculo: return "Vehículo"
        case .camara: return "Cámara"
        case .banco: return "Banco"
        case .cajero: return "Cajero"
        case .antena: return "Antena"
        case .evento: return "Evento"
        case .hallazgo: return "Hallazgo"
        case .puntoDeInteres: return "Punto de interés"
        }
    }

    /// Nombre de SF Symbol sugerido para el pin — vive aquí (no solo en la
    /// vista) porque tanto el mapa como cualquier lista futura de
    /// ubicaciones deben usar el mismo glifo por tipo de punto.
    public var symbolName: String {
        switch self {
        case .domicilio: return "house.fill"
        case .avistamiento: return "eye.fill"
        case .vehiculo: return "car.fill"
        case .camara: return "video.fill"
        case .banco: return "building.columns.fill"
        case .cajero: return "banknote.fill"
        case .antena: return "antenna.radiowaves.left.and.right"
        case .evento: return "exclamationmark.triangle.fill"
        case .hallazgo: return "magnifyingglass"
        case .puntoDeInteres: return "mappin"
        }
    }
}
