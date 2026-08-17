import Foundation
import SwiftData
import ArgosCore

/// Orquesta ARGOS EXTRACT (sección 13) sobre ítems y sobre mensajes de
/// chats importados: corre los detectores de patrón
/// (`ArgosCore.EntityExtractor`) y de nombres (`PersonNameExtractor`)
/// sobre el texto disponible, y crea una propuesta (`EntityCandidateEntity`)
/// por cada hallazgo nuevo. No reevalúa duplicados ya propuestos para la
/// misma fuente, para que volver a correr la extracción no reviva algo que
/// el analista ya descartó ni duplique lo que ya confirmó.
///
/// El resultado siempre entra como propuesta (`VerificationStatus.recibido`)
/// — nunca como hecho. Confirmar o rechazar es una acción humana separada.
struct EntityExtractionService {
    let context: ModelContext
    let currentUser: String

    @discardableResult
    func extractEntities(for item: ItemEntity) -> [EntityCandidateEntity] {
        var sources: [(text: String, label: String)] = []
        if let ocrText = item.ocrText, !ocrText.isEmpty { sources.append((ocrText, "Texto OCR")) }
        if let notes = item.notes, !notes.isEmpty { sources.append((notes, "Nota")) }
        guard !sources.isEmpty else { return [] }

        let created = detect(in: sources, existing: item.entityCandidates, caseArgosCode: item.caseArgosCode) { entity in
            entity.itemRef = item
        }

        if !created.isEmpty {
            AuditLogService(context: context).record(
                user: currentUser,
                action: .extraccionDeTexto,
                caseCode: item.caseArgosCode,
                itemFilename: item.originalFilename,
                sha256: item.sha256,
                detail: "ARGOS EXTRACT: \(created.count) entidad(es) propuesta(s), pendientes de validación"
            )
        }
        return created
    }

    @discardableResult
    func extractEntities(for message: MessageEntity) -> [EntityCandidateEntity] {
        guard let body = message.body, !body.isEmpty else { return [] }
        let sources = [(text: body, label: "Mensaje de chat")]

        return detect(in: sources, existing: message.entityCandidates, caseArgosCode: message.caseArgosCode) { entity in
            entity.messageRef = message
        }
        // Sin registro de auditoría por mensaje individual — con miles de
        // mensajes por chat, un renglón de bitácora por cada uno sería
        // ruido, no trazabilidad. `extractEntities(forChat:)` registra un
        // solo evento agregado para la conversación completa.
    }

    @discardableResult
    func extractEntities(forChat chat: ChatImportEntity) -> [EntityCandidateEntity] {
        let created = chat.messages.flatMap { extractEntities(for: $0) }

        if !created.isEmpty {
            AuditLogService(context: context).record(
                user: currentUser,
                action: .extraccionDeTexto,
                caseCode: chat.caseArgosCode,
                itemFilename: chat.chatName,
                detail: "ARGOS EXTRACT sobre conversación: \(created.count) entidad(es) propuesta(s) en \(chat.messages.count) mensajes"
            )
        }
        return created
    }

    /// Lógica común: corre ambos detectores sobre cada fuente de texto,
    /// descarta lo que ya existía para esa fuente, e inserta el resto.
    private func detect(
        in sources: [(text: String, label: String)],
        existing: [EntityCandidateEntity],
        caseArgosCode: String,
        link: (EntityCandidateEntity) -> Void
    ) -> [EntityCandidateEntity] {
        let nameExtractor = PersonNameExtractor()
        var seenKeys = Set(existing.map(Self.dedupeKey))

        var created: [EntityCandidateEntity] = []
        for source in sources {
            let candidates = EntityExtractor.extract(from: source.text) + nameExtractor.extract(from: source.text)
            for candidate in candidates {
                let key = "\(candidate.category.rawValue):\(candidate.label):\(candidate.value.lowercased())"
                guard !seenKeys.contains(key) else { continue }
                seenKeys.insert(key)

                let entity = EntityCandidateEntity(
                    caseArgosCode: caseArgosCode, candidate: candidate, sourceLabel: source.label
                )
                link(entity)
                context.insert(entity)
                created.append(entity)
            }
        }
        return created
    }

    private static func dedupeKey(_ entity: EntityCandidateEntity) -> String {
        "\(entity.categoryRaw):\(entity.label):\(entity.value.lowercased())"
    }
}
