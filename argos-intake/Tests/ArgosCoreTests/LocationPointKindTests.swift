import XCTest
@testable import ArgosCore

final class LocationPointKindTests: XCTestCase {
    func testEveryCaseHasNonEmptyDisplayNameAndSymbol() {
        for kind in LocationPointKind.allCases {
            XCTAssertFalse(kind.displayName.isEmpty, "\(kind) sin nombre para mostrar")
            XCTAssertFalse(kind.symbolName.isEmpty, "\(kind) sin símbolo")
        }
    }

    func testMatchesSectionSixteenTaxonomy() {
        let expected: Set<LocationPointKind> = [
            .domicilio, .avistamiento, .vehiculo, .camara, .banco,
            .cajero, .antena, .evento, .hallazgo, .puntoDeInteres
        ]
        XCTAssertEqual(Set(LocationPointKind.allCases), expected)
    }
}
