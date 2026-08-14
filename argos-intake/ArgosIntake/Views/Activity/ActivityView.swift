import SwiftUI
import SwiftData
import ArgosCore

/// Últimos eventos e incorporaciones (sección 20), respaldados por la
/// bitácora de auditoría (sección 12) — es la misma fuente de datos, solo
/// que aquí se presenta como actividad reciente en lugar de bitácora cruda.
struct ActivityView: View {
    @Environment(\.modelContext) private var context
    @State private var events: [AuditLogEntity] = []

    private let dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "dd/MM/yyyy HH:mm:ss"
        return formatter
    }()

    var body: some View {
        List(events) { event in
            VStack(alignment: .leading, spacing: 4) {
                HStack {
                    Text(event.action.rawValue)
                        .font(.caption.bold())
                        .foregroundStyle(ArgosTheme.cyan)
                    Spacer()
                    Text(dateFormatter.string(from: event.timestamp))
                        .font(.caption2)
                        .foregroundStyle(ArgosTheme.textSecondary)
                }
                if let itemFilename = event.itemFilename {
                    Text(itemFilename).foregroundStyle(ArgosTheme.textPrimary)
                }
                HStack(spacing: 8) {
                    Text("Usuario: \(event.user)")
                    if let caseCode = event.caseCode { Text("Caso: \(caseCode)") }
                }
                .font(.caption2)
                .foregroundStyle(ArgosTheme.textSecondary)
            }
            .listRowBackground(ArgosTheme.surface)
        }
        .scrollContentBackground(.hidden)
        .navigationTitle("Actividad")
        .task(loadEvents)
        .refreshable { await loadEvents() }
    }

    @Sendable
    private func loadEvents() async {
        events = (try? AuditLogService(context: context).recentEvents()) ?? []
    }
}
