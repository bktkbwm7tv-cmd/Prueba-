import Foundation

/// Resultado de una clasificación automática. Siempre es una *propuesta*:
/// section 6/13 exige que el analista pueda confirmar o corregir, nunca que
/// la clasificación automática se trate como hecho definitivo.
public struct ClassificationResult: Codable, Hashable, Sendable {
    public let type: ItemType
    public let suggestedSubtype: ItemSubtype?
    public let matchedExtension: String?

    public init(type: ItemType, suggestedSubtype: ItemSubtype? = nil, matchedExtension: String? = nil) {
        self.type = type
        self.suggestedSubtype = suggestedSubtype
        self.matchedExtension = matchedExtension
    }
}

/// Clasificación automática por extensión de archivo (sección 6).
/// Determinista y sin red: opera únicamente sobre el nombre de archivo.
public enum FileClassifier {
    private static let imageExtensions: Set<String> = [
        "jpg", "jpeg", "png", "heic", "heif", "tiff", "tif", "webp"
    ]
    private static let videoExtensions: Set<String> = [
        "mp4", "mov", "m4v", "avi", "mkv", "3gp"
    ]
    private static let audioExtensions: Set<String> = [
        "m4a", "mp3", "wav", "aac", "opus", "amr", "caf"
    ]
    private static let documentExtensions: Set<String> = [
        "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "csv", "zip", "rtf"
    ]

    /// Sección 6: subtipo sugerido de documento según nombre/extensión.
    /// Solo cubre lo determinable sin abrir el archivo (extensión); la
    /// clasificación semántica por contenido (oficio, IPH, dictamen, etc.)
    /// pertenece a MVP2 (OCR + extracción de entidades, sección 13-14).
    public static func classify(filename: String) -> ClassificationResult {
        let ext = (filename as NSString).pathExtension.lowercased()
        guard !ext.isEmpty else {
            return ClassificationResult(type: .other, suggestedSubtype: .otros, matchedExtension: nil)
        }

        if imageExtensions.contains(ext) {
            return ClassificationResult(type: .image, suggestedSubtype: nil, matchedExtension: ext)
        }
        if videoExtensions.contains(ext) {
            return ClassificationResult(type: .video, suggestedSubtype: nil, matchedExtension: ext)
        }
        if audioExtensions.contains(ext) {
            return ClassificationResult(type: .audio, suggestedSubtype: .notaDeVoz, matchedExtension: ext)
        }
        if documentExtensions.contains(ext) {
            return ClassificationResult(type: .document, suggestedSubtype: nil, matchedExtension: ext)
        }
        return ClassificationResult(type: .other, suggestedSubtype: .otros, matchedExtension: ext)
    }

    public static func isKnownExtension(_ filename: String) -> Bool {
        let ext = (filename as NSString).pathExtension.lowercased()
        return imageExtensions.contains(ext)
            || videoExtensions.contains(ext)
            || audioExtensions.contains(ext)
            || documentExtensions.contains(ext)
    }
}
