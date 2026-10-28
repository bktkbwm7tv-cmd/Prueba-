import SwiftUI
import SwiftData
import ArgosCore

/// Creación de caso (sección 8/35 — MVP1 punto 1). `argosCaseCode` es el
/// token corto que aparecerá en cada ID ARGOS de este caso, por lo que se
/// valida como único antes de guardar.
struct NewCaseView: View {
    @Environment(\.modelContext) private var context
    @Environment(\.dismiss) private var dismiss
    @EnvironmentObject private var session: AppSession
    @Query private var existingCases: [CaseEntity]

    @State private var name = ""
    @State private var caseCode = ""
    @State private var folio = ""
    @State private var institucion = ""
    @State private var unidad = ""
    @State private var responsable = ""
    @State private var prioridad: PriorityLevel = .media
    @State private var descripcion = ""
    @State private var errorMessage: String?

    var body: some View {
        NavigationStack {
            Form {
                Section("Identificación") {
                    TextField("Nombre del caso", text: $name)
                    TextField("Código corto (p. ej. CFE)", text: $caseCode)
                        .textInputAutocapitalization(.characters)
                    TextField("Número de carpeta de investigación", text: $folio)
                }
                Section("Institución") {
                    TextField("Institución", text: $institucion)
                    TextField("Unidad", text: $unidad)
                    TextField("Responsable", text: $responsable)
                }
                Section("Clasificación") {
                    Picker("Prioridad", selection: $prioridad) {
                        ForEach(PriorityLevel.allCases, id: \.self) { Text($0.rawValue).tag($0) }
                    }
                    TextField("Descripción breve", text: $descripcion, axis: .vertical)
                }
                if let errorMessage {
                    Text(errorMessage).foregroundStyle(ArgosTheme.alertRed)
                }
            }
            .navigationTitle("Nuevo caso")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancelar") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Crear", action: create)
                        .disabled(name.trimmingCharacters(in: .whitespaces).isEmpty || caseCode.trimmingCharacters(in: .whitespaces).isEmpty)
                }
            }
        }
    }

    private func create() {
        let normalizedCode = caseCode.trimmingCharacters(in: .whitespaces).uppercased()
        guard normalizedCode != InboxCaseCode.value else {
            errorMessage = "\"INBOX\" está reservado para la bandeja de entrada."
            return
        }
        guard !existingCases.contains(where: { $0.argosCaseCode == normalizedCode }) else {
            errorMessage = "Ya existe un caso con el código \"\(normalizedCode)\"."
            return
        }

        let newCase = CaseEntity(
            argosCaseCode: normalizedCode,
            name: name.trimmingCharacters(in: .whitespaces),
            folioInvestigacion: folio.isEmpty ? nil : folio,
            institucion: institucion.isEmpty ? nil : institucion,
            unidad: unidad.isEmpty ? nil : unidad,
            responsable: responsable.isEmpty ? nil : responsable,
            prioridad: prioridad,
            descripcionBreve: descripcion.isEmpty ? nil : descripcion
        )
        context.insert(newCase)

        AuditLogService(context: context).record(
            user: session.currentAnalyst,
            action: .cambioDeMetadatosAdministrativos,
            caseCode: normalizedCode,
            detail: "Creación de caso \"\(newCase.name)\""
        )

        dismiss()
    }
}
