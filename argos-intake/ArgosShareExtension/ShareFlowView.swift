import SwiftUI
import SwiftData
import UniformTypeIdentifiers
import ArgosCore

/// Ventana rápida "Guardar en ARGOS" (sección 4). Deliberadamente corta:
/// Caso → Tipo → Etiquetas → Nota → GUARDAR, "el menor número posible de
/// pasos" como exige el instructivo.
struct ShareFlowView: View {
    let providers: [NSItemProvider]
    let onFinish: () -> Void
    let onCancel: () -> Void

    @Environment(\.modelContext) private var context
    @Query(sort: \CaseEntity.name) private var cases: [CaseEntity]

    @State private var selectedCaseCode: String = InboxCaseCode.value
    @State private var newCaseName = ""
    @State private var creatingNewCase = false
    @State private var overrideType: ItemType?
    @State private var selectedTags: [TagEntity] = []
    @State private var note = ""
    @State private var isSaving = false
    @State private var errorMessage: String?
    @State private var loadedFiles: [LoadedFile] = []

    private struct LoadedFile: Identifiable {
        let id = UUID()
        let url: URL
        let filename: String
    }

    var body: some View {
        NavigationStack {
            Form {
                Section("Caso") {
                    Picker("Caso", selection: $selectedCaseCode) {
                        Text("Bandeja de entrada (sin clasificar)").tag(InboxCaseCode.value)
                        ForEach(cases.filter { $0.argosCaseCode != InboxCaseCode.value }) { c in
                            Text("\(c.name) (\(c.argosCaseCode))").tag(c.argosCaseCode)
                        }
                        Text("+ Crear nuevo caso…").tag("__NEW__")
                    }
                    .onChange(of: selectedCaseCode) { _, newValue in
                        creatingNewCase = (newValue == "__NEW__")
                    }
                    if creatingNewCase {
                        TextField("Nombre del nuevo caso", text: $newCaseName)
                    }
                }

                Section("Tipo de información") {
                    Text(loadedFiles.isEmpty ? "Detectando…" : "\(loadedFiles.count) archivo(s) — ARGOS propone el tipo automáticamente por archivo.")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Picker("Forzar tipo (opcional)", selection: $overrideType) {
                        Text("Automático").tag(ItemType?.none)
                        ForEach(ItemType.allCases, id: \.self) { Text($0.displayName).tag(ItemType?.some($0)) }
                    }
                }

                Section("Etiquetas") {
                    TagPickerView(selectedTags: $selectedTags)
                }

                Section("Nota — ¿qué representa este archivo?") {
                    TextField("Nota breve", text: $note, axis: .vertical)
                }

                if let errorMessage {
                    Text(errorMessage).foregroundStyle(.red)
                }
            }
            .navigationTitle("Guardar en ARGOS")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancelar", action: onCancel)
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button(isSaving ? "Guardando…" : "GUARDAR EN ARGOS") { Task { await save() } }
                        .disabled(isSaving || loadedFiles.isEmpty || (creatingNewCase && newCaseName.trimmingCharacters(in: .whitespaces).isEmpty))
                }
            }
            .task { await loadProviders() }
        }
    }

    private func loadProviders() async {
        var results: [LoadedFile] = []
        for provider in providers {
            if let (url, filename) = await Self.materialize(provider: provider) {
                results.append(LoadedFile(url: url, filename: filename))
            }
        }
        loadedFiles = results
        if results.isEmpty {
            errorMessage = "No se pudo leer el contenido compartido."
        }
    }

    /// Copia el contenido entregado por el share sheet de WhatsApp (o
    /// cualquier otra app) a un archivo temporal legible por
    /// `IngestionService`. No se accede a WhatsApp de ninguna otra forma —
    /// solo se procesa lo que el sistema ya nos compartió (ver CLAUDE.md
    /// del instructivo: nunca saltarse las restricciones internas de la app).
    private static func materialize(provider: NSItemProvider) async -> (URL, String)? {
        await withCheckedContinuation { continuation in
            let preferredType = provider.registeredTypeIdentifiers.first ?? UTType.data.identifier
            provider.loadFileRepresentation(forTypeIdentifier: preferredType) { url, error in
                guard let url, error == nil else {
                    continuation.resume(returning: nil)
                    return
                }
                let filename = provider.suggestedName ?? url.lastPathComponent
                let tempURL = FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
                    .appendingPathExtension(url.pathExtension)
                try? FileManager.default.copyItem(at: url, to: tempURL)
                continuation.resume(returning: (tempURL, filename))
            }
        }
    }

    private func resolveCase() -> CaseEntity? {
        if creatingNewCase {
            let code = "C\(Int(Date().timeIntervalSince1970 % 100000))"
            let newCase = CaseEntity(argosCaseCode: code, name: newCaseName.trimmingCharacters(in: .whitespaces))
            context.insert(newCase)
            return newCase
        }
        if selectedCaseCode == InboxCaseCode.value {
            if let inbox = cases.first(where: { $0.argosCaseCode == InboxCaseCode.value }) { return inbox }
            let inbox = CaseEntity(argosCaseCode: InboxCaseCode.value, name: "Bandeja de entrada")
            context.insert(inbox)
            return inbox
        }
        return cases.first { $0.argosCaseCode == selectedCaseCode }
    }

    private func save() async {
        isSaving = true
        defer { isSaving = false }

        guard let caseEntity = resolveCase() else {
            errorMessage = "Selecciona un caso válido."
            return
        }

        let service = IngestionService(context: context, currentUser: "ANALISTA01")
        for file in loadedFiles {
            do {
                _ = try service.ingest(
                    fileAt: file.url,
                    originalFilename: file.filename,
                    into: caseEntity,
                    source: "Share Extension",
                    userSuppliedType: overrideType,
                    note: note.isEmpty ? nil : note,
                    tags: selectedTags
                )
            } catch {
                errorMessage = "Error al guardar \(file.filename): \(error.localizedDescription)"
            }
            try? FileManager.default.removeItem(at: file.url)
        }

        if errorMessage == nil {
            onFinish()
        }
    }
}
