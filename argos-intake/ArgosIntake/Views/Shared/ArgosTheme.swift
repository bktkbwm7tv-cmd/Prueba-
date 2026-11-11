import SwiftUI
import ArgosCore

/// Estética ARGOS (sección 21): fondo azul marino muy oscuro, acentos cian
/// y blanco, rojo solo para alertas, amarillo para pendientes, verde para
/// validado. Deliberadamente austera — "debe transmitir inteligencia,
/// investigación, trazabilidad, control, precisión", no un videojuego.
enum ArgosTheme {
    static let background = Color(red: 0.02, green: 0.05, blue: 0.11)
    static let surface = Color(red: 0.05, green: 0.09, blue: 0.17)
    static let surfaceElevated = Color(red: 0.08, green: 0.13, blue: 0.22)
    static let cyan = Color(red: 0.29, green: 0.85, blue: 0.94)
    static let textPrimary = Color.white
    static let textSecondary = Color(white: 0.72)
    static let alertRed = Color(red: 0.92, green: 0.24, blue: 0.24)
    static let pendingYellow = Color(red: 0.95, green: 0.78, blue: 0.20)
    static let validatedGreen = Color(red: 0.30, green: 0.80, blue: 0.46)
    static let hairline = Color.white.opacity(0.12)

    static func color(for verification: VerificationStatus) -> Color {
        switch verification {
        case .recibido: return textSecondary
        case .verificado: return validatedGreen
        case .noVerificado: return pendingYellow
        case .descartado: return alertRed
        }
    }

    static func color(for priority: PriorityLevel) -> Color {
        switch priority {
        case .baja: return validatedGreen
        case .media: return pendingYellow
        case .alta: return alertRed
        case .critica: return alertRed
        }
    }
}

extension View {
    /// Fondo estándar de pantalla ARGOS.
    func argosBackground() -> some View {
        self.background(ArgosTheme.background.ignoresSafeArea())
    }
}
