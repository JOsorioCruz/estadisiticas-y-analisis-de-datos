"""Exporta todos los textos del trabajo a un único documento de Word (.docx).

Reúne portada, presentación, introducción, objetivos, la Tabla 1, los textos y tablas de los ejercicios 2 y 3, conclusiones,
bibliografía y anexos. Las cifras salen de los mismos módulos que arman el libro de Excel. No lleva imágenes: los gráficos
están en el libro de Excel. Como el PDF, no incluye el tutor, la fecha, la línea del CTEV, el recuadro del quiz ni la nota
de confirmación del foro. Se ejecuta desde la raíz con `.venv/bin/python src/exportar_docx.py`.
"""
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from carga import BASE, cargar_datos
from ej1_tabla import TABLA_1
import ej2_dispersion as disp
import ej2_graficos as graf
import ej2_medidas as med
import ej2_preguntas as preg
import ej3_correlacion as cor
import ej3_predicciones as pred
import ej3_regresion as reg
from ej2_tabla import AMPLITUD, LIM_INICIAL, VARIABLE, _etiqueta, calcular_tabla, numero_intervalos
from textos_libro import sin_frase_quiz, textos

RUTA_DOCX = BASE / "output" / "textos_actividad_probabilidad_y_estadistica_unidad_2.docx"
SALTO = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'


def fx(x, d=2):
    """Número con coma decimal y d decimales fijos."""
    return f"{x:.{d}f}".replace(".", ",")


def esc(t):
    """Escapa los caracteres que Markdown interpretaría (corchetes, barras, asteriscos)."""
    return re.sub(r"([\\|\[\]*<>`_$])", r"\\\1", str(t))


def esc_apa(t):
    """Igual que esc, pero conserva los asteriscos que marcan la cursiva de una referencia APA."""
    return re.sub(r"([\\|\[\]<>`_$])", r"\\\1", str(t))


def tabla(encabezados, filas, anchos):
    """Tabla de Markdown; las rayas del separador dan los anchos relativos de las columnas en Word."""
    def fila(celdas):
        return "| " + " | ".join(esc(c) for c in celdas) + " |"
    sep = "|" + "|".join("-" * a for a in anchos) + "|"
    return "\n".join([fila(encabezados), sep] + [fila(f) for f in filas]) + "\n\n"


def parrafos(*ps):
    return "\n\n".join(esc(p) for p in ps) + "\n\n"


def construir_markdown():
    df = cargar_datos()
    t = sin_frase_quiz(textos())
    v = df[VARIABLE].to_numpy()
    n = len(v)
    tab = calcular_tabla(df[VARIABLE])
    k = len(tab)
    lab = [_etiqueta(r.Li, r.Ls, i == k - 1) for i, r in enumerate(tab.itertuples())]
    md = []

    # Portada
    p = dict(t["portada"])
    md.append('::: {custom-style="Title"}\nActividad No 2 de Probabilidad y Estadística\n:::\n\n')
    md.append('::: {custom-style="Subtitle"}\nGuía de actividad No 2: Estadística descriptiva\n:::\n\n')
    md.append("**Universidad de Cartagena**\n\n" + "\n\n".join(f"**{k}:** {esc(p[k])}" for k in ("Programa", "Asignatura", "Código", "Autor", "Semestre")) + "\n\n")
    md.append(SALTO)

    # Presentación, introducción y objetivos
    md.append("# Presentación\n\n" + parrafos(*t["presentacion"]))
    md.append("# Introducción\n\n" + parrafos(*t["introduccion"]))
    o = t["objetivos"]
    md.append("# Objetivos\n\n## Objetivo general\n\n" + parrafos(o["general"]) + "## Objetivos específicos\n\n"
              + "\n".join(f"{i}. {esc(x)}" for i, x in enumerate(o["especificos"], 1)) + "\n\n")

    # Ejercicio 1
    md.append(SALTO + "# Ejercicio 1: definiciones de conceptos estadísticos\n\n## Tabla 1. Definiciones de conceptos\n\n")
    md.append(tabla(["Conceptos", "Definiciones", "Ejemplos"], TABLA_1, [14, 43, 43]))

    # Ejercicio 2
    md.append(SALTO + "# Ejercicio 2: estadística descriptiva de la velocidad registrada\n\n")
    md.append(parrafos("Variable elegida: velocidad registrada (km/h), variable cuantitativa continua, con 400 registros."))
    md.append("## Tabla de frecuencia con datos agrupados\n\n")
    md.append(parrafos(
        f"Hay n = {n} datos, con un mínimo de {fx(v.min(), 1).replace(',0', '') if False else med.fmt(v.min())} km/h y un máximo de {med.fmt(v.max())} km/h, por lo que el rango es {med.fmt(v.max() - v.min())} km/h. "
        f"Por la regla de Sturges, k = 1 + log2({n}) = {fx(1 + __import__('math').log2(n))}, que se redondea hacia arriba a {numero_intervalos(n)} intervalos. "
        f"La amplitud teórica es {fx((v.max() - v.min()) / k)} y se adoptó {AMPLITUD}, redondeada hacia arriba, con el primer límite en {LIM_INICIAL}. "
        "Los intervalos son cerrados a la izquierda y abiertos a la derecha, salvo el último, que incluye su límite superior."))
    md.append(tabla(["Intervalo (km/h)", "Marca de clase xi", "fi", "Fi", "hi (%)", "Hi (%)"],
                    [[lab[i], fx(r.xi, 1), int(r.fi), int(r.Fi), fx(r.hi_pct), fx(r.Hi_pct)] for i, r in enumerate(tab.itertuples())]
                    + [["Total", "", int(tab.fi.sum()), "", fx(tab.hi_pct.sum()), ""]], [24, 18, 12, 12, 17, 17]))
    md.append("## Gráficos y conclusiones\n\n")
    md.append(parrafos("El histograma, el diagrama circular y el polígono de frecuencia están en la hoja Ejercicio 2 del libro de Excel, como gráficos nativos. Las conclusiones de cada uno son las siguientes."))
    for titulo, texto in graf.conclusiones(tab).items():
        md.append(f"### {esc(titulo)}\n\n" + parrafos(texto))
    md.append("## Preguntas con base en la tabla de frecuencia\n\n")
    r = preg.respuestas(tab)
    p1, p2 = preg.texto_respuestas(tab, r)
    md.append("### ¿En cuál intervalo se observa la mayor cantidad de datos?\n\n" + parrafos(p1))
    md.append("### ¿Hasta cuál intervalo se acumula el 60 % de los datos?\n\n" + parrafos(p2))
    medidas, veces = med.definir_medidas(v)
    mval = {nombre: valor for nombre, _, _, valor in medidas}
    imax = int(tab.fi.idxmax())
    interp = med.interpretaciones(medidas, veces, f"[{tab.Li[imax]:g} - {tab.Ls[imax]:g})", n)
    md.append("## Medidas de tendencia central y de posición\n\n")
    md.append(tabla(["Medida", "Resultado", "Interpretación"], [[nombre, fx(valor), interp[nombre]] for nombre, _, _, valor in medidas], [16, 15, 69]))
    x = disp.calcular(v)
    di, an = disp.textos(x, mval["Media"], mval["Mediana"], tab)
    md.append("## Dispersión, asimetría y curtosis\n\n")
    md.append(tabla(["Medida", "Resultado", "Interpretación"],
                    [[nombre, fx(valor, 4 if nombre in ("Asimetría", "Curtosis (exceso)") else 2), di[nombre]] for nombre, valor in x.items()], [22, 15, 63]))
    md.append("### Convención adoptada para interpretar\n\n" + parrafos(
        "Usamos la varianza y la desviación típica muestrales (VAR.S y STDEV.S) porque los 400 registros se toman como una muestra de la accidentalidad del Tolima. "
        f"Para clasificar usamos convenciones de uso común en estadística descriptiva, que no proceden de las lecturas del curso: homogénea si el CV es menor que {disp.CV_LIMITE} %, "
        f"casi simétrica si el valor absoluto de la asimetría es menor que {str(disp.ASIM_LIMITE).replace('.', ',')}, y platicúrtica si la curtosis en exceso es negativa. "
        "SKEW y KURT son las versiones de muestra que calcula Excel."))
    md.append("### Análisis de la distribución\n\n")
    for pregunta, texto in an.items():
        md.append(f"**{esc(pregunta)}** " + esc(texto) + "\n\n")

    # Ejercicio 3
    md.append(SALTO + "# Ejercicio 3: regresión lineal y correlación\n\n")
    md.append(parrafos("Variable independiente (x): años de experiencia del conductor. Variable dependiente (y): número de infracciones en los últimos cinco años."))
    c = reg.calcular(df)
    trm = reg.tramos(df)
    rt = reg.textos(c, trm)
    md.append("## Ecuación de regresión lineal\n\n")
    md.append(tabla(["Medida", "Resultado", "Interpretación"], [
        ["Pendiente (b)", fx(c["pendiente"], 4), rt["Pendiente"]],
        ["Intercepto (a)", fx(c["intercepto"], 4), rt["Intercepto"]],
        ["Ecuación de la recta", reg.ecuacion_texto(c["intercepto"], c["pendiente"]).replace(".", ","), "Es la recta de mínimos cuadrados: con ella se estima el número de infracciones a partir de los años de experiencia."],
        ["Tipo de relación", c["tipo"].capitalize(), rt["Tipo de relación"]],
    ], [18, 17, 65]))
    md.append("## Diagrama de dispersión con la recta de regresión\n\n")
    md.append(parrafos("El diagrama está en la hoja Ejercicio 3 del libro de Excel, con la línea de tendencia lineal. " + rt["Gráfico"]))
    md.append("### Patrón de los datos\n\n" + parrafos(rt["Patrón"]))
    cc = cor.calcular(df)
    ct = cor.textos(cc, trm)
    md.append("## Coeficiente de determinación, confiabilidad y correlación de Pearson\n\n")
    md.append(tabla(["Medida", "Resultado", "Interpretación"], [
        ["Coeficiente de determinación (R²)", fx(cc["R2"], 4), ct["R2"]],
        ["Confiabilidad del modelo (%)", fx(cc["confiabilidad"]), ct["confiabilidad"]],
        ["Coeficiente de correlación de Pearson (r)", fx(cc["r"], 4), ct["r"]],
        ["Nivel de correlación lineal", cc["nivel"], ct["nivel"]],
    ], [24, 15, 61]))
    md.append("### Escala adoptada para el nivel de correlación (|r|)\n\n")
    md.append(tabla(["Intervalo de |r|", "Nivel"], [["|r| = 1", "Perfecta"], ["0,90 a menos de 1", "Excelente"], ["0,80 a menos de 0,90", "Aceptable"],
                                                     ["0,50 a menos de 0,80", "Regular"], ["Mayor que 0 y menor que 0,50", "Mínima"], ["|r| = 0", "Sin correlación"]], [50, 50]))
    md.append(parrafos("Esta escala es una convención de uso común que adoptamos en este trabajo. No proviene de las lecturas del curso, y otras escalas usan límites distintos."))
    md.append("### Cómo leer estos resultados\n\n" + parrafos(ct["nota"]))
    pc = pred.calcular(df)
    pt, general = pred.textos(pc)
    md.append("## Predicciones con la ecuación de regresión\n\n")
    md.append(parrafos("La ecuación es y = a + b x, con a y b tomados de la pendiente y el intercepto."))
    md.append(tabla(["Predicción", "Experiencia x (años)", "Infracciones estimadas", "Promedio observado", "Conductores con ese x"],
                    [[f"Predicción {i}", f["x"], fx(f["pred"]), fx(f["obs"]), f["n"]] for i, f in enumerate(pc["filas"], 1)], [16, 20, 22, 21, 21]))
    for i, texto in enumerate(pt, 1):
        md.append(f"**Predicción {i}.** " + esc(texto) + "\n\n")
    md.append(f"**Error típico de la estimación (STEYX):** {fx(pc['error'])} infracciones. " + esc(general) + "\n\n")

    # Conclusiones, bibliografía y anexos
    md.append(SALTO + "# Conclusiones\n\n")
    for titulo, texto in t["conclusiones"]:
        md.append(f"## {esc(titulo)}\n\n" + parrafos(texto))
    md.append(SALTO + "# Bibliografía\n\n")
    for ref in t["bibliografia"]["Obligatoria (referencias del enunciado; confirmar que se consultaron)"]:
        md.append(esc_apa(ref) + "\n\n")
    md.append(SALTO + "# Anexos\n\n")
    an_ = t["anexos"]
    md.append("## Anexo A. Hoja de datos\n\n" + parrafos(*an_["Anexo A. Hoja de datos"]))
    b1, b2 = an_["Anexo B. Verificación de los cálculos"]
    md.append("## Anexo B. Verificación de los cálculos\n\n" + parrafos(b1.replace("La tabla lista cada comparación.", "La tabla con cada comparación está en la hoja Anexos del libro de Excel."), b2))
    md.append("## Anexo C. Variables elegidas en el foro\n\n" + tabla(
        ["Nombre", "Variable del ejercicio 2", "Variables del ejercicio 3"],
        [["Jairo Alonso Osorio Cruz", "Velocidad registrada", "Años de experiencia del conductor (x) e histórico de infracciones (y)"]], [30, 30, 40]))
    d = an_["Anexo D. Convenciones adoptadas"]
    md.append("## Anexo D. Convenciones adoptadas\n\n" + parrafos(d[0]) + "\n".join(f"- {esc(x)}" for x in d[1:]) + "\n")
    return "".join(md)


def preparar_plantilla(destino):
    """Plantilla de Word de pandoc con bordes en las tablas, encabezado sombreado, letra de 11 puntos e idioma español."""
    base = Path(tempfile.mkdtemp()) / "base.docx"
    base.write_bytes(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], capture_output=True, check=True).stdout)
    with zipfile.ZipFile(base) as z:
        archivos = {n: z.read(n) for n in z.namelist()}
    s = archivos["word/styles.xml"].decode("utf-8")
    bordes = "".join(f'<w:{l} w:val="single" w:sz="4" w:space="0" w:color="808080"/>' for l in ("top", "left", "bottom", "right", "insideH", "insideV"))
    s = s.replace('<w:tblInd w:w="0" w:type="dxa" />', '<w:tblInd w:w="0" w:type="dxa" /><w:tblBorders>' + bordes + "</w:tblBorders>", 1)
    s = s.replace('<w:tblStylePr w:type="firstRow">\n      <w:tcPr>', '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/></w:rPr>\n      <w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>', 1)
    s = s.replace('<w:sz w:val="24" />\n        <w:szCs w:val="24" />', '<w:sz w:val="22" />\n        <w:szCs w:val="22" />', 1)
    s = s.replace('<w:lang w:val="en-US"', '<w:lang w:val="es-CO"', 1)
    # letra Calibri en todo el documento (la plantilla de pandoc usa fuentes del tema, que en Word salen serif)
    s = re.sub(r'<w:rFonts [^>]*?(?:asciiTheme|hAnsiTheme)="(?:minor|major)HAnsi"[^>]*/>', '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri" w:eastAsia="Calibri"/>', s)
    s = s.replace('<w:rFonts w:cstheme="majorBidi" w:eastAsiaTheme="majorEastAsia" />', '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri" w:eastAsia="Calibri"/>')      # estilos de título
    assert "Calibri" in s and "insideH" in s and 'w:fill="D9E2F3"' in s and "es-CO" in s
    archivos["word/styles.xml"] = s.encode("utf-8")
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in archivos.items():
            z.writestr(n, b)


def main():
    md = construir_markdown()
    assert chr(0x2014) not in md, "hay un guion largo"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        plantilla, origen = tmp / "plantilla.docx", tmp / "textos.md"
        preparar_plantilla(plantilla)
        origen.write_text(md, encoding="utf-8")
        RUTA_DOCX.parent.mkdir(exist_ok=True)
        subprocess.run(["pandoc", str(origen), "-f", "markdown-smart-tex_math_dollars", "-t", "docx", "--reference-doc", str(plantilla),
                        "-M", "lang=es-CO", "-o", str(RUTA_DOCX)], check=True)
    print(f"Documento generado: {RUTA_DOCX.relative_to(BASE)}")


if __name__ == "__main__":
    main()
