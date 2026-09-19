"""Copia exacta de la hoja DATOS del Anexo 1 dentro de un libro de xlsxwriter."""
import xlsxwriter.utility as xu

HOJA = "DATOS"


def escribir_datos(wb, df, nombre=HOJA):
    ws = wb.add_worksheet(nombre)
    negrita = wb.add_format({"bold": True})
    ws.write_row(0, 0, list(df.columns), negrita)
    for i, fila in enumerate(df.itertuples(index=False), start=1):
        for j, valor in enumerate(fila):
            ws.write(i, j, valor.item() if hasattr(valor, "item") else valor)
    return ws


def rango(df, columna, hoja=HOJA):
    """Referencia absoluta de la columna de datos, por ejemplo DATOS!$E$2:$E$401."""
    letra = xu.xl_col_to_name(list(df.columns).index(columna))
    return f"{hoja}!${letra}$2:${letra}${len(df) + 1}"
