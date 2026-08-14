import Foundation
import Crypto

public enum FileHasherError: Error, Sendable {
    case unableToOpenFile(URL)
}

/// Calcula SHA-256 de archivos de evidencia (sección 10/11).
///
/// El hash siempre corresponde al ARCHIVO ORIGINAL, nunca a un derivado
/// (miniatura, preview, texto OCR). Lee en bloques para no cargar videos o
/// paquetes de exportación completos en memoria.
public enum FileHasher {
    private static let chunkSize = 1 << 20 // 1 MiB

    public static func sha256Hex(ofFileAt url: URL) throws -> String {
        guard let stream = InputStream(url: url) else {
            throw FileHasherError.unableToOpenFile(url)
        }
        return try sha256Hex(reading: stream)
    }

    public static func sha256Hex(ofData data: Data) -> String {
        let digest = SHA256.hash(data: data)
        return digest.map { String(format: "%02x", $0) }.joined()
    }

    private static func sha256Hex(reading stream: InputStream) throws -> String {
        stream.open()
        defer { stream.close() }

        var hasher = SHA256()
        var buffer = [UInt8](repeating: 0, count: chunkSize)

        while stream.hasBytesAvailable {
            let bytesRead = stream.read(&buffer, maxLength: chunkSize)
            if bytesRead < 0 {
                throw stream.streamError ?? FileHasherError.unableToOpenFile(URL(fileURLWithPath: "/"))
            }
            if bytesRead == 0 { break }
            hasher.update(data: buffer[0..<bytesRead])
        }

        let digest = hasher.finalize()
        return digest.map { String(format: "%02x", $0) }.joined()
    }
}
