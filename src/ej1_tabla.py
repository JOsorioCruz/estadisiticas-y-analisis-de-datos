"""Ejercicio 1: Tabla 1 (definiciones y ejemplos), texto aprobado en la tarea 03, y comprobación de sus cifras."""
import numpy as np

from carga import cargar_datos
from ej2_tabla import VARIABLE
from ej3_regresion import X, Y

# (concepto, definición, ejemplos)
TABLA_1 = [
    ('Frecuencia absoluta', 'Es la cantidad de veces que aparece un valor, o un grupo de valores, dentro de los datos. Se obtiene contando, así que siempre es un número entero, y si sumamos las frecuencias de todos los valores obtenemos el total de datos (n).', 'De los 400 accidentes de la base, 185 ocurrieron en Ibagué, 119 en Melgar y 96 en Espinal. Esos tres números son las frecuencias absolutas del municipio y suman 400.'),
    ('Frecuencia relativa', 'Es la parte del total que representa cada valor. Se calcula dividiendo su frecuencia absoluta entre el total de datos y da un número entre 0 y 1, que también se puede escribir como porcentaje. Sirve para comparar grupos sin que importe cuántos datos tenga cada uno, y todas las frecuencias relativas juntas suman 1.', 'En Ibagué ocurrieron 185 de los 400 accidentes, es decir 185/400 = 0,4625, o sea el 46,25%. Melgar aporta el 29,75% y Espinal el 24%. Por nivel educativo, los conductores bachilleres son 210/400 = 52,5%.'),
    ('Media', 'Es el promedio de los datos: sumamos todos los valores y dividimos entre la cantidad de valores. Representa el punto de equilibrio de los datos, por eso un valor muy alejado del resto la mueve con facilidad. Solo se puede calcular con variables numéricas.', 'Al sumar las velocidades registradas de los 400 accidentes y dividir entre 400 resulta 89,86 km/h, es decir que en promedio el vehículo causante iba casi a 90 km/h. El costo medio por accidente es de 188,21 millones de pesos.'),
    ('Medidas de dispersión', 'Indican qué tan juntos o qué tan repartidos están los datos alrededor de su centro. Dos conjuntos pueden tener la misma media y comportarse muy distinto: en uno los datos son parecidos entre sí y en otro están muy dispersos. Las más usadas son el rango (máximo menos mínimo), la varianza, la desviación típica y el coeficiente de variación, que es la desviación dividida entre la media y permite comparar variables con unidades diferentes.', 'Las velocidades van de 32,1 a 140,8 km/h, así que el rango es de 108,7 km/h. La desviación típica es de 30,39 km/h y el coeficiente de variación de 33,8%, lo que indica que las velocidades se alejan en promedio unos 30 km/h de la media. En cambio, los años de experiencia tienen media de 3,60 y desviación de 3,97, un coeficiente de variación de 110,2%, mucho más disperso en términos relativos.'),
    ('Regresión lineal', 'Es una técnica que busca la recta que mejor describe cómo cambia una variable (la dependiente, y) cuando cambia otra (la independiente, x). La recta se escribe y = a + bx: la pendiente b dice cuánto cambia y por cada unidad que aumenta x, y el intercepto a es el valor de y cuando x vale 0. Se ajusta por mínimos cuadrados, de modo que las distancias de los puntos a la recta sean lo más pequeñas posible en conjunto. Sirve para predecir dentro del rango observado, pero por sí sola no demuestra que una variable cause la otra.', 'Con los años de experiencia (x) y el histórico de infracciones (y) de los 400 conductores, la recta es y = 1,73 + 0,77x. La pendiente indica que por cada año más de experiencia, el modelo asocia unas 0,77 infracciones adicionales en los últimos cinco años.'),
    ('Correlación de Pearson', 'Es un número r, entre -1 y 1, que mide qué tan fuerte es la relación lineal entre dos variables numéricas y en qué sentido va. Si r se acerca a 1, cuando una variable sube la otra también; si se acerca a -1, cuando una sube la otra baja; y si está cerca de 0 no hay relación lineal, aunque podría existir otro tipo de relación. No depende de las unidades en que estén medidas las variables, y al elevarlo al cuadrado se obtiene el coeficiente de determinación.', 'Entre años de experiencia e infracciones, r = 0,77: relación positiva y fuerte. Entre velocidad y costo del accidente, r = 0,04: casi nula, es decir que en esta base ir más rápido no se asocia linealmente con un costo mayor.'),
]

RUTULO_QUIZ = "Evidencia del quiz: insertar captura aquí"


def comprobar_cifras(df=None):
    """Cada cifra citada en los ejemplos se compara con los datos; si algo cambia, el script se detiene."""
    df = cargar_datos() if df is None else df
    n = len(df)
    mun = df["MUNICIPIO DEL SINIESTRO"].value_counts()
    niv = df["NIVEL EDUCATIVO DEL CONDUCTOR"].value_counts()
    v = df[VARIABLE]
    c = df["COSTO ACCIDENTE (MILLONES DE PESOS)"]
    x, y = df[X], df[Y]
    b, a = np.polyfit(x, y, 1)
    ej = {conc: e for conc, _, e in TABLA_1}
    esperado = [
        ("Frecuencia absoluta", "185 ocurrieron en Ibagué, 119 en Melgar y 96 en Espinal", (mun["Ibagué"], mun["Melgar"], mun["Espinal"]) == (185, 119, 96) and n == 400),
        ("Frecuencia relativa", "185/400 = 0,4625", abs(mun["Ibagué"] / n - 0.4625) < 1e-12),
        ("Frecuencia relativa", "29,75%", abs(mun["Melgar"] / n * 100 - 29.75) < 1e-9),
        ("Frecuencia relativa", "24%", abs(mun["Espinal"] / n * 100 - 24) < 1e-9),
        ("Frecuencia relativa", "210/400 = 52,5%", niv["Bachiller"] == 210 and abs(niv["Bachiller"] / n * 100 - 52.5) < 1e-9),
        ("Media", "89,86 km/h", round(v.mean(), 2) == 89.86),
        ("Media", "188,21 millones", round(c.mean(), 2) == 188.21),
        ("Medidas de dispersión", "32,1 a 140,8", (v.min(), v.max()) == (32.1, 140.8)),
        ("Medidas de dispersión", "108,7 km/h", round(v.max() - v.min(), 1) == 108.7),
        ("Medidas de dispersión", "30,39 km/h", round(v.std(ddof=1), 2) == 30.39),
        ("Medidas de dispersión", "33,8%", round(v.std(ddof=1) / v.mean() * 100, 1) == 33.8),
        ("Medidas de dispersión", "media de 3,60", round(x.mean(), 2) == 3.60),
        ("Medidas de dispersión", "desviación de 3,97", round(x.std(ddof=1), 2) == 3.97),
        ("Medidas de dispersión", "110,2%", round(x.std(ddof=1) / x.mean() * 100, 1) == 110.2),
        ("Regresión lineal", "y = 1,73 + 0,77x", round(a, 2) == 1.73 and round(b, 2) == 0.77),
        ("Regresión lineal", "0,77 infracciones", round(b, 2) == 0.77),
        ("Correlación de Pearson", "r = 0,77", round(np.corrcoef(x, y)[0, 1], 2) == 0.77),
        ("Correlación de Pearson", "r = 0,04", round(np.corrcoef(v, c)[0, 1], 2) == 0.04),
    ]
    for concepto, fragmento, cierto in esperado:
        assert fragmento in ej[concepto], (concepto, fragmento)
        assert cierto, (concepto, fragmento)
    return len(esperado)


if __name__ == "__main__":
    print(f"{comprobar_cifras()} cifras de la Tabla 1 comprobadas contra los datos")
