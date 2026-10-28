import SwiftUI
import SwiftData
import ArgosCore

/// Módulo de Coincidencias ARGOS (sección 19): entidades que ARGOS EXTRACT
/// propuso en más de un caso. Se presenta explícitamente como algo por
/// analizar, nunca como una vinculación confirmada — ese es el límite que
/// marca el instructivo, y esta pantalla no lo cruza en ningún texto.
struct CoincidenciasView: View {
    @Environment(\.modelContext) private var context
    @State private var groups: [CoincidenceGroup] = []
    @State private var errorMessage: String?

    private var groupsByCategory: [(EntityCategory, [CoincidenceGroup])] {
        Dictionary(grouping: groups, by: \.category)
            .sorted { $0.key.rawValue < $1.key.rawValue }
    }

    var body: some View {
        Group {
            if let errorMessage {
                ContentUnavailableView("No se pudo cargar", systemImage: "exclamationmark.triangle", description: Text(errorMessage))
                    .foregroundStyle(ArgosTheme.textSecondary)
            } else if groups.isEmpty {
                ContentUnavailableView(
                    "Sin coincidencias",
                    systemImage: "point.3.connected.trianglepath.dotted",
                    description: Text("Ninguna entidad confirmada o propuesta por ARGOS EXTRACT aparece todavía en más de un caso.")
                )
                .foregroundStyle(ArgosTheme.textSecondary)
            } else {
                List {
                    Section {
                        Text("Coincidencia de información susceptible de análisis. Ninguna de estas entradas implica, por sí sola, una vinculación entre casos — corresponde al analista determinarlo.")
                            .font(.caption)
                            .foregroundStyle(ArgosTheme.textSecondary)
                    }
                    .listRowBackground(ArgosTheme.surface)

                    ForEach(groupsByCategory, id: \.0) { category, groupsInCategory in
                        Section("\(category.displayName) (\(groupsInCategory.count))") {
                            ForEach(groupsInCategory) { group in
                                CoincidenceGroupRow(group: group)
                            }
                        }
                        .listRowBackground(ArgosTheme.surface)
                    }
                }
                .scrollContentBackground(.hidden)
            }
        }
        .navigationTitle("Coincidencias ARGOS")
        .argosBackground()
        .task(loadCoincidences)
        .refreshable { await loadCoincidences() }
    }

    @Sendable
    private func loadCoincidences() async {
        do {
            groups = try CoincidenciasService(context: context).findCoincidences()
            errorMessage = nil
        } catch {
            errorMessage = error.localizedDescription
        }
    }
}

private struct CoincidenceGroupRow: View {
    let group: CoincidenceGroup

    var body: some View {
        DisclosureGroup {
            ForEach(group.occurrencesByCase, id: \.caseEntity.persistentModelID) { entry in
                NavigationLink {
                    CaseDetailView(caseEntity: entry.caseEntity)
                } label: {
                    HStack {
                        VStack(alignment: .leading, spacing: 2) {
                            Text(entry.caseEntity.name).foregroundStyle(ArgosTheme.textPrimary)
                            Text(entry.caseEntity.argosCaseCode).font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
                        }
                        Spacer()
                        statusSummary(for: entry.candidates)
                    }
                }
            }
        } label: {
            HStack {
                Text(group.value).font(.subheadline.monospaced()).foregroundStyle(ArgosTheme.cyan)
                Spacer()
                Text("\(group.caseCount) casos")
                    .font(.caption2.bold())
                    .padding(.horizontal, 7).padding(.vertical, 2)
                    .background(ArgosTheme.surfaceElevated, in: Capsule())
                    .foregroundStyle(ArgosTheme.textSecondary)
            }
        }
    }

    private func statusSummary(for candidates: [EntityCandidateEntity]) -> some View {
        let verifiedCount = candidates.filter { $0.status == .verificado }.count
        return Text(verifiedCount > 0 ? "\(verifiedCount)/\(candidates.count) verificada(s)" : "\(candidates.count) propuesta(s)")
            .font(.caption2)
            .foregroundStyle(verifiedCount > 0 ? ArgosTheme.validatedGreen : ArgosTheme.textSecondary)
    }
}
