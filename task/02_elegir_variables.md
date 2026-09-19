# Tarea 02: Elegir variables (decisión de Jairo)
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Fijar la variable del ejercicio 2 y el par de variables del ejercicio 3.

## Entradas (archivos o decisiones que necesita)
- Informe de la tarea 01.
- Lo que hayan elegido tus compañeros de grupo en el foro.

## Pasos
1. Proponer candidatas con su justificación estadística (ver abajo).
2. Jairo elige y confirma que no chocan con el grupo.
3. Registrar la elección en `plan.md`.

## Entregable (archivo o celdas concretas que produce)
Variables fijadas en `plan.md`.

## Criterio de aceptación (cómo compruebo que está bien)
Una sola variable cuantitativa para el ejercicio 2 y dos cuantitativas para el ejercicio 3, confirmadas por Jairo.

Nota de apoyo: fallecidos (5 valores distintos) y heridos (6) rinden poco en una tabla agrupada. Edad, velocidad, costo, experiencia e infracciones son mejores candidatas. Para el ejercicio 3 conviene calcular antes las correlaciones entre pares para ver cuáles tienen una relación que valga la pena analizar.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
Propuesta enviada a Jairo, a la espera de su elección (n = 400, con `src/carga.py`). Con Sturges, k = 10 intervalos para cualquier variable.

**Candidatas para el ejercicio 2**

| Variable | Valores distintos | Media | CV | Asimetría | Curtosis (exceso) | Comentario |
|---|---|---|---|---|---|---|
| Edad | 39 | 30.89 | 27.9% | 0.98 | 0.88 | Cola derecha moderada, agrupa bien. |
| Velocidad | 261 | 89.86 | 33.8% | -0.26 | -1.01 | Casi simétrica, agrupa muy bien. |
| Costo | 285 | 188.21 | 62.1% | 0.17 | -1.28 | Casi uniforme, agrupa bien. |
| Años de experiencia | 19 | 3.60 | 110.2% | 2.45 | 8.10 | Muy asimétrica y heterogénea, con muchos valores bajos. |
| Histórico de infracciones | 20 | 4.51 | 88.0% | 1.52 | 2.98 | Asimétrica a la derecha. |
| Fallecidos | 5 | 2.10 | 65.6% | -0.05 | -1.23 | Descartable: 5 valores no dan tabla agrupada útil. |
| Heridos | 6 | 3.47 | 39.1% | 0.04 | -0.62 | Descartable: 6 valores no dan tabla agrupada útil. |

**Correlaciones de Pearson entre pares (ejercicio 3), ordenadas por |r|**

| Par (x, y) | r | R² |
|---|---|---|
| Experiencia, Infracciones | 0.772 | 0.597 |
| Edad, Experiencia | 0.434 | 0.188 |
| Edad, Infracciones | 0.340 | 0.116 |
| Edad, Heridos | -0.207 | 0.043 |
| Heridos, Infracciones | -0.141 | 0.020 |
| Velocidad, Infracciones | -0.135 | 0.018 |
| Costo, Experiencia | 0.134 | 0.018 |
| Edad, Fallecidos | 0.134 | 0.018 |
| Edad, Costo | 0.121 | 0.015 |
| Velocidad, Costo | 0.040 | 0.002 |

Los 21 pares posibles están calculados. Los pares restantes tienen |r| menor que 0.13 y R² menor que 0.02.
Notas: El único par con relación lineal marcada es Experiencia con Infracciones. El resto son débiles o inexistentes, lo cual también es un resultado válido para el enunciado (incluye el nivel "sin correlación"), pero da predicciones poco confiables.

**Elección de Jairo**
- Ejercicio 2: **Velocidad registrada (km/h)**, columna E de `DATOS`. Cuantitativa continua, 261 valores distintos, mín 32.1, máx 140.8, media 89.86, CV 33.8%, asimetría -0.26.
- Ejercicio 3: **Años de experiencia del conductor** (variable independiente x, columna H) e **Histórico de infracciones** (variable dependiente y, columna I). r = 0.772 y R² = 0.597 calculados con scipy sobre los 400 registros, solo como referencia: los valores oficiales se calculan con fórmulas de Excel en las tareas 09 y 10.
- Supuesto mío, aceptado al aprobar la tarea (sin objeción de Jairo): experiencia va como x porque es razonable pensar que la experiencia influye en las infracciones acumuladas, y no al revés. Para el coeficiente de correlación da igual, pero cambia la ecuación de regresión y las predicciones.
- Pendiente de tu lado: que la combinación no choque con las de tu grupo en el foro (lo confirmaste al elegir, pero avísame si al publicar hay conflicto).
