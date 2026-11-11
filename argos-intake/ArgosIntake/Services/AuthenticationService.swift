import Foundation
import LocalAuthentication
import Security
import ArgosCore

enum AuthenticationError: Error {
    case biometryUnavailable(String)
    case biometryFailed(Error)
    case pinNotSet
    case pinIncorrect
    case keychainError(OSStatus)
}

/// Seguridad de acceso (sección 25): Face ID / Touch ID como método
/// principal, con PIN de aplicación como respaldo. Nunca se guarda la
/// contraseña/PIN en texto plano — se guarda únicamente su hash en Keychain
/// (`kSecClassGenericPassword`, no en `UserDefaults`).
@MainActor
final class AuthenticationService: ObservableObject {
    @Published private(set) var isUnlocked = false

    private let keychainService = "mx.argos.intake.pin"
    private let keychainAccount = "app-lock-pin-hash"

    /// Intenta desbloquear con Face ID / Touch ID / passcode del sistema.
    /// Si el dispositivo no tiene biometría configurada, el llamador debe
    /// ofrecer el PIN de respaldo (`unlock(withPIN:)`).
    func unlockWithBiometrics(reason: String = "Desbloquear ARGOS INTAKE") async throws {
        let context = LAContext()
        var evaluationError: NSError?

        guard context.canEvaluatePolicy(.deviceOwnerAuthentication, error: &evaluationError) else {
            throw AuthenticationError.biometryUnavailable(evaluationError?.localizedDescription ?? "No disponible")
        }

        do {
            let success = try await context.evaluatePolicy(.deviceOwnerAuthentication, localizedReason: reason)
            isUnlocked = success
        } catch {
            throw AuthenticationError.biometryFailed(error)
        }
    }

    func lock() {
        isUnlocked = false
    }

    // MARK: - PIN de respaldo (Keychain)

    func hasPINConfigured() -> Bool {
        (try? readPINHash()) != nil
    }

    func setPIN(_ pin: String) throws {
        let hash = Self.hash(pin)
        try writePINHash(hash)
    }

    func unlock(withPIN pin: String) throws {
        guard let stored = try readPINHash() else { throw AuthenticationError.pinNotSet }
        guard Self.hash(pin) == stored else { throw AuthenticationError.pinIncorrect }
        isUnlocked = true
    }

    private static func hash(_ value: String) -> String {
        // SHA-256 vía ArgosCore.FileHasher (misma primitiva CryptoKit/swift-crypto
        // usada para hashes de evidencia, sección 10) — nunca se persiste el PIN.
        ArgosCore.FileHasher.sha256Hex(ofData: Data(value.utf8))
    }

    private func writePINHash(_ hash: String) throws {
        let data = Data(hash.utf8)
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: keychainService,
            kSecAttrAccount as String: keychainAccount
        ]
        SecItemDelete(query as CFDictionary)

        var attributes = query
        attributes[kSecValueData as String] = data
        attributes[kSecAttrAccessible as String] = kSecAttrAccessibleWhenUnlockedThisDeviceOnly

        let status = SecItemAdd(attributes as CFDictionary, nil)
        guard status == errSecSuccess else { throw AuthenticationError.keychainError(status) }
    }

    private func readPINHash() throws -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: keychainService,
            kSecAttrAccount as String: keychainAccount,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]
        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        if status == errSecItemNotFound { return nil }
        guard status == errSecSuccess, let data = result as? Data else {
            throw AuthenticationError.keychainError(status)
        }
        return String(decoding: data, as: UTF8.self)
    }
}
