import SwiftUI

/// Pantalla de bloqueo (sección 25). Face ID / Touch ID como camino
/// principal; PIN de respaldo cuando la biometría no está disponible o
/// falla. No expone ningún dato del expediente antes de desbloquear.
struct LockScreenView: View {
    @EnvironmentObject private var auth: AuthenticationService
    @State private var pin: String = ""
    @State private var showPINField = false
    @State private var errorMessage: String?

    var body: some View {
        VStack(spacing: 24) {
            Spacer()

            Image(systemName: "shield.lefthalf.filled")
                .font(.system(size: 56))
                .foregroundStyle(ArgosTheme.cyan)

            VStack(spacing: 4) {
                Text("ARGOS INTAKE")
                    .font(.title2.bold())
                    .foregroundStyle(ArgosTheme.textPrimary)
                Text("Sistema de Ingesta, Clasificación y Trazabilidad")
                    .font(.caption)
                    .foregroundStyle(ArgosTheme.textSecondary)
            }

            if let errorMessage {
                Text(errorMessage)
                    .font(.footnote)
                    .foregroundStyle(ArgosTheme.alertRed)
            }

            if showPINField {
                SecureField("PIN de aplicación", text: $pin)
                    .textFieldStyle(.roundedBorder)
                    .frame(maxWidth: 240)
                    .onSubmit(attemptPINUnlock)

                Button("Desbloquear con PIN", action: attemptPINUnlock)
                    .buttonStyle(.borderedProminent)
                    .tint(ArgosTheme.cyan)
            } else {
                Button {
                    Task { await attemptBiometricUnlock() }
                } label: {
                    Label("Desbloquear con Face ID / Touch ID", systemImage: "faceid")
                }
                .buttonStyle(.borderedProminent)
                .tint(ArgosTheme.cyan)

                Button("Usar PIN") { showPINField = true }
                    .foregroundStyle(ArgosTheme.textSecondary)
            }

            Spacer()
            Text("Uso Institucional")
                .font(.caption2)
                .foregroundStyle(ArgosTheme.textSecondary.opacity(0.6))
        }
        .padding()
        .argosBackground()
        .task { await attemptBiometricUnlock() }
    }

    private func attemptBiometricUnlock() async {
        do {
            try await auth.unlockWithBiometrics()
            errorMessage = nil
        } catch {
            showPINField = true
        }
    }

    private func attemptPINUnlock() {
        do {
            try auth.unlock(withPIN: pin)
            errorMessage = nil
        } catch {
            errorMessage = "PIN incorrecto."
        }
        pin = ""
    }
}
