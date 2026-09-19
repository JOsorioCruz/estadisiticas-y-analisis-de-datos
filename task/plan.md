# Plan de la Actividad No 2 de Probabilidad y Estadística (AF17401)

Regla de trabajo: una tarea por vez, y solo cuando Jairo diga "aprobada la tarea N". Al terminar cada una se actualiza su archivo y esta tabla, se muestra el resultado y se detiene el trabajo.

## Estado de las tareas

| # | Tarea | Estado | Aprobada por Jairo | Archivo |
|---|-------|--------|--------------------|---------|
| 00 | Preparar entorno | Aprobada | [x] | [00_preparar_entorno.md](00_preparar_entorno.md) |
| 01 | Cargar y validar la base | Aprobada | [x] | [01_cargar_y_validar_la_base.md](01_cargar_y_validar_la_base.md) |
| 02 | Elegir variables (decisión de Jairo) | Aprobada | [x] | [02_elegir_variables.md](02_elegir_variables.md) |
| 03 | Ejercicio 1: definiciones y ejemplos | Aprobada | [x] | [03_ejercicio_1_definiciones_y_ejemplos.md](03_ejercicio_1_definiciones_y_ejemplos.md) |
| 04 | Ejercicio 2: tabla de frecuencia agrupada | Aprobada | [x] | [04_ejercicio_2_tabla_de_frecuencia_agrupada.md](04_ejercicio_2_tabla_de_frecuencia_agrupada.md) |
| 05 | Ejercicio 2: histograma, circular y polígono | Aprobada | [x] | [05_ejercicio_2_histograma_circular_y_poligono.md](05_ejercicio_2_histograma_circular_y_poligono.md) |
| 06 | Ejercicio 2: intervalo de mayor frecuencia y 60% acumulado | Aprobada | [x] | [06_ejercicio_2_intervalo_mayor_y_60_acumulado.md](06_ejercicio_2_intervalo_mayor_y_60_acumulado.md) |
| 07 | Ejercicio 2: tendencia central, posición y tabla interpretada | Aprobada | [x] | [07_ejercicio_2_tendencia_central_posicion_y_tabla_interpretada.md](07_ejercicio_2_tendencia_central_posicion_y_tabla_interpretada.md) |
| 08 | Ejercicio 2: dispersión, asimetría, curtosis y homogeneidad | Aprobada | [x] | [08_ejercicio_2_dispersion_asimetria_curtosis_y_homogeneidad.md](08_ejercicio_2_dispersion_asimetria_curtosis_y_homogeneidad.md) |
| 09 | Ejercicio 3: ecuación de regresión y diagrama de dispersión | Aprobada | [x] | [09_ejercicio_3_ecuacion_de_regresion_y_diagrama_de_dispersion.md](09_ejercicio_3_ecuacion_de_regresion_y_diagrama_de_dispersion.md) |
| 10 | Ejercicio 3: R², confiabilidad, Pearson y nivel de correlación | Aprobada | [x] | [10_ejercicio_3_r2_confiabilidad_pearson_y_nivel_de_correlacion.md](10_ejercicio_3_r2_confiabilidad_pearson_y_nivel_de_correlacion.md) |
| 11 | Ejercicio 3: tres predicciones | Aprobada | [x] | [11_ejercicio_3_tres_predicciones.md](11_ejercicio_3_tres_predicciones.md) |
| 12 | Verificación cruzada | Aprobada | [x] | [12_verificacion_cruzada.md](12_verificacion_cruzada.md) |
| 13 | Redactar textos del libro | Aprobada | [x] | [13_redactar_textos_del_libro.md](13_redactar_textos_del_libro.md) |
| 14 | Ensamblar el libro | Aprobada | [x] | [14_ensamblar_el_libro.md](14_ensamblar_el_libro.md) |
| 15 | Revisión final y entrega | Aprobada | [x] | [15_revision_final_y_entrega.md](15_revision_final_y_entrega.md) |

## Variables elegidas (se llena en la tarea 02)

| Ejercicio | Variable(s) |
|-----------|-------------|
| Ejercicio 2 | Velocidad registrada (km/h) |
| Ejercicio 3 | Años de experiencia del conductor (x) e Histórico de infracciones (y) |

## Ajustes respecto al prompt inicial

- La carpeta `BASE` del prompt (`semestre vi/probabilidad y estadistica/unidad_2/actividad_unidad_2/`) no existe en esta ubicación. El enunciado y el Anexo 1 están en la raíz de este proyecto, así que aquí `BASE` es la raíz del proyecto.
- El `.venv` ya existe en la raíz (Python 3.13.5, solo con pip). No se instaló nada todavía.
- Ni el Python del sistema ni el `.venv` tienen `openpyxl`, contrario a lo que decía el prompt. Se instala en la tarea 00.
- LibreOffice sí está instalado (`/opt/homebrew/bin/soffice`), así que la verificación de la tarea 12 puede incluir recálculo con LibreOffice.
- Hay 13 registros repetidos en la base (filas idénticas en las 9 columnas). Decisión de Jairo (tarea 01): se conservan los 400 registros, y se menciona el hallazgo en la Introducción o en Anexos.
- El quiz no aparece en el PDF: está en la plataforma y lo haces tú.

## Preguntas abiertas

1. Nombre del archivo final. Por defecto: `actividad_probabilidad_y_estadistica_unidad_2.xlsx`. La guía dice "Unidad I", pero la carpeta dice `unidad_2`.
2. Fecha de la portada. No se copian las fechas de 2024 del PDF.
3. Nombre del tutor.
4. ¿Tienes la plantilla del foro colaborativo? Si la tienes, se usa como base de estructura.
5. Fuente de los criterios de homogeneidad (coeficiente de variación) y de clasificación de la correlación. Si no salen de las lecturas, elegimos una convención y la citamos como tal.
6. Carpeta de entrega de la tarea 15: el prompt menciona `actividades/probabilidad y estadistica/`, que no está en este proyecto. Hay un `~/WebstormProjects/AGENTE_UNIVERSIDAD`, pero no lo toco sin que me indiques si es ahí.
