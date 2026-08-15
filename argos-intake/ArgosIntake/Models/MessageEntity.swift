import Foundation
import SwiftData
import ArgosCore

/// Un mensaje individual dentro de una conversación importada (sección 5,
/// entidad MESSAGE de la sección 38). No lleva un `ArgosIdentifier` propio
/// — sería un volumen desproporcionado de identificadores de nivel
/// superior para lo que es, en esencia, una línea de una fuente ya
/// identificada (`chatRef.originalItem`); su trazabilidad viene de esa
/// relación y de `rawLine`, que preserva el texto original verbatim.
///
/// Cuando el mensaje referencia un adjunto y el archivo correspondiente se
/// localiza dentro del paquete exportado, `linkedItem` apunta al
/// `ItemEntity` que preserva ese archivo de forma independiente — con su
/// propio hash e ID ARGOS — completando la cadena archivo → mensaje →
/// conversación exigida por el instructivo.
@Model
final class MessageEntity {
    @Attribute(.unique) var id: UUID

    var chatRef: ChatImportEntity?
    var caseArgosCode: String
    var sequenceIndex: Int

    var timestamp: Date?
    var sender: String?
    var isSystemEvent: Bool
    var body: String?

    /// Nombre de archivo tal como aparece en el `.txt` (p. ej.
    /// "00000001-PHOTO-2024-01-01.jpg"), antes de intentar vincularlo.
    var attachmentFilename: String?
    var linkedItem: ItemEntity?

    /// Línea (o líneas, si el mensaje era multilínea) tal como aparecían en
    /// el archivo original, sin normalizar — para auditar cualquier
    /// desacuerdo con la interpretación automática.
    var rawLine: String

    init(
        caseArgosCode: String,
        sequenceIndex: Int,
        timestamp: Date?,
        sender: String?,
        isSystemEvent: Bool,
        body: String?,
        attachmentFilename: String?,
        rawLine: String
    ) {
        self.id = UUID()
        self.caseArgosCode = caseArgosCode.uppercased()
        self.sequenceIndex = sequenceIndex
        self.timestamp = timestamp
        self.sender = sender
        self.isSystemEvent = isSystemEvent
        self.body = body
        self.attachmentFilename = attachmentFilename
        self.linkedItem = nil
        self.rawLine = rawLine
    }
}
