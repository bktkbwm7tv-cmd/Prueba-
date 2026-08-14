import Foundation
import SwiftData
import ArgosCore

enum IngestionError: Error {
    case caseNotFound(String)
}

/// Orquesta el flujo completo de un archivo entrante hasta convertirse en
/// un `ItemEntity` trazable (secciones 4, 6, 9, 10, 11):
///
/// 1. clasificar por extensión;
/// 2. calcular SHA-256 del archivo tal como llegó;
/// 3. preservar el original (copia, nunca movimiento destructivo);
/// 4. asignar el siguiente `ArgosIdentifier` para (caso, año, tipo);
/// 5. crear el `ItemEntity` y registrar el evento de IMPORTACIÓN en la
///    bitácora.
///
/// Es el mismo camino tanto si el archivo llega por Share Extension, por
/// importación manual o por Captura Rápida — todas las entradas convergen
/// aquí para que la trazabilidad sea uniforme.
struct IngestionService {
    let context: ModelContext
    let storage: FileStorageService
    let currentUser: String

    init(context: ModelContext, storage: FileStorageService = FileStorageService(), currentUser: String) {
        self.context = context
        self.storage = storage
        self.currentUser = currentUser
    }

    @discardableResult
    func ingest(
        fileAt sourceURL: URL,
        originalFilename: String,
        into caseEntity: CaseEntity,
        source: String,
        sourceChat: String? = nil,
        sourceSender: String? = nil,
        userSuppliedType: ItemType? = nil,
        userSuppliedSubtype: ItemSubtype? = nil,
        note: String? = nil,
        tags: [TagEntity] = []
    ) throws -> ItemEntity {
        let classification = FileClassifier.classify(filename: originalFilename)
        let type = userSuppliedType ?? classification.type
        let subtype = userSuppliedSubtype ?? classification.suggestedSubtype

        let sha256 = try FileHasher.sha256Hex(ofFileAt: sourceURL)
        let attributes = try? FileManager.default.attributesOfItem(atPath: sourceURL.path)
        let sizeBytes = (attributes?[.size] as? NSNumber)?.int64Value ?? 0

        let year = Calendar.current.component(.year, from: Date())
        let sequence = nextSequence(caseCode: caseEntity.argosCaseCode, year: year, type: type)
        let argosId = ArgosIdentifierGenerator.next(
            caseCode: caseEntity.argosCaseCode, year: year, type: type,
            highestExistingSequence: sequence - 1
        )

        let itemUUID = UUID()
        let ext = (originalFilename as NSString).pathExtension
        let storedFilename = "\(itemUUID.uuidString).\(ext)"

        let (relativePath, _) = try storage.storeOriginal(
            from: sourceURL, caseCode: caseEntity.argosCaseCode,
            itemId: itemUUID, storedFilename: storedFilename
        )

        let item = ItemEntity(
            argosIdentifier: argosId,
            caseArgosCode: caseEntity.argosCaseCode,
            type: type,
            subtype: subtype,
            originalFilename: originalFilename,
            storedFilename: storedFilename,
            fileExtension: ext,
            mimeType: nil,
            sizeBytes: sizeBytes,
            sha256: sha256,
            source: source,
            originalRelativePath: relativePath
        )
        item.itemId = itemUUID
        item.sourceChat = sourceChat
        item.sourceSender = sourceSender
        item.notes = note
        item.tags = tags
        item.caseRef = caseEntity

        context.insert(item)
        caseEntity.updatedAt = Date()

        AuditLogService(context: context).record(
            user: currentUser,
            action: .importacion,
            caseCode: caseEntity.argosCaseCode,
            itemFilename: originalFilename,
            sha256: sha256,
            detail: "ID: \(argosId.description)"
        )

        return item
    }

    /// Consecutivo por (caso, año, tipo) — sección 9. Se calcula en cada
    /// ingesta a partir de lo ya persistido, evitando llevar un contador
    /// separado que pudiera desincronizarse de los ítems reales.
    private func nextSequence(caseCode: String, year: Int, type: ItemType) -> Int {
        let code = caseCode.uppercased()
        let typeRaw = type.rawValue
        let calendar = Calendar.current
        let yearStart = calendar.date(from: DateComponents(year: year, month: 1, day: 1)) ?? .distantPast
        let yearEnd = calendar.date(from: DateComponents(year: year + 1, month: 1, day: 1)) ?? .distantFuture

        let descriptor = FetchDescriptor<ItemEntity>(
            predicate: #Predicate {
                $0.caseArgosCode == code && $0.typeRaw == typeRaw
                    && $0.createdAt >= yearStart && $0.createdAt < yearEnd
            },
            sortBy: [SortDescriptor(\.sequenceInCaseTypeYear, order: .reverse)]
        )
        var limited = descriptor
        limited.fetchLimit = 1
        let highest = (try? context.fetch(limited).first?.sequenceInCaseTypeYear) ?? 0
        return highest + 1
    }
}
