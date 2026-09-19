# Tarea 10: Ejercicio 3: R², confiabilidad, Pearson y nivel de correlación
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Calcular R² y r, expresar el porcentaje de confiabilidad e indicar el nivel de correlación lineal.

## Entradas (archivos o decisiones que necesita)
- Ecuación de la tarea 09.
- Criterio de clasificación de la correlación (perfecta, excelente, aceptable, regular, mínima, sin correlación).

## Pasos
1. Calcular con `RSQ` y `CORREL`.
2. Pedir a Jairo el criterio de clasificación de las lecturas. Si no lo tiene, elegir una convención juntos y citarla como tal.
3. Interpretar r y R² en el contexto de accidentes.

## Entregable (archivo o celdas concretas que produce)
Medidas e interpretación.

## Criterio de aceptación (cómo compruebo que está bien)
R² = r² dentro de la tolerancia, y el nivel asignado cita el criterio usado.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej3_correlacion.py`: bloque "Coeficiente de determinación, confiabilidad y correlación de Pearson" en la hoja `Ej3 Regresión`, con fórmulas, interpretación, escala y verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej3_correlacion.py`.
- `src/ej3_regresion.py`: solo devuelve ahora la fila libre y el resumen por tramos.
- `output/ej3_correlacion_borrador.xlsx`: hoja `Ej3 Regresión` (tarea 09 más este bloque) y `DATOS`. Borrador de trabajo.

**Criterio:** Jairo no respondió a la escala propuesta, así que se usó la propuesta. Queda declarada en el libro como convención adoptada, no de las lecturas.

| |r| | Nivel |
|---|---|
| 1 | Perfecta |
| 0,90 a menos de 1 | Excelente |
| 0,80 a menos de 0,90 | Aceptable |
| 0,50 a menos de 0,80 | Regular |
| mayor que 0 y menor que 0,50 | Mínima |
| 0 | Sin correlación |

**Resultados**

| Medida | Resultado | Fórmula de Excel |
|---|---|---|
| Coeficiente de determinación (R²) | 0,5966 | `RSQ(y, x)` |
| Confiabilidad del modelo | **59,66 %** | R² x 100 |
| Coeficiente de correlación de Pearson (r) | **0,7724** | `CORREL(y, x)` |
| Nivel de correlación lineal | **Regular** | `IF` anidado sobre |r| |

- **R²:** La recta explica el 59,66 % de la variación del número de infracciones a partir de los años de experiencia. El 40,34 % restante depende de otros factores o de variación que la recta no recoge.
- **Confiabilidad:** Es el mismo R² expresado en porcentaje: 59,66 %. El modelo da una idea general de cuántas infracciones se esperan según la experiencia, pero deja sin explicar cerca del 40 % de la variación, así que sus predicciones son orientativas y no exactas.
- **r:** Es 0,7724, un valor positivo: al aumentar los años de experiencia tienden a aumentar las infracciones. Elevado al cuadrado da 0,5966, que es el R².
- **Nivel:** Regular según la escala adoptada (|r| entre 0,50 y 0,80). Como r = 0,77 está cerca del límite de 0,80 que separaría 'aceptable', conviene citar el valor de r junto con la etiqueta.
- **Lectura:** Estos valores resumen el ajuste global de la recta. El diagrama mostró tres tramos y, entre 2 y 10 años de experiencia, el promedio de infracciones casi no cambia (entre 4,33 y 6,00), así que un R² de 59,66 % no significa que las infracciones suban de forma continua con cada año. Además, una correlación, por alta que sea, no prueba que la experiencia cause las infracciones.

**Verificación**
- numpy `corrcoef`, scipy `pearsonr` y `linregress` dan r = 0,7724166864, iguales entre sí; r² = 0,5966275374 = R².
- LibreOffice recalculó una copia sin valores guardados: R², confiabilidad, r y nivel coinciden con Python (diferencia menor que 1e-9).
- La función de nivel se comprobó con valores límite (1, -0,95, 0,80, -0,50, 0,49 y 0).
- Revisión visual del bloque renderizado.
- Sin guiones largos.

**Observaciones para Jairo**
- r = 0,7724 queda "regular" pero cerca del borde de "aceptable" (0,80). Con un corte en 0,75 la etiqueta sería otra. Si las lecturas traen una escala, se cambia la lista `ESCALA` y la fórmula `IF` y se regenera.
- Se dejó la advertencia sobre los tres tramos y sobre correlación y causalidad, porque el diagrama de la tarea 09 lo justifica.
