import SwiftUI
import SwiftData
import ArgosCore

/// Bandeja de entrada (sección 24): ítems sin caso asignado, o pendientes
/// de revisión dentro de un caso. Permite selección múltiple para mover en
/// bloque a un caso y categoría, como pide el ejemplo del instructivo
/// ("Seleccionar 15 fotografías → mover a Caso X → categoría VEHÍCULOS").
struct InboxView: View {
    @Environment(\.modelContext) private var context
    @Query(sort: \ItemEntity.importedAt, order: .reverse) private var allItems: [ItemEntity]
    @Query(sort: \CaseEntity.name) private var cases: [CaseEntity]

    @State private var selection = Set<PersistentIdentifier>()
    @State private var statusFilter: InboxStatus = .pendiente
    @State private var showingBulkAssign = false

    private var filteredItems: [ItemEntity] {
        allItems.filter { $0.inboxStatus == statusFilter }
    }

    var body: some View {
        VStack(spacing: 0) {
            header

            if filteredItems.isEmpty {
                ContentUnavailableView(
                    "Sin elementos en \"\(statusFilter.rawValue)\"",
                    systemImage: "tray",
                    description: Text("Los archivos compartidos desde WhatsApp u otras apps aparecerán aquí.")
                )
                .foregroundStyle(ArgosTheme.textSecondary)
                Spacer()
            } else {
                List(filteredItems, id: \.persistentModelID, selection: $selection) { item in
                    InboxRow(item: item)
                        .listRowBackground(ArgosTheme.surface)
                }
                .scrollContentBackground(.hidden)
                .environment(\.editMode, .constant(.active))
            }
        }
        .navigationTitle("Bandeja de entrada")
        .toolbar {
            if !selection.isEmpty {
                ToolbarItem(placement: .primaryAction) {
                    Button("Mover a caso (\(selection.count))") { showingBulkAssign = true }
                }
            }
        }
        .sheet(isPresented: $showingBulkAssign) {
            BulkAssignSheet(
                itemIDs: selection,
                cases: cases,
                onComplete: { selection.removeAll() }
            )
        }
    }

    private var header: some View {
        Picker("Estado", selection: $statusFilter) {
            ForEach(InboxStatus.allCases, id: \.self) { status in
                Text(status.rawValue).tag(status)
            }
        }
        .pickerStyle(.segmented)
        .padding()
    }
}

private struct InboxRow: View {
    let item: ItemEntity

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: item.type.symbolName)
                .foregroundStyle(ArgosTheme.cyan)
                .frame(width: 28)

            VStack(alignment: .leading, spacing: 2) {
                Text(item.originalFilename)
                    .foregroundStyle(ArgosTheme.textPrimary)
                Text("\(item.argosIdentifier) · \(item.type.displayName)")
                    .font(.caption)
                    .foregroundStyle(ArgosTheme.textSecondary)
            }

            Spacer()

            Text(item.caseArgosCode)
                .font(.caption2.monospaced())
                .padding(.horizontal, 8).padding(.vertical, 3)
                .background(ArgosTheme.surfaceElevated, in: Capsule())
                .foregroundStyle(ArgosTheme.textSecondary)
        }
    }
}

private struct BulkAssignSheet: View {
    @Environment(\.modelContext) private var context
    @Environment(\.dismiss) private var dismiss

    let itemIDs: Set<PersistentIdentifier>
    let cases: [CaseEntity]
    let onComplete: () -> Void

    @State private var targetCase: CaseEntity?
    @State private var newStatus: InboxStatus = .clasificado

    var body: some View {
        NavigationStack {
            Form {
                Section("Caso destino") {
                    Picker("Caso", selection: $targetCase) {
                        Text("Sin cambio").tag(CaseEntity?.none)
                        ForEach(cases) { c in
                            Text("\(c.name) (\(c.argosCaseCode))").tag(CaseEntity?.some(c))
                        }
                    }
                }
                Section("Nuevo estatus en bandeja") {
                    Picker("Estatus", selection: $newStatus) {
                        ForEach(InboxStatus.allCases, id: \.self) { Text($0.rawValue).tag($0) }
                    }
                }
            }
            .navigationTitle("Mover \(itemIDs.count) elementos")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancelar") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Aplicar") { apply() }
                }
            }
        }
    }

    private func apply() {
        for id in itemIDs {
            guard let item = context.registeredModel(for: id) as ItemEntity? else { continue }
            if let targetCase {
                item.caseRef = targetCase
                item.caseArgosCode = targetCase.argosCaseCode
            }
            item.inboxStatus = newStatus
        }
        onComplete()
        dismiss()
    }
}
