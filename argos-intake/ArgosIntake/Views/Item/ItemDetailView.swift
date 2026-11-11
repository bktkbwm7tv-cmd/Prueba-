import SwiftUI
import SwiftData
import ArgosCore

/// Ficha de archivo (secciones 15 y 39): imagen/preview, archivo original,
/// fecha, tamaño, hash, caso, chat de origen, remitente, etiquetas, notas.
/// El original nunca se edita desde aquí — solo se editan metadatos
/// administrativos (notas, etiquetas, estatus de verificación).
struct ItemDetailView: View {
    @Bindable var item: ItemEntity
    @Environment(\.modelContext) private var context
    @EnvironmentObject private var session: AppSession

    @State private var showingTechnicalDetails = false
    @State private var isRunningOCR = false
    @State private var ocrErrorMessage: String?
    @State private var isRunningExtraction = false
    @State private var extractionMessage: String?

    var body: some View {
        Form {
            Section {
                VStack(alignment: .leading, spacing: 4) {
                    Text(item.originalFilename).font(.headline).foregroundStyle(ArgosTheme.textPrimary)
                    Text(item.argosIdentifier).font(.caption.monospaced()).foregroundStyle(ArgosTheme.cyan)
                }
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Clasificación") {
                Picker("Tipo", selection: Binding(get: { item.type }, set: { item.type = $0 })) {
                    ForEach(ItemType.allCases, id: \.self) { Text($0.displayName).tag($0) }
                }
                Picker("Subtipo", selection: Binding(get: { item.subtype }, set: { item.subtype = $0 })) {
                    Text("Sin especificar").tag(ItemSubtype?.none)
                    ForEach(ItemSubtype.allCases, id: \.self) { Text($0.displayName).tag(ItemSubtype?.some($0)) }
                }
                Picker("Verificación", selection: Binding(get: { item.verificationStatus }, set: { updateVerification($0) })) {
                    ForEach(VerificationStatus.allCases, id: \.self) { Text($0.rawValue).tag($0) }
                }
            }
            .listRowBackground(ArgosTheme.surface)

            if item.type == .location {
                Section("Punto en el mapa (sección 16)") {
                    Picker("Tipo de punto", selection: Binding(get: { item.locationPointKind }, set: { item.locationPointKind = $0 })) {
                        Text("Sin clasificar").tag(LocationPointKind?.none)
                        ForEach(LocationPointKind.allCases, id: \.self) { kind in
                            Label(kind.displayName, systemImage: kind.symbolName).tag(LocationPointKind?.some(kind))
                        }
                    }
                    if let latitude = item.latitude, let longitude = item.longitude {
                        LabeledContent("Coordenadas", value: String(format: "%.6f, %.6f", latitude, longitude))
                    } else {
                        Text("Sin coordenadas registradas.").font(.caption).foregroundStyle(ArgosTheme.textSecondary)
                    }
                }
                .listRowBackground(ArgosTheme.surface)
            }

            Section("Origen") {
                LabeledContent("Caso", value: item.caseArgosCode)
                LabeledContent("Fuente", value: item.source)
                if let chat = item.sourceChat { LabeledContent("Chat de origen", value: chat) }
                if let sender = item.sourceSender { LabeledContent("Remitente", value: sender) }
                LabeledContent("Importado", value: item.importedAt.formatted(date: .abbreviated, time: .shortened))
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Etiquetas") {
                TagPickerView(selectedTags: Binding(get: { item.tags }, set: { item.tags = $0 }))
            }
            .listRowBackground(ArgosTheme.surface)

            Section("Nota — ¿qué representa este archivo?") {
                TextField("Nota", text: Binding(get: { item.notes ?? "" }, set: { item.notes = $0.isEmpty ? nil : $0 }), axis: .vertical)
            }
            .listRowBackground(ArgosTheme.surface)

            if isOCREligible {
                Section("Texto extraído (OCR)") {
                    if let ocrText = item.ocrText, !ocrText.isEmpty {
                        Text(ocrText)
                            .font(.caption)
                            .foregroundStyle(ArgosTheme.textSecondary)
                            .lineLimit(8)
                        if let confidence = item.ocrConfidence {
                            LabeledContent("Confianza", value: "\(Int((confidence * 100).rounded()))%")
                        }
                    } else {
                        Text("Sin texto extraído todavía.")
                            .font(.caption)
                            .foregroundStyle(ArgosTheme.textSecondary)
                    }

                    Button {
                        Task { await runOCR() }
                    } label: {
                        Label(
                            isRunningOCR ? "Extrayendo texto…" : (item.ocrText == nil ? "Extraer texto (OCR)" : "Volver a extraer"),
                            systemImage: "text.viewfinder"
                        )
                    }
                    .disabled(isRunningOCR)

                    if let ocrErrorMessage {
                        Text(ocrErrorMessage).font(.caption).foregroundStyle(ArgosTheme.alertRed)
                    }
                }
                .listRowBackground(ArgosTheme.surface)
            }

            entitiesSection

            Section {
                DisclosureGroup("Detalles técnicos", isExpanded: $showingTechnicalDetails) {
                    LabeledContent("Extensión", value: item.fileExtension)
                    LabeledContent("Tamaño", value: ByteCountFormatter.string(fromByteCount: item.sizeBytes, countStyle: .file))
                    LabeledContent("SHA-256", value: item.sha256).font(.caption.monospaced())
                    LabeledContent("Nombre almacenado", value: item.storedFilename).font(.caption)
                    LabeledContent("Estatus de clasificación", value: item.classificationStatus.rawValue)
                    LabeledContent("Estatus en bandeja", value: item.inboxStatus.rawValue)
                }
            }
            .listRowBackground(ArgosTheme.surface)
        }
        .scrollContentBackground(.hidden)
        .navigationTitle("Ficha del elemento")
    }

    @ViewBuilder
    private var entitiesSection: some View {
        Section("Entidades detectadas (ARGOS EXTRACT)") {
            Text("Propuestas automáticas — ninguna se trata como hecho confirmado hasta que la revises.")
                .font(.caption)
                .foregroundStyle(ArgosTheme.textSecondary)

            EntityCandidateGroupedList(candidates: item.entityCandidates, onConfirm: confirm, onReject: reject)

            Button {
                Task { await runEntityExtraction() }
            } label: {
                Label(isRunningExtraction ? "Analizando…" : "Detectar entidades", systemImage: "sparkle.magnifyingglass")
            }
            .disabled(isRunningExtraction || (item.ocrText == nil && item.notes == nil))

            if let extractionMessage {
                Text(extractionMessage).font(.caption).foregroundStyle(ArgosTheme.textSecondary)
            }
        }
        .listRowBackground(ArgosTheme.surface)
    }

    private func runEntityExtraction() async {
        isRunningExtraction = true
        extractionMessage = nil
        defer { isRunningExtraction = false }

        let service = EntityExtractionService(context: context, currentUser: session.currentAnalyst)
        let created = service.extractEntities(for: item)
        extractionMessage = created.isEmpty
            ? "No se detectaron entidades nuevas."
            : "\(created.count) entidad(es) nueva(s) propuesta(s)."
    }

    private func confirm(_ candidate: EntityCandidateEntity) {
        candidate.status = .verificado
        candidate.reviewedAt = Date()
        candidate.reviewedBy = session.currentAnalyst
        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: item.caseArgosCode,
            itemFilename: item.originalFilename,
            detail: "Entidad confirmada: \(candidate.label) \"\(candidate.value)\""
        )
    }

    private func reject(_ candidate: EntityCandidateEntity) {
        candidate.status = .descartado
        candidate.reviewedAt = Date()
        candidate.reviewedBy = session.currentAnalyst
        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: item.caseArgosCode,
            itemFilename: item.originalFilename,
            detail: "Entidad descartada: \(candidate.label) \"\(candidate.value)\""
        )
    }

    private var isOCREligible: Bool {
        item.type == .image || (item.type == .document && item.fileExtension.lowercased() == "pdf")
    }

    private func runOCR() async {
        isRunningOCR = true
        ocrErrorMessage = nil
        defer { isRunningOCR = false }

        let storage = FileStorageService()
        do {
            let result = try await OCRService().extractText(from: item, storage: storage)
            item.ocrText = result.text
            item.ocrConfidence = result.confidence

            if let derived = try? storage.storeDerived(
                data: Data(result.text.utf8),
                caseCode: item.caseArgosCode,
                itemId: item.itemId,
                filename: "\(item.itemId.uuidString)_ocr.txt"
            ) {
                item.ocrRelativePath = derived.relativePath
            }

            AuditLogService(context: context).record(
                user: session.currentAnalyst,
                action: .extraccionDeTexto,
                caseCode: item.caseArgosCode,
                itemFilename: item.originalFilename,
                sha256: item.sha256,
                detail: "OCR: \(result.text.count) caracteres extraídos"
            )
        } catch OCRError.noTextFound {
            ocrErrorMessage = "No se detectó texto en este archivo."
        } catch {
            ocrErrorMessage = "No se pudo extraer texto: \(error.localizedDescription)"
        }
    }

    private func updateVerification(_ newValue: VerificationStatus) {
        item.verificationStatus = newValue
        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: item.caseArgosCode,
            itemFilename: item.originalFilename,
            sha256: item.sha256,
            detail: "Verificación → \(newValue.rawValue)"
        )
    }
}
