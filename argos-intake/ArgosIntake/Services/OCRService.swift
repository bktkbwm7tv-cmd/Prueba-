import Foundation
import Vision
import PDFKit
import ImageIO
#if canImport(UIKit)
import UIKit
#endif
import ArgosCore

enum OCRError: Error {
    case unsupportedType
    case unreadableFile
    case noTextFound
}

enum OCRSource {
    /// Texto reconocido por Vision sobre una imagen.
    case visionImage
    /// Capa de texto ya embebida en el PDF — no es reconocimiento, es
    /// lectura exacta, por eso no trae nivel de confianza.
    case pdfEmbeddedText
    /// PDF sin capa de texto (escaneado): cada página se renderizó como
    /// imagen y se corrió Vision sobre ella.
    case visionPDFPages
}

struct OCRResult {
    let text: String
    /// 0.0–1.0, promedio de las observaciones de Vision. `nil` cuando el
    /// texto es de `pdfEmbeddedText` (sección 14: "cuando pueda determinarse").
    let confidence: Double?
    let source: OCRSource
}

/// OCR sobre imágenes y PDFs (sección 14). El original nunca se abre para
/// escribir — solo se lee para generar un derivado (texto extraído), que
/// el llamador decide dónde guardar. Para PDFs, se intenta primero la capa
/// de texto embebida (más rápida y exacta que el reconocimiento visual) y
/// solo se recurre a Vision página por página cuando el PDF es un escaneo
/// sin texto seleccionable.
struct OCRService {
    func extractText(from item: ItemEntity, storage: FileStorageService) async throws -> OCRResult {
        let isPDF = item.fileExtension.lowercased() == "pdf"
        guard item.type == .image || (item.type == .document && isPDF) else {
            throw OCRError.unsupportedType
        }

        let fileURL = try storage.absoluteURL(forRelativePath: item.originalRelativePath)

        if isPDF {
            return try await extractFromPDF(at: fileURL)
        }
        return try await extractFromImage(at: fileURL)
    }

    private func extractFromImage(at url: URL) async throws -> OCRResult {
        guard let cgImage = Self.loadCGImage(at: url) else { throw OCRError.unreadableFile }
        let recognized = try await Self.runVision(on: cgImage)
        guard !recognized.text.isEmpty else { throw OCRError.noTextFound }
        return recognized
    }

    private func extractFromPDF(at url: URL) async throws -> OCRResult {
        guard let document = PDFDocument(url: url) else { throw OCRError.unreadableFile }

        var embeddedText = ""
        for pageIndex in 0..<document.pageCount {
            if let pageText = document.page(at: pageIndex)?.string,
               !pageText.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                embeddedText += (embeddedText.isEmpty ? "" : "\n\n") + pageText
            }
        }
        if !embeddedText.isEmpty {
            return OCRResult(text: embeddedText, confidence: nil, source: .pdfEmbeddedText)
        }

        // Sin capa de texto: es un escaneo. Renderizar cada página y correr
        // Vision sobre la imagen resultante.
        var pageTexts: [String] = []
        var confidences: [Double] = []
        for pageIndex in 0..<document.pageCount {
            guard let page = document.page(at: pageIndex), let cgImage = Self.renderPage(page) else { continue }
            let recognized = try await Self.runVision(on: cgImage)
            if !recognized.text.isEmpty { pageTexts.append(recognized.text) }
            if let confidence = recognized.confidence { confidences.append(confidence) }
        }

        guard !pageTexts.isEmpty else { throw OCRError.noTextFound }
        let averageConfidence = confidences.isEmpty ? nil : confidences.reduce(0, +) / Double(confidences.count)
        return OCRResult(text: pageTexts.joined(separator: "\n\n"), confidence: averageConfidence, source: .visionPDFPages)
    }

    private static func loadCGImage(at url: URL) -> CGImage? {
        guard let source = CGImageSourceCreateWithURL(url as CFURL, nil) else { return nil }
        return CGImageSourceCreateImageAtIndex(source, 0, nil)
    }

    /// Renderiza una página de PDF como imagen a 2x para dar a Vision
    /// suficiente resolución sin generar bitmaps innecesariamente grandes.
    private static func renderPage(_ page: PDFPage) -> CGImage? {
        #if canImport(UIKit)
        let bounds = page.bounds(for: .mediaBox)
        let scale: CGFloat = 2.0
        let size = CGSize(width: bounds.width * scale, height: bounds.height * scale)
        guard size.width > 0, size.height > 0 else { return nil }

        let renderer = UIGraphicsImageRenderer(size: size)
        let image = renderer.image { context in
            UIColor.white.setFill()
            context.fill(CGRect(origin: .zero, size: size))
            context.cgContext.translateBy(x: 0, y: size.height)
            context.cgContext.scaleBy(x: scale, y: -scale)
            page.draw(with: .mediaBox, to: context.cgContext)
        }
        return image.cgImage
        #else
        return nil
        #endif
    }

    private static func runVision(on cgImage: CGImage) async throws -> OCRResult {
        try await withCheckedThrowingContinuation { continuation in
            let request = VNRecognizeTextRequest { request, error in
                if let error {
                    continuation.resume(throwing: error)
                    return
                }
                let observations = (request.results as? [VNRecognizedTextObservation]) ?? []
                var lines: [String] = []
                var confidences: [Double] = []
                for observation in observations {
                    guard let candidate = observation.topCandidates(1).first else { continue }
                    lines.append(candidate.string)
                    confidences.append(Double(candidate.confidence))
                }
                let averageConfidence = confidences.isEmpty ? nil : confidences.reduce(0, +) / Double(confidences.count)
                continuation.resume(returning: OCRResult(
                    text: lines.joined(separator: "\n"), confidence: averageConfidence, source: .visionImage
                ))
            }
            request.recognitionLevel = .accurate
            request.usesLanguageCorrection = true
            // Español primero: es el idioma de operación del producto.
            request.recognitionLanguages = ["es-MX", "es-ES", "en-US"]

            let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
            do {
                try handler.perform([request])
            } catch {
                continuation.resume(throwing: error)
            }
        }
    }
}
