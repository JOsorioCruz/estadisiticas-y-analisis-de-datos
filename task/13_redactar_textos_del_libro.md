# Tarea 13: Redactar textos del libro
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Escribir Presentación, Introducción, Objetivos, Conclusiones, Bibliografía APA 7 y Anexos.

## Entradas (archivos o decisiones que necesita)
- Resultados de las tareas 03 a 12.
- Datos de portada: tutor y fecha, que faltan.

## Pasos
1. Redactar cada texto en un archivo aparte para revisión de Jairo antes de escribirlo al libro.
2. Objetivo general: el resultado de aprendizaje del enunciado. Un objetivo específico por ejercicio.
3. Conclusiones apoyadas en números obtenidos.
4. Bibliografía solo con las dos lecturas y, con autorización, el Anexo 1 y la documentación de las librerías usadas.

## Entregable (archivo o celdas concretas que produce)
Textos aprobados.

## Criterio de aceptación (cómo compruebo que está bien)
Sin guiones largos, con tildes correctas y cada afirmación rastreable a un número del libro.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/textos_libro.py`: fuente única de los textos. Calcula las cifras desde los datos con los mismos módulos que arman las hojas y lleva `assert` que detienen el script si un dato cambia y el texto dejaría de ser cierto. La tarea 14 lo importará para escribir el libro. Se ejecuta con `.venv/bin/python src/textos_libro.py`.
- `output/textos/01_portada.md` a `07_anexos.md`: los textos para tu revisión, uno por archivo. Nada de esto está escrito todavía en el libro.

**Contenido (léelo en `output/textos/`)**
- **Portada:** universidad, CTEV, programa, asignatura, código AF17401, título, autor Jairo Alonso Osorio Cruz, semestre VI. **Tutor y fecha quedan como PENDIENTE**, porque no los tengo y no los invento.
- **Presentación** (2 párrafos) e **Introducción** (4 párrafos: problemática, base y su hallazgo de 13 parejas repetidas, estadística descriptiva, organización del libro).
- **Objetivos:** el general es el resultado de aprendizaje del enunciado, y hay un específico por ejercicio.
- **Conclusiones:** una por ejercicio y una general, apoyadas en cifras del libro (por ejemplo: media 89,86 km/h; intervalo modal [109 - 120) con 62 accidentes; CV 33,82 %; y = 1,7278 + 0,7723 x; r = 0,7724; R² = 59,66 %; predicciones y error típico de 2,52).
- **Bibliografía:** dividida en obligatoria (las dos lecturas del enunciado) y opcional (Anexo 1, NumPy, SciPy, pandas y XlsxWriter).
- **Anexos:** A hoja de datos y las 13 parejas repetidas (filas exactas), B verificación (141 valores), C variables elegidas en el foro, D convenciones adoptadas.

**Cifras comprobadas:** 45 % de los accidentes a 98 km/h o más (180 de 400), 13 parejas repetidas separadas exactamente por 100 filas, municipios 185, 119 y 96. El resto sale de los módulos ya verificados en la tarea 12.

**Cosas que necesito de Jairo (bloquean la tarea 14 o las decisiones del texto)**
1. Nombre del tutor y fecha de la portada.
2. Nombre del archivo final (por defecto `actividad_probabilidad_y_estadistica_unidad_2.xlsx`).
3. Plantilla del foro: ¿existe? Si sí, la estructura puede cambiar.
4. Bibliografía: confirmar que consultaste las dos lecturas (no puedo afirmarlo yo) y decidir qué entra de la lista opcional. Las referencias de NumPy, SciPy y pandas las escribí de memoria: **verifica los datos** (autores, año, DOI, páginas) antes de entregar. La de XlsxWriter va sin año porque no lo sé con seguridad.
5. Anexo C: confirmar que publicaste esa combinación en el foro.
6. Decidir si el Anexo B debe decir que el libro se generó con un programa de Python. Es un dato verdadero y lo dejé, pero es decisión tuya si lo declaras.
7. Carpeta de entrega de la tarea 15.

**Observaciones**
- Los textos están en un registro neutro de estudiante, en plural o impersonal, sin guiones largos ni frase de remate. Reescribe con tu voz lo que quieras; la rúbrica del ejercicio 1 lo pide, y en los demás ejercicios ayuda.
- La conclusión del ejercicio 1 dice que el quiz se adjunta como evidencia. No incluye ninguna nota, porque no la conozco.
- Las conclusiones dicen que las convenciones (homogeneidad, asimetría, correlación) son de uso común y no de las lecturas. Si encuentras los criterios en las lecturas, se cambian en los módulos y en Anexo D.
