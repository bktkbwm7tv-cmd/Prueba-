import XCTest
@testable import ArgosCore

final class FileHasherTests: XCTestCase {
    func testKnownVectorEmptyString() {
        // SHA-256("") — vector de prueba estándar (NIST/FIPS 180-4).
        let hash = FileHasher.sha256Hex(ofData: Data())
        XCTAssertEqual(hash, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    }

    func testKnownVectorAbc() {
        let hash = FileHasher.sha256Hex(ofData: Data("abc".utf8))
        XCTAssertEqual(hash, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    }

    func testFileHashMatchesDataHashAndIsStable() throws {
        let tmpURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString, isDirectory: false)
        let payload = Data(repeating: 0xAB, count: 5 * 1024 * 1024 + 17) // spans multiple chunks
        try payload.write(to: tmpURL)
        defer { try? FileManager.default.removeItem(at: tmpURL) }

        let fromFile = try FileHasher.sha256Hex(ofFileAt: tmpURL)
        let fromData = FileHasher.sha256Hex(ofData: payload)
        XCTAssertEqual(fromFile, fromData)

        // Recalcular debe producir exactamente el mismo hash (integridad).
        let again = try FileHasher.sha256Hex(ofFileAt: tmpURL)
        XCTAssertEqual(fromFile, again)
    }

    func testMissingFileThrows() {
        let missing = FileManager.default.temporaryDirectory
            .appendingPathComponent("no-existe-\(UUID().uuidString)")
        XCTAssertThrowsError(try FileHasher.sha256Hex(ofFileAt: missing))
    }
}
