# Tarea 06: Ejercicio 2: intervalo de mayor frecuencia y 60% acumulado
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Responder las dos preguntas del enunciado con base en la tabla.

## Entradas (archivos o decisiones que necesita)
- Tabla de la tarea 04.

## Pasos
1. Identificar el intervalo con mayor fi.
2. Identificar el primer intervalo cuyo Hi alcanza o supera el 60%.
3. Justificar ambas respuestas citando las celdas de la tabla.

## Entregable (archivo o celdas concretas que produce)
Respuestas justificadas.

## Criterio de aceptación (cómo compruebo que está bien)
Ambas respuestas coinciden con un cálculo independiente en Python.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej2_preguntas.py`: bloque "Preguntas con base en la tabla de frecuencia", con fórmulas de Excel, texto de respuesta y verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej2_preguntas.py`. Reutiliza los módulos de las tareas 04 y 05 (a `ej2_graficos.py` solo le añadí que devuelva la fila libre donde termina el último gráfico).
- `output/ej2_preguntas_borrador.xlsx`: tabla, gráficos y este bloque en la hoja `Ej2 Tabla`, más la hoja `DATOS`. Borrador de trabajo.

**Respuestas**

1. **¿En cuál intervalo se observa la mayor cantidad de datos?** En **[109 - 120) km/h**, con **62 accidentes** de los 400 (15,5 %). Es el intervalo modal de la tabla.
   - Fórmula: `=INDEX(A13:A22, MATCH(MAX(E13:E22), E13:E22, 0))`.

2. **¿Hasta cuál intervalo se acumula el 60 %?** En **[98 - 109) km/h**. Hasta [87 - 98) el acumulado es 55,0 % (220 accidentes), aún por debajo del 60 %. Con los 48 accidentes de [98 - 109) pasa a 67,0 % (268 accidentes). Es decir, el 67 % de los accidentes ocurrió a menos de 109 km/h.
   - Fórmula: `=INDEX(A13:A22, COUNTIF(H13:H22,"<"&0,6)+1)`, es decir, cuenta cuántos intervalos tienen acumulado menor que 60 % y toma el siguiente. El 60 % está en una celda amarilla editable.
   - Complemento: si los datos se reparten parejo dentro del intervalo, el 60 % se alcanza cerca de **102,6 km/h** (interpolación lineal dentro de [98 - 109)).

**Verificación**
- Con los datos crudos y `np.histogram` (sin pasar por la tabla): fi máxima = 62 en [109 - 120); acumulado antes = 0,5500 y después = 0,6700. Coincide con las respuestas.
- LibreOffice recalculó una copia **sin valores guardados**: las siete celdas de respuesta coinciden con Python (diferencia menor que 1e-9).
- Revisión visual del bloque renderizado.
- Sin guiones largos.

**Nota para Jairo**
- El 102,6 km/h es solo una estimación por interpolación sobre datos agrupados. El percentil 60 exacto con los 400 datos crudos es 100,88 km/h. Los dos caen dentro de [98 - 109), que es lo que pregunta el enunciado. Si quieres, puedo dejar solo el intervalo y quitar la estimación. La dejé porque el texto ya dice que supone un reparto parejo.
- La respuesta al enunciado depende de la tabla de la tarea 04 (amplitud 11 desde 32). Si se cambiara la amplitud o el inicio, hay que volver a ejecutar los scripts: las etiquetas de los intervalos y los textos de respuesta se generan desde Python, no desde Excel.
