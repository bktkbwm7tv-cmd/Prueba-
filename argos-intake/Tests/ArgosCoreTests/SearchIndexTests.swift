import XCTest
@testable import ArgosCore

final class SearchIndexTests: XCTestCase {
    private let documents: [SearchDocument] = [
        SearchDocument(
            id: "1", caseCode: "CFE", argosId: "ARGOS-CFE-2026-VEH-000001",
            fields: ["IMG_8734.HEIC", "Jeep Cherokee gris placa NJR-524-C", "vehículo"]
        ),
        SearchDocument(
            id: "2", caseCode: "OPX", argosId: "ARGOS-OPX-2026-DOC-000004",
            fields: ["oficio_bbva.pdf", "Transferencia BBVA a nombre de Luis Enrique"]
        ),
        SearchDocument(
            id: "3", caseCode: "CFE", argosId: "ARGOS-CFE-2026-MSG-000012",
            fields: ["chat_export.txt", "Mensaje sobre reunión en Iztapalapa"]
        )
    ]

    func testFindsPlateAcrossFields() {
        let matches = SearchIndex.search(query: "NJR-524-C", in: documents)
        XCTAssertEqual(matches.count, 1)
        XCTAssertEqual(matches.first?.document.id, "1")
    }

    func testIsCaseAndDiacriticInsensitive() {
        let matches = SearchIndex.search(query: "IZTAPALAPA", in: documents)
        XCTAssertEqual(matches.first?.document.id, "3")

        let accentless = SearchIndex.search(query: "vehiculo", in: documents)
        XCTAssertEqual(accentless.first?.document.id, "1")
    }

    func testMultipleDocumentsCanMatchSameQuery() {
        let matches = SearchIndex.search(query: "BBVA", in: documents)
        XCTAssertEqual(matches.map(\.document.id), ["2"])
    }

    func testEmptyQueryReturnsNoResults() {
        XCTAssertTrue(SearchIndex.search(query: "   ", in: documents).isEmpty)
    }

    func testNoMatchReturnsEmpty() {
        XCTAssertTrue(SearchIndex.search(query: "no-existe-en-ningun-caso", in: documents).isEmpty)
    }
}
