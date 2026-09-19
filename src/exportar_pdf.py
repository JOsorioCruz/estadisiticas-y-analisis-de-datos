"""Exporta la entrega a PDF: el mismo libro, sin la hoja DATOS de 400 filas, sin el tutor, la fecha ni la línea del CTEV
de la portada, sin el recuadro de la evidencia del quiz y sin la nota de confirmación del foro del Anexo C. El libro de Excel conserva todo eso.

Se ejecuta desde la raíz con `.venv/bin/python src/exportar_pdf.py`. Genera output/<nombre del libro>.pdf.
"""
import subprocess
import tempfile
from pathlib import Path

from carga import BASE, cargar_datos
from generar_libro import RUTA_LIBRO, calcular_verificacion, construir_libro
from ej2_tabla import SOFFICE

RUTA_PDF = RUTA_LIBRO.with_suffix(".pdf")


def main():
    df = cargar_datos()
    filas = calcular_verificacion(df)
    with tempfile.TemporaryDirectory() as tmp:
        libro = Path(tmp) / RUTA_LIBRO.name
        construir_libro(libro, df, valores=True, filas_verif=filas, ocultar_datos=True, para_pdf=True)
        subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(libro)], check=True, capture_output=True)
        RUTA_PDF.write_bytes((Path(tmp) / RUTA_PDF.name).read_bytes())
    print(f"PDF generado: {RUTA_PDF.relative_to(BASE)}")


if __name__ == "__main__":
    main()
