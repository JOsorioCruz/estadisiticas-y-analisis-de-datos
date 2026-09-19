# Entrega de la Actividad No 2 (AF17401)

Este documento explica qué se entrega, cómo cubre cada punto del enunciado y de la rúbrica, y qué debe hacer el autor antes de subirla a la plataforma.

## Qué se entrega

| Archivo | Para qué sirve |
|---|---|
| `output/actividad_probabilidad_y_estadistica_unidad_2.xlsx` | **Entrega principal.** El enunciado pide el trabajo escrito consolidado en Excel. |
| `output/actividad_probabilidad_y_estadistica_unidad_2.pdf` | Copia en PDF de 20 páginas para leer el trabajo sin abrir Excel. Es el mismo libro sin la hoja `DATOS` de 400 filas, con cada gráfico junto a su conclusión y el enlace al repositorio al inicio de la portada. Por pedido del autor **no incluye** el tutor, la fecha, la línea del CTEV, el recuadro del quiz ni la nota de confirmación del foro del Anexo C. |
| `output/textos_actividad_probabilidad_y_estadistica_unidad_2.docx` | Todos los textos del trabajo en un solo documento de Word de 15 páginas, con las mismas exclusiones que el PDF y sin imágenes. |

Si el docente solo acepta Excel, se sube el `.xlsx`. El PDF es un complemento.

## Cómo cubre el enunciado

### Ejercicio 1 (rúbrica: 1,0 punto)

| Lo que pide el enunciado | Dónde está |
|---|---|
| Tabla 1 con seis conceptos: definición con palabras propias y ejemplos | Hoja **Ejercicio 1**, tabla `Conceptos, Definiciones, Ejemplos` |
| Captura del quiz como evidencia en la hoja del ejercicio 1 | Hoja **Ejercicio 1**, recuadro `Evidencia del quiz: insertar captura aquí` (lo llena el autor) |

### Ejercicio 2 (rúbrica: 1,5 puntos), variable: velocidad registrada (km/h)

| Lo que pide el enunciado | Dónde está (hoja **Ejercicio 2**) |
|---|---|
| Tabla de frecuencia con datos agrupados | Bloque superior: parámetros (n, rango, k de Sturges, amplitud) y tabla con `fi`, `Fi`, `hi`, `Hi` y porcentajes |
| Histograma, diagrama circular y polígono, con conclusiones | Bloque `Gráficos estadísticos y conclusiones`: tres gráficos nativos, cada uno con su conclusión debajo |
| ¿En cuál intervalo hay más datos? ¿Hasta cuál se acumula el 60 %? | Bloque `Preguntas con base en la tabla de frecuencia` |
| Media, mediana y moda con fórmulas de Excel | Bloque `Medidas de tendencia central y de posición` (`AVERAGE`, `MEDIAN`, `MODE.SNGL`) |
| Cuartil 1, decil 5 y percentil 80 | Mismo bloque (`QUARTILE.INC`, `PERCENTILE.INC`); se añadieron Q3 y P10 como en el ejemplo del enunciado |
| Interpretación en una tabla `Medida, Resultado, Interpretación` | Mismo bloque: una frase por medida en el contexto de accidentes |
| Varianza, desviación típica, coeficiente de variación, asimetría y curtosis | Bloque `Dispersión, asimetría y curtosis` (`VAR.S`, `STDEV.S`, `SKEW`, `KURT`) |
| ¿Homogénea o heterogénea? ¿Qué concentración y asimetría? | Bloque `Análisis de la distribución`: tres preguntas con su respuesta |

### Ejercicio 3 (rúbrica: 1,5 puntos), variables: años de experiencia (x) e histórico de infracciones (y)

| Lo que pide el enunciado | Dónde está (hoja **Ejercicio 3**) |
|---|---|
| Ecuación de regresión lineal | Bloque `Ecuación de regresión lineal` (`SLOPE`, `INTERCEPT`) |
| Diagrama de dispersión con la recta; relación positiva, negativa o sin relación | Diagrama nativo con línea de tendencia, y el tipo de relación con su lectura |
| Coeficiente de determinación y porcentaje de confiabilidad | Bloque `Coeficiente de determinación, confiabilidad y correlación de Pearson` (`RSQ`) |
| Coeficiente de Pearson y nivel de correlación lineal | Mismo bloque (`CORREL`), con la escala de niveles declarada |
| Tres predicciones con la ecuación | Bloque `Predicciones con la ecuación de regresión`, con los valores de x editables |

### Criterios que no dependen del libro

| Criterio | Puntos | Quién lo hace |
|---|---|---|
| Participación en el foro | 0,5 | El autor, a mano |
| Entrega a tiempo y siguiendo las indicaciones | 0,5 | El autor, a mano |

### Reglas de forma del enunciado

| Regla | Cómo se cumple |
|---|---|
| Entrega en Excel | Libro `.xlsx` con las hojas Portada, Presentación, Introducción, Objetivos, Ejercicio 1, 2 y 3, Conclusiones, Bibliografía, Anexos y DATOS |
| Ortografía correcta | Se pasó el corrector del sistema en español por todos los textos; solo marcó términos técnicos, funciones de Excel y una URL |
| Referencias en normas APA | Bibliografía en APA 7 con las dos lecturas del enunciado |
| Plantilla del foro | El enunciado menciona una plantilla que no se tiene en este proyecto. Se siguió la estructura de la guía del prompt. Si el autor la tiene, conviene compararla con el libro |

## Qué debe hacer el autor antes de subirla

El libro entregado por este proyecto tiene tres campos amarillos marcados `PENDIENTE` (tutor, fecha y confirmación de las variables del foro) y el recuadro del quiz vacío, porque son datos que solo el autor conoce. Pasos, en este orden:

1. **Completar tutor y fecha.** Copiar `datos_entrega.ejemplo.json` como `datos_entrega.json` en la raíz, escribir el tutor y la fecha, y poner `"foro_confirmado": true` cuando haya confirmado que su combinación de variables es la que publicó en el foro. Ese archivo no se sube al repositorio.
2. **Regenerar el libro y el PDF.**
   ```bash
   .venv/bin/python src/generar_libro.py
   .venv/bin/python src/exportar_pdf.py
   ```
3. **Hacer el quiz** en la plataforma y **pegar la captura** en el recuadro de la hoja `Ejercicio 1` del `.xlsx`. **Después de pegarla no se debe volver a ejecutar `generar_libro.py`**, porque sobrescribe el archivo y la captura se perdería.
4. **PDF y Word.** Ninguno de los dos lleva el recuadro del quiz, el tutor ni la fecha, así que no dependen de los pasos 1 y 3: se regeneran con `.venv/bin/python src/exportar_pdf.py` y `.venv/bin/python src/exportar_docx.py` cuando cambie algún texto.
5. **Leer los textos y reescribir con su voz** lo que no suene como él, sobre todo la Tabla 1 (la rúbrica pide que esté con sus propias palabras). Los cambios se hacen en `src/ej1_tabla.py` y `src/textos_libro.py` si se quiere regenerar, o directamente en el Excel si ya pegó la captura.
6. **Abrir el libro en Microsoft Excel** y comprobar que los valores coinciden con la tabla de verificación de Anexos. La verificación se hizo con LibreOffice y no se probó en Excel.
7. **Bibliografía:** confirmar que consultó las dos lecturas. Si quiere añadir el Anexo 1 y las librerías de Python, están redactadas en `output/textos/06_bibliografia.md`, pero sus datos se escribieron de memoria y deben verificarse.
8. **Anexo B:** decidir si el libro debe decir que se generó con un programa de Python. Ahora lo dice.
9. **Participar en el foro y subir el archivo** a la plataforma a tiempo.

### Carpeta de entrega local

Según la convención del repositorio `AGENTE_UNIVERSIDAD`, las actividades van en `actividades/<materia>/` con el nombre `actividad_<materia>_unidad_<N>`:

```
AGENTE_UNIVERSIDAD/actividades/probabilidad y estadistica/actividad_probabilidad_y_estadistica_unidad_2.xlsx
```

**Ya hay ahí una copia de trabajo del libro**, hecha el 18 de septiembre de 2026 con el libro tal como estaba: con los campos `PENDIENTE` y el recuadro del quiz vacío. No es la versión final. Cuando el autor termine los pasos anteriores hay que **volver a copiar el libro final, que reemplaza a esa copia**, desde la raíz de este proyecto:

```bash
cp output/actividad_probabilidad_y_estadistica_unidad_2.xlsx "$HOME/WebstormProjects/AGENTE_UNIVERSIDAD/actividades/probabilidad y estadistica/"
```

## Nombre del archivo y fechas

El nombre `actividad_probabilidad_y_estadistica_unidad_2.xlsx` sigue la carpeta `unidad_2` en la que se guardó el enunciado. La guía se titula "Unidad I" y trae fechas de marzo de 2024; esas fechas **no** se copiaron a la portada. Si el nombre debe ser otro, se cambia la constante `NOMBRE_ARCHIVO` en `src/generar_libro.py`.
