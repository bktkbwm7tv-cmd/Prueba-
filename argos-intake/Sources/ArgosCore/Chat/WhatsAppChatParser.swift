import Foundation

/// Un mensaje reconstruido de un `.txt` de exportación de WhatsApp
/// (sección 5). Nunca es un ITEM por sí mismo — es un renglón dentro de una
/// conversación importada; el llamador decide cómo persistirlo.
public struct ParsedWhatsAppMessage: Equatable, Sendable {
    public let date: Date?
    public let rawTimestamp: String
    public let sender: String?
    public let isSystemEvent: Bool
    public let body: String
    public let attachmentFilename: String?
    public let rawLine: String

    public init(
        date: Date?,
        rawTimestamp: String,
        sender: String?,
        isSystemEvent: Bool,
        body: String,
        attachmentFilename: String?,
        rawLine: String
    ) {
        self.date = date
        self.rawTimestamp = rawTimestamp
        self.sender = sender
        self.isSystemEvent = isSystemEvent
        self.body = body
        self.attachmentFilename = attachmentFilename
        self.rawLine = rawLine
    }
}

/// Resultado agregado de una importación, útil para el resumen que se
/// muestra al analista antes de confirmar (sección 5): nombre del chat,
/// participantes detectados, rango de fechas.
public struct ParsedWhatsAppChat: Sendable {
    public let messages: [ParsedWhatsAppMessage]

    public init(messages: [ParsedWhatsAppMessage]) {
        self.messages = messages
    }

    public var participants: [String] {
        var seen = Set<String>()
        var ordered: [String] = []
        for message in messages {
            guard let sender = message.sender, !message.isSystemEvent, !seen.contains(sender) else { continue }
            seen.insert(sender)
            ordered.append(sender)
        }
        return ordered
    }

    public var dateRange: (start: Date, end: Date)? {
        let dates = messages.compactMap(\.date)
        guard let start = dates.min(), let end = dates.max() else { return nil }
        return (start, end)
    }
}

/// Reconstruye mensajes, remitente, fecha/hora y adjuntos referenciados a
/// partir del texto plano que WhatsApp genera al exportar un chat
/// (sección 5). Soporta los dos formatos de línea que WhatsApp produce —
/// iOS (con corchetes, con segundos) y Android (con guion, sin corchetes) —
/// y las variantes en español e inglés de las referencias a adjuntos
/// (`<attached: X>`, `<adjunto: X>`, `<archivo adjunto: X>`, "imagen
/// omitida" / "image omitted"). No intenta leer el `.zip` en sí: opera
/// sobre el texto ya extraído del `_chat.txt`.
///
/// Ambigüedad conocida: el orden día/mes en la marca de tiempo depende del
/// idioma/región del teléfono que exportó, y el `.txt` no lo declara.
/// `parseDate` prueba primero los patrones DD/MM y luego MM/DD; como
/// `DateFormatter` rechaza combinaciones con mes fuera de 1-12, la
/// interpretación inválida simplemente no produce fecha y se usa la otra —
/// y cuando ambas son válidas (p. ej. 05/06), se asume DD/MM por el
/// contexto del producto (México). Un caso realmente ambiguo debe quedar
/// visible para que el analista lo corrija, no oculto en un dato asumido.
public enum WhatsAppChatParser {
    /// Marca el inicio de un mensaje nuevo: `[D/M/AA, H:MM:SS]` (iOS) o
    /// `D/M/AA, H:MM -` (Android), con o sin AM/PM.
    private static let iosLinePattern = try! NSRegularExpression(
        pattern: #"^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}(?::\d{2})?(?:\s?[AaPp]\.?\s?[Mm]\.?)?)\]\s(.*)$"#
    )
    private static let androidLinePattern = try! NSRegularExpression(
        pattern: #"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}(?:\s?[AaPp]\.?\s?[Mm]\.?)?)\s-\s(.*)$"#
    )
    /// "Remitente: mensaje" — el remitente no contiene ":" y es razonablemente corto.
    private static let senderPattern = try! NSRegularExpression(
        pattern: #"^([^:\n]{1,60}?):\s(.*)$"#, options: [.dotMatchesLineSeparators]
    )
    private static let attachmentPattern = try! NSRegularExpression(
        pattern: #"<[^:<>]{1,40}:\s*([^<>]+?)>"#
    )
    /// Marcas de dirección invisibles (LRM/RLM) que iOS antepone a cada línea.
    private static let invisibleMarks = CharacterSet(charactersIn: "\u{200E}\u{200F}\u{FEFF}")

    public static func parse(_ text: String) -> ParsedWhatsAppChat {
        let lines = text
            .components(separatedBy: .newlines)
            .map { $0.trimmingCharacters(in: invisibleMarks) }

        var messages: [ParsedWhatsAppMessage] = []

        for line in lines {
            if let match = matchLineStart(line) {
                messages.append(makeMessage(rawTimestamp: match.timestamp, remainder: match.remainder, rawLine: line))
            } else if !line.isEmpty, var last = messages.popLast() {
                // Continuación de un mensaje multilínea (sección 5, punto 4-5).
                let joinedBody = last.body.isEmpty ? line : last.body + "\n" + line
                last = ParsedWhatsAppMessage(
                    date: last.date, rawTimestamp: last.rawTimestamp, sender: last.sender,
                    isSystemEvent: last.isSystemEvent, body: joinedBody,
                    attachmentFilename: last.attachmentFilename ?? extractAttachment(from: line),
                    rawLine: last.rawLine + "\n" + line
                )
                messages.append(last)
            }
            // Líneas vacías fuera de un mensaje se ignoran.
        }

        return ParsedWhatsAppChat(messages: messages)
    }

    private struct LineStart { let timestamp: String; let remainder: String }

    private static func matchLineStart(_ line: String) -> LineStart? {
        let range = NSRange(line.startIndex..<line.endIndex, in: line)
        if let m = iosLinePattern.firstMatch(in: line, range: range), m.numberOfRanges == 4 {
            let date = string(line, m.range(at: 1))
            let time = string(line, m.range(at: 2))
            let remainder = string(line, m.range(at: 3))
            return LineStart(timestamp: "\(date), \(time)", remainder: remainder)
        }
        if let m = androidLinePattern.firstMatch(in: line, range: range), m.numberOfRanges == 4 {
            let date = string(line, m.range(at: 1))
            let time = string(line, m.range(at: 2))
            let remainder = string(line, m.range(at: 3))
            return LineStart(timestamp: "\(date), \(time)", remainder: remainder)
        }
        return nil
    }

    private static func makeMessage(rawTimestamp: String, remainder: String, rawLine: String) -> ParsedWhatsAppMessage {
        let range = NSRange(remainder.startIndex..<remainder.endIndex, in: remainder)
        if let m = senderPattern.firstMatch(in: remainder, range: range), m.numberOfRanges == 3 {
            let sender = string(remainder, m.range(at: 1))
            let body = string(remainder, m.range(at: 2))
            return ParsedWhatsAppMessage(
                date: parseDate(fromCombined: rawTimestamp), rawTimestamp: rawTimestamp,
                sender: sender, isSystemEvent: false, body: body,
                attachmentFilename: extractAttachment(from: body), rawLine: rawLine
            )
        }
        // Sin "Remitente:" al inicio → evento de sistema (creación de grupo,
        // aviso de cifrado, cambio de número, etc.), sección 5.
        return ParsedWhatsAppMessage(
            date: parseDate(fromCombined: rawTimestamp), rawTimestamp: rawTimestamp,
            sender: nil, isSystemEvent: true, body: remainder,
            attachmentFilename: nil, rawLine: rawLine
        )
    }

    private static func extractAttachment(from text: String) -> String? {
        let range = NSRange(text.startIndex..<text.endIndex, in: text)
        guard let m = attachmentPattern.firstMatch(in: text, range: range), m.numberOfRanges == 2 else { return nil }
        return string(text, m.range(at: 1)).trimmingCharacters(in: .whitespaces)
    }

    private static func string(_ source: String, _ range: NSRange) -> String {
        guard let r = Range(range, in: source) else { return "" }
        return String(source[r])
    }

    // MARK: - Fecha

    /// Intenta varios formatos porque el `.txt` no declara el suyo.
    /// DD/MM se prueba antes que MM/DD (contexto del producto: México).
    private static func parseDate(fromCombined combined: String) -> Date? {
        let candidates = [
            "d/M/yy, H:mm:ss", "d/M/yyyy, H:mm:ss",
            "d/M/yy, h:mm:ss a", "d/M/yyyy, h:mm:ss a",
            "d/M/yy, H:mm", "d/M/yyyy, H:mm",
            "d/M/yy, h:mm a", "d/M/yyyy, h:mm a",
            "M/d/yy, H:mm:ss", "M/d/yyyy, H:mm:ss",
            "M/d/yy, h:mm:ss a", "M/d/yyyy, h:mm:ss a",
            "M/d/yy, H:mm", "M/d/yyyy, H:mm",
            "M/d/yy, h:mm a", "M/d/yyyy, h:mm a"
        ]
        // "h:mm a" solo reconoce los símbolos AM/PM del locale (en_US_POSIX
        // espera "AM"/"PM" exactos); WhatsApp en español exporta "a. m." /
        // "p. m.", así que se normaliza antes de intentar cada patrón.
        var normalized = combined.replacingOccurrences(of: "\u{202F}", with: " ")
        normalized = normalized.replacingOccurrences(
            of: #"(?i)a\.?\s?m\.?"#, with: "AM", options: .regularExpression
        )
        normalized = normalized.replacingOccurrences(
            of: #"(?i)p\.?\s?m\.?"#, with: "PM", options: .regularExpression
        )
        for pattern in candidates {
            let formatter = DateFormatter()
            formatter.locale = Locale(identifier: "en_US_POSIX")
            formatter.dateFormat = pattern
            formatter.isLenient = false
            if let date = formatter.date(from: normalized) {
                return date
            }
        }
        return nil
    }
}
