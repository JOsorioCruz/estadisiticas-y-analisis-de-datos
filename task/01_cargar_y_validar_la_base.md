# Tarea 01: Cargar y validar la base
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Leer la hoja `DATOS` del Anexo 1 y contrastarla con el perfil previo.

## Entradas (archivos o decisiones que necesita)
- `Anexo 1 - Base de datos .xlsx` (hoja `DATOS`, A1:I401).
- Entorno de la tarea 00.

## Pasos
1. Escribir `src/carga.py` con una función que lea la hoja `DATOS` con ruta relativa.
2. Comprobar dimensiones, tipos, nulos, duplicados y rangos.
3. Contrastar con la sección 4 del prompt e informar cualquier diferencia.
4. Reportar los **13 registros repetidos** ya detectados en la revisión previa (filas idénticas en las 9 columnas) y preguntar a Jairo si se conservan (por defecto sí, porque el Anexo 1 debe copiarse sin modificar).
5. Preguntar a Jairo los puntos abiertos 1 a 4 de la sección 9 si no se resolvieron antes.

## Entregable (archivo o celdas concretas que produce)
`src/carga.py` y un informe corto de validación en el Resultado.

## Criterio de aceptación (cómo compruebo que está bien)
400 filas, 9 columnas, sin nulos, y los conteos y rangos coinciden con lo esperado o las diferencias quedan explicadas.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
Archivo producido: `src/carga.py` (funciones `cargar_datos()` y `validar()`, ruta relativa al proyecto). Se ejecuta con `.venv/bin/python src/carga.py`.

**Validación (todo coincide con la sección 4 del prompt)**
- 400 filas x 9 columnas, encabezados iguales a los del Anexo 1.
- Nulos: 0 en las 9 columnas.
- Tipos: municipio y nivel educativo son texto; edad, fallecidos, heridos, experiencia e infracciones son enteros; velocidad y costo son decimales.
- Municipios: Ibagué 185, Melgar 119, Espinal 96. Nivel educativo: Bachiller 210, Superior 190. Sin espacios sobrantes.
- Rangos (mín a máx, valores distintos): edad 16 a 62 (39); fallecidos 0 a 4 (5); heridos 1 a 6 (6); velocidad 32.1 a 140.8 (261); costo 1.4 a 399.1 (285); experiencia 0 a 30 (19); infracciones 0 a 20 (20).

**Hallazgos que no estaban en el prompt**
1. **13 registros repetidos** (26 filas en 13 parejas idénticas en las 9 columnas). Hay un patrón claro: cada pareja está separada exactamente por 100 filas y todas caen en el mismo tramo. Filas de Excel: 213/313, 214/314, 220/320, 221/321, 227/327, 237/337, 240/340, 241/341, 246/346, 269/369, 285/385, 300/400, 301/401. Como velocidad y costo tienen decimales, que dos accidentes coincidan en todo por azar es muy improbable, así que parece una copia dentro de la base y no coincidencia.
2. **Coherencia edad y experiencia:** ningún registro tiene experiencia mayor o igual que la edad. Pero 3 registros tienen más años de experiencia que `edad - 16` (por ejemplo, edad 16 con 6 años de licencia, fila 32 de Excel; y edad 16 con 1 año, filas 228 y 328). Con la edad mínima de 18 años para licencia serían 17 registros. Solo lo dejo anotado: no se corrige nada, porque la hoja debe quedar idéntica al Anexo 1.

**Decisión de Jairo: conservar los 400 registros**
- Sobre los repetidos: mi propuesta es **conservar los 400 registros** tal cual, y mencionar el hallazgo en la Introducción o en Anexos. Los promedios y demás medidas cambiarían poco, pero un docente que verifique con la base original espera n = 400. La alternativa sería analizar 387 registros únicos, y eso no coincidiría con el Anexo 1. Jairo aprobó conservar los 400 registros, sin quitar los repetidos.

**Puntos abiertos de la sección 9 (siguen sin respuesta)**
Nombre del archivo final, fecha de portada, tutor, plantilla del foro y fuente de los criterios de homogeneidad y de correlación. La carpeta de entrega de la tarea 15 también sigue por definir.
