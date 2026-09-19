# Tarea 11: Ejercicio 3: tres predicciones
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Hacer tres predicciones con la ecuación de regresión.

## Entradas (archivos o decisiones que necesita)
- Ecuación de la tarea 09 y rango observado de la variable independiente.

## Pasos
1. Elegir tres valores dentro del rango observado (Jairo puede sugerir otros).
2. Calcular cada predicción con una fórmula de Excel basada en la pendiente y el intercepto.
3. Interpretar cada una y advertir cuánto confiar en ella según R².

## Entregable (archivo o celdas concretas que produce)
Tabla de predicciones.

## Criterio de aceptación (cómo compruebo que está bien)
Los tres valores están dentro del rango observado y las predicciones coinciden con el cálculo en Python.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej3_predicciones.py`: bloque "Predicciones con la ecuación de regresión" en la hoja `Ej3 Regresión`, con verificación. Se ejecuta desde la raíz con `.venv/bin/python src/ej3_predicciones.py`.
- `output/ej3_predicciones_borrador.xlsx`: hoja `Ej3 Regresión` completa (tareas 09, 10 y 11) y `DATOS`. Borrador de trabajo.

**Elección de valores.** Jairo no indicó otros, así que se usó la regla del plan: valores dentro del rango observado (0 a 30 años) y uno por cada tramo del patrón de la tarea 09. Las celdas de x son amarillas y se pueden cambiar; la predicción se recalcula con `=a + b * x` apuntando a las celdas de pendiente e intercepto.

**Resultados** (ecuación y = 1,7278 + 0,7723 x)

| Predicción | x (años) | ŷ (infracciones) | Promedio observado con ese x | Conductores con ese x | Dentro del rango |
|---|---|---|---|---|---|
| 1 | 1 | 2,50 | 0,51 | 65 | Sí |
| 2 | 5 | 5,59 | 5,38 | 16 | Sí |
| 3 | 12 | 11,00 | 15,50 | 8 | Sí |

Error típico de la estimación (`STEYX`): **2,52 infracciones**.

**Interpretaciones (texto del libro)**
1. Para un conductor con 1 año de experiencia, el modelo estima 2,50 infracciones en los últimos cinco años. Los 65 conductores con 1 año tuvieron en promedio 0,51; la estimación queda por encima de lo observado y la recta sobreestima en este tramo.
2. Para un conductor con 5 años de experiencia, el modelo estima 5,59 infracciones en los últimos cinco años. Los 16 conductores con 5 años tuvieron en promedio 5,38; la estimación coincide bien con lo observado.
3. Para un conductor con 12 años de experiencia, el modelo estima 11,00 infracciones en los últimos cinco años. Los 8 conductores con 12 años tuvieron en promedio 15,50; la estimación queda por debajo de lo observado y la recta subestima en este tramo.
- **Uso:** Las tres predicciones usan valores dentro del rango observado (0 a 30 años), que es donde la ecuación puede usarse. El error típico de la estimación es de 2,52 infracciones, así que cada predicción debe leerse con un margen de ese orden. Por el patrón de tres tramos visto en el diagrama, la recta funciona mejor en el tramo intermedio (2 a 10 años) que en los extremos.

**Verificación**
- LibreOffice recalculó una copia sin valores guardados: predicciones, promedios observados (`AVERAGEIF`), conteos (`COUNTIF`), "dentro del rango" y `STEYX` coinciden con numpy. Diferencia máxima 4,6e-14.
- La predicción se comparó además con `numpy.polyfit` (segunda implementación, distinta de scipy).
- El texto lleva `assert` que comprueban que la primera sobreestima, la segunda coincide y la tercera subestima; si cambiaran los valores de x, el script avisa en lugar de afirmar algo falso.
- Revisión visual del bloque renderizado.
- Sin guiones largos.

**Observaciones para Jairo**
- Las tres predicciones se eligieron a propósito para mostrar dónde la recta acierta (tramo medio) y dónde se equivoca (extremos). Si prefieres tres predicciones "favorables" o valores tuyos, se cambian en `PREDICCIONES` o en las celdas amarillas, pero el texto tiene `assert` que se detendrán si ya no coinciden con esas frases. Si eso pasa, te aviso y adapto los textos.
- Con 1 año la diferencia entre lo estimado (2,50) y lo observado (0,51) es de unas 2 infracciones, del orden del error típico (2,52).
