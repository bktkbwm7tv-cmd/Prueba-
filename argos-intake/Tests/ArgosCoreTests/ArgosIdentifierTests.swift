import XCTest
@testable import ArgosCore

final class ArgosIdentifierTests: XCTestCase {
    func testDescriptionMatchesMasterInstructionExample() {
        let id = ArgosIdentifier(caseCode: "CFE", year: 2026, type: .image, sequence: 123)
        XCTAssertEqual(id.description, "ARGOS-CFE-2026-IMG-000123")
    }

    func testCaseCodeIsUppercased() {
        let id = ArgosIdentifier(caseCode: "cfe", year: 2026, type: .document, sequence: 1)
        XCTAssertEqual(id.caseCode, "CFE")
    }

    func testRoundTripParsing() {
        let original = ArgosIdentifier(caseCode: "OPX", year: 2026, type: .vehicle, sequence: 42)
        let parsed = ArgosIdentifier(parsing: original.description)
        XCTAssertEqual(parsed, original)
    }

    func testParsingRejectsMalformedStrings() {
        XCTAssertNil(ArgosIdentifier(parsing: "NOT-AN-ARGOS-ID"))
        XCTAssertNil(ArgosIdentifier(parsing: "ARGOS-CFE-2026-ZZZ-000001"))
        XCTAssertNil(ArgosIdentifier(parsing: "ARGOS-CFE-notayear-IMG-000001"))
    }

    func testGeneratorIncrementsFromHighestExisting() {
        let next = ArgosIdentifierGenerator.next(
            caseCode: "CFE", year: 2026, type: .image, highestExistingSequence: 122
        )
        XCTAssertEqual(next.sequence, 123)
    }

    func testGeneratorStartsAtOneWhenNoneExist() {
        let next = ArgosIdentifierGenerator.next(
            caseCode: "CFE", year: 2026, type: .image, highestExistingSequence: 0
        )
        XCTAssertEqual(next.sequence, 1)
    }
}
