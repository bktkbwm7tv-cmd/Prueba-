import Foundation

/// Categorías de entidad de "13. Extracción inteligente de información".
/// `persona` no se detecta aquí — requiere NaturalLanguage (solo Apple),
/// así que vive en el target de la app; este archivo cubre lo que es
/// determinable por patrón, sin ambigüedad de plataforma.
public enum EntityCategory: String, Codable, CaseIterable, Sendable, Hashable {
    case persona, telefono, vehiculo, geografia, financiero, identificador

    public var displayName: String {
        switch self {
        case .persona: return "Persona"
        case .telefono: return "Telefonía"
        case .vehiculo: return "Vehículo"
        case .geografia: return "Geografía"
        case .financiero: return "Financiero"
        case .identificador: return "Identificador"
        }
    }
}

/// Una entidad propuesta automáticamente — nunca un hecho confirmado
/// (sección 13: "Nunca considerar automáticamente una detección como un
/// hecho confirmado"; sección 29: separar EXTRACCIÓN AUTOMÁTICA de HECHO,
/// INFERENCIA y VALIDACIÓN HUMANA). El llamador decide cómo persistir el
/// estado de confirmación — esta capa solo detecta.
public struct ExtractedEntityCandidate: Equatable, Sendable {
    public let category: EntityCategory
    /// Etiqueta específica dentro de la categoría, p. ej. "RFC", "CURP",
    /// "Teléfono", "Correo electrónico" — más preciso que la categoría sola.
    public let label: String
    public let value: String
    /// Fragmento de texto alrededor de la coincidencia, para que el
    /// analista vea el contexto sin tener que reabrir la fuente completa.
    public let context: String

    public init(category: EntityCategory, label: String, value: String, context: String) {
        self.category = category
        self.label = label
        self.value = value
        self.context = context
    }
}

/// Detección por patrón de identificadores estructurados (sección 13).
/// Deliberadamente conservador: un falso positivo que el analista debe
/// descartar es aceptable, pero inventar una lectura (p. ej. "adivinar" una
/// dirección a partir de texto libre sin un gazetteer real) no lo es — por
/// eso no hay un extractor de domicilios/colonias en esta versión; ver el
/// comentario junto a `coordinatePattern`.
public enum EntityExtractor {
    private static let contextRadius = 24

    public static func extract(from text: String) -> [ExtractedEntityCandidate] {
        guard !text.isEmpty else { return [] }
        var candidates: [ExtractedEntityCandidate] = []
        var seenValues = Set<String>()

        for detector in detectors {
            for match in matches(of: detector.pattern, in: text) {
                let value = match.trimmingCharacters(in: .whitespaces)
                let key = "\(detector.category.rawValue):\(detector.label):\(value.lowercased())"
                guard !value.isEmpty, !seenValues.contains(key) else { continue }
                seenValues.insert(key)
                candidates.append(ExtractedEntityCandidate(
                    category: detector.category, label: detector.label, value: value,
                    context: context(for: value, in: text)
                ))
            }
        }
        return candidates
    }

    private struct Detector {
        let category: EntityCategory
        let label: String
        let pattern: NSRegularExpression
    }

    private static let detectors: [Detector] = [
        Detector(category: .identificador, label: "Correo electrónico", pattern: emailPattern),
        Detector(category: .identificador, label: "URL", pattern: urlPattern),
        Detector(category: .identificador, label: "RFC", pattern: rfcPattern),
        Detector(category: .identificador, label: "CURP", pattern: curpPattern),
        Detector(category: .telefono, label: "IMEI", pattern: imeiPattern),
        Detector(category: .telefono, label: "Teléfono", pattern: phonePattern),
        Detector(category: .financiero, label: "CLABE", pattern: clabePattern),
        Detector(category: .financiero, label: "Tarjeta", pattern: cardPattern),
        Detector(category: .vehiculo, label: "Posible placa vehicular", pattern: platePattern),
        Detector(category: .geografia, label: "Coordenadas", pattern: coordinatePattern)
    ]

    // MARK: - Patrones

    private static let emailPattern = try! NSRegularExpression(
        pattern: #"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"#
    )
    private static let urlPattern = try! NSRegularExpression(
        pattern: #"\bhttps?://[^\s<>"]+"#
    )
    /// RFC de persona física (13) o moral (12): 3-4 letras, 6 dígitos
    /// (fecha AAMMDD), 3 caracteres de homoclave.
    private static let rfcPattern = try! NSRegularExpression(
        pattern: #"\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b"#
    )
    /// CURP: 4 letras + 6 dígitos + sexo (H/M) + 5 letras + homoclave + dígito.
    private static let curpPattern = try! NSRegularExpression(
        pattern: #"\b[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d\b"#
    )
    private static let imeiPattern = try! NSRegularExpression(pattern: #"\b\d{15}\b"#)
    /// Teléfono mexicano de 10 dígitos, con o sin lada país/separadores.
    private static let phonePattern = try! NSRegularExpression(
        pattern: #"\b(?:\+?52[\s-]?)?(?:1[\s-]?)?\d{2,3}[\s-]?\d{3,4}[\s-]?\d{4}\b"#
    )
    private static let clabePattern = try! NSRegularExpression(pattern: #"\b\d{18}\b"#)
    /// 16 dígitos (el largo más común de tarjeta), agrupados de 4 en 4 con
    /// separador o corridos. Se fija en 16 exactos — no un rango — para no
    /// duplicar coincidencias con IMEI (15) o CLABE (18) sobre la misma cadena.
    private static let cardPattern = try! NSRegularExpression(
        pattern: #"\b(?:\d{4}[\s-]){3}\d{4}\b|\b\d{16}\b"#
    )
    /// Formato conservador (letras-dígitos-letra) para reducir falsos
    /// positivos — las placas mexicanas varían mucho por estado y época;
    /// esto es una sugerencia, nunca una lectura oficial.
    private static let platePattern = try! NSRegularExpression(
        pattern: #"\b[A-Z]{3}[\s-]\d{3}[\s-][A-Z]\b|\b[A-Z]{3}\d{4}\b"#
    )
    /// Pares de coordenadas decimales (lat, long). No hay extractor de
    /// domicilios/colonias en texto libre: sin un gazetteer real de
    /// municipios y estados, "detectar" una dirección sería adivinar, y
    /// eso contradice el principio de cero información inventada.
    private static let coordinatePattern = try! NSRegularExpression(
        pattern: #"-?\d{1,3}\.\d{3,8},\s*-?\d{1,3}\.\d{3,8}"#
    )

    // MARK: - Utilidades

    private static func matches(of regex: NSRegularExpression, in text: String) -> [String] {
        let range = NSRange(text.startIndex..<text.endIndex, in: text)
        return regex.matches(in: text, range: range).compactMap { match in
            guard let r = Range(match.range, in: text) else { return nil }
            return String(text[r])
        }
    }

    private static func context(for value: String, in text: String) -> String {
        guard let range = text.range(of: value) else { return value }
        let start = text.index(range.lowerBound, offsetBy: -contextRadius, limitedBy: text.startIndex) ?? text.startIndex
        let end = text.index(range.upperBound, offsetBy: contextRadius, limitedBy: text.endIndex) ?? text.endIndex
        var snippet = String(text[start..<end]).trimmingCharacters(in: .whitespacesAndNewlines)
        if start != text.startIndex { snippet = "…" + snippet }
        if end != text.endIndex { snippet += "…" }
        return snippet
    }
}
