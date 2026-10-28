import Foundation
import SwiftData
import ArgosCore

/// Etiqueta libre aplicable a ítems y casos (sección 4). El nombre es texto
/// libre ("Cherokee gris", "Luis Enrique") mientras que `category` restringe
/// a la lista cerrada del instructivo para que el buscador y el módulo de
/// coincidencias (sección 19) puedan agrupar por tipo de entidad.
@Model
final class TagEntity {
    @Attribute(.unique) var id: UUID
    var name: String
    var categoryRaw: String
    var createdAt: Date

    @Relationship var items: [ItemEntity] = []
    @Relationship var cases: [CaseEntity] = []

    var category: TagCategory {
        get { TagCategory(rawValue: categoryRaw) ?? .otros }
        set { categoryRaw = newValue.rawValue }
    }

    init(name: String, category: TagCategory) {
        self.id = UUID()
        self.name = name
        self.categoryRaw = category.rawValue
        self.createdAt = Date()
    }
}
