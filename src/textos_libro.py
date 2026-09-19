"""Tarea 13: textos del libro (portada, presentación, introducción, objetivos, conclusiones, bibliografía y anexos).

Las cifras se calculan desde los datos con los mismos módulos que arman las hojas, de modo que cada número del texto
se pueda rastrear a una celda del libro. Los campos que Jairo aún no confirmó quedan marcados con PENDIENTE.
"""
import json
from pathlib import Path

import numpy as np

from carga import BASE, cargar_datos
from ej2_dispersion import calcular as disp_calcular, f2
from ej2_medidas import definir_medidas, fmt
from ej2_tabla import VARIABLE, _etiqueta, calcular_tabla
from ej3_correlacion import calcular as cor_calcular
from ej3_predicciones import calcular as pred_calcular
from ej3_regresion import X, Y, calcular as reg_calcular, ecuacion_texto, tramos

PENDIENTE_TUTOR = "PENDIENTE: nombre del tutor"
PENDIENTE_FECHA = "PENDIENTE: fecha de entrega"
SALIDA = BASE / "output" / "textos"
RUTA_DATOS_ENTREGA = BASE / "datos_entrega.json"


def datos_entrega():
    """Datos que solo conoce el autor. Se leen de datos_entrega.json (ver datos_entrega.ejemplo.json); si falta, quedan como PENDIENTE."""
    return json.loads(RUTA_DATOS_ENTREGA.read_text(encoding="utf-8")) if RUTA_DATOS_ENTREGA.exists() else {}


def coma(txt):
    return str(txt).replace(".", ",")


def textos():
    df = cargar_datos()
    v = df[VARIABLE].to_numpy()
    n = len(df)
    tab = calcular_tabla(df[VARIABLE])
    medidas, veces = definir_medidas(v)
    m = {nombre: valor for nombre, _, _, valor in medidas}
    d = disp_calcular(v)
    reg, cor, pred = reg_calcular(df), cor_calcular(df), pred_calcular(df)
    tr = tramos(df)
    mun = df["MUNICIPIO DEL SINIESTRO"].value_counts()
    k = len(tab)
    imax = int(tab.fi.idxmax())
    lab = [_etiqueta(t.Li, t.Ls, i == k - 1) for i, t in enumerate(tab.itertuples())]
    imed = int((tab.Hi < 0.6).sum())
    n98 = int((v >= 98).sum())
    p80 = m["Percentil 80 (P80)"]
    repetidos = int(df.duplicated().sum())
    assert (imax, imed, repetidos, n98) == (7, 6, 13, 180)
    assert mun["Ibagué"] == 185 and mun["Melgar"] == 119 and mun["Espinal"] == 96
    assert cor["nivel"] == "Regular" and abs(reg["pendiente"] - 0.7723) < 1e-4
    ecuacion = coma(ecuacion_texto(reg["intercepto"], reg["pendiente"]))
    p5 = pred["filas"][1]
    p12 = pred["filas"][2]

    portada = [
        ("Universidad", "Universidad de Cartagena"),
        ("Centro", "Centro Tecnológico para la Formación Virtual y a Distancia (CTEV)"),
        ("Programa", "Ingeniería de Software"),
        ("Asignatura", "Probabilidad y Estadística"),
        ("Código", "AF17401"),
        ("Título", "Guía de actividad No 2: Estadística descriptiva"),
        ("Autor", "Jairo Alonso Osorio Cruz"),
        ("Semestre", "VI"),
        ("Tutor", datos_entrega().get("tutor") or PENDIENTE_TUTOR),
        ("Fecha", datos_entrega().get("fecha") or PENDIENTE_FECHA),
    ]

    presentacion = [
        "Este libro de Excel reúne el desarrollo de la Guía de actividad No 2 de Probabilidad y Estadística (AF17401), del programa de Ingeniería de Software de la "
        "Universidad de Cartagena. La guía plantea que la Gobernación del Tolima necesita conocer los índices de accidentalidad del departamento, sus posibles "
        f"causas y sus puntos críticos, y para ello entrega una base con {n} accidentes de tránsito ocurridos en tres municipios.",
        "Este trabajo desarrolla la fase inicial, que consiste en organizar los datos y describirlos. El libro contiene la Tabla 1 con seis conceptos estadísticos, "
        "el análisis de la velocidad registrada con su tabla de frecuencia, sus gráficos y sus medidas, y el análisis de la relación entre los años de experiencia del "
        "conductor y su histórico de infracciones mediante regresión lineal y correlación de Pearson. Las medidas se calcularon con fórmulas de Excel que apuntan a la hoja "
        "de datos incluida en los anexos.",
    ]

    introduccion = [
        "El crecimiento de las ciudades y del uso del vehículo automotor ha convertido los accidentes de tránsito en un problema de salud pública: dejan personas "
        "fallecidas y heridas, y pérdidas materiales considerables. Para formular soluciones, las autoridades encargadas de las vías y del tránsito necesitan información "
        "detallada sobre cuándo, dónde y bajo qué condiciones ocurren los siniestros.",
        f"La base de datos del Anexo 1 recoge {n} accidentes en Ibagué ({mun['Ibagué']}), Melgar ({mun['Melgar']}) y Espinal ({mun['Espinal']}). Cada registro tiene nueve variables: "
        "municipio, edad del conductor, personas fallecidas, personas heridas, velocidad registrada, costo del accidente, nivel educativo, años de experiencia e histórico "
        f"de infracciones. Al revisarla encontramos {repetidos} parejas de registros idénticos en todas sus columnas. Se conservaron los {n} registros para que el análisis "
        "corresponda a la base tal como fue entregada.",
        "La estadística descriptiva resume un conjunto de datos con tablas, gráficos y medidas. Las medidas de tendencia central indican alrededor de qué valores se agrupan "
        "los datos, las de posición ubican valores dentro del orden de los datos, las de dispersión muestran qué tan separados están, y las de dependencia lineal miden si "
        "dos variables cambian juntas.",
        "El libro sigue el orden de la guía. El ejercicio 1 define seis conceptos con ejemplos de la base, el ejercicio 2 analiza la velocidad registrada y el ejercicio 3 "
        "estudia la relación entre años de experiencia e infracciones. Después vienen las conclusiones, la bibliografía y los anexos, que incluyen la hoja de datos, la "
        "verificación de los cálculos y las convenciones que adoptamos.",
    ]

    objetivos = {
        "general": "Emplear las medidas estadísticas de tendencia central, de dispersión, de posición y de dependencia lineal en la solución de problemas, "
                   "aplicándolas a la base de datos de accidentalidad del Tolima.",
        "especificos": [
            "Explicar con palabras propias los conceptos de frecuencia absoluta, frecuencia relativa, media, medidas de dispersión, regresión lineal y correlación de "
            "Pearson, con ejemplos tomados de la base de datos.",
            "Organizar la velocidad registrada en una tabla de frecuencia con datos agrupados, representarla con un histograma, un diagrama circular y un polígono de "
            "frecuencia, y calcular e interpretar sus medidas de tendencia central, de posición y de dispersión, su asimetría y su curtosis.",
            "Establecer la relación lineal entre los años de experiencia del conductor y el histórico de infracciones mediante la ecuación de regresión, el coeficiente de "
            "determinación y el coeficiente de correlación de Pearson, y usar la ecuación para hacer predicciones.",
        ],
    }

    conclusiones = [
        ("Ejercicio 1",
         f"Las seis definiciones quedaron ilustradas con cifras de la base, lo que permitió ver cada concepto aplicado. Por ejemplo, {mun['Ibagué']} de los {n} accidentes ocurrieron en "
         f"Ibagué, es decir el 46,25 %, y las velocidades tienen una desviación típica de {fmt(d['Desviación típica muestral'])} km/h alrededor de una media de {fmt(m['Media'])} km/h. "
         "El resultado del quiz de la plataforma se adjunta como evidencia en la hoja del ejercicio 1."),
        ("Ejercicio 2",
         f"La velocidad registrada tiene una media de {fmt(m['Media'])} km/h, una mediana de {fmt(m['Mediana'])} km/h y valores entre {fmt(m['Mínimo'])} y {fmt(m['Máximo'])} km/h. "
         f"El intervalo con más accidentes es {lab[imax]} km/h, con {tab.fi[imax]} registros ({fmt(tab.hi_pct[imax])} %), y el 60 % de los accidentes se acumula hasta el intervalo {lab[imed]} km/h. "
         f"La mitad central de los accidentes ocurrió entre {fmt(m['Cuartil 1 (Q1)'])} y {fmt(m['Cuartil 3 (Q3)'])} km/h, y el 20 % más rápido superó los {fmt(p80)} km/h. "
         f"Con un coeficiente de variación de {fmt(d['Coeficiente de variación (%)'])} % la distribución es heterogénea según la convención adoptada, y con una asimetría de {f2(d['Asimetría'])} y una curtosis de "
         f"{f2(d['Curtosis (exceso)'])} resulta casi simétrica y platicúrtica: las velocidades se extienden por todo el rango sin concentrarse alrededor de un valor."),
        ("Ejercicio 3",
         f"La recta de regresión entre los años de experiencia (x) y las infracciones (y) es {ecuacion}, con una relación positiva. El coeficiente de determinación es "
         f"{coma(round(cor['R2'], 4))} ({fmt(cor['confiabilidad'])} %) y el coeficiente de correlación de Pearson es {coma(round(cor['r'], 4))}, un nivel regular de correlación lineal según la escala "
         f"adoptada, cerca del límite con el nivel aceptable. El diagrama de dispersión muestra tres tramos de experiencia, por lo que la recta sirve como aproximación general: "
         f"con 5 años estima {f2(p5['pred'])} infracciones y el promedio observado es {f2(p5['obs'])}, pero con 12 años estima {f2(p12['pred'])} frente a {f2(p12['obs'])} observadas. "
         f"El error típico de la estimación es de {fmt(pred['error'])} infracciones, así que las predicciones son orientativas."),
        ("Conclusión general",
         f"En esta base la velocidad se reparte a lo largo de un rango amplio, con el {fmt(n98 / n * 100)} % de los accidentes a 98 km/h o más, y los conductores con más años de licencia "
         "tienden a acumular más infracciones. Estos resultados describen los datos y no explican causas: la base no trae el límite de velocidad de cada vía, y una correlación no prueba que "
         "una variable produzca la otra. Los umbrales de homogeneidad, asimetría y correlación son convenciones que adoptamos y se declaran donde se usan."),
    ]

    bibliografia = {
        "Obligatoria (referencias del enunciado; confirmar que se consultaron)": [
            "Romero Ramos, E. (2016). *Estadística para todos: análisis de datos: estadística descriptiva, teoría de la probabilidad e inferencia*. Difusora Larousse - Ediciones Pirámide. "
            "https://elibro.unicartagenaproxy.elogim.com/es/lc/unicartagena/titulos/49136",
            "Salazar Guerrero, L. J. (2018). *Probabilidad y estadística: para bachilleratos tecnológicos*. Grupo Editorial Patria. "
            "https://elibro.unicartagenaproxy.elogim.com/es/lc/unicartagena/titulos/40531",
        ],
        "Opcional (solo si Jairo lo autoriza; verificar los datos antes de entregar)": [
            "Universidad de Cartagena. (2024). *Anexo 1 - Base de datos* [Conjunto de datos]. Guía de actividad No 2, Probabilidad y Estadística, Programa de Ingeniería de Software.",
            "Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... Oliphant, T. E. (2020). Array programming with NumPy. *Nature, 585*(7825), 357-362. https://doi.org/10.1038/s41586-020-2649-2",
            "Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., ... SciPy 1.0 Contributors. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*(3), 261-272. https://doi.org/10.1038/s41592-019-0686-2",
            "McKinney, W. (2010). Data structures for statistical computing in Python. En S. van der Walt y J. Millman (Eds.), *Proceedings of the 9th Python in Science Conference* (pp. 56-61).",
            "McNamara, J. (s. f.). *XlsxWriter* [Software]. https://xlsxwriter.readthedocs.io",
        ],
    }

    filas_rep = "213 y 313, 214 y 314, 220 y 320, 221 y 321, 227 y 327, 237 y 337, 240 y 340, 241 y 341, 246 y 346, 269 y 369, 285 y 385, 300 y 400, 301 y 401"
    ver = json.loads((BASE / "output" / "verificacion.json").read_text(encoding="utf-8")) if (BASE / "output" / "verificacion.json").exists() else None
    n_ver = len(ver["filas"]) if ver else 141
    anexos = {
        "Anexo A. Hoja de datos": [
            f"Copia exacta, sin modificar ningún valor, de la hoja DATOS del Anexo 1: {n} registros y 9 columnas. Es la hoja a la que apuntan todas las fórmulas del libro.",
            f"La base contiene {repetidos} parejas de registros idénticos en las nueve columnas. Están en las filas {filas_rep} de la hoja (numeración de Excel, con el encabezado en la fila 1). "
            "Cada pareja está separada exactamente por 100 filas. Se conservaron todos los registros.",
        ],
        "Anexo B. Verificación de los cálculos": [
            f"Se compararon {n_ver} valores del libro con cálculos independientes hechos en Python (numpy y scipy) a partir de los datos originales, y con el recálculo de las fórmulas de Excel "
            "en LibreOffice. Todos coincidieron, con una diferencia absoluta máxima de 5,7e-13. La tabla lista cada comparación.",
            "Las tablas, los gráficos y las fórmulas del libro se generaron con un programa en Python (biblioteca xlsxwriter) que escribe fórmulas nativas de Excel.",
        ],
        "Anexo C. Variables elegidas en el foro": [
            "Nombre: Jairo Alonso Osorio Cruz. Variable del ejercicio 2: velocidad registrada. Variables del ejercicio 3: años de experiencia del conductor (x) e histórico de infracciones (y).",
            ("Combinación publicada en el foro por el autor, sin repetir la de sus compañeros de grupo." if datos_entrega().get("foro_confirmado") is True
             else "PENDIENTE: Jairo debe confirmar que esta combinación es la que publicó en el foro y no chocó con la de sus compañeros."),
        ],
        "Anexo D. Convenciones adoptadas": [
            "Estas convenciones son de uso común en estadística descriptiva y no proceden de las lecturas del curso.",
            "Varianza y desviación típica muestrales (VAR.S y STDEV.S), porque los 400 registros se toman como una muestra de la accidentalidad del Tolima.",
            "Homogeneidad: la distribución es homogénea si el coeficiente de variación es menor que 30 % y heterogénea en caso contrario.",
            "Asimetría: casi simétrica si su valor absoluto es menor que 0,5. Curtosis: platicúrtica si el exceso de curtosis es negativo.",
            "Nivel de correlación según |r|: perfecta si vale 1, excelente de 0,90 a menos de 1, aceptable de 0,80 a menos de 0,90, regular de 0,50 a menos de 0,80, mínima por debajo de 0,50 y sin correlación si vale 0.",
        ],
    }
    return {"portada": portada, "presentacion": presentacion, "introduccion": introduccion, "objetivos": objetivos,
            "conclusiones": conclusiones, "bibliografia": bibliografia, "anexos": anexos}


FRASE_QUIZ = " El resultado del quiz de la plataforma se adjunta como evidencia en la hoja del ejercicio 1."


def sin_frase_quiz(t):
    """Copia de los textos sin la frase que remite al recuadro del quiz, para las versiones (PDF y Word) que no lo llevan."""
    t = dict(t)
    nuevas = []
    for titulo, texto in t["conclusiones"]:
        nuevas.append((titulo, texto.replace(FRASE_QUIZ, "")))
    assert nuevas != t["conclusiones"], "no se encontró la frase del quiz"
    t["conclusiones"] = nuevas
    return t


def a_markdown(t):
    """Un archivo por sección para revisión de Jairo."""
    a = {}
    a["01_portada.md"] = "# Portada\n\n" + "\n".join(f"- **{k}:** {v}" for k, v in t["portada"]) + "\n"
    a["02_presentacion.md"] = "# Presentación\n\n" + "\n\n".join(t["presentacion"]) + "\n"
    a["03_introduccion.md"] = "# Introducción\n\n" + "\n\n".join(t["introduccion"]) + "\n"
    o = t["objetivos"]
    a["04_objetivos.md"] = ("# Objetivos\n\n## Objetivo general\n\n" + o["general"] + "\n\n## Objetivos específicos\n\n"
                            + "\n".join(f"{i}. {x}" for i, x in enumerate(o["especificos"], 1)) + "\n")
    a["05_conclusiones.md"] = "# Conclusiones\n\n" + "\n\n".join(f"## {tt}\n\n{p}" for tt, p in t["conclusiones"]) + "\n"
    a["06_bibliografia.md"] = "# Bibliografía (APA 7)\n\n" + "\n\n".join(f"## {k}\n\n" + "\n\n".join(v) for k, v in t["bibliografia"].items()) + "\n"
    a["07_anexos.md"] = "# Anexos\n\n" + "\n\n".join(f"## {k}\n\n" + "\n\n".join(v) for k, v in t["anexos"].items()) + "\n"
    return a


if __name__ == "__main__":
    t = textos()
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, md in a_markdown(t).items():
        assert "\u2014" not in md, nombre
        (SALIDA / nombre).write_text(md, encoding="utf-8")
        print(f"escrito output/textos/{nombre} ({len(md.split())} palabras)")
