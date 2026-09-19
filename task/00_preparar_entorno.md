# Tarea 00: Preparar entorno
Estado: Aprobada
Aprobada por Jairo: [x]

## Objetivo
Dejar listo el entorno de Python reproducible para las tareas siguientes.

## Entradas (archivos o decisiones que necesita)
- El `.venv` que ya existe en la raíz (Python 3.13.5, creado por PyCharm, solo con pip).
- Tu aprobación para instalar paquetes.
- Confirmación de si se usa ese `.venv` tal cual.

## Pasos
1. Confirmar con Jairo que se reutiliza el `.venv` existente.
2. Instalar `pandas`, `numpy`, `scipy`, `xlsxwriter` y `openpyxl` (con aprobación).
3. Generar `requirements.txt` con las versiones exactas.
4. Comprobar que LibreOffice responde en modo headless (`/opt/homebrew/bin/soffice --version`).
5. Anotar versiones en el Resultado.

## Entregable (archivo o celdas concretas que produce)
`requirements.txt` y entorno funcionando, con versiones anotadas.

## Criterio de aceptación (cómo compruebo que está bien)
`python -c "import pandas, numpy, scipy, xlsxwriter, openpyxl"` corre sin error dentro del `.venv` y `soffice --version` responde.

## Resultado (se llena al terminar: valores obtenidos, hallazgos, dudas)
- Se reutilizó el `.venv` existente de la raíz (Python 3.13.5).
- Instalados: pandas 3.0.6, numpy 2.5.3, scipy 1.18.1, xlsxwriter 3.2.9, openpyxl 3.1.5. Dependencias: et_xmlfile 2.0.0, python-dateutil 2.9.0.post0, six 1.17.0.
- `requirements.txt` generado con `pip freeze` (8 paquetes con versión exacta).
- Comprobación: `import pandas, numpy, scipy, xlsxwriter, openpyxl` corre sin error.
- LibreOffice 26.8.0.3 disponible en `/opt/homebrew/bin/soffice` (responde en modo headless).
- Nota: pip avisa que existe la versión 26.2.1 (el `.venv` tiene 26.0.1). No se actualizó porque no afecta el trabajo.
