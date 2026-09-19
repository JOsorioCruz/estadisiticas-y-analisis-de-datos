"""Tarea 15: revisión final del libro contra el enunciado, la rúbrica y la lista de comprobación."""
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

import openpyxl

from carga import BASE, RUTA_ANEXO, cargar_datos
from ej1_tabla import RUTULO_QUIZ
from generar_libro import HOJAS, RUTA_LIBRO, construir_libro

TEXTO = ("Presentación", "Introducción", "Objetivos", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Conclusiones", "Bibliografía", "Anexos")
resultado = []


def marcar(punto, ok, detalle=""):
    resultado.append((punto, ok, detalle))
    print(f"[{'OK' if ok else 'REVISAR'}] {punto}" + (f": {detalle}" if detalle else ""))


def formulas(ws):
    """Texto de todas las fórmulas de una hoja, sin el prefijo _xlfn."""
    return [c.value.replace("_xlfn.", "") for fila in ws.iter_rows() for c in fila if isinstance(c.value, str) and c.value.startswith("=")]


def celdas_de_texto(wb):
    """(hoja, coordenada, texto) de las celdas de texto que escribió el autor, sin la hoja DATOS ni la tabla de verificación."""
    for h in wb.worksheets:
        if h.title == "DATOS":
            continue
        for fila in h.iter_rows():
            for c in fila:
                if isinstance(c.value, str) and not c.value.startswith("="):
                    if h.title == "Anexos" and c.column >= 3 and c.row > 12:
                        continue
                    yield h.title, c.coordinate, c.value


def ortografia(textos):
    """Palabras que el corrector del sistema (español) marca como mal escritas."""
    entrada = "\n".join(re.sub(r"\s+", " ", t) for t in textos)
    r = subprocess.run(["swift", str(BASE / "src" / "corrector.swift")], input=entrada, capture_output=True, text=True, check=True)
    return sorted(set(r.stdout.split()))


def numeros_del_libro(wb_valores, df):
    """Conjunto de números (como texto con coma decimal) que existen en el libro recalculado o en los datos."""
    conocidos = set()
    def agregar(x):
        for d in range(0, 5):
            conocidos.add(f"{abs(round(float(x), d)):.{d}f}".replace(".", ","))
            s = f"{abs(round(float(x), d)):g}".replace(".", ",")
            conocidos.add(s)
    for h in wb_valores.worksheets:
        if h.title in ("DATOS", "Anexos"):
            continue
        for fila in h.iter_rows():
            for c in fila:
                if isinstance(c.value, (int, float)) and not isinstance(c.value, bool):
                    agregar(c.value)
    return conocidos


def main():
    df = cargar_datos()
    wb = openpyxl.load_workbook(RUTA_LIBRO)
    print(f"Revisando {RUTA_LIBRO.relative_to(BASE)}\n")

    # 1. Estructura y orden de las hojas
    marcar("Hojas en el orden de la sección 7", wb.sheetnames == HOJAS, " | ".join(wb.sheetnames))

    # 2. Ejercicio 1
    e1 = wb["Ejercicio 1"]
    filas1 = [[c.value for c in f] for f in e1.iter_rows(min_row=5, max_row=10, max_col=3)]
    conceptos = [f[0] for f in filas1]
    marcar("Ejercicio 1: seis conceptos con definición y ejemplo",
           conceptos == ["Frecuencia absoluta", "Frecuencia relativa", "Media", "Medidas de dispersión", "Regresión lineal", "Correlación de Pearson"]
           and all(f[1] and f[2] and len(f[1]) > 150 and len(f[2]) > 60 for f in filas1), ", ".join(conceptos))
    marcar("Ejercicio 1: espacio rotulado para el quiz", any(c.value == RUTULO_QUIZ for f in e1.iter_rows() for c in f))

    # 3. Ejercicio 2: cada viñeta del enunciado
    e2 = wb["Ejercicio 2"]
    f2 = " ".join(formulas(e2))
    marcar("Ejercicio 2: tabla de frecuencia agrupada con fórmulas COUNTIFS", f2.count("COUNTIFS(") == 10, f"{f2.count('COUNTIFS(')} fórmulas COUNTIFS")
    marcar("Ejercicio 2: media, mediana y moda con fórmulas de Excel", all(k in f2 for k in ("AVERAGE(DATOS", "MEDIAN(", "MODE.SNGL(")))
    marcar("Ejercicio 2: Q1, D5 y P80 (y Q3, P10) con fórmulas", f2.count("QUARTILE.INC(") == 2 and f2.count("PERCENTILE.INC(") == 3)
    marcar("Ejercicio 2: varianza, desviación, CV, asimetría y curtosis", all(k in f2 for k in ("VAR.S(", "STDEV.S(", "SKEW(", "KURT(")) and "*100" in f2)
    marcar("Ejercicio 2: pregunta del intervalo mayor y del 60 %", "INDEX(" in f2 and "COUNTIF(" in f2 and "MATCH(MAX(" in f2)
    textos2 = [t for h, _, t in celdas_de_texto(wb) if h == "Ejercicio 2"]
    for etiqueta, clave in (("interpretación de medidas", "El decil 5 deja"), ("conclusión del histograma", "Conclusión del histograma"),
                            ("conclusión del circular", "Conclusión del diagrama circular"), ("conclusión del polígono", "Conclusión del polígono"),
                            ("homogénea o heterogénea", "¿La distribución es homogénea o heterogénea?"), ("concentración", "¿Qué tipo de concentración presentan los datos?"),
                            ("asimetría", "¿Qué tipo de asimetría presentan los datos?")):
        marcar(f"Ejercicio 2: {etiqueta}", any(clave in t for t in textos2))

    # 4. Ejercicio 3
    e3 = wb["Ejercicio 3"]
    f3 = " ".join(formulas(e3))
    marcar("Ejercicio 3: ecuación de regresión (SLOPE, INTERCEPT)", "SLOPE(" in f3 and "INTERCEPT(" in f3)
    marcar("Ejercicio 3: R², confiabilidad, r y nivel de correlación", all(k in f3 for k in ("RSQ(", "CORREL(", "ABS(")) and "*100" in f3)
    marcar("Ejercicio 3: tres predicciones con la ecuación", len(re.findall(r"\$B\$\d+\+\$B\$\d+\*B\d+", f3)) == 3)
    textos3 = " ".join(t for h, _, t in celdas_de_texto(wb) if h == "Ejercicio 3")
    marcar("Ejercicio 3: relación positiva/negativa/sin relación indicada", "Positiva" in textos3 or "Positiva." in textos3)

    # 5. Gráficos: nativos, con título, ejes rotulados y unidades
    with zipfile.ZipFile(RUTA_LIBRO) as z:
        nombres = z.namelist()
        marcar("Sin ninguna imagen insertada", not [n for n in nombres if n.startswith("xl/media/")])
        graficos = sorted(n for n in nombres if re.match(r"xl/charts/chart\d+\.xml$", n))
        for g in graficos:
            xml = z.read(g).decode("utf-8")
            tipo = next(t for t in ("barChart", "pieChart", "scatterChart") if t in xml)
            titulos = re.findall(r"<c:title>.*?</c:title>", xml, flags=re.S)
            rotulos = [re.sub(r"<[^>]+>", "", t) for t in titulos]
            hay_ejes = tipo != "pieChart"
            ok = len(rotulos) >= (3 if hay_ejes else 1) and all(rotulos)
            unidades = any(("km/h" in r or "años" in r or "número" in r.lower() or "Número" in r) for r in rotulos[1:]) if hay_ejes else "km/h" in rotulos[0]
            marcar(f"Gráfico {g.split('/')[-1]} ({tipo}): título, ejes rotulados y unidades", ok and unidades, " | ".join(rotulos))
        marcar("Cuatro gráficos: histograma, circular, polígono y dispersión con recta", len(graficos) == 4)
        raiz = "".join(z.read(g).decode("utf-8") for g in graficos)
        marcar("Diagrama de dispersión con línea de tendencia lineal", '<c:trendlineType val="linear"/>' in raiz)
        crudo = "".join(z.read(n).decode("utf-8", "ignore") for n in nombres if n.endswith(".xml"))
    marcar("Ningún guion largo en el archivo", chr(0x2014) not in crudo)

    # 6. Hoja DATOS
    anexo = list(openpyxl.load_workbook(RUTA_ANEXO)["DATOS"].iter_rows(values_only=True))
    libro = list(wb["DATOS"].iter_rows(values_only=True))
    marcar("Hoja DATOS idéntica al Anexo 1", anexo == libro, f"{len(libro) - 1} registros")

    # 7. Ortografía con el corrector del sistema
    textos = [t for _, _, t in celdas_de_texto(wb)]
    marcadas = ortografia(textos)
    print(f"\nPalabras marcadas por el corrector del sistema (a revisar a mano): {marcadas}\n")
    resultado.append(("Ortografía: palabras marcadas", None, ", ".join(marcadas)))

    # 8. Trazabilidad: cada cifra de los textos existe en el libro recalculado
    with tempfile.TemporaryDirectory() as tmp:
        from ej2_tabla import recalcular_con_libreoffice
        lo = openpyxl.load_workbook(recalcular_con_libreoffice(RUTA_LIBRO, tmp), data_only=True)
    conocidos = numeros_del_libro(lo, df)
    sin_origen = {}
    for h, coord, t in celdas_de_texto(wb):
        if h in ("Portada", "Bibliografía", "Anexos") or h == "Ejercicio 1":
            continue
        limpio = re.sub(r"\[\d+ - \d+[\)\]]|\d+\. |https?://\S+|\(\d{4}\)", " ", t)
        for n in re.findall(r"(?<![\w.])\d+(?:,\d+)?", limpio):
            if n not in conocidos:
                sin_origen.setdefault(n, []).append(f"{h}!{coord}")
    print("Cifras de los textos que no coinciden con ninguna celda numérica del libro (a explicar):")
    for n, donde in sorted(sin_origen.items(), key=lambda x: float(x[0].replace(",", "."))):
        print(f"   {n}: {donde[:3]}")
    resultado.append(("Cifras de textos sin celda equivalente", None, ", ".join(sorted(sin_origen))))

    # 9. Campos pendientes
    pend = [(h, c, t) for h, c, t in celdas_de_texto(wb) if "PENDIENTE" in t]
    print(f"\nCampos PENDIENTE: {[(h, c) for h, c, _ in pend]}")
    fallos = [p for p, ok, _ in resultado if ok is False]
    print(f"\nComprobaciones automáticas: {sum(1 for _, ok, _ in resultado if ok)} OK, {len(fallos)} por revisar")
    assert not fallos, fallos


if __name__ == "__main__":
    main()
