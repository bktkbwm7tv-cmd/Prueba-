# ARGOS INTAKE

Sistema de Ingesta, Clasificación y Trazabilidad de Información Investigativa.

> De la información dispersa al expediente estructurado.

WhatsApp (u otra app) es un canal de entrada, nunca el repositorio del caso. ARGOS INTAKE
convierte lo que un investigador comparte o importa en un expediente digital preservado,
clasificado, indexado, buscable y auditable — sin modificar jamás el archivo original.

Este directorio implementa el **MVP 1** completo descrito en la instrucción maestra (creación de
casos, Share Extension "Guardar en ARGOS", importación de archivos, bandeja de entrada,
clasificación automática por extensión, preservación del original, SHA-256, fichas de archivo,
búsqueda, etiquetas, Face ID/PIN y almacenamiento local) más dos piezas de **MVP 2**: importación
de chats completos de WhatsApp (sección 5) y OCR sobre imágenes y PDFs (sección 14). Extracción de
entidades, mapa, timeline, coincidencias entre casos, multiusuario/servidor y ARGOS AI siguen fuera
de este alcance a propósito (la propia instrucción maestra lo pide así, sección 35).

## Por qué este código no está compilado ni probado en este entorno

Esta sesión corrió en un contenedor Linux sin Xcode ni el toolchain de Swift para Apple platforms
(no hay `swift`, ni SDK de iOS/macOS, ni simulador). El código se escribió a mano siguiendo las
convenciones idiomáticas de Swift/SwiftUI/SwiftData/CryptoKit, pero **nadie lo ha compilado
todavía**. Antes de darlo por bueno, ábrelo en Xcode en una Mac y corrige lo que el compilador
señale — es razonable esperar errores menores de tipado o de referencias en un proyecto de este
tamaño escrito sin retroalimentación del compilador.

La única pieza que sí se diseñó para poder probarse sin Xcode es `ArgosCore` (ver abajo): lógica
de negocio pura en Swift estándar + [swift-crypto](https://github.com/apple/swift-crypto), sin
UIKit/SwiftUI/SwiftData/ZIPFoundation. Esto incluye el parser de exportaciones de WhatsApp — la
lectura del `.zip` en sí (que si depende de una librería de Apple-platforms) vive en el target de
la app, no en `ArgosCore`. En una máquina con el toolchain de Swift para Linux o macOS, se corre con:

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
    Chat/WhatsAppChatParser      — parsing de `_chat.txt` (iOS/Android, ES/EN) — sección 5
  Tests/ArgosCoreTests/          — XCTest para cada módulo de arriba

  project.yml                    — especificación XcodeGen del proyecto Xcode (ver abajo)

  ArgosIntake/                   — target de app (iPadOS → iOS → macOS, sección 3)
    App/ArgosIntakeApp.swift     — entry point, ModelContainer compartido (App Group), AppSession
    Models/                      — @Model de SwiftData: CaseEntity, ItemEntity, TagEntity,
                                    AuditLogEntity, ChatImportEntity, MessageEntity
    Services/
      FileStorageService         — preservación de originales vs. derivados (secciones 10, 40)
      IngestionService            — pipeline único de ingesta (clasificar → hash → preservar →
                                     ID ARGOS → bitácora), usado por Share Extension, Captura
                                     Rápida, importación manual e importación de chats
      ChatImportService            — preserva el paquete, extrae el `.zip` (ZIPFoundation),
                                      parsea con WhatsAppChatParser y vincula cada adjunto
                                      encontrado a su propio ItemEntity vía IngestionService
      AuditLogService              — bitácora de auditoría, solo-inserción (sección 12)
      OCRService                    — Vision (imágenes) + PDFKit (texto embebido, o cada página
                                       renderizada y reconocida con Vision si el PDF es un escaneo)
      SearchService                — construye el índice de búsqueda desde SwiftData
                                      (ítems, su texto OCR, y mensajes de chats importados)
      AuthenticationService        — Face ID/Touch ID (LocalAuthentication) + PIN en Keychain
    Views/
      RootView                    — NavigationSplitView de 4 áreas (sección 20) + botón "+" flotante
      Inbox/InboxView              — bandeja de entrada con selección múltiple (sección 24)
      Cases/                       — lista de casos, alta de caso, ficha de expediente,
                                      ImportChatView (importar chat), ChatDetailView (conversación
                                      reconstruida: mensajes en orden + adjuntos vinculados)
      Search/SearchView            — buscador global (sección 18)
      Activity/ActivityView        — bitácora como actividad reciente
      Item/ItemDetailView          — ficha de archivo (secciones 15, 39), con extracción de texto
                                      (OCR) bajo demanda para imágenes y PDF
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
  usuario lo compartió o importó explícitamente desde el sistema operativo (share sheet, importar
  chat, o selector de archivos) — no hay lectura de la base de datos de WhatsApp ni ningún otro
  mecanismo no oficial.
- **Importar chat no sustituye la ingesta normal, la reutiliza.** `ChatImportService` preserva el
  `.txt`/`.zip` exportado como un `ItemEntity` más (vía `IngestionService`, con su propio hash e ID
  ARGOS), y cada adjunto de multimedia que logra vincular a un mensaje se preserva de la misma
  forma, como su propio ítem independiente — nunca se trata "el mensaje" y "la foto que trae" como
  una sola cosa. Así se cumple la cadena exigida en la sección 5: archivo → mensaje → conversación →
  importación → caso, siempre reconstruible.
- **La extracción del `.zip` no es una modificación del original.** El paquete preservado en el
  paso 1 de `ChatImportService` es la evidencia de referencia y no se toca; extraerlo a un
  directorio temporal solo sirve para leer su contenido y copiar los adjuntos, que luego se
  preservan por su cuenta con su propio hash — el directorio de extracción se borra al terminar.
- **OCR es bajo demanda, no automático.** El analista dispara la extracción desde la ficha del
  archivo; nada se ejecuta en segundo plano al importar. El texto se guarda dos veces con dos
  propósitos distintos: `ItemEntity.ocrText` (caché en el modelo, lo que `SearchService` indexa
  directamente) y un `.txt` en `Derivados/` vía `FileStorageService.storeDerived` (el producto
  derivado auditable que pide la sección 14) — ninguno de los dos toca el archivo original. Para
  PDF se intenta primero la capa de texto embebida (exacta, sin "nivel de confianza" porque no es
  reconocimiento) y solo se cae a Vision página por página cuando el PDF es un escaneo sin texto.

### Qué falta para tener un `.xcodeproj` abrible

Este repositorio no incluye un `.xcodeproj` binario (generarlo a mano sin Xcode es frágil y
propenso a errores). En su lugar, `project.yml` es la especificación declarativa para
[XcodeGen](https://github.com/yonaskolb/XcodeGen). En una Mac con Xcode y XcodeGen instalados:

```
cd argos-intake
xcodegen generate
open ArgosIntake.xcodeproj
```

`xcodegen generate` resuelve automáticamente la dependencia remota de SPM
([ZIPFoundation](https://github.com/weichsel/ZIPFoundation), usada solo por `ChatImportService`
para leer los `.zip` que exporta WhatsApp) — no hace falta agregarla a mano en Xcode, pero si
`xcodegen generate` falla al resolver paquetes por falta de red, revisa `project.yml`.

Antes de compilar hay que completar, dentro de Xcode (no se puede generar sin macOS/Xcode desde
este entorno):

1. **Asset Catalog** (`Assets.xcassets`) con el ícono de la app y los colores de `ArgosTheme` como
   Color Sets, para que también respondan a Dark Mode del sistema si se desea.
2. **App Group** `group.mx.argos.intake` habilitado en el Apple Developer account del equipo, y
   asignado a ambos targets en la pestaña *Signing & Capabilities*.
3. **Firma de código** (equipo de desarrollo, bundle identifiers definitivos si no se usan los de
   `project.yml`).
4. Revisar cualquier error de compilación — ver la sección de arriba sobre por qué este código no
   se compiló en esta sesión. La lógica de fechas de `WhatsAppChatParser` en particular merece una
   prueba manual con una exportación real: la ambigüedad día/mes de WhatsApp es un problema del
   formato, no solo del código, así que vale la pena confirmar con chats reales de tu región.
5. **Vision/OCR no puede probarse en simulador de forma confiable para todos los idiomas** — probar
   `OCRService` con fotografías y PDF reales en un dispositivo, no solo en el simulador.

## Estética ARGOS (sección 21)

`Views/Shared/ArgosTheme.swift` centraliza la paleta: fondo azul marino muy oscuro, acentos cian y
blanco, rojo solo para alertas, amarillo para pendientes, verde para validado — la misma lógica de
semáforo que usan los reportes ARGOS de este repositorio, aplicada aquí a estados de verificación y
prioridad de caso en lugar de al Nivel de Riesgo Nacional.

## Próximos pasos (MVP2 / MVP3)

Ver secciones 36-37 de la instrucción maestra. Importación de chats de WhatsApp (sección 5) y OCR
(sección 14) ya están implementados; en orden sugerido para lo que sigue, tras validar todo lo
anterior en un dispositivo real:

1. ARGOS EXTRACT: extracción de entidades (personas, teléfonos, vehículos, geografía, financiero,
   identificadores) con distinción explícita entre HECHO / EXTRACCIÓN AUTOMÁTICA / INFERENCIA /
   VALIDACIÓN HUMANA (sección 29) — ahora que hay texto OCR además de notas y mensajes, esto tiene
   más de dónde extraer.
2. Mapa del caso (MapKit) y Timeline ARGOS que mezcle mensajes, fotos, documentos y eventos.
3. Módulo de Coincidencias ARGOS entre casos (sección 19).
4. Multiusuario, servidor institucional, sincronización, red de vínculos y ARGOS AI (MVP3).
