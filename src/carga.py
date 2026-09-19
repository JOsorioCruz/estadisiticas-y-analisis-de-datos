"""Carga y validación de la hoja DATOS del Anexo 1 (Actividad No 2, AF17401)."""
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent.parent
RUTA_ANEXO = BASE / "Anexo 1 - Base de datos .xlsx"
HOJA = "DATOS"

COLUMNAS_ESPERADAS = [
    "MUNICIPIO DEL SINIESTRO",
    "EDAD CONDUCTOR",
    "NÚMERO DE PERSONAS FALLECIDAS",
    "NÚMERO DE PERSONAS HERIDAS",
    "VELOCIDAD REGISTRADA (km/H)",
    "COSTO ACCIDENTE (MILLONES DE PESOS)",
    "NIVEL EDUCATIVO DEL CONDUCTOR",
    "AÑOS DE EXPERIENCIA DEL CONDUCTOR",
    "HISTÓRICO DE INFRACCIONES",
]
CUANTITATIVAS = [c for c in COLUMNAS_ESPERADAS if c not in (COLUMNAS_ESPERADAS[0], COLUMNAS_ESPERADAS[6])]


def cargar_datos(ruta: Path = RUTA_ANEXO) -> pd.DataFrame:
    """Lee la hoja DATOS tal cual está en el Anexo 1, sin transformar valores."""
    return pd.read_excel(ruta, sheet_name=HOJA, engine="openpyxl")


def validar(df: pd.DataFrame) -> None:
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    print("Encabezados iguales a los esperados:", list(df.columns) == COLUMNAS_ESPERADAS)
    print("\nTipos:\n" + df.dtypes.to_string())
    print("\nNulos por columna:\n" + df.isna().sum().to_string())
    print("\nFilas repetidas (excedentes):", int(df.duplicated().sum()))
    print("Filas que pertenecen a algún grupo repetido:", int(df.duplicated(keep=False).sum()))
    for col in (COLUMNAS_ESPERADAS[0], COLUMNAS_ESPERADAS[6]):
        print(f"\n{col}:\n" + df[col].value_counts().to_string())
        print("Espacios sobrantes:", int((df[col] != df[col].str.strip()).sum()))
    print("\nRangos de variables cuantitativas:")
    resumen = df[CUANTITATIVAS].agg(["min", "max", "nunique"]).T
    print(resumen.to_string())


if __name__ == "__main__":
    validar(cargar_datos())
