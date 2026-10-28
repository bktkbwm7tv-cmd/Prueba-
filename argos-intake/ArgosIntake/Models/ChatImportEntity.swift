import Foundation
import SwiftData
import ArgosCore

/// Una importación de chat de WhatsApp (sección 5, segunda modalidad de
/// ingesta junto a la Share Extension). Representa la conversación como un
/// todo — nombre, participantes, rango de fechas — y es el punto de
/// reconstrucción intermedio en la cadena exigida por el instructivo:
/// archivo → mensaje → **conversación** → importación → caso.
///
/// `originalItem` es el `.txt`/`.zip` tal como se importó, preservado por
/// `FileStorageService` igual que cualquier otro original (sección 5.1:
/// "preservar el paquete original") — nunca se modifica ni se sustituye
/// por los mensajes ya parseados.
@Model
final class ChatImportEntity {
    @Attribute(.unique) var id: UUID

    var caseArgosCode: String
    var caseRef: CaseEntity?

    /// Nombre editable por el analista; por defecto, el nombre del archivo
    /// importado (WhatsApp no incluye el nombre del chat dentro del texto).
    var chatName: String
    var participants: [String]
    var importedAt: Date

    var originalItem: ItemEntity?

    var dateRangeStart: Date?
    var dateRangeEnd: Date?

    @Relationship(deleteRule: .cascade, inverse: \MessageEntity.chatRef)
    var messages: [MessageEntity] = []

    var messageCount: Int { messages.count }

    init(caseArgosCode: String, chatName: String, participants: [String] = []) {
        self.id = UUID()
        self.caseArgosCode = caseArgosCode.uppercased()
        self.chatName = chatName
        self.participants = participants
        self.importedAt = Date()
        self.dateRangeStart = nil
        self.dateRangeEnd = nil
    }
}
