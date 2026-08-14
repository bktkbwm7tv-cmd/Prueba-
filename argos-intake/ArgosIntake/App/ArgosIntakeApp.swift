import SwiftUI
import SwiftData

@main
struct ArgosIntakeApp: App {
    @StateObject private var auth = AuthenticationService()
    @StateObject private var session = AppSession()

    var sharedModelContainer: ModelContainer = {
        let schema = Schema([
            CaseEntity.self,
            ItemEntity.self,
            TagEntity.self,
            AuditLogEntity.self
        ])
        // Almacenamiento local-first (sección 27): el store SwiftData vive en
        // el contenedor del App Group para que la Share Extension pueda
        // escribir ítems directamente sin pasar por la app principal.
        let groupURL = FileManager.default
            .containerURL(forSecurityApplicationGroupIdentifier: FileStorageService.appGroupIdentifier)
        let configuration: ModelConfiguration
        if let groupURL {
            configuration = ModelConfiguration(schema: schema, url: groupURL.appendingPathComponent("ArgosIntake.store"))
        } else {
            configuration = ModelConfiguration(schema: schema)
        }

        do {
            return try ModelContainer(for: schema, configurations: [configuration])
        } catch {
            fatalError("No fue posible inicializar el almacenamiento local de ARGOS INTAKE: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            Group {
                if auth.isUnlocked {
                    RootView()
                        .environmentObject(session)
                } else {
                    LockScreenView()
                }
            }
            .environmentObject(auth)
            .preferredColorScheme(.dark)
        }
        .modelContainer(sharedModelContainer)
    }
}

/// Estado de sesión mínimo (sección 26 — preparado para multiusuario, con
/// un único analista local en MVP1). El nombre se usa como `user` en cada
/// entrada de la bitácora de auditoría.
final class AppSession: ObservableObject {
    @Published var currentAnalyst: String = UserDefaults.standard.string(forKey: "argos.currentAnalyst") ?? "ANALISTA01" {
        didSet { UserDefaults.standard.set(currentAnalyst, forKey: "argos.currentAnalyst") }
    }
}
