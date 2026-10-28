import SwiftUI

/// Las cuatro áreas de la pantalla inicial (sección 20): Bandeja de
/// Entrada, Casos, Buscador, Actividad. `NavigationSplitView` da el
/// "panel lateral + contenido principal" pedido en la sección 22 para
/// iPad mini, y se degrada automáticamente a navegación por pestañas en
/// iPhone en tamaños compactos.
struct RootView: View {
    enum Section: String, CaseIterable, Identifiable {
        case inbox = "Bandeja de entrada"
        case cases = "Casos"
        case search = "Buscador"
        case activity = "Actividad"

        var id: String { rawValue }

        var systemImage: String {
            switch self {
            case .inbox: return "tray.full"
            case .cases: return "folder"
            case .search: return "magnifyingglass"
            case .activity: return "clock.arrow.circlepath"
            }
        }
    }

    @State private var selection: Section? = .inbox
    @State private var showingQuickCapture = false
    @State private var selectedCase: CaseEntity?

    var body: some View {
        NavigationSplitView {
            List(Section.allCases, selection: $selection) { section in
                Label(section.rawValue, systemImage: section.systemImage)
                    .tag(section)
            }
            .navigationTitle("ARGOS INTAKE")
            .listStyle(.sidebar)
            .scrollContentBackground(.hidden)
            .background(ArgosTheme.background)
        } detail: {
            ZStack(alignment: .bottomTrailing) {
                detailView
                    .argosBackground()

                QuickCaptureButton { showingQuickCapture = true }
                    .padding(24)
            }
        }
        .tint(ArgosTheme.cyan)
        .sheet(isPresented: $showingQuickCapture) {
            QuickCaptureView(preselectedCase: selectedCase)
        }
    }

    @ViewBuilder
    private var detailView: some View {
        switch selection {
        case .inbox, nil:
            InboxView()
        case .cases:
            CasesListView(onSelect: { selectedCase = $0 })
        case .search:
            SearchView()
        case .activity:
            ActivityView()
        }
    }
}

/// Botón flotante "+" de Captura Rápida (sección 23), presente en cualquier
/// pantalla principal para no obligar a navegar antes de capturar algo en
/// campo.
private struct QuickCaptureButton: View {
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Image(systemName: "plus")
                .font(.title2.bold())
                .foregroundStyle(.black)
                .frame(width: 56, height: 56)
                .background(ArgosTheme.cyan, in: Circle())
                .shadow(radius: 8)
        }
        .accessibilityLabel("Captura rápida")
    }
}
