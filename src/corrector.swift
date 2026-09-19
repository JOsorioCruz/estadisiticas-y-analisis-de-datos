import AppKit
import Foundation
// Lee líneas de stdin y escribe las palabras que el corrector del sistema marca como mal escritas en español.
let sc = NSSpellChecker.shared
let idiomas = sc.availableLanguages.filter { $0.hasPrefix("es") }
FileHandle.standardError.write("idiomas es disponibles: \(idiomas)\n".data(using: .utf8)!)
let lengua = idiomas.contains("es_CO") ? "es_CO" : (idiomas.first ?? "es")
let tag = NSSpellChecker.uniqueSpellDocumentTag()
var vistos = Set<String>()
while let linea = readLine() {
    let ns = linea as NSString
    var pos = 0
    while pos < ns.length {
        let r = sc.checkSpelling(of: linea, startingAt: pos, language: lengua, wrap: false, inSpellDocumentWithTag: tag, wordCount: nil)
        if r.location == NSNotFound { break }
        let palabra = ns.substring(with: r)
        if !vistos.contains(palabra) { vistos.insert(palabra); print(palabra) }
        pos = r.location + r.length
    }
}
