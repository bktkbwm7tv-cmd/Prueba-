import SwiftUI
import ArgosCore

/// Una entidad propuesta por ARGOS EXTRACT (sección 13), con acciones para
/// confirmarla o rechazarla — nunca se muestra como un hecho ya validado.
/// Compartida entre `ItemDetailView` y `ChatDetailView`, que son las dos
/// superficies donde ARGOS EXTRACT corre.
struct EntityCandidateRow: View {
    @Bindable var candidate: EntityCandidateEntity
    let onConfirm: () -> Void
    let onReject: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                Text(candidate.label).font(.caption.bold()).foregroundStyle(ArgosTheme.textPrimary)
                Spacer()
                statusPill
            }
            Text(candidate.value).font(.subheadline.monospaced()).foregroundStyle(ArgosTheme.cyan)
            Text(candidate.context).font(.caption2).foregroundStyle(ArgosTheme.textSecondary)
            Text("Fuente: \(candidate.sourceLabel)").font(.caption2).foregroundStyle(ArgosTheme.textSecondary)

            if candidate.status == .recibido {
                HStack {
                    Button("Confirmar", action: onConfirm).font(.caption)
                    Button("Rechazar", role: .destructive, action: onReject).font(.caption)
                }
            }
        }
        .padding(.vertical, 2)
    }

    private var statusPill: some View {
        Text(candidate.status.rawValue)
            .font(.caption2.bold())
            .padding(.horizontal, 6).padding(.vertical, 2)
            .background(ArgosTheme.color(for: candidate.status).opacity(0.18), in: Capsule())
            .foregroundStyle(ArgosTheme.color(for: candidate.status))
    }
}

/// Lista de propuestas agrupadas por categoría (persona, teléfono,
/// vehículo, geografía, financiero, identificador), con estado vacío.
struct EntityCandidateGroupedList: View {
    let candidates: [EntityCandidateEntity]
    let onConfirm: (EntityCandidateEntity) -> Void
    let onReject: (EntityCandidateEntity) -> Void

    private var byCategory: [(EntityCategory, [EntityCandidateEntity])] {
        Dictionary(grouping: candidates, by: \.category)
            .sorted { $0.key.rawValue < $1.key.rawValue }
    }

    var body: some View {
        if candidates.isEmpty {
            Text("Sin entidades detectadas todavía.")
                .font(.caption)
                .foregroundStyle(ArgosTheme.textSecondary)
        } else {
            ForEach(byCategory, id: \.0) { category, items in
                DisclosureGroup("\(category.displayName) (\(items.count))") {
                    ForEach(items, id: \.persistentModelID) { candidate in
                        EntityCandidateRow(
                            candidate: candidate,
                            onConfirm: { onConfirm(candidate) },
                            onReject: { onReject(candidate) }
                        )
                    }
                }
            }
        }
    }
}
