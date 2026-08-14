# ARGOS INTAKE

Sistema de Ingesta, Clasificación y Trazabilidad de Información Investigativa.

> De la información dispersa al expediente estructurado.

WhatsApp (u otra app) es un canal de entrada, nunca el repositorio del caso. ARGOS INTAKE
convierte lo que un investigador comparte o importa en un expediente digital preservado,
clasificado, indexado, buscable y auditable — sin modificar jamás el archivo original.

Este directorio implementa el **MVP 1** descrito en la instrucción maestra: creación de casos,
Share Extension ("Guardar en ARGOS"), importación de archivos, bandeja de entrada, clasificación
automática por extensión, preservación del original, SHA-256, fichas de archivo, búsqueda,
etiquetas, Face ID/PIN y almacenamiento local. OCR, extracción de entidades, importación de chats
completos, mapa, timeline, coincidencias entre casos, multiusuario/servidor y ARGOS AI son MVP2/MVP3
y quedan fuera de este alcance a propósito (la propia instrucción maestra lo pide así, sección 35).

## Por qué este código no está compilado ni probado en este entorno

Esta sesión corrió en un contenedor Linux sin Xcode ni el toolchain de Swift para Apple platforms
(no hay `swift`, ni SDK de iOS/macOS, ni simulador). El código se escribió a mano siguiendo las
convenciones idiomáticas de Swift/SwiftUI/SwiftData/CryptoKit, pero **nadie lo ha compilado
todavía**. Antes de darlo por bueno, ábrelo en Xcode en una Mac y corrige lo que el compilador
señale — es razonable esperar errores menores de tipado o de referencias en un proyecto de este
tamaño escrito sin retroalimentación del compilador.

La única pieza que sí se diseñó para poder probarse sin Xcode es `ArgosCore` (ver abajo): lógica
de negocio pura en Swift estándar + [swift-crypto](https://github.com/apple/swift-crypto), sin
UIKit/SwiftUI/SwiftData. En una máquina con el toolchain de Swift para Linux o macOS, se corre con:

```
cd argos-intake
swift test
```

## Arquitectura

```
argos-intake/
  Package.swift                  — paquete SPM ArgosCore (multiplataforma, sin UIKit/SwiftData)
  Sources/ArgosCore/
    Models/                      — ItemType, ItemSubtype, CaseStatus, PriorityLevel,
                                    InboxStatus, VerificationStatus, ClassificationStatus, TagCategory
    Identifiers/ArgosIdentifier  — formato ARGOS-[CASO]-[AÑO]-[TIPO]-[CONSECUTIVO] (sección 9)
    Classification/FileClassifier — clasificación automática por extensión (sección 6)
    Hashing/FileHasher           — SHA-256 en streaming vía swift-crypto/CryptoKit (sección 10-11)
    Search/SearchIndex           — coincidencia de texto normalizado (sección 18)
    Audit/AuditEvent             — catálogo de acciones auditables + AuditLogEntry (sección 11-12)
  Tests/ArgosCoreTests/          — XCTest para cada módulo de arriba

  project.yml                    — especificación XcodeGen del proyecto Xcode (ver abajo)

  ArgosIntake/                   — target de app (iPadOS → iOS → macOS, sección 3)
    App/ArgosIntakeApp.swift     — entry point, ModelContainer compartido (App Group), AppSession
    Models/                      — @Model de SwiftData: CaseEntity, ItemEntity, TagEntity, AuditLogEntity
    Services/
      FileStorageService         — preservación de originales vs. derivados (secciones 10, 40)
      IngestionService            — pipeline único de ingesta (clasificar → hash → preservar →
                                     ID ARGOS → bitácora), usado por Share Extension, Captura
                                     Rápida e importación manual
      AuditLogService              — bitácora de auditoría, solo-inserción (sección 12)
      SearchService                — construye el índice de búsqueda desde SwiftData
      AuthenticationService        — Face ID/Touch ID (LocalAuthentication) + PIN en Keychain
    Views/
      RootView                    — NavigationSplitView de 4 áreas (sección 20) + botón "+" flotante
      Inbox/InboxView              — bandeja de entrada con selección múltiple (sección 24)
      Cases/                       — lista de casos, alta de caso, ficha de expediente
      Search/SearchView            — buscador global (sección 18)
      Activity/ActivityView        — bitácora como actividad reciente
      Item/ItemDetailView          — ficha de archivo (secciones 15, 39)
      Capture/QuickCaptureView     — botón flotante "+" (sección 23): foto/video, documento,
                                      ubicación, nota — todo converge en IngestionService
      Auth/LockScreenView          — pantalla de bloqueo
      Shared/                      — tema visual ARGOS y selector de etiquetas reutilizado

  ArgosShareExtension/            — target de Share Extension "Guardar en ARGOS" (sección 4)
    ShareViewController           — punto de entrada del sistema (NSExtensionItem → SwiftUI)
    ShareFlowView                 — Caso → Tipo → Etiquetas → Nota → GUARDAR
```

### Decisiones de diseño relevantes

- **Original vs. derivado (sección 40).** `FileStorageService` es el único código con permiso de
  escribir en `Originales/`; todo derivado (preview, OCR, miniatura) vive en `Derivados/<caso>/<item>/`
  con nombre distinto. El hash SHA-256 siempre corresponde al original.
- **Un solo pipeline de ingesta.** Share Extension, Captura Rápida e importación manual llaman al
  mismo `IngestionService`, para que la trazabilidad (ID ARGOS, hash, bitácora) sea idéntica sin
  importar el punto de entrada — nunca hay un camino "secundario" que se salte la preservación o el
  registro de auditoría.
- **Almacenamiento compartido vía App Group.** La Share Extension corre en un proceso separado de
  la app; ambas apuntan al mismo store de SwiftData y a la misma carpeta de originales dentro de
  `group.mx.argos.intake`, siguiendo el principio local-first de la sección 27.
- **`ArgosCore` sin dependencias de Apple UI.** Clasificación, hashing, identificadores y búsqueda
  son Swift puro (con `swift-crypto`, que en plataformas Apple simplemente reexporta CryptoKit).
  Es la única parte del proyecto que se pudo verificar con pruebas unitarias en este entorno.
- **Nunca accede a WhatsApp directamente.** Todo lo que entra a ARGOS INTAKE llega porque el
  usuario lo compartió o importó explícitamente desde el sistema operativo (share sheet o selector
  de archivos) — no hay lectura de la base de datos de WhatsApp ni ningún otro mecanismo no oficial.

### Qué falta para tener un `.xcodeproj` abrible

Este repositorio no incluye un `.xcodeproj` binario (generarlo a mano sin Xcode es frágil y
propenso a errores). En su lugar, `project.yml` es la especificación declarativa para
[XcodeGen](https://github.com/yonaskolb/XcodeGen). En una Mac con Xcode y XcodeGen instalados:

```
cd argos-intake
xcodegen generate
open ArgosIntake.xcodeproj
```

Antes de compilar hay que completar, dentro de Xcode (no se puede generar sin macOS/Xcode desde
este entorno):

1. **Asset Catalog** (`Assets.xcassets`) con el ícono de la app y los colores de `ArgosTheme` como
   Color Sets, para que también respondan a Dark Mode del sistema si se desea.
2. **App Group** `group.mx.argos.intake` habilitado en el Apple Developer account del equipo, y
   asignado a ambos targets en la pestaña *Signing & Capabilities*.
3. **Firma de código** (equipo de desarrollo, bundle identifiers definitivos si no se usan los de
   `project.yml`).
4. Revisar cualquier error de compilación — ver la sección de arriba sobre por qué este código no
   se compiló en esta sesión.

## Estética ARGOS (sección 21)

`Views/Shared/ArgosTheme.swift` centraliza la paleta: fondo azul marino muy oscuro, acentos cian y
blanco, rojo solo para alertas, amarillo para pendientes, verde para validado — la misma lógica de
semáforo que usan los reportes ARGOS de este repositorio, aplicada aquí a estados de verificación y
prioridad de caso en lugar de al Nivel de Riesgo Nacional.

## Próximos pasos (MVP2 / MVP3)

Ver secciones 36-37 de la instrucción maestra. En orden sugerido tras validar MVP1 en un
dispositivo real:

1. Importación de chats completos de WhatsApp (sección 5) — parsing del `.txt`/`.zip` exportado.
2. OCR sobre imágenes y PDFs (Vision framework) guardando el texto como derivado, nunca como
   modificación del original.
3. ARGOS EXTRACT: extracción de entidades (personas, teléfonos, vehículos, geografía, financiero,
   identificadores) con distinción explícita entre HECHO / EXTRACCIÓN AUTOMÁTICA / INFERENCIA /
   VALIDACIÓN HUMANA (sección 29).
4. Mapa del caso (MapKit) y Timeline ARGOS.
5. Módulo de Coincidencias ARGOS entre casos (sección 19).
6. Multiusuario, servidor institucional, sincronización, red de vínculos y ARGOS AI (MVP3).
