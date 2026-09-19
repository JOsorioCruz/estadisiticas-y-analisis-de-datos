# Tarea 14: Ensamblar el libro
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Generar el libro completo con `xlsxwriter` y todas las hojas de la sección 7.

## Entradas (archivos o decisiones que necesita)
- Todas las tareas anteriores aprobadas.
- Nombre final del archivo.

## Pasos
1. Escribir `src/generar_libro.py`, reproducible y con rutas relativas.
2. Crear las hojas en este orden: Portada, Presentación, Introducción, Objetivos, Ejercicio 1, Ejercicio 2, Ejercicio 3, Conclusiones, Bibliografía, Anexos.
3. Copiar la hoja de datos idéntica al Anexo 1 y apuntar las fórmulas a ella.
4. Dar formato legible, sin imágenes.

## Entregable (archivo o celdas concretas que produce)
`output/actividad_probabilidad_y_estadistica_unidad_2.xlsx` (nombre por confirmar).

## Criterio de aceptación (cómo compruebo que está bien)
El libro abre en Excel y en LibreOffice, las fórmulas muestran valores, y la hoja de datos coincide celda por celda con el Anexo 1.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/generar_libro.py`: genera el libro completo, con doble pasada (la primera calcula la tabla de verificación sobre el propio libro; la segunda la incluye en Anexos) y verifica el archivo final. Se ejecuta desde la raíz con `.venv/bin/python src/generar_libro.py`. Sin rutas absolutas ni pasos manuales.
- `src/ej1_tabla.py`: la Tabla 1 aprobada en la tarea 03, más 18 comprobaciones de las cifras de los ejemplos contra los datos.
- `output/actividad_probabilidad_y_estadistica_unidad_2.xlsx`: **el libro final** (nombre por defecto, por confirmar).
- Los `output/*_borrador.xlsx` son intermedios de las tareas 04 a 11 y ya no se usan. Se pueden borrar al cerrar la tarea 15 (no los toqué).

**Hojas, en el orden de la sección 7 del prompt**
Portada | Presentación | Introducción | Objetivos | Ejercicio 1 | Ejercicio 2 | Ejercicio 3 | Conclusiones | Bibliografía | Anexos | DATOS

- **Portada:** datos del prompt; tutor y fecha en celdas amarillas con `PENDIENTE`.
- **Ejercicio 1:** Tabla 1 (Conceptos, Definiciones, Ejemplos) y un recuadro grande rotulado `Evidencia del quiz: insertar captura aquí`.
- **Ejercicio 2:** variable elegida, tabla de frecuencia, histograma, circular y polígono con sus conclusiones, respuestas a las dos preguntas, tabla de medidas con interpretación, análisis de dispersión, homogeneidad, concentración y asimetría.
- **Ejercicio 3:** variables, ecuación, diagrama de dispersión con recta, R², confiabilidad, r, nivel y tres predicciones.
- **Bibliografía:** solo las dos lecturas del enunciado, con cursiva APA. La lista opcional (Anexo 1, NumPy, SciPy, pandas, XlsxWriter) **no entró**, porque no la autorizaste.
- **Anexos:** A hoja de datos y las 13 parejas repetidas, B tabla de verificación (141 filas), C variables del foro, D convenciones adoptadas.
- **DATOS:** copia exacta del Anexo 1, en la última hoja, con la primera fila fija. Se llama `DATOS` como en el original porque todas las fórmulas apuntan a ella.

**Verificación sobre el archivo final**
- 141 comparaciones contra numpy y scipy: **141 coinciden recalculando con LibreOffice y 141 coinciden en los valores guardados**. Diferencia máxima 5,7e-13.
- 169 celdas con fórmula, **0 errores de Excel** (`#NAME?`, `#VALUE!`, etc.) tras recalcular.
- 4 gráficos nativos (1 de columnas, 1 circular y 2 de dispersión: el polígono y el diagrama con recta) y **ninguna imagen** en el libro.
- Cero guiones largos en celdas, hojas y gráficos (búsqueda en todo el XML del archivo).
- Hoja `DATOS` idéntica al Anexo 1 (400 registros).
- Prefijo `_xlfn.` presente en las funciones nuevas (`MODE.SNGL`, `STDEV.S`, etc.).
- Reproducible: dos ejecuciones seguidas dan el mismo contenido celda por celda.
- Revisión visual: rendericé con LibreOffice las hojas Portada, Introducción, Ejercicio 1, Ejercicio 2, Bibliografía y Anexos. No revisé una a una las hojas Presentación, Objetivos, Conclusiones ni el ejercicio 3 completo en el libro final (sí en los borradores por bloque).

**Pendientes que impiden la entrega (dependen de Jairo)**
1. Tutor y fecha de la portada (celdas amarillas).
2. Confirmar el nombre del archivo.
3. Plantilla del foro: si existe, hay que revisar la estructura.
4. Bibliografía: confirmar que consultaste las dos lecturas y decidir si entra la lista opcional (las referencias de NumPy, SciPy y pandas se escribieron de memoria y deben verificarse).
5. Anexo C: confirmar la combinación publicada en el foro (celda amarilla).
6. Pegar la captura del quiz en su recuadro.
7. Carpeta de entrega de la tarea 15.

**Limitaciones que conviene conocer**
- El recálculo se hizo en LibreOffice, no en Microsoft Excel. No puedo probar el archivo en Excel desde aquí. Si algo se ve o se calcula distinto al abrirlo allí, avísame.
- Los gráficos con etiquetas de porcentaje y la ecuación de la línea de tendencia se dibujan distinto según el visor; en LibreOffice el porcentaje sale con punto decimal y la ecuación con más decimales.
- La ortografía y las tildes no se revisaron con una herramienta, solo al leer los textos. La tarea 15 incluye una revisión con lista de comprobación.
