import SwiftUI
import SwiftData
import PhotosUI
import CoreLocation
import UniformTypeIdentifiers
import ArgosCore

/// Captura Rápida (sección 23): botón flotante "+" que añade información al
/// caso seleccionado sin navegar por múltiples pantallas. Todas las
/// opciones convergen en `IngestionService`, igual que la Share Extension,
/// para que la trazabilidad sea idéntica sin importar el punto de entrada.
struct QuickCaptureView: View {
    @Environment(\.modelContext) private var context
    @Environment(\.dismiss) private var dismiss
    @EnvironmentObject private var session: AppSession
    @Query(sort: \CaseEntity.name) private var cases: [CaseEntity]

    let preselectedCase: CaseEntity?

    @State private var targetCase: CaseEntity?
    @State private var photoPickerItem: PhotosPickerItem?
    @State private var noteText = ""
    @State private var statusMessage: String?
    @State private var locationFetcher = OneShotLocationFetcher()

    var body: some View {
        NavigationStack {
            Form {
                Section("Caso") {
                    Picker("Caso destino", selection: $targetCase) {
                        Text("Bandeja de entrada (sin clasificar)").tag(CaseEntity?.none)
                        ForEach(cases) { c in
                            Text("\(c.name) (\(c.argosCaseCode))").tag(CaseEntity?.some(c))
                        }
                    }
                }

                Section("Fotografía / Video") {
                    PhotosPicker(selection: $photoPickerItem, matching: .any(of: [.images, .videos])) {
                        Label("Seleccionar de la fototeca", systemImage: "photo.on.rectangle")
                    }
                    .onChange(of: photoPickerItem) { _, newValue in
                        Task { await ingestPhotoPickerItem(newValue) }
                    }
                }

                Section("Documento") {
                    Button {
                        showingDocumentPicker = true
                    } label: {
                        Label("Escoger documento", systemImage: "doc.badge.plus")
                    }
                }

                Section("Ubicación") {
                    Button {
                        Task { await ingestCurrentLocation() }
                    } label: {
                        Label("Guardar ubicación actual", systemImage: "mappin.and.ellipse")
                    }
                }

                Section("Nota") {
                    TextField("¿Qué representa este elemento?", text: $noteText, axis: .vertical)
                    Button("Guardar nota") { ingestNote() }
                        .disabled(noteText.trimmingCharacters(in: .whitespaces).isEmpty)
                }

                if let statusMessage {
                    Text(statusMessage).foregroundStyle(ArgosTheme.validatedGreen)
                }
            }
            .navigationTitle("Captura rápida")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cerrar") { dismiss() }
                }
            }
            .fileImporter(isPresented: $showingDocumentPicker, allowedContentTypes: [.item], allowsMultipleSelection: false) { result in
                Task { await ingestDocumentPickerResult(result) }
            }
        }
        .onAppear { targetCase = preselectedCase }
    }

    @State private var showingDocumentPicker = false

    private func resolveCase() -> CaseEntity {
        if let targetCase { return targetCase }
        if let inbox = cases.first(where: { $0.argosCaseCode == InboxCaseCode.value }) { return inbox }
        let inbox = CaseEntity(argosCaseCode: InboxCaseCode.value, name: "Bandeja de entrada")
        context.insert(inbox)
        return inbox
    }

    private func ingest(fileAt url: URL, filename: String, source: String, cleanupTemp: Bool) {
        let caseEntity = resolveCase()
        let service = IngestionService(context: context, currentUser: session.currentAnalyst)
        do {
            let item = try service.ingest(fileAt: url, originalFilename: filename, into: caseEntity, source: source)
            statusMessage = "Guardado como \(item.argosIdentifier)"
        } catch {
            statusMessage = "Error al guardar: \(error.localizedDescription)"
        }
        if cleanupTemp { try? FileManager.default.removeItem(at: url) }
    }

    private func ingestPhotoPickerItem(_ pickerItem: PhotosPickerItem?) async {
        guard let pickerItem else { return }
        guard let data = try? await pickerItem.loadTransferable(type: Data.self) else { return }

        let utType = pickerItem.supportedContentTypes.first
        let ext = utType?.preferredFilenameExtension ?? "dat"
        let filename = "captura_\(Int(Date().timeIntervalSince1970)).\(ext)"
        let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent(filename)
        try? data.write(to: tempURL)
        ingest(fileAt: tempURL, filename: filename, source: "Captura rápida", cleanupTemp: true)
        photoPickerItem = nil
    }

    private func ingestDocumentPickerResult(_ result: Result<[URL], Error>) async {
        guard case .success(let urls) = result, let url = urls.first else { return }
        let accessed = url.startAccessingSecurityScopedResource()
        defer { if accessed { url.stopAccessingSecurityScopedResource() } }
        ingest(fileAt: url, filename: url.lastPathComponent, source: "Captura rápida", cleanupTemp: false)
    }

    private func ingestNote() {
        let text = noteText.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty else { return }
        let filename = "nota_\(Int(Date().timeIntervalSince1970)).txt"
        let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent(filename)
        try? text.write(to: tempURL, atomically: true, encoding: .utf8)
        ingest(fileAt: tempURL, filename: filename, source: "Captura rápida — nota", cleanupTemp: true)
        noteText = ""
    }

    private func ingestCurrentLocation() async {
        do {
            let coordinate = try await locationFetcher.fetchCurrentLocation()
            let filename = "ubicacion_\(Int(Date().timeIntervalSince1970)).txt"
            let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent(filename)
            let content = "latitud: \(coordinate.latitude)\nlongitud: \(coordinate.longitude)\nfecha: \(Date())"
            try content.write(to: tempURL, atomically: true, encoding: .utf8)

            let caseEntity = resolveCase()
            let service = IngestionService(context: context, currentUser: session.currentAnalyst)
            let item = try service.ingest(
                fileAt: tempURL, originalFilename: filename, into: caseEntity,
                source: "Captura rápida — ubicación", userSuppliedType: .location
            )
            item.latitude = coordinate.latitude
            item.longitude = coordinate.longitude
            statusMessage = "Ubicación guardada como \(item.argosIdentifier)"
            try? FileManager.default.removeItem(at: tempURL)
        } catch {
            statusMessage = "No fue posible obtener la ubicación: \(error.localizedDescription)"
        }
    }
}

/// Envoltura mínima de CoreLocation para una sola lectura de posición,
/// usada por la opción "Guardar ubicación actual" (sección 16).
@MainActor
final class OneShotLocationFetcher: NSObject, CLLocationManagerDelegate {
    private let manager = CLLocationManager()
    private var continuation: CheckedContinuation<CLLocationCoordinate2D, Error>?

    func fetchCurrentLocation() async throws -> CLLocationCoordinate2D {
        manager.delegate = self
        manager.requestWhenInUseAuthorization()
        return try await withCheckedThrowingContinuation { continuation in
            self.continuation = continuation
            manager.requestLocation()
        }
    }

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        continuation?.resume(returning: location.coordinate)
        continuation = nil
    }

    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        continuation?.resume(throwing: error)
        continuation = nil
    }
}
