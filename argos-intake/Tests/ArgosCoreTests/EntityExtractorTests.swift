import XCTest
@testable import ArgosCore

final class EntityExtractorTests: XCTestCase {
    // Bloque de texto ficticio con un ejemplo de cada tipo de identificador
    // que EntityExtractor debe reconocer. Ningún dato aquí corresponde a
    // una persona, cuenta o vehículo real.
    private let sample = """
    Contacto: demo.contacto@correoejemplo.com
    Sitio: https://ejemplo-demo.mx/perfil
    Teléfono: 55 1234 5678
    RFC: DEMO800101AB1
    CURP: DEMO800101HDFRRNA9
    IMEI: 356789012345678
    CLABE: 002180012345678901
    Tarjeta: 4111 1111 1111 1111
    Placa: DEM-123-A
    Ubicación: 19.432608, -99.133209
    """

    private func value(_ candidates: [ExtractedEntityCandidate], label: String) -> String? {
        candidates.first { $0.label == label }?.value
    }

    func testDetectsEmail() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "Correo electrónico"), "demo.contacto@correoejemplo.com")
    }

    func testDetectsURL() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "URL"), "https://ejemplo-demo.mx/perfil")
    }

    func testDetectsPhoneAsTelefonoCategory() {
        let result = EntityExtractor.extract(from: sample)
        let phone = result.first { $0.label == "Teléfono" }
        XCTAssertEqual(phone?.value, "55 1234 5678")
        XCTAssertEqual(phone?.category, .telefono)
    }

    func testDetectsRFC() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "RFC"), "DEMO800101AB1")
    }

    func testDetectsCURPDistinctFromRFC() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "CURP"), "DEMO800101HDFRRNA9")
        // La CURP no debe además reportarse como RFC de 13 caracteres:
        // solo debe existir un valor de RFC (el de la línea "RFC:").
        let rfcValues = result.filter { $0.label == "RFC" }.map(\.value)
        XCTAssertEqual(rfcValues, ["DEMO800101AB1"])
    }

    func testDetectsIMEIWithoutDuplicatingAsCard() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "IMEI"), "356789012345678")
        // Un IMEI de 15 dígitos no debe también dispararse como "Tarjeta"
        // (16 exactos) sobre la misma cadena.
        XCTAssertFalse(result.contains { $0.label == "Tarjeta" && $0.value == "356789012345678" })
    }

    func testDetectsCLABEWithoutDuplicatingAsCard() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "CLABE"), "002180012345678901")
        XCTAssertFalse(result.contains { $0.label == "Tarjeta" && $0.value == "002180012345678901" })
    }

    func testDetectsGroupedCardNumber() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "Tarjeta"), "4111 1111 1111 1111")
    }

    func testDetectsConservativePlateFormat() {
        let result = EntityExtractor.extract(from: sample)
        let plate = result.first { $0.label == "Posible placa vehicular" }
        XCTAssertEqual(plate?.value, "DEM-123-A")
        XCTAssertEqual(plate?.category, .vehiculo)
    }

    func testDetectsCoordinatePair() {
        let result = EntityExtractor.extract(from: sample)
        XCTAssertEqual(value(result, label: "Coordenadas"), "19.432608, -99.133209")
    }

    func testContextIncludesSurroundingText() {
        let result = EntityExtractor.extract(from: sample)
        let email = result.first { $0.label == "Correo electrónico" }
        XCTAssertTrue(email?.context.contains("Contacto") ?? false)
    }

    func testDeduplicatesRepeatedValues() {
        let repeated = "Tel 55 1234 5678, otra vez 55 1234 5678"
        let result = EntityExtractor.extract(from: repeated)
        XCTAssertEqual(result.filter { $0.label == "Teléfono" }.count, 1)
    }

    func testEmptyTextProducesNoCandidates() {
        XCTAssertTrue(EntityExtractor.extract(from: "").isEmpty)
    }

    func testPlainTextWithoutIdentifiersProducesNoCandidates() {
        let result = EntityExtractor.extract(from: "Reunión programada para revisar el expediente el jueves.")
        XCTAssertTrue(result.isEmpty)
    }
}
