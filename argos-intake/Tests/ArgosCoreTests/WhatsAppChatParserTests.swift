import XCTest
@testable import ArgosCore

final class WhatsAppChatParserTests: XCTestCase {
    // Texto de ejemplo con formato iOS (corchetes, con segundos), en
    // español, con adjunto, evento de sistema y mensaje multilínea. Todos
    // los nombres/archivos son ficticios.
    private let iosSample = """
    [12/08/24, 09:15:03] Ana Demo: Buenos días
    [12/08/24, 09:15:47] Beto Demo: Hola, ¿ya viste el documento?
    [12/08/24, 09:16:02] Beto Demo: <archivo adjunto: 00000001-DOCUMENT-2024-08-12.pdf>
    [12/08/24, 09:20:11] Ana Demo: Sí, lo reviso
    en un momento y te confirmo
    [12/08/24, 09:25:00] Ana Demo creó el grupo "Caso Demo"
    """

    private let androidSample = """
    12/08/24, 9:16 a. m. - Beto Demo: image omitted
    12/08/24, 9:17 a. m. - Ana Demo: Recibido, gracias
    """

    func testParsesSenderAndBody() {
        let result = WhatsAppChatParser.parse(iosSample)
        // 5 mensajes de nivel superior: la línea de continuación (5) se
        // fusiona en el mensaje multilínea (4), no cuenta aparte.
        XCTAssertEqual(result.messages.count, 5)
        XCTAssertEqual(result.messages[0].sender, "Ana Demo")
        XCTAssertEqual(result.messages[0].body, "Buenos días")
        XCTAssertEqual(result.messages[1].sender, "Beto Demo")
        XCTAssertEqual(result.messages[1].body, "Hola, ¿ya viste el documento?")
    }

    func testDetectsSpanishAttachmentReference() {
        let result = WhatsAppChatParser.parse(iosSample)
        let attachmentMessage = result.messages[2]
        XCTAssertEqual(attachmentMessage.sender, "Beto Demo")
        XCTAssertEqual(attachmentMessage.attachmentFilename, "00000001-DOCUMENT-2024-08-12.pdf")
    }

    func testJoinsMultilineMessageAndKeepsFirstTimestamp() {
        let result = WhatsAppChatParser.parse(iosSample)
        let multiline = result.messages[3]
        XCTAssertEqual(multiline.sender, "Ana Demo")
        XCTAssertEqual(multiline.body, "Sí, lo reviso\nen un momento y te confirmo")
        XCTAssertEqual(multiline.rawTimestamp, "12/08/24, 09:20:11")
    }

    func testDetectsSystemEventWithoutSender() {
        let result = WhatsAppChatParser.parse(iosSample)
        let event = result.messages[4]
        XCTAssertTrue(event.isSystemEvent)
        XCTAssertNil(event.sender)
        XCTAssertEqual(event.body, "Ana Demo creó el grupo \"Caso Demo\"")
    }

    func testParsesAndroidDashFormatWithoutBrackets() {
        let result = WhatsAppChatParser.parse(androidSample)
        XCTAssertEqual(result.messages.count, 2)
        XCTAssertEqual(result.messages[0].sender, "Beto Demo")
        XCTAssertEqual(result.messages[0].body, "image omitted")
        XCTAssertNil(result.messages[0].attachmentFilename)
        XCTAssertEqual(result.messages[1].sender, "Ana Demo")
    }

    func testParticipantsExcludeSystemEventsAndPreserveFirstAppearanceOrder() {
        let result = WhatsAppChatParser.parse(iosSample)
        XCTAssertEqual(result.participants, ["Ana Demo", "Beto Demo"])
    }

    func testDateRangeSpansFirstAndLastParsedMessage() {
        let result = WhatsAppChatParser.parse(iosSample)
        guard let range = result.dateRange else { return XCTFail("Se esperaba un rango de fechas") }
        XCTAssertLessThanOrEqual(range.start, range.end)
    }

    func testAmbiguousDayMonthDefaultsToDayFirst() {
        // "05/06/24" es ambiguo (5 de junio vs. 6 de mayo); el analizador
        // debe asumir día/mes (contexto México) cuando ambas lecturas son
        // válidas.
        let result = WhatsAppChatParser.parse("[05/06/24, 10:00:00] Ana Demo: prueba")
        guard let date = result.messages.first?.date else { return XCTFail("Se esperaba una fecha") }
        let components = Calendar(identifier: .gregorian).dateComponents([.day, .month], from: date)
        XCTAssertEqual(components.day, 5)
        XCTAssertEqual(components.month, 6)
    }

    func testDayOverTwelveIsUnambiguousUnderDayFirst() {
        // día=25 solo cabe como día (no como mes), así que "25/03/24" no es
        // ambiguo y debe leerse como 25 de marzo bajo DD/MM.
        let result = WhatsAppChatParser.parse("[25/03/24, 10:00:00] Ana Demo: prueba")
        guard let date = result.messages.first?.date else { return XCTFail("Se esperaba una fecha") }
        let components = Calendar(identifier: .gregorian).dateComponents([.day, .month], from: date)
        XCTAssertEqual(components.day, 25)
        XCTAssertEqual(components.month, 3)
    }

    func testInvalidDayFirstReadingFallsBackToMonthFirst() {
        // "08/25/24": como DD/MM, mes=25 es inválido, así que la única
        // lectura posible es MM/DD → 25 de agosto.
        let result = WhatsAppChatParser.parse("[08/25/24, 10:00:00] Ana Demo: prueba")
        guard let date = result.messages.first?.date else { return XCTFail("Se esperaba una fecha") }
        let components = Calendar(identifier: .gregorian).dateComponents([.day, .month], from: date)
        XCTAssertEqual(components.day, 25)
        XCTAssertEqual(components.month, 8)
    }

    func testEnglishAttachedMarkerAlsoParses() {
        let result = WhatsAppChatParser.parse("[01/02/24, 08:00:00] Ana Demo: <attached: 00000003-IMAGE-2024.jpg>")
        XCTAssertEqual(result.messages.first?.attachmentFilename, "00000003-IMAGE-2024.jpg")
    }

    func testSpanishMeridiemTimeParsesToCorrectHour() {
        let result = WhatsAppChatParser.parse(androidSample)
        guard let date = result.messages.first?.date else { return XCTFail("Se esperaba una fecha para \"9:16 a. m.\"") }
        let hour = Calendar(identifier: .gregorian).component(.hour, from: date)
        XCTAssertEqual(hour, 9)
    }

    func testEmptyInputProducesNoMessages() {
        XCTAssertTrue(WhatsAppChatParser.parse("").messages.isEmpty)
    }
}
