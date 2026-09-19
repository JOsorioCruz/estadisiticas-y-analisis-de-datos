# Tarea 05: Ejercicio 2: histograma, circular y polígono
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Crear los tres gráficos nativos a partir de la tabla y redactar sus conclusiones.

## Entradas (archivos o decisiones que necesita)
- Tabla de la tarea 04.

## Pasos
1. Crear con `xlsxwriter` un histograma (columnas sin separación), un diagrama circular y un polígono de frecuencia.
2. Título, ejes rotulados y unidades en cada uno.
3. Redactar una conclusión por gráfico con base en los números de la tabla.

## Entregable (archivo o celdas concretas que produce)
Tres gráficos nativos y su texto.

## Criterio de aceptación (cómo compruebo que está bien)
Ninguna imagen insertada, los tres gráficos se abren como gráficos de Excel y cada conclusión se rastrea a un valor de la tabla.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos**
- `src/ej2_graficos.py`: agrega al libro los tres gráficos, un bloque auxiliar para el polígono y las conclusiones. Se ejecuta desde la raíz con `.venv/bin/python src/ej2_graficos.py`. Reutiliza `src/ej2_tabla.py` (tarea 04), al que solo le añadí dos posiciones al valor de retorno.
- `output/ej2_graficos_borrador.xlsx`: hojas `Ej2 Tabla` (tabla, gráficos y conclusiones) y `DATOS`. Es un borrador de trabajo.

**Gráficos (los tres son gráficos nativos de Excel)**
1. **Histograma:** columnas sin separación entre barras, con `fi` de la tabla como valores y los intervalos como categorías. Título, eje X "Velocidad registrada (km/h)", eje Y "Número de accidentes (fi)" y etiquetas de valor.
2. **Diagrama circular:** una porción por intervalo, con porcentajes y leyenda de intervalos. Título con unidad (km/h).
3. **Polígono de frecuencia:** dispersión con líneas rectas sobre las marcas de clase. Se cierra con dos clases vacías en los extremos (marcas 26,5 y 147,5 con fi = 0), que salen de fórmulas en un bloque auxiliar (columnas L y M de la misma hoja, rotulado "Auxiliar del polígono").

**Conclusiones (texto generado con los valores de la tabla; se pueden retocar a tu voz)**

**Conclusión del histograma.** El intervalo con la barra más alta es [109 - 120) km/h, con 62 accidentes (15,5 %), y el de la barra más baja es [54 - 65) km/h, con solo 18 (4,5 %). Ese valle es un hueco entre dos intervalos vecinos que tienen 40 y 38 accidentes, así que la distribución no es simétrica ni tiene un único pico. Entre 87 y 120 km/h se concentran 160 accidentes (40,0 %), cuatro de cada diez. La base no trae el límite de velocidad de cada vía, por lo que esto muestra dónde se concentran los siniestros y no cuáles velocidades son excesivas.

**Conclusión del diagrama circular.** Cada porción es el porcentaje de accidentes de un intervalo de velocidad. La más grande es [109 - 120) con 15,5 % y la más pequeña es [54 - 65) con 4,5 %. Como ninguna porción pasa del 15,5 %, ninguna franja de velocidad domina sobre las demás. Los tres intervalos vecinos con más accidentes, de 87 a 120 km/h, suman el 40,0 %. Con diez porciones es difícil comparar tamaños a simple vista, por eso conviene apoyarse en el histograma.

**Conclusión del polígono de frecuencia.** El polígono une las marcas de clase y se cierra con dos intervalos vacíos, uno antes y otro después (marcas 26,5 y 147,5 km/h), por eso empieza y termina en 0. Arranca en 34 accidentes en la marca 37,5, cae a 18 en la marca 59,5 y desde ese valle sube, con una pequeña baja en 103,5, hasta el pico de 62 en 114,5 km/h. Después baja a 34 y 36. Como el punto medio del rango es 87 km/h y 230 accidentes (57,5 %) se registraron a esa velocidad o más, la distribución se inclina hacia las velocidades altas.

**Verificación**
- Los tres archivos de gráfico están en el libro (`xl/charts/chart1..3.xml`, tipos barChart, pieChart y scatterChart) y **no hay imágenes** (`xl/media` no existe).
- Referencias leídas del XML: histograma y circular apuntan a `'Ej2 Tabla'!$A$13:$A$22` (intervalos) y `$E$13:$E$22` (fi); el polígono apunta a `$L$13:$L$24` y `$M$13:$M$24` (12 puntos con las clases vacías).
- Recálculo con LibreOffice de una copia sin valores guardados: el auxiliar del polígono coincide con numpy (diferencia máxima 0).
- Revisión visual: se renderizó el libro con LibreOffice y se revisaron los tres gráficos y los textos (títulos, ejes, etiquetas).
- Cada cifra citada en las conclusiones sale de la tabla de la tarea 04 (por ejemplo: 62 accidentes en [109 - 120), 18 en [54 - 65), 160 = 50 + 48 + 62 en 87 a 120 km/h, 230 = 57,5 % a 87 km/h o más). El texto lleva comprobaciones (`assert`) para que no siga afirmando algo si los datos cambian.
- Sin guiones largos.

**Observaciones para Jairo**
- El circular con diez porciones se lee peor que el histograma. La conclusión lo dice, porque es una limitación real del gráfico y no un defecto del archivo.
- Las etiquetas del circular en la vista previa de LibreOffice salen con punto decimal (10.0 %). En Excel en español saldrán con la coma de tu configuración regional.
- Para imprimir, la hoja está en horizontal y ajustada a una página de ancho.
