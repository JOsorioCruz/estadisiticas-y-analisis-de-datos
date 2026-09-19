# Anexos

## Anexo A. Hoja de datos

Copia exacta, sin modificar ningún valor, de la hoja DATOS del Anexo 1: 400 registros y 9 columnas. Es la hoja a la que apuntan todas las fórmulas del libro.

La base contiene 13 parejas de registros idénticos en las nueve columnas. Están en las filas 213 y 313, 214 y 314, 220 y 320, 221 y 321, 227 y 327, 237 y 337, 240 y 340, 241 y 341, 246 y 346, 269 y 369, 285 y 385, 300 y 400, 301 y 401 de la hoja (numeración de Excel, con el encabezado en la fila 1). Cada pareja está separada exactamente por 100 filas. Se conservaron todos los registros.

## Anexo B. Verificación de los cálculos

Se compararon 141 valores del libro con cálculos independientes hechos en Python (numpy y scipy) a partir de los datos originales, y con el recálculo de las fórmulas de Excel en LibreOffice. Todos coincidieron, con una diferencia absoluta máxima de 5,7e-13. La tabla lista cada comparación.

Las tablas, los gráficos y las fórmulas del libro se generaron con un programa en Python (biblioteca xlsxwriter) que escribe fórmulas nativas de Excel.

## Anexo C. Variables elegidas en el foro

Nombre: Jairo Alonso Osorio Cruz. Variable del ejercicio 2: velocidad registrada. Variables del ejercicio 3: años de experiencia del conductor (x) e histórico de infracciones (y).

PENDIENTE: Jairo debe confirmar que esta combinación es la que publicó en el foro y no chocó con la de sus compañeros.

## Anexo D. Convenciones adoptadas

Estas convenciones son de uso común en estadística descriptiva y no proceden de las lecturas del curso.

Varianza y desviación típica muestrales (VAR.S y STDEV.S), porque los 400 registros se toman como una muestra de la accidentalidad del Tolima.

Homogeneidad: la distribución es homogénea si el coeficiente de variación es menor que 30 % y heterogénea en caso contrario.

Asimetría: casi simétrica si su valor absoluto es menor que 0,5. Curtosis: platicúrtica si el exceso de curtosis es negativo.

Nivel de correlación según |r|: perfecta si vale 1, excelente de 0,90 a menos de 1, aceptable de 0,80 a menos de 0,90, regular de 0,50 a menos de 0,80, mínima por debajo de 0,50 y sin correlación si vale 0.
