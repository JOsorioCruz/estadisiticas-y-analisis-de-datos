# Actividad No 2 de Probabilidad y Estadística: accidentalidad en el Tolima

Trabajo de la **Guía de actividad No 2: Estadística descriptiva** (código AF17401), del programa de Ingeniería de Software de la Universidad de Cartagena. Autor: Jairo Alonso Osorio Cruz, semestre VI.

La guía plantea que la Gobernación del Tolima necesita conocer los índices de accidentalidad del departamento. Para eso entrega una base con 400 accidentes de tránsito de Ibagué, Melgar y Espinal. Este proyecto resuelve los tres ejercicios de la guía y produce como resultado **un libro de Excel** y una **copia en PDF**, generados con Python y verificados de forma independiente.

- Ejercicio 1: definiciones de seis conceptos estadísticos, con ejemplos tomados de la base.
- Ejercicio 2: análisis de una variable, la velocidad registrada (tabla de frecuencia, gráficos, medidas de tendencia central, de posición y de dispersión, asimetría y curtosis).
- Ejercicio 3: regresión lineal y correlación entre los años de experiencia del conductor y su histórico de infracciones.

> Este es un trabajo académico individual. Los materiales del curso (el enunciado y la base de datos) pertenecen a la Universidad de Cartagena.

## Contenido del repositorio

```
.
├── README.md                     este archivo
├── ENTREGA.md                    qué se entrega, cómo cubre el enunciado y pasos antes de subirlo
├── Actividad No 2 ... .pdf       enunciado y rúbrica del docente
├── Anexo 1 - Base de datos .xlsx base de datos original (hoja DATOS, 400 registros)
├── requirements.txt              versiones exactas de los paquetes de Python
├── datos_entrega.ejemplo.json    plantilla para tutor y fecha de la portada
├── task/                         plan.md y un archivo por tarea (00 a 15) con su resultado
├── src/                          scripts de Python, uno por tarea o módulo reutilizable
└── output/                       libro final, PDF, textos para revisión y tabla de verificación
```

`main.py` es el archivo de ejemplo que crea PyCharm y no forma parte del trabajo.

## La entrega

| Archivo | Descripción |
|---|---|
| `output/actividad_probabilidad_y_estadistica_unidad_2.xlsx` | Libro de Excel completo. Todas las medidas son fórmulas de Excel que apuntan a la hoja `DATOS`. |
| `output/actividad_probabilidad_y_estadistica_unidad_2.pdf` | Copia en PDF de 21 páginas, sin la hoja de datos, con cada gráfico junto a su conclusión. |

Hojas del libro, en orden: **Portada, Presentación, Introducción, Objetivos, Ejercicio 1, Ejercicio 2, Ejercicio 3, Conclusiones, Bibliografía, Anexos y DATOS**. La hoja `DATOS` es una copia exacta del Anexo 1.

La portada tiene tres campos amarillos por completar (tutor, fecha y confirmación de las variables del foro) y la hoja del Ejercicio 1 tiene un recuadro para pegar la captura del quiz. Los pasos están en [ENTREGA.md](ENTREGA.md).

## Resultados principales

**Ejercicio 2: velocidad registrada (km/h), n = 400**

| Medida | Resultado |
|---|---|
| Tabla de frecuencia | 10 intervalos por la regla de Sturges, amplitud 11, desde 32 |
| Intervalo con más accidentes | [109 - 120) km/h, con 62 accidentes (15,5 %) |
| Intervalo donde se acumula el 60 % | [98 - 109) km/h (acumulado 67 %) |
| Media, mediana y moda | 89,86 · 94,05 · 81,6 |
| Mínimo, máximo y rango | 32,1 · 140,8 · 108,7 |
| Q1, D5, Q3, P10 y P80 | 66,25 · 94,05 · 114,85 · 44,03 · 117,98 |
| Varianza y desviación típica muestrales | 923,52 · 30,39 |
| Coeficiente de variación | 33,82 %, distribución heterogénea según la convención adoptada |
| Asimetría y curtosis | -0,26 (casi simétrica) · -1,00 (platicúrtica) |

**Ejercicio 3: años de experiencia (x) e infracciones (y)**

| Medida | Resultado |
|---|---|
| Ecuación de regresión | y = 1,7278 + 0,7723 x |
| Relación | Positiva |
| Coeficiente de determinación (confiabilidad) | 0,5966 (59,66 %) |
| Coeficiente de Pearson y nivel | 0,7724, regular según la escala adoptada |
| Predicciones | 1 año: 2,50 · 5 años: 5,59 · 12 años: 11,00 infracciones |
| Error típico de la estimación | 2,52 infracciones |

### Hallazgos sobre los datos

- **13 parejas de registros idénticos** en las nueve columnas, cada una separada exactamente por 100 filas. Se conservaron los 400 registros para que el análisis coincida con la base entregada. Las filas exactas están en el Anexo A del libro.
- **La relación entre experiencia e infracciones tiene forma de escalón**, no de nube continua. Con 0 o 1 año (118 conductores) las infracciones van de 0 a 2. Con 2 a 10 años (256) van de 2 a 8 y su promedio casi no cambia (4,33 a 6,00). Con 11 años o más (26) van de 10 a 20. La recta sirve como aproximación general, pero acierta en el tramo medio y falla en los extremos. Por eso las tres predicciones se eligieron una por tramo, para mostrar dónde funciona el modelo y dónde no.
- **Tres registros** tienen más años de experiencia que `edad - 16` (por ejemplo, edad 16 con 6 años de licencia). Es una observación de calidad de datos y no se corrigió nada, porque la hoja debe quedar idéntica al Anexo 1.

### Convenciones adoptadas

Son convenciones de uso común en estadística descriptiva. **No proceden de las lecturas del curso**, porque no se contó con su texto, y así se declara en el libro (Anexo D).

- Varianza y desviación muestrales (`VAR.S`, `STDEV.S`), porque los 400 registros se toman como una muestra de la accidentalidad del Tolima.
- Distribución homogénea si el coeficiente de variación es menor que 30 %, y heterogénea en caso contrario. Con 33,82 % la clasificación queda cerca del límite y el texto lo dice.
- Casi simétrica si el valor absoluto de la asimetría es menor que 0,5. Platicúrtica si el exceso de curtosis es negativo.
- Nivel de correlación según |r|: perfecta si vale 1, excelente de 0,90 a menos de 1, aceptable de 0,80 a menos de 0,90, regular de 0,50 a menos de 0,80, mínima por debajo de 0,50 y sin correlación si vale 0.

Si las lecturas traen otros criterios, se cambian en `src/ej2_dispersion.py` (`CV_LIMITE`, `ASIM_LIMITE`) y en `src/ej3_correlacion.py` (`ESCALA`), y se regenera el libro.

## Cómo se verificó

- **Valores.** 141 valores del libro se compararon con cálculos independientes hechos en Python con numpy y scipy, y con el recálculo de las fórmulas en LibreOffice. Los 141 coinciden, recalculados y guardados en el archivo, con una diferencia máxima de 5,7e-13. La tabla completa está en la hoja Anexos y en `output/verificacion.json`.
- **La verificación puede fallar.** Se inyectaron errores a propósito (0,001 en una media y 0,1 en una moda) y se detectaron.
- **Estructura.** 169 celdas con fórmula y 0 errores de Excel tras recalcular. Cuatro gráficos nativos (histograma, circular, polígono y dispersión con línea de tendencia), ninguna imagen, ningún guion largo y hoja `DATOS` idéntica al Anexo 1.
- **Revisión final** (`src/revision_final.py`). 28 comprobaciones automáticas de cada viñeta del enunciado, de los gráficos (título, ejes y unidades), de las fórmulas y de los textos, todas en orden. Cada cifra que aparece en un texto se rastreó a una celda del libro o a un cálculo sobre los datos.
- **Ortografía.** Se pasó el corrector del sistema en español por todos los textos. Solo marcó términos técnicos, funciones de Excel en inglés, un nombre propio y una URL.
- **Reproducibilidad.** Dos ejecuciones seguidas de `generar_libro.py` producen el mismo contenido, celda por celda.

### Limitaciones

- El recálculo se hizo en **LibreOffice**, no en Microsoft Excel. Las fórmulas usan funciones estándar con el prefijo `_xlfn.` donde hace falta (por ejemplo `MODE.SNGL` y `STDEV.S`), pero no se probaron en Excel.
- Las etiquetas de porcentaje del gráfico circular y la ecuación de la línea de tendencia se dibujan distinto según el visor.
- Los resultados describen la base de datos y no explican causas: la base no trae el límite de velocidad de cada vía, y una correlación no prueba que una variable produzca la otra.

## Cómo reproducirlo

Requisitos: Python 3.13, los paquetes de `requirements.txt` (pandas, numpy, scipy, xlsxwriter y openpyxl) y **LibreOffice**, porque la verificación y el PDF se generan con él. La ruta del ejecutable está en la constante `SOFFICE` de `src/ej2_tabla.py` (`/opt/homebrew/bin/soffice`, la de Homebrew en macOS); en otro sistema hay que ajustarla. La revisión ortográfica usa `swift`, que viene con las herramientas de línea de comandos de Xcode.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Desde la raíz del proyecto:

```bash
.venv/bin/python src/generar_libro.py     # genera y verifica el libro final
.venv/bin/python src/exportar_pdf.py      # genera la copia en PDF
.venv/bin/python src/revision_final.py    # revisión final contra el enunciado y la rúbrica
.venv/bin/python src/verificacion.py      # tabla de verificación cruzada (output/verificacion.json)
```

Para poner el tutor y la fecha en la portada, copiar `datos_entrega.ejemplo.json` como `datos_entrega.json` (que el `.gitignore` excluye) y completarlo antes de generar. **Aviso:** `generar_libro.py` sobrescribe el `.xlsx`, así que cualquier cambio hecho a mano en el archivo, como la captura del quiz, se pierde si se vuelve a ejecutar.

### Scripts de `src/`

| Script | Qué hace |
|---|---|
| `carga.py` | Lee y valida la hoja `DATOS` del Anexo 1 |
| `hoja_datos.py` | Copia la hoja `DATOS` al libro y arma las referencias de rango |
| `ej1_tabla.py` | Tabla 1 y comprobación de las cifras de sus ejemplos contra los datos |
| `ej2_tabla.py` | Tabla de frecuencia con datos agrupados, con fórmulas `COUNTIFS` |
| `ej2_graficos.py` | Histograma, circular y polígono de frecuencia, con sus conclusiones |
| `ej2_preguntas.py` | Intervalo de mayor frecuencia e intervalo del 60 % acumulado |
| `ej2_medidas.py` | Tendencia central y posición, con la tabla `Medida, Resultado, Interpretación` |
| `ej2_dispersion.py` | Dispersión, asimetría, curtosis y homogeneidad |
| `ej3_regresion.py` | Ecuación de regresión y diagrama de dispersión con recta |
| `ej3_correlacion.py` | Coeficiente de determinación, confiabilidad, r de Pearson y nivel de correlación |
| `ej3_predicciones.py` | Tres predicciones con la ecuación |
| `textos_libro.py` | Portada, presentación, introducción, objetivos, conclusiones, bibliografía y anexos |
| `verificacion.py` | Verificación cruzada contra numpy y scipy con recálculo de LibreOffice |
| `generar_libro.py` | Ensambla el libro completo y lo verifica |
| `exportar_pdf.py` | Exporta el libro a PDF sin la hoja de datos |
| `revision_final.py` | Revisión final contra el enunciado, la rúbrica y la lista de comprobación |
| `corrector.swift` | Usa el corrector ortográfico del sistema para revisar los textos |

Cada módulo de ejercicio se puede ejecutar solo: genera un borrador en `output/` (ignorado por git) y se verifica a sí mismo.

## Cómo se trabajó

El trabajo se hizo en **16 tareas pequeñas, una por una y cada una aprobada por el autor**. Cada tarea tiene su archivo en `task/` con objetivo, pasos, criterio de aceptación y resultado con números reales, y `task/plan.md` es el índice con el estado.

| # | Tarea |
|---|---|
| 00 | Preparar el entorno |
| 01 | Cargar y validar la base |
| 02 | Elegir las variables |
| 03 | Ejercicio 1: definiciones y ejemplos |
| 04 | Ejercicio 2: tabla de frecuencia agrupada |
| 05 | Ejercicio 2: histograma, circular y polígono |
| 06 | Ejercicio 2: intervalo mayor y 60 % acumulado |
| 07 | Ejercicio 2: tendencia central, posición y tabla interpretada |
| 08 | Ejercicio 2: dispersión, asimetría, curtosis y homogeneidad |
| 09 | Ejercicio 3: ecuación de regresión y diagrama de dispersión |
| 10 | Ejercicio 3: R², confiabilidad, Pearson y nivel de correlación |
| 11 | Ejercicio 3: tres predicciones |
| 12 | Verificación cruzada |
| 13 | Redactar los textos del libro |
| 14 | Ensamblar el libro |
| 15 | Revisión final y entrega |

Decisiones del autor: variable del ejercicio 2 (velocidad), par del ejercicio 3 (experiencia con infracciones, en ese sentido), conservar los 400 registros, incluir Q3 y P10 además de lo exigido, usar `VAR.S`, y adoptar las convenciones de homogeneidad, asimetría y correlación.

## Reglas del proyecto

- Nada de lo que aparece en el libro está inventado: cada número sale de la base real y cada interpretación se rastrea a una celda.
- Las definiciones, interpretaciones y conclusiones están escritas con lenguaje de estudiante, en primera persona plural o impersonal.
- El libro de Excel no contiene imágenes: los gráficos son nativos de Excel.
- No hay ningún guion largo en el libro, en el PDF ni en los textos.
- Este proyecto no hace el quiz de la plataforma, no publica en el foro y no sube el archivo a la plataforma.
