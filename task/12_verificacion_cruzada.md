# Tarea 12: Verificación cruzada
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Comparar cada valor del libro contra numpy y scipy, y contra LibreOffice.

## Entradas (archivos o decisiones que necesita)
- Medidas de las tareas 04 a 11.

## Pasos
1. Recalcular el archivo con LibreOffice en modo headless.
2. Leer los valores recalculados y compararlos con numpy y scipy.
3. Registrar diferencias en una tabla.

## Entregable (archivo o celdas concretas que produce)
Tabla de verificación con diferencias, para Anexos.

## Criterio de aceptación (cómo compruebo que está bien)
Todas las diferencias están por debajo de la tolerancia declarada, o cada excepción queda explicada.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/verificacion.py`: reconstruye los borradores de los ejercicios 2 y 3, recalcula con LibreOffice y compara cada valor. Se ejecuta desde la raíz con `.venv/bin/python src/verificacion.py`.
- `output/verificacion.json`: la tabla completa (141 filas: ejercicio, bloque, medida, valor de Excel recalculado, valor de Python, diferencia y resultado). La tarea 14 la usará para la hoja de Anexos.
- Cambios menores en `src/ej2_dispersion.py` y `src/ej3_predicciones.py`: ahora devuelven también las celdas de los demás bloques.

**Método**
1. Cada libro se genera dos veces: una **sin valores guardados** en las fórmulas, que LibreOffice recalcula desde cero, y otra **con los valores guardados**, que es lo que verá quien abra el archivo sin recalcular.
2. Los valores esperados se calculan en `verificacion.py` desde los datos crudos con numpy y scipy (`histogram`, `percentile`, `skew`, `kurtosis`, `polyfit`, `pearsonr`), sin reutilizar las funciones de cada módulo. La moda se calcula como Excel: el primer valor más frecuente en orden de datos.
3. Se comparan también los valores guardados contra los esperados.
4. Se compara la hoja `DATOS` de ambos libros con el Anexo 1, celda por celda.
5. Tolerancia: 1e-9 en valor absoluto; los textos (intervalos, ecuación, niveles) deben ser idénticos.

**Resultado**
- **141 comparaciones: 141 coinciden** con numpy/scipy tras recalcular en LibreOffice, y **141 valores guardados** coinciden también.
- Diferencia máxima absoluta: **5,7e-13** (tolerancia 1e-9).
- Hoja `DATOS` idéntica al Anexo 1 en ambos libros (400 registros).

| Ejercicio | Bloque | Valores | Diferencia máxima |
|---|---|---|---|
| 2 | Tabla de frecuencia (9 columnas x 10 intervalos) | 90 | 7,1e-15 |
| 2 | Parámetros de la tabla (n, mín, máx, R, k, R/k) | 6 | 1,4e-14 |
| 2 | Preguntas (mayor frecuencia y 60 %) | 7 | 3,3e-13 |
| 2 | Tendencia central y posición | 11 | 1,4e-14 |
| 2 | Dispersión, asimetría y curtosis | 5 | 5,7e-13 |
| 3 | Regresión lineal | 5 | 4,4e-15 |
| 3 | R², r y nivel | 4 | 1,4e-14 |
| 3 | Predicciones | 13 | 4,6e-14 |

**Prueba de que la verificación puede fallar:** se introdujeron a propósito un error de 0,001 en la media esperada y de 0,1 en la moda. Ambos se marcaron como fallo (diferencias 1,0e-3 y 1,0e-1) y el valor correcto pasó.

**Lo que esta verificación cubre y lo que no**
- Cubre: valores numéricos y etiquetas de texto que salen de fórmulas de Excel.
- No cubre: las frases de interpretación (se generan con f-strings desde los mismos números, y varias tienen `assert`), los gráficos (revisados por separado en las tareas 05 y 09) ni el comportamiento en Microsoft Excel. El recálculo se hizo en LibreOffice, no en Excel. Las fórmulas usan funciones estándar y el prefijo `_xlfn.` donde hace falta, pero no puedo probarlas en Excel desde aquí.
- La verificación de la tarea 14 (libro final) deberá repetirse contra el archivo ensamblado, porque hoy verifica los borradores por bloque.

**Observaciones para Jairo**
- Si el docente o tú abren el archivo en Excel y algún valor no coincide con el de estas tablas, avísame: sería un problema de compatibilidad de Excel y no del cálculo.
