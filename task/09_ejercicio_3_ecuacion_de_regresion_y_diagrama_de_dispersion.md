# Tarea 09: Ejercicio 3: ecuación de regresión y diagrama de dispersión
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Obtener la ecuación de regresión y graficar la dispersión con la recta.

## Entradas (archivos o decisiones que necesita)
- Par de variables fijado en la tarea 02.

## Pasos
1. Calcular pendiente e intercepto con `SLOPE` e `INTERCEPT`.
2. Crear el diagrama de dispersión nativo con línea de tendencia lineal.
3. Indicar si la relación es positiva, negativa o inexistente, según el signo de la pendiente y la nube de puntos.

## Entregable (archivo o celdas concretas que produce)
Gráfico nativo y ecuación.

## Criterio de aceptación (cómo compruebo que está bien)
La pendiente y el intercepto coinciden con scipy; el gráfico tiene título, ejes rotulados y unidades.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej3_regresion.py`: hoja `Ej3 Regresión` con datos de partida, pendiente, intercepto, ecuación, tipo de relación, gráfico y lectura, más verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej3_regresion.py`.
- `output/ej3_regresion_borrador.xlsx`: hojas `Ej3 Regresión` y `DATOS`. Borrador de trabajo.

**Variables (tarea 02):** x = años de experiencia del conductor (columna H), y = histórico de infracciones en los últimos cinco años (columna I), n = 400.

**Resultados**

| Medida | Resultado | Fórmula de Excel |
|---|---|---|
| Pendiente (b) | 0,7723 | `SLOPE(y, x)` |
| Intercepto (a) | 1,7278 | `INTERCEPT(y, x)` |
| Ecuación | **y = 1,7278 + 0,7723 x** | `="y = "&ROUND(a,4)&...` |
| Tipo de relación | Positiva | `IF` sobre el signo de b |
| Promedio observado con x = 0 | 1,06 | `AVERAGEIF(x, 0, y)` |

- **Pendiente:** Por cada año más de experiencia, el modelo asocia unas 0,77 infracciones adicionales en los últimos cinco años. Esto describe una asociación y no demuestra que la experiencia cause las infracciones.
- **Intercepto:** Es el valor que da la recta para un conductor con 0 años de experiencia: 1,73 infracciones. Ojo: los 53 conductores con 0 años tuvieron en promedio 1,06, así que la recta se aleja algo de los datos en ese extremo.
- **Tipo de relación:** Positiva. La pendiente es mayor que cero y la nube de puntos sube de izquierda a derecha: a más años de experiencia, tienden a ser más las infracciones acumuladas. La fuerza de esa relación se mide con el coeficiente de determinación y con r.

**Gráfico:** diagrama de dispersión nativo de Excel (`scatterChart`) con los 400 pares y línea de tendencia lineal nativa con la ecuación visible. Título, ejes rotulados y unidades. La recta la dibuja Excel con `trendline`, no es una imagen. Como las dos variables son números enteros, muchos conductores comparten la misma pareja de valores y sus puntos quedan uno encima de otro. Por eso se ven menos puntos que los 400 registros.

**Hallazgo importante: la relación tiene forma de escalón**
Los datos no forman una nube pareja, sino tres tramos. Con 0 o 1 año de experiencia (118 conductores) las infracciones van de 0 a 2. Con 2 a 10 años (256) van de 2 a 8 y su promedio casi no cambia de un año a otro (entre 4,33 y 6,00). Con 11 años o más (26) van de 10 a 20. La recta resume ese escalón con una sola pendiente, así que sirve como aproximación general pero no describe bien cada tramo por separado.

Esto no invalida la recta, pero condiciona la lectura y la tarea 11 (predicciones). Datos por tramo: x = 0 o 1 (118 casos): y entre 0 y 2. x = 2 a 10 (256): y entre 2 y 8, con promedios por año entre 4,33 y 6,00. x = 11 o más (26): y entre 10 y 20. La recta sube de 1,73 a 9,5 en los primeros 10 años, mientras el promedio real dentro de ese tramo casi no se mueve. Por eso el R² que se calcule en la tarea 10 (referencia de scipy: 0,60) hay que leerlo como el ajuste global de esa recta y no como prueba de una subida continua año a año.

**Verificación**
- LibreOffice recalculó una copia sin valores guardados: pendiente, intercepto, ecuación, tipo de relación y promedio con x = 0 coinciden con scipy (`linregress`). Diferencias menores que 1e-9.
- Segunda implementación independiente con `numpy.polyfit`: b = 0,7723038154 y a = 1,7277755049, iguales a scipy.
- XML del gráfico: `scatterChart`, `trendlineType linear`, ecuación visible, referencias a `DATOS!$H$2:$H$401` y `DATOS!$I$2:$I$401`. Sin imágenes (`xl/media` no existe).
- El texto del patrón lleva `assert` que comprueban que los tres tramos siguen siendo cierta descripción de los datos.
- Revisión visual de la hoja renderizada. La ecuación de la etiqueta del gráfico la escribe el visor (LibreOffice la muestra con más decimales que Excel).
- Sin guiones largos.

**Observaciones para Jairo**
1. La ecuación en la celda usa `ROUND` y concatenación, no `TEXT`, para que salga bien con la coma decimal de un Excel en español.
2. Los marcadores tienen transparencia en el archivo. LibreOffice no la dibuja y no la uso en el texto; en Excel debería verse.
3. El escalón afecta a las tareas siguientes: la tarea 10 dará R² y r, pero la interpretación debe mencionar que se concentran en tres bloques. En la tarea 11 elegiré predicciones dentro de cada tramo y avisaré dónde la recta se aleja del promedio real. Dime si prefieres otras reglas.
