# Tarea 03: Ejercicio 1: definiciones y ejemplos
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Redactar la Tabla 1 (Concepto, Definición, Ejemplos) de los seis conceptos.

## Entradas (archivos o decisiones que necesita)
- Lecturas del enunciado (Romero Ramos, 2016; Salazar Guerrero, 2018), si Jairo las comparte.
- Ejemplos tomados de la base de accidentes.

## Pasos
1. Redactar cada definición en palabras de Jairo, en primera persona plural o impersonal.
2. Poner ejemplos con datos reales de la base (frecuencia absoluta, frecuencia relativa, media, dispersión, regresión lineal, Pearson).
3. Pedir el texto de las lecturas si hace falta fundamentar alguna definición.
4. Dejar previsto el rótulo `Evidencia del quiz: insertar captura aquí`.

## Entregable (archivo o celdas concretas que produce)
Contenido de la Tabla 1 para revisión (en el Resultado de este archivo).

## Criterio de aceptación (cómo compruebo que está bien)
Seis conceptos completos, con definición propia y al menos un ejemplo cada uno, sin guiones largos y sin definiciones inventadas. El quiz y su captura los hace Jairo.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
Borrador de la Tabla 1 para revisión de Jairo. Todos los números salen de la base real (n = 400), calculados con scipy y pandas. Los decimales van con coma, como en el texto en español.

**Aclaraciones**
- No recibí el texto de las lecturas. Las definiciones son las usuales de estadística descriptiva, escritas con lenguaje propio, y **no las atribuyo a Romero Ramos (2016) ni a Salazar Guerrero (2018)**. Si Jairo las consulta y confirma que coinciden, se pueden citar en la Bibliografía.
- Los ejemplos de regresión y correlación usan la ecuación y r calculados con scipy. Los valores oficiales del libro salen de fórmulas de Excel en las tareas 09 y 10 y deben coincidir con estos.

**Tabla 1. Definiciones de conceptos**

| Concepto | Definición | Ejemplos |
|---|---|---|
| Frecuencia absoluta | Es la cantidad de veces que aparece un valor, o un grupo de valores, dentro de los datos. Se obtiene contando, así que siempre es un número entero, y si sumamos las frecuencias de todos los valores obtenemos el total de datos (n). | De los 400 accidentes de la base, 185 ocurrieron en Ibagué, 119 en Melgar y 96 en Espinal. Esos tres números son las frecuencias absolutas del municipio y suman 400. |
| Frecuencia relativa | Es la parte del total que representa cada valor. Se calcula dividiendo su frecuencia absoluta entre el total de datos y da un número entre 0 y 1, que también se puede escribir como porcentaje. Sirve para comparar grupos sin que importe cuántos datos tenga cada uno, y todas las frecuencias relativas juntas suman 1. | En Ibagué ocurrieron 185 de los 400 accidentes, es decir 185/400 = 0,4625, o sea el 46,25%. Melgar aporta el 29,75% y Espinal el 24%. Por nivel educativo, los conductores bachilleres son 210/400 = 52,5%. |
| Media | Es el promedio de los datos: sumamos todos los valores y dividimos entre la cantidad de valores. Representa el punto de equilibrio de los datos, por eso un valor muy alejado del resto la mueve con facilidad. Solo se puede calcular con variables numéricas. | Al sumar las velocidades registradas de los 400 accidentes y dividir entre 400 resulta 89,86 km/h, es decir que en promedio el vehículo causante iba casi a 90 km/h. El costo medio por accidente es de 188,21 millones de pesos. |
| Medidas de dispersión | Indican qué tan juntos o qué tan repartidos están los datos alrededor de su centro. Dos conjuntos pueden tener la misma media y comportarse muy distinto: en uno los datos son parecidos entre sí y en otro están muy dispersos. Las más usadas son el rango (máximo menos mínimo), la varianza, la desviación típica y el coeficiente de variación, que es la desviación dividida entre la media y permite comparar variables con unidades diferentes. | Las velocidades van de 32,1 a 140,8 km/h, así que el rango es de 108,7 km/h. La desviación típica es de 30,39 km/h y el coeficiente de variación de 33,8%, lo que indica que las velocidades se alejan en promedio unos 30 km/h de la media. En cambio, los años de experiencia tienen media de 3,60 y desviación de 3,97, un coeficiente de variación de 110,2%, mucho más disperso en términos relativos. |
| Regresión lineal | Es una técnica que busca la recta que mejor describe cómo cambia una variable (la dependiente, y) cuando cambia otra (la independiente, x). La recta se escribe y = a + bx: la pendiente b dice cuánto cambia y por cada unidad que aumenta x, y el intercepto a es el valor de y cuando x vale 0. Se ajusta por mínimos cuadrados, de modo que las distancias de los puntos a la recta sean lo más pequeñas posible en conjunto. Sirve para predecir dentro del rango observado, pero por sí sola no demuestra que una variable cause la otra. | Con los años de experiencia (x) y el histórico de infracciones (y) de los 400 conductores, la recta es y = 1,73 + 0,77x. La pendiente indica que por cada año más de experiencia, el modelo asocia unas 0,77 infracciones adicionales en los últimos cinco años. |
| Correlación de Pearson | Es un número r, entre -1 y 1, que mide qué tan fuerte es la relación lineal entre dos variables numéricas y en qué sentido va. Si r se acerca a 1, cuando una variable sube la otra también; si se acerca a -1, cuando una sube la otra baja; y si está cerca de 0 no hay relación lineal, aunque podría existir otro tipo de relación. No depende de las unidades en que estén medidas las variables, y al elevarlo al cuadrado se obtiene el coeficiente de determinación. | Entre años de experiencia e infracciones, r = 0,77: relación positiva y fuerte. Entre velocidad y costo del accidente, r = 0,04: casi nula, es decir que en esta base ir más rápido no se asocia linealmente con un costo mayor. |

**Verificación de cada número citado (calculado con pandas y scipy)**
- Frecuencias por municipio: 185, 119, 96 (suman 400). Relativas: 0,4625, 0,2975, 0,24.
- Nivel educativo: Bachiller 210 (52,5%), Superior 190 (47,5%).
- Velocidad: media 89,8615; mín 32,1; máx 140,8; rango 108,7; desviación típica muestral 30,3895; CV 33,82%.
- Costo medio: 188,2105 millones.
- Experiencia: media 3,6025; desviación típica muestral 3,9697; CV 110,2%.
- Regresión experiencia (x) sobre infracciones (y): pendiente 0,7723; intercepto 1,7278; r = 0,7724; R² = 0,5966.
- Velocidad con costo: r = 0,040.

**Rótulo previsto para la hoja del ejercicio 1:** `Evidencia del quiz: insertar captura aquí`, con un espacio en blanco debajo. El quiz y la captura los hace Jairo.

**Decisiones que dejo a Jairo**
1. Leer cada definición y reescribir con su voz lo que no suene como él. La rúbrica premia que estén "con sus palabras".
2. Decidir si desea citar las lecturas en esta tabla (hoy no se citan).
