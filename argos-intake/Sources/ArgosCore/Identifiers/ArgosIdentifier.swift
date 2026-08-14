import Foundation

/// Identificador único e inalterable de cada elemento incorporado a ARGOS.
///
/// Formato (sección 9): `ARGOS-[CASO]-[AÑO]-[TIPO]-[CONSECUTIVO]`
/// Ejemplo: `ARGOS-CFE-2026-IMG-000123`
///
/// El consecutivo se calcula por combinación (caso, año, tipo) — no es
/// global — de modo que cada rama de conteo sea legible y auditable de
/// forma independiente.
public struct ArgosIdentifier: Codable, Hashable, Sendable, CustomStringConvertible {
    public let caseCode: String
    public let year: Int
    public let type: ItemType
    public let sequence: Int

    public init(caseCode: String, year: Int, type: ItemType, sequence: Int) {
        self.caseCode = caseCode.uppercased()
        self.year = year
        self.type = type
        self.sequence = sequence
    }

    public var description: String {
        let seq = String(format: "%06d", sequence)
        return "ARGOS-\(caseCode)-\(year)-\(type.rawValue)-\(seq)"
    }

    /// Parsing estricto: usado por la bitácora y el buscador para validar
    /// referencias cruzadas. Un ID que no se puede parsear no es un ID ARGOS.
    public init?(parsing string: String) {
        let parts = string.split(separator: "-", omittingEmptySubsequences: true).map(String.init)
        guard parts.count == 5, parts[0] == "ARGOS" else { return nil }
        guard let year = Int(parts[2]), year > 2000, year < 2100 else { return nil }
        guard let type = ItemType(rawValue: parts[3]) else { return nil }
        guard let sequence = Int(parts[4]) else { return nil }
        self.init(caseCode: parts[1], year: year, type: type, sequence: sequence)
    }
}

/// Genera consecutivos por (caso, año, tipo). El llamador es responsable de
/// persistir `highestSequence` de forma durable (SwiftData) y de pasarlo de
/// vuelta en cada llamada — este generador no guarda estado por diseño, para
/// que sea trivialmente testable y libre de condiciones de carrera ocultas.
public enum ArgosIdentifierGenerator {
    public static func next(
        caseCode: String,
        year: Int,
        type: ItemType,
        highestExistingSequence: Int
    ) -> ArgosIdentifier {
        ArgosIdentifier(
            caseCode: caseCode,
            year: year,
            type: type,
            sequence: highestExistingSequence + 1
        )
    }
}
