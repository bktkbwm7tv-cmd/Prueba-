import SwiftUI
import SwiftData
import ArgosCore

/// Selector de etiquetas (sección 4/18-19). Reutilizado en la ficha de
/// archivo y en el flujo de captura/Share Extension. Crear una etiqueta
/// nueva requiere elegir una categoría de la lista cerrada del instructivo
/// — el nombre en sí es texto libre.
struct TagPickerView: View {
    @Environment(\.modelContext) private var context
    @Query(sort: \TagEntity.name) private var allTags: [TagEntity]

    @Binding var selectedTags: [TagEntity]
    @State private var newTagName = ""
    @State private var newTagCategory: TagCategory = .otros

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            if !selectedTags.isEmpty {
                FlowChips(tags: selectedTags) { tag in
                    selectedTags.removeAll { $0.id == tag.id }
                }
            }

            Menu("Agregar etiqueta existente") {
                ForEach(allTags.filter { tag in !selectedTags.contains { $0.id == tag.id } }) { tag in
                    Button("\(tag.name) (\(tag.category.displayName))") {
                        selectedTags.append(tag)
                    }
                }
            }
            .disabled(allTags.isEmpty)

            HStack {
                TextField("Nueva etiqueta", text: $newTagName)
                Picker("Categoría", selection: $newTagCategory) {
                    ForEach(TagCategory.allCases, id: \.self) { Text($0.displayName).tag($0) }
                }
                .pickerStyle(.menu)
                Button("Añadir", action: addNewTag)
                    .disabled(newTagName.trimmingCharacters(in: .whitespaces).isEmpty)
            }
        }
    }

    private func addNewTag() {
        let tag = TagEntity(name: newTagName.trimmingCharacters(in: .whitespaces), category: newTagCategory)
        context.insert(tag)
        selectedTags.append(tag)
        newTagName = ""
    }
}

private struct FlowChips: View {
    let tags: [TagEntity]
    let onRemove: (TagEntity) -> Void

    var body: some View {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 100))], alignment: .leading, spacing: 6) {
            ForEach(tags) { tag in
                HStack(spacing: 4) {
                    Text(tag.name)
                    Button { onRemove(tag) } label: {
                        Image(systemName: "xmark.circle.fill")
                    }
                }
                .font(.caption)
                .padding(.horizontal, 8).padding(.vertical, 4)
                .background(ArgosTheme.surfaceElevated, in: Capsule())
                .foregroundStyle(ArgosTheme.cyan)
            }
        }
    }
}
