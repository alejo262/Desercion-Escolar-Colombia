"""Tablero HTML de deserción escolar alojado en Streamlit."""
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(
    page_title="Deserción escolar en Colombia",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with st.expander("Descargar el documento y consultar el proyecto"):
    cols = st.columns(3)
    files = [
        ("Documento del proyecto", "Proyecto-BI-2026-2.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        ("Notebook de preparación", "Desercion-Escolar-Colombia.ipynb", "application/x-ipynb+json"),
        ("Tablero HTML", "Desercion-Escolar-Colombia.html", "text/html"),
    ]
    for col, (label, filename, mime) in zip(cols, files):
        col.download_button(label, (ROOT / filename).read_bytes(), file_name=filename, mime=mime)
    st.link_button("Repositorio en GitHub", "https://github.com/alejo262/Desercion-Escolar-Colombia")

st.iframe(
    ROOT / "Desercion-Escolar-Colombia.html",
    width="stretch",
    height="content",
    alt="Tablero interactivo de deserción escolar en Colombia con filtros de año, territorio y rango",
)
