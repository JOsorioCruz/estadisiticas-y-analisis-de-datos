# Tarea 07: Ejercicio 2: tendencia central, posición y tabla interpretada
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Calcular media, mediana, moda, mín, máx, rango, Q1, D5 y P80 con fórmulas de Excel e interpretarlos.

## Entradas (archivos o decisiones que necesita)
- Variable fijada en la tarea 02.

## Pasos
1. Usar `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `MIN`, `MAX`, `QUARTILE.INC`, `PERCENTILE.INC` (D5 como percentil 50, P80).
2. Verificar cada valor contra numpy.
3. Armar la tabla `Medida | Resultado | Interpretación` como el ejemplo del enunciado, con una frase por medida en el contexto de accidentes.
4. Preguntar a Jairo si además quiere Q3 y P10, que aparecen en el ejemplo del enunciado.

## Entregable (archivo o celdas concretas que produce)
Tabla de medidas interpretada.

## Criterio de aceptación (cómo compruebo que está bien)
Cada valor coincide con numpy y cada interpretación se rastrea a un número de la tabla.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej2_medidas.py`: bloque "Medidas de tendencia central y de posición", con fórmulas, interpretaciones y verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej2_medidas.py`.
- `output/ej2_medidas_borrador.xlsx`: hoja `Ej2 Tabla` con tabla, gráficos, preguntas y este bloque, más `DATOS`. Borrador de trabajo.
- `src/ej2_preguntas.py`: solo registra la fila libre donde termina su bloque.

**Decisión de Jairo:** incluir Q3 y P10 además de lo que exige el enunciado (Q1, D5, P80), igual que el ejemplo del docente.

**Tabla `Medida | Resultado | Interpretación`** (velocidad registrada, n = 400)

| Medida | Resultado | Fórmula de Excel | Interpretación |
|---|---|---|---|
| Moda | 81,60 | `MODE.SNGL` | La velocidad que más se repite en los accidentes es 81,6 km/h, con 5 registros. Al ser una variable continua este valor pesa poco: el intervalo más frecuente de la tabla es [109 - 120) km/h. |
| Media | 89,86 | `AVERAGE` | En promedio, el vehículo causante del accidente iba a 89,86 km/h. |
| Mediana | 94,05 | `MEDIAN` | La mitad de los accidentes ocurrió a 94,05 km/h o menos y la otra mitad a más de 94,05 km/h. Queda por encima de la media (89,86), lo que apunta a una ligera cola hacia las velocidades bajas. |
| Mínimo | 32,10 | `MIN` | La velocidad más baja registrada en un accidente fue de 32,1 km/h. |
| Máximo | 140,80 | `MAX` | La velocidad más alta registrada en un accidente fue de 140,8 km/h. |
| Rango | 108,70 | Máximo - Mínimo | Entre el accidente de menor velocidad y el de mayor velocidad hay 108,7 km/h de diferencia. |
| Cuartil 1 (Q1) | 66,25 | `QUARTILE.INC(rango, 1)` | El 25 % de los accidentes ocurrió a velocidades entre 32,1 y 66,25 km/h. |
| Decil 5 (D5) | 94,05 | `PERCENTILE.INC(rango, 0.5)` | El decil 5 deja el 50 % de los accidentes a 94,05 km/h o menos, por eso coincide con la mediana. |
| Cuartil 3 (Q3) | 114,85 | `QUARTILE.INC(rango, 3)` | El 75 % de los accidentes ocurrió a velocidades entre 32,1 y 114,85 km/h, y solo el 25 % superó los 114,85 km/h. |
| Percentil 10 (P10) | 44,03 | `PERCENTILE.INC(rango, 0.1)` | El 10 % de los accidentes ocurrió a velocidades entre 32,1 y 44,03 km/h. |
| Percentil 80 (P80) | 117,98 | `PERCENTILE.INC(rango, 0.8)` | El 80 % de los accidentes ocurrió a 117,98 km/h o menos, y el 20 % restante superó esa velocidad. |

Detalles de método:
- Excel no tiene función de decil, así que D5 se calcula como el percentil 50.
- La moda es única (81,6 aparece 5 veces; el siguiente valor más repetido aparece 4). No hay empate que resolver.
- Cuartiles y percentiles usan el método inclusivo (`.INC`), el mismo que `np.percentile` con interpolación lineal.
- Las medidas apuntan a la hoja de datos (`DATOS!$E$2:$E$401`).

**Verificación**
- LibreOffice recalculó una copia **sin valores guardados** y se comparó cada medida con numpy y con pandas (`quantile`, `mean`, `median`, y un cálculo propio de la moda). Diferencia máxima entre las tres fuentes: 1,4e-14.
- Se comprobó con conteos directos que Q1, P10, P80 dejan exactamente 100, 40 y 320 datos a su izquierda o igual (25 %, 10 % y 80 % de 400), lo que respalda las frases de interpretación.
- Revisión visual de la tabla renderizada.
- Sin guiones largos.

**Hallazgo técnico importante (afecta a las tareas 08 a 14)**
- La primera verificación devolvió `#NAME?` en la moda, los cuartiles y los percentiles. Causa: `MODE.SNGL`, `QUARTILE.INC` y `PERCENTILE.INC` son funciones "nuevas" que en el archivo requieren el prefijo `_xlfn.`; sin él, **Excel también mostraría `#NAME?`** al recalcular. La solución fue abrir el libro con `xlsxwriter.Workbook(..., {"use_future_functions": True})`, que añade el prefijo solo. Se confirmó en el XML: 1 `_xlfn.MODE.SNGL`, 3 `_xlfn.PERCENTILE.INC` y 2 `_xlfn.QUARTILE.INC`.
- Esa opción hay que mantenerla en el libro final (tarea 14). También aplica a `VAR.S`, `STDEV.S`, `VAR.P` y otras de la tarea 08.

**Observación para Jairo:** la interpretación de la mediana dice "ligera cola hacia las velocidades bajas" porque la mediana (94,05) supera a la media (89,86). Es una pista, no una conclusión: la asimetría se calcula en la tarea 08.
