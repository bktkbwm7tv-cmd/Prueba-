import Foundation
import NaturalLanguage
import ArgosCore

/// Detección de nombres de persona y organización (sección 13). Usa
/// NaturalLanguage — por eso vive en el target de la app y no en
/// `ArgosCore`, que se mantiene libre de dependencias exclusivas de Apple.
/// Igual que `EntityExtractor`, esto nunca produce un hecho: es una
/// propuesta que el analista debe confirmar, corregir o rechazar.
struct PersonNameExtractor {
    private let contextRadius = 24

    func extract(from text: String) -> [ExtractedEntityCandidate] {
        guard !text.isEmpty else { return [] }

        let tagger = NLTagger(tagSchemes: [.nameType])
        tagger.string = text
        let options: NLTagger.Options = [.omitWhitespace, .omitPunctuation, .joinNames]

        var candidates: [ExtractedEntityCandidate] = []
        var seen = Set<String>()

        tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .word, scheme: .nameType, options: options) { tag, range in
            guard let tag, let label = Self.label(for: tag) else { return true }

            let value = String(text[range]).trimmingCharacters(in: .whitespacesAndNewlines)
            guard !value.isEmpty else { return true }

            let key = "\(label):\(value.lowercased())"
            guard !seen.contains(key) else { return true }
            seen.insert(key)

            candidates.append(ExtractedEntityCandidate(
                category: .persona,
                label: label,
                value: value,
                context: context(for: range, in: text)
            ))
            return true
        }

        return candidates
    }

    private static func label(for tag: NLTag) -> String? {
        switch tag {
        case .personalName: return "Nombre de persona"
        case .organizationName: return "Organización"
        default: return nil
        }
    }

    private func context(for range: Range<String.Index>, in text: String) -> String {
        let start = text.index(range.lowerBound, offsetBy: -contextRadius, limitedBy: text.startIndex) ?? text.startIndex
        let end = text.index(range.upperBound, offsetBy: contextRadius, limitedBy: text.endIndex) ?? text.endIndex
        var snippet = String(text[start..<end]).trimmingCharacters(in: .whitespacesAndNewlines)
        if start != text.startIndex { snippet = "…" + snippet }
        if end != text.endIndex { snippet += "…" }
        return snippet
    }
}
