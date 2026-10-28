import XCTest
@testable import ArgosCore

final class ItemTypeTests: XCTestCase {
    func testEveryCaseHasNonEmptySymbolName() {
        for type in ItemType.allCases {
            XCTAssertFalse(type.symbolName.isEmpty, "\(type) sin símbolo")
        }
    }
}
