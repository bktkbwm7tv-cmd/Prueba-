import XCTest
@testable import ArgosCore

final class FileClassifierTests: XCTestCase {
    func testImageExtensions() {
        for name in ["foto.jpg", "foto.JPEG", "foto.heic", "foto.PNG", "foto.webp"] {
            XCTAssertEqual(FileClassifier.classify(filename: name).type, .image, name)
        }
    }

    func testVideoExtensions() {
        XCTAssertEqual(FileClassifier.classify(filename: "clip.mp4").type, .video)
        XCTAssertEqual(FileClassifier.classify(filename: "clip.MOV").type, .video)
    }

    func testAudioSuggestsNotaDeVozByDefault() {
        let result = FileClassifier.classify(filename: "nota.m4a")
        XCTAssertEqual(result.type, .audio)
        XCTAssertEqual(result.suggestedSubtype, .notaDeVoz)
    }

    func testDocumentExtensions() {
        for name in ["oficio.pdf", "reporte.docx", "datos.xlsx", "recibo.csv"] {
            XCTAssertEqual(FileClassifier.classify(filename: name).type, .document, name)
        }
    }

    func testUnknownExtensionFallsBackToOther() {
        let result = FileClassifier.classify(filename: "archivo.xyz123")
        XCTAssertEqual(result.type, .other)
        XCTAssertEqual(result.matchedExtension, "xyz123")
    }

    func testNoExtensionFallsBackToOtherWithoutExtension() {
        let result = FileClassifier.classify(filename: "sin_extension")
        XCTAssertEqual(result.type, .other)
        XCTAssertNil(result.matchedExtension)
    }

    func testIsKnownExtension() {
        XCTAssertTrue(FileClassifier.isKnownExtension("a.jpg"))
        XCTAssertFalse(FileClassifier.isKnownExtension("a.exe"))
    }
}
