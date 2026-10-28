import SwiftUI
import MapKit
import ArgosCore

/// Mapa del Caso (sección 16): un punto por cada ítem con coordenadas
/// registradas. El tipo de punto (domicilio, avistamiento, vehículo,
/// cámara, banco, cajero, antena, evento, hallazgo, punto de interés) es
/// lo único que diferencia un pin de otro — nunca un color de riesgo,
/// porque esta sección del instructivo no define un semáforo para el mapa
/// de ARGOS INTAKE (a diferencia del mapa nacional de los reportes ARGOS).
struct CaseMapView: View {
    let caseEntity: CaseEntity

    @State private var cameraPosition: MapCameraPosition = .automatic
    @State private var selectedItem: ItemEntity?

    private var locatedItems: [(item: ItemEntity, coordinate: CLLocationCoordinate2D)] {
        caseEntity.items.compactMap { item in
            guard let latitude = item.latitude, let longitude = item.longitude else { return nil }
            return (item, CLLocationCoordinate2D(latitude: latitude, longitude: longitude))
        }
    }

    var body: some View {
        Group {
            if locatedItems.isEmpty {
                ContentUnavailableView(
                    "Sin ubicaciones",
                    systemImage: "map",
                    description: Text("Los elementos con coordenadas — guardados desde Captura Rápida u otra fuente — aparecerán aquí.")
                )
                .foregroundStyle(ArgosTheme.textSecondary)
            } else {
                Map(position: $cameraPosition) {
                    ForEach(locatedItems, id: \.item.persistentModelID) { entry in
                        Annotation(entry.item.originalFilename, coordinate: entry.coordinate) {
                            PointPin(kind: entry.item.locationPointKind ?? .puntoDeInteres)
                                .onTapGesture { selectedItem = entry.item }
                        }
                    }
                }
                .mapStyle(.standard)
            }
        }
        .navigationTitle("Mapa — \(caseEntity.name)")
        .sheet(item: $selectedItem) { item in
            NavigationStack {
                ItemDetailView(item: item)
                    .toolbar {
                        ToolbarItem(placement: .cancellationAction) {
                            Button("Cerrar") { selectedItem = nil }
                        }
                    }
            }
        }
    }
}

private struct PointPin: View {
    let kind: LocationPointKind

    var body: some View {
        ZStack {
            Circle().fill(ArgosTheme.cyan).frame(width: 30, height: 30)
            Image(systemName: kind.symbolName)
                .font(.caption)
                .foregroundStyle(Color(red: 0.02, green: 0.08, blue: 0.13))
        }
        .shadow(radius: 3)
        .accessibilityLabel(kind.displayName)
    }
}
