import Foundation

enum FileStorageError: Error {
    case appGroupContainerUnavailable
    case sourceUnreadable(URL)
}

/// Preservación del archivo original (secciones 10 y 40).
///
/// Regla fundamental: **el archivo original nunca se modifica**. Esta clase
/// es el único punto del código con permiso de escribir dentro de
/// `Originales/`; todo lo demás (miniaturas, previews, texto OCR) se
/// escribe bajo `Derivados/` con un nombre distinto, para que jamás se
/// pueda confundir un derivado con la evidencia fuente.
///
/// El contenedor usa un App Group compartido para que la Share Extension
/// (proceso separado de la app principal) escriba en el mismo almacenamiento
/// local — ver "27. Sincronización" y "28. Almacenamiento institucional":
/// local-first hoy, con una capa intercambiable después.
struct FileStorageService {
    static let appGroupIdentifier = "group.mx.argos.intake"

    private let fileManager: FileManager

    init(fileManager: FileManager = .default) {
        self.fileManager = fileManager
    }

    private func containerURL() throws -> URL {
        guard let url = fileManager.containerURL(forSecurityApplicationGroupIdentifier: Self.appGroupIdentifier) else {
            throw FileStorageError.appGroupContainerUnavailable
        }
        return url
    }

    private func originalsDirectory(caseCode: String) throws -> URL {
        let dir = try containerURL()
            .appendingPathComponent("Originales", isDirectory: true)
            .appendingPathComponent(caseCode.uppercased(), isDirectory: true)
        try fileManager.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir
    }

    private func derivedDirectory(caseCode: String, itemId: UUID) throws -> URL {
        let dir = try containerURL()
            .appendingPathComponent("Derivados", isDirectory: true)
            .appendingPathComponent(caseCode.uppercased(), isDirectory: true)
            .appendingPathComponent(itemId.uuidString, isDirectory: true)
        try fileManager.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir
    }

    /// Copia el archivo fuente al almacenamiento de originales sin tocar el
    /// archivo de origen. Devuelve la ruta relativa al contenedor (lo que se
    /// guarda en `ItemEntity.originalRelativePath`) y la URL absoluta.
    func storeOriginal(
        from sourceURL: URL,
        caseCode: String,
        itemId: UUID,
        storedFilename: String
    ) throws -> (relativePath: String, absoluteURL: URL) {
        guard fileManager.isReadableFile(atPath: sourceURL.path) else {
            throw FileStorageError.sourceUnreadable(sourceURL)
        }

        let dir = try originalsDirectory(caseCode: caseCode)
        let destination = dir.appendingPathComponent(storedFilename, isDirectory: false)

        if fileManager.fileExists(atPath: destination.path) {
            try fileManager.removeItem(at: destination)
        }
        try fileManager.copyItem(at: sourceURL, to: destination)

        // Marcar como solo-lectura en el sistema de archivos: un candado
        // adicional (no el único) contra modificaciones accidentales del
        // original una vez preservado.
        try? fileManager.setAttributes([.posixPermissions: 0o444], ofItemAtPath: destination.path)

        let relative = "Originales/\(caseCode.uppercased())/\(storedFilename)"
        return (relative, destination)
    }

    /// Escribe un derivado (preview, miniatura, texto OCR) bajo `Derivados/`.
    /// Nunca comparte carpeta ni nombre con el original.
    func storeDerived(
        data: Data,
        caseCode: String,
        itemId: UUID,
        filename: String
    ) throws -> (relativePath: String, absoluteURL: URL) {
        let dir = try derivedDirectory(caseCode: caseCode, itemId: itemId)
        let destination = dir.appendingPathComponent(filename, isDirectory: false)
        try data.write(to: destination, options: .atomic)
        let relative = "Derivados/\(caseCode.uppercased())/\(itemId.uuidString)/\(filename)"
        return (relative, destination)
    }

    func absoluteURL(forRelativePath relativePath: String) throws -> URL {
        try containerURL().appendingPathComponent(relativePath)
    }
}
