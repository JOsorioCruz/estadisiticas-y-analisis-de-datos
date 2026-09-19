# Tarea 04: Ejercicio 2: tabla de frecuencia agrupada
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Construir la tabla de frecuencia con datos agrupados de la variable elegida.

## Entradas (archivos o decisiones que necesita)
- Variable fijada en la tarea 02.
- Aprobación de la regla para el número de intervalos.

## Pasos
1. Proponer el número de intervalos (Sturges u otra) y pedir aprobación.
2. Calcular amplitud, límites, marca de clase, fi, Fi, hi, Hi y porcentajes.
3. Escribir las frecuencias con fórmulas `COUNTIFS` o `FREQUENCY` apuntando a la hoja de datos, con valor calculado en Python.

## Entregable (archivo o celdas concretas que produce)
Tabla con fórmulas en un módulo `src/ej2_tabla.py`.

## Criterio de aceptación (cómo compruebo que está bien)
La suma de fi es 400, Hi termina en 100% y cada frecuencia coincide con el conteo directo en Python.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej2_tabla.py`: calcula la tabla con numpy, la escribe con fórmulas de Excel y se verifica sola. Se ejecuta desde la raíz con `.venv/bin/python src/ej2_tabla.py`.
- `src/hoja_datos.py`: copia la hoja `DATOS` del Anexo 1 al libro y arma las referencias de rango (`DATOS!$E$2:$E$401`). Lo reutilizarán las tareas siguientes.
- `output/ej2_tabla_borrador.xlsx`: hojas `Ej2 Tabla` y `DATOS`. Es un borrador de trabajo, no el libro final.

**Decisión de construcción (Jairo aprobó la tarea con la propuesta Sturges)**
- n = 400, mínimo 32,1, máximo 140,8, rango R = 108,7.
- Sturges: k = 1 + log2(400) = 9,64, redondeado hacia arriba a **k = 10**.
- Amplitud teórica R/k = 10,87, adoptada **A = 11** (redondeada hacia arriba, para que los 10 intervalos cubran hasta 142 y no dejen fuera el máximo).
- Primer límite inferior **32** (número redondo por debajo del mínimo). Si Jairo prefiere otra amplitud o inicio, se cambian dos celdas amarillas de la hoja.
- Intervalos cerrados a la izquierda y abiertos a la derecha, salvo el último, que incluye su límite superior (142).

**Tabla resultante**

| Intervalo | Marca xi | fi | Fi | hi | Hi | hi % | Hi % |
|---|---|---|---|---|---|---|---|
| [32 - 43) | 37,5 | 34 | 34 | 0,0850 | 0,0850 | 8,50 | 8,50 |
| [43 - 54) | 48,5 | 40 | 74 | 0,1000 | 0,1850 | 10,00 | 18,50 |
| [54 - 65) | 59,5 | 18 | 92 | 0,0450 | 0,2300 | 4,50 | 23,00 |
| [65 - 76) | 70,5 | 38 | 130 | 0,0950 | 0,3250 | 9,50 | 32,50 |
| [76 - 87) | 81,5 | 40 | 170 | 0,1000 | 0,4250 | 10,00 | 42,50 |
| [87 - 98) | 92,5 | 50 | 220 | 0,1250 | 0,5500 | 12,50 | 55,00 |
| [98 - 109) | 103,5 | 48 | 268 | 0,1200 | 0,6700 | 12,00 | 67,00 |
| [109 - 120) | 114,5 | 62 | 330 | 0,1550 | 0,8250 | 15,50 | 82,50 |
| [120 - 131) | 125,5 | 34 | 364 | 0,0850 | 0,9100 | 8,50 | 91,00 |
| [131 - 142] | 136,5 | 36 | 400 | 0,0900 | 1,0000 | 9,00 | 100,00 |
| Total | | 400 | | 1,0000 | | 100,00 | |

Adelanto para la tarea 06, sin cerrarla aún: el intervalo con mayor fi parece ser [109 - 120) con 62, y el 60% acumulado se cruza en [98 - 109) (Hi = 67%).

**Fórmulas en Excel:** `COUNTIFS(DATOS!$E$2:$E$401,">="&B,DATOS!$E$2:$E$401,"<"&C)` (el último intervalo usa `"<="`), `COUNT`, `MIN`, `MAX`, `ROUNDUP(1+LOG(n,2),0)` para k, y sumas acumuladas. Cada celda lleva también el valor calculado en Python.

**Verificación**
1. Se construyó una copia del libro **sin valores guardados** en las fórmulas y LibreOffice la recalculó desde cero (con un perfil temporal que fuerza el recálculo). Comparada con numpy: diferencia máxima 1,4e-14 en Li, Ls, xi, fi, Fi, hi, Hi y porcentajes. Parámetros recalculados: n = 400, mín 32,1, máx 140,8, R 108,7, k 10, R/k 10,87.
2. `np.histogram` con los mismos límites da fi = [34, 40, 18, 38, 40, 50, 48, 62, 34, 36], que suman 400 y coinciden con la tabla.
3. La hoja `DATOS` del borrador es idéntica al Anexo 1, celda por celda (401 filas con el encabezado).
4. Sin guiones largos en el texto de la hoja.

**Incidente durante la tarea:** la primera verificación con LibreOffice no recalculó y dejó ceros. Lo detecté porque la diferencia daba 400. Se resolvió con el perfil temporal de recálculo. Después corregí una fila mal leída en el propio script de verificación (leía el mínimo en lugar de n).
