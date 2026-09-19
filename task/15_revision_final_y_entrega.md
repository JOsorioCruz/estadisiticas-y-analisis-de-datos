# Tarea 15: Revisión final y entrega
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Revisar el libro contra la rúbrica y la lista de comprobación, y copiarlo a la carpeta de entrega.

## Entradas (archivos o decisiones que necesita)
- Libro de la tarea 14.
- Ubicación de la carpeta de entrega (ver pregunta abierta en `plan.md`).

## Pasos
1. Recorrer la lista de comprobación de la sección 8 y marcar cada punto con evidencia.
2. Buscar explícitamente guiones largos en todas las celdas.
3. Copiar el libro a la carpeta de entrega con tu aprobación.

## Entregable (archivo o celdas concretas que produce)
Copia en la carpeta de entrega.

## Criterio de aceptación (cómo compruebo que está bien)
Todos los puntos de la lista de comprobación cumplen. No se hace commit ni push.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
**Archivos producidos en esta tarea**
- `src/revision_final.py`: revisión automática del libro contra el enunciado, la rúbrica y la lista de comprobación (28 comprobaciones).
- `src/exportar_pdf.py` y `output/actividad_probabilidad_y_estadistica_unidad_2.pdf`: copia en PDF de 21 páginas, sin la hoja `DATOS`, con saltos de página para que cada gráfico quede junto a su conclusión.
- `src/corrector.swift`: usa el corrector ortográfico del sistema en español.
- `README.md`: documentación completa del trabajo, pensada para un repositorio.
- `ENTREGA.md`: qué se entrega, cómo se cubre cada viñeta del enunciado y de la rúbrica, y los pasos del autor antes de subirlo.
- `.gitignore` y `datos_entrega.ejemplo.json`: excluyen entorno, editor y borradores, y permiten poner tutor y fecha sin editar código.
- Cambios en `src/generar_libro.py`: escala e impresión fijas con saltos de página en las hojas de los ejercicios 2 y 3, y datos opcionales de portada. Cambios menores en `src/ej2_graficos.py` y `src/textos_libro.py`.

**Lista de comprobación de la sección 8 del prompt**

| Punto | Estado | Evidencia |
|---|---|---|
| Los tres ejercicios completos, cada viñeta con su respuesta visible | Cumple | `revision_final.py`: 19 comprobaciones de viñetas en OK. La correspondencia viñeta a hoja está en `ENTREGA.md` |
| Variable del ejercicio 2 única y cuantitativa; dos en el ejercicio 3; coinciden con el foro | Parcial | Velocidad; experiencia e infracciones. **La coincidencia con el foro la confirma Jairo** (celda amarilla del Anexo C) |
| Todas las medidas son fórmulas de Excel y coinciden con la verificación | Cumple | 169 celdas con fórmula; 141 de 141 valores coinciden con numpy y scipy, recalculados y guardados; diferencia máxima 5,7e-13 |
| Cuatro gráficos nativos con título, ejes rotulados y unidades | Cumple | Extraído del XML de cada gráfico; el circular no tiene ejes por su tipo |
| Definiciones del ejercicio 1 en sus palabras, con ejemplos | Parcial | Redactadas y aprobadas por Jairo; 18 cifras de los ejemplos comprobadas contra los datos. **Conviene que las relea con su voz** |
| Espacio rotulado para el quiz y ninguna imagen | Cumple | Recuadro `Evidencia del quiz: insertar captura aquí`; `xl/media` no existe |
| Hojas en el orden pedido | Cumple | Portada, Presentación, Introducción, Objetivos, Ejercicio 1, 2 y 3, Conclusiones, Bibliografía, Anexos, DATOS |
| Bibliografía APA 7 con fuentes realmente usadas | Parcial | Solo las dos lecturas del enunciado. **Jairo debe confirmar que las consultó**; la lista opcional no se incluyó |
| Ortografía y tildes revisadas; ningún guion largo | Cumple | Corrector del sistema en español: solo falsos positivos (funciones en inglés, términos técnicos, un nombre propio y una URL). Búsqueda de guion largo: 0 en celdas, gráficos, hojas, textos, README y scripts |
| Hoja de datos idéntica al Anexo 1 | Cumple | 400 registros comparados celda por celda |
| Sin afirmaciones sin sustento: cada interpretación se rastrea a un número del libro | Cumple | Cada cifra de los textos se comparó con las celdas numéricas del libro recalculado. Las 21 que no eran una celda se verificaron una por una contra los datos (por ejemplo 45 % = 180/400, 57,5 % = 230/400, 40,34 % = 100 - 59,66) o son límites de la escala adoptada |

**Comprobaciones de la rúbrica**
- Criterio 1 (Ejercicio 1, 1,0): la Tabla 1 completa, con los seis conceptos y ejemplos. Nivel superior si Jairo confirma que están en sus palabras.
- Criterio 2 (Ejercicio 2, 1,5): tabla, tres gráficos con conclusiones, todas las medidas solicitadas y respuestas a las preguntas.
- Criterio 3 (Ejercicio 3, 1,5): diagrama de dispersión con recta y todas las medidas solicitadas.
- Criterios 4 y 5 (foro y entrega a tiempo, 0,5 + 0,5): los hace Jairo a mano.

**Entrega a la carpeta local y repositorio (Jairo respondió "sí" a ambas ofertas)**
- La carpeta `~/WebstormProjects/AGENTE_UNIVERSIDAD/actividades/probabilidad y estadistica/` existía, con la actividad de la unidad 1, y el nombre por defecto coincide con la convención de ese repositorio. Se comprobó antes que el destino no tenía ya el archivo, para no sobrescribir nada.
- **Se copió ahí el `.xlsx` como copia de trabajo**, todavía con los campos `PENDIENTE` y el recuadro del quiz vacío. Cuando Jairo termine, debe volver a copiar el libro final, que reemplaza a esta copia (comando en `ENTREGA.md`).
- Se hizo `git init` en este proyecto, con un primer commit local. No se hizo push ni se configuró ningún remoto. El commit no lleva trailer `Co-Authored-By` ni pie de "Generated with Claude Code", como pide el `CLAUDE.md` de `AGENTE_UNIVERSIDAD` y el prompt.
- `main.py` (ejemplo de PyCharm) no se incluyó en el commit.

**Pendientes que solo puede resolver Jairo**
1. Tutor y fecha (`datos_entrega.json`, o directamente en la portada).
2. Confirmar la combinación de variables publicada en el foro (Anexo C).
3. Hacer el quiz y pegar la captura en su recuadro. Después no volver a ejecutar `generar_libro.py`, porque sobrescribe el archivo.
4. Confirmar que consultó las dos lecturas y decidir la bibliografía opcional (sus datos se escribieron de memoria y deben verificarse).
5. Decidir si el Anexo B declara que el libro se generó con Python.
6. Confirmar el nombre final del archivo.
7. Abrir el libro en Microsoft Excel para comprobar los valores (la verificación se hizo con LibreOffice).
8. Foro y subida a la plataforma.
9. Volver a copiar el libro final a la carpeta de entrega local y, si se sube al repositorio remoto, hacer el `push` (no se hizo).

**Limpieza pendiente (no la hice sin pedirlo):** `output/*_borrador.xlsx` son intermedios que ya no se usan. Están en `.gitignore`, así que no subirán al repositorio.

**Incidentes durante la tarea:** un `rm` con comodín en zsh abortó dos veces la cadena de comandos por no encontrar archivos y lo repetí sin él; la primera versión de los saltos de página partía un gráfico de su conclusión y dejaba una página en blanco, y se corrigió con otra escala y con el área de impresión. Además, durante el cierre la carpeta `task/` dejó de ser visible unos minutos (no la toqué yo) y el registro de esta tarea falló; al reaparecer comprobé que los 17 archivos estaban íntegros y lo completé.
