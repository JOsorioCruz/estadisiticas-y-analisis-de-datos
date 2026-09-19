# Tarea 08: Ejercicio 2: dispersión, asimetría, curtosis y homogeneidad
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Calcular varianza, desviación típica, coeficiente de variación, asimetría y curtosis, y responder si la distribución es homogénea o heterogénea y qué concentración y asimetría tiene.

## Entradas (archivos o decisiones que necesita)
- Variable fijada en la tarea 02.
- Decisión sobre `VAR.S` o `VAR.P`.
- Criterio de homogeneidad y de clasificación de asimetría y curtosis.

## Pasos
1. Preguntar a Jairo si usa `VAR.S` o `VAR.P`, con justificación. Los 400 registros pueden verse como muestra de la accidentalidad del Tolima o como la población de esta base.
2. Pedir la convención del CV para llamar homogénea o heterogénea una distribución, y la lectura de asimetría y curtosis, si no salen de las lecturas. Si se elige una convención, se cita como tal.
3. Calcular con `VAR.*`, `STDEV.*`, `SKEW` y `KURT` y verificar contra scipy.
4. Redactar un párrafo de análisis.

## Entregable (archivo o celdas concretas que produce)
Tabla de medidas y párrafo de análisis.

## Criterio de aceptación (cómo compruebo que está bien)
Valores iguales a scipy dentro de una tolerancia de 1e-9 y conclusión apoyada en un criterio declarado.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej2_dispersion.py`: bloque "Dispersión, asimetría y curtosis", con fórmulas, interpretaciones, convención y análisis, más verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej2_dispersion.py`. Usa `use_future_functions` para que `VAR.S` y `STDEV.S` lleven el prefijo `_xlfn.`.
- `output/ej2_dispersion_borrador.xlsx`: hoja `Ej2 Tabla` completa hasta esta tarea, más `DATOS`. Borrador de trabajo.

**Decisiones de Jairo:** varianza y desviación muestrales (`VAR.S`, `STDEV.S`), y las convenciones propuestas para interpretar.

**Convención adoptada (declarada en el libro como convención de uso común, no de las lecturas)**
- Homogénea si CV menor que 30 %; heterogénea si es 30 % o más.
- Casi simétrica si |asimetría| menor que 0,5; en otro caso, asimétrica positiva o negativa según el signo.
- Platicúrtica si la curtosis en exceso es negativa; leptocúrtica si es positiva.

**Resultados (velocidad registrada, n = 400)**

| Medida | Resultado | Fórmula de Excel | Interpretación |
|---|---|---|---|
| Varianza muestral | 923,5201 | `VAR.S` | Es el promedio de los cuadrados de las distancias de cada velocidad a la media, y vale 923,52 (km/h)². Como está en unidades al cuadrado, se interpreta mejor con la desviación típica. |
| Desviación típica muestral | 30,3895 | `STDEV.S` | Las velocidades se desvían típicamente unos 30,39 km/h de la media de 89,86 km/h. |
| Coeficiente de variación (%) | 33,8181 | Desviación típica / Media x 100 | La desviación típica equivale al 33,82 % de la media. Es la medida que usamos para decidir si la distribución es homogénea. |
| Asimetría | -0,2611 | `SKEW` | Es -0,26: negativa y de tamaño pequeño. La cola es un poco más larga hacia las velocidades bajas, en línea con que la mediana (94,05) quede por encima de la media (89,86). |
| Curtosis (exceso) | -1,0033 | `KURT` | Es -1,00, medida en exceso respecto a la distribución normal (que vale 0). Al ser negativa la distribución es platicúrtica, más aplanada que la normal. |

**Respuestas del enunciado**

**¿La distribución es homogénea o heterogénea?** Es heterogénea. Con la convención adoptada (CV menor que 30 % es homogénea), el coeficiente de variación de 33,82 % la deja del lado heterogéneo, aunque cerca del límite. Las velocidades cambian de forma apreciable de un accidente a otro, y con otro umbral la etiqueta podría cambiar, por eso conviene dar el valor del CV junto con la conclusión.

**¿Qué tipo de concentración presentan los datos?** La curtosis en exceso de -1,00 indica una distribución platicúrtica, es decir, con poca concentración de datos alrededor de la media. Las velocidades se extienden a lo largo del rango en vez de agruparse alrededor de un solo pico, algo que también se ve en el histograma: ningún intervalo pasa de 15,5 % de los accidentes.

**¿Qué tipo de asimetría presentan los datos?** La asimetría de -0,26 es negativa. Con la convención adoptada (valor absoluto menor que 0,5 es casi simétrica), la distribución es casi simétrica, con una cola ligeramente más larga hacia las velocidades bajas. Esto coincide con que la media (89,86) sea algo menor que la mediana (94,05).

**Verificación**
- LibreOffice recalculó una copia **sin valores guardados**. Comparación de las cinco medidas contra scipy/numpy y contra pandas (`var`, `std`, `skew`, `kurt`): diferencia máxima 5,7e-13.
- El CV se calcula en Excel dividiendo las celdas de desviación típica y media de la propia hoja (`=B/B*100`), así que queda rastreable.
- Coherencia entre resultados: media (89,86) menor que mediana (94,05) concuerda con asimetría negativa; curtosis negativa concuerda con que el histograma no tenga un pico dominante (mayor porción 15,5 %).
- Revisión visual del bloque renderizado.
- Sin guiones largos.

**Observaciones para Jairo**
- El CV de 33,82 % está cerca del umbral de 30 %. Con otra convención (por ejemplo 50 %) la etiqueta sería "homogénea". El texto lo dice, y conviene mantenerlo así, porque es una limitación real de clasificar con un umbral. Si consigues las lecturas, se puede cambiar la convención en una constante (`CV_LIMITE`) y volver a generar.
- Los tres textos de análisis y las cinco interpretaciones tienen un registro neutro. Puedes retocarlos a tu voz.
- Los textos comprueban con `assert` que las etiquetas (heterogénea, casi simétrica, platicúrtica) siguen siendo ciertas, para que un cambio de datos o de umbral no deje afirmaciones falsas.
