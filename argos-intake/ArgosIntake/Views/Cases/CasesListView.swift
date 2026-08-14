import SwiftUI
import SwiftData
import ArgosCore

/// Expedientes activos (sección 20). Cada fila resume la ficha maestra del
/// caso (sección 8): estatus, prioridad y número de ítems incorporados.
struct CasesListView: View {
    @Query(sort: \CaseEntity.updatedAt, order: .reverse) private var cases: [CaseEntity]
    @State private var showingNewCase = false

    let onSelect: (CaseEntity) -> Void

    var body: some View {
        Group {
            if cases.isEmpty {
                ContentUnavailableView(
                    "Sin casos",
                    systemImage: "folder.badge.plus",
                    description: Text("Crea un caso para empezar a incorporar información.")
                )
                .foregroundStyle(ArgosTheme.textSecondary)
            } else {
                List(cases) { caseEntity in
                    NavigationLink {
                        CaseDetailView(caseEntity: caseEntity)
                            .onAppear { onSelect(caseEntity) }
                    } label: {
                        CaseRow(caseEntity: caseEntity)
                    }
                    .listRowBackground(ArgosTheme.surface)
                }
                .scrollContentBackground(.hidden)
            }
        }
        .navigationTitle("Casos")
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button {
                    showingNewCase = true
                } label: {
                    Label("Nuevo caso", systemImage: "plus")
                }
            }
        }
        .sheet(isPresented: $showingNewCase) {
            NewCaseView()
        }
    }
}

private struct CaseRow: View {
    let caseEntity: CaseEntity

    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text(caseEntity.name)
                    .font(.headline)
                    .foregroundStyle(ArgosTheme.textPrimary)
                Text("\(caseEntity.argosCaseCode) · \(caseEntity.items.count) elementos")
                    .font(.caption)
                    .foregroundStyle(ArgosTheme.textSecondary)
            }
            Spacer()
            VStack(alignment: .trailing, spacing: 4) {
                Text(caseEntity.estatus.rawValue)
                    .font(.caption2)
                    .foregroundStyle(ArgosTheme.textSecondary)
                Circle()
                    .fill(ArgosTheme.color(for: caseEntity.prioridad))
                    .frame(width: 10, height: 10)
            }
        }
        .padding(.vertical, 4)
    }
}
