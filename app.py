"""Presenta el tablero HTML con los datos preparados del proyecto."""
from pathlib import Path
import base64
import json
import re
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent

def cargar_tablero():
    """Actualiza los datos y las descargas sin cambiar el diseño del HTML."""
    limpio = ROOT / "limpieza/datos_limpios.csv"
    datos = pd.read_csv(limpio, dtype={"c_digo_departamento": str})
    records = json.loads(datos.to_json(orient="records", force_ascii=False, double_precision=10))
    assets = {}
    for key, path, mime in [
        ("original", ROOT / "limpieza/datos_originales_men.csv", "text/csv;charset=utf-8"),
        ("clean", limpio, "text/csv;charset=utf-8"),
        ("notebook", ROOT / "Desercion-Escolar-Colombia.ipynb", "application/x-ipynb+json"),
    ]:
        assets[key] = {"name": path.name, "mime": mime, "base64": base64.b64encode(path.read_bytes()).decode()}
    html = (ROOT / "Desercion-Escolar-Colombia.html").read_text(encoding="utf-8")
    payload = "<script>const DATA=" + json.dumps(records, ensure_ascii=False, allow_nan=False).replace("</", "<\\/")
    payload += ";\nconst ASSETS=" + json.dumps(assets) + ";</script>"
    html, count = re.subn(r"<script>const DATA=.*?;</script>", lambda _: payload, html, count=1, flags=re.S)
    if count != 1:
        raise ValueError("No se encontró el bloque de datos del tablero HTML.")
    return html

if __name__ == "__main__":
    st.set_page_config(page_title="Deserción escolar en Colombia", page_icon="📊", layout="wide")
    st.iframe(
        cargar_tablero(),
        width="stretch",
        height="content",
        alt="Tablero interactivo de deserción escolar en Colombia con filtros de año, territorio y rango",
    )
