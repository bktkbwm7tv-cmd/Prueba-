import UIKit
import SwiftUI
import SwiftData

/// Punto de entrada de la Share Extension "Guardar en ARGOS" (sección 4).
/// Su única responsabilidad es extraer los adjuntos del `NSExtensionItem`
/// que iOS le entrega y delegar toda la interfaz a `ShareFlowView`.
final class ShareViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        let attachments = (extensionContext?.inputItems as? [NSExtensionItem])?
            .compactMap(\.attachments)
            .flatMap { $0 } ?? []

        let container: ModelContainer
        do {
            container = try Self.makeSharedModelContainer()
        } catch {
            extensionContext?.cancelRequest(withError: error)
            return
        }

        let rootView = ShareFlowView(
            providers: attachments,
            onFinish: { [weak self] in self?.extensionContext?.completeRequest(returningItems: nil) },
            onCancel: { [weak self] in
                self?.extensionContext?.cancelRequest(withError: NSError(domain: "mx.argos.intake", code: -1))
            }
        )
        .modelContainer(container)

        let hosting = UIHostingController(rootView: rootView)
        addChild(hosting)
        view.addSubview(hosting.view)
        hosting.view.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            hosting.view.topAnchor.constraint(equalTo: view.topAnchor),
            hosting.view.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            hosting.view.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            hosting.view.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
        hosting.didMove(toParent: self)
    }

    /// Mismo store SwiftData que la app principal, vía App Group — la
    /// extensión y la app comparten un único almacenamiento local
    /// (sección 27: local-first).
    private static func makeSharedModelContainer() throws -> ModelContainer {
        let schema = Schema([
            CaseEntity.self,
            ItemEntity.self,
            TagEntity.self,
            AuditLogEntity.self
        ])
        guard let groupURL = FileManager.default
            .containerURL(forSecurityApplicationGroupIdentifier: FileStorageService.appGroupIdentifier)
        else {
            throw FileStorageError.appGroupContainerUnavailable
        }
        let configuration = ModelConfiguration(schema: schema, url: groupURL.appendingPathComponent("ArgosIntake.store"))
        return try ModelContainer(for: schema, configurations: [configuration])
    }
}
