"""Sincroniza el HTML con el CSV preparado y el notebook del proyecto."""
from pathlib import Path
import base64
import json
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def actualizar():
    csv = ROOT / 'datos/preparados/datos_limpios_powerbi.csv'
    datos = pd.read_csv(csv, dtype={'c_digo_departamento': str})
    requeridas = {'ano', 'c_digo_departamento', 'departamento', 'desercion', 'rango_desercion', 'variacion_interanual_pp'}
    if not requeridas.issubset(datos.columns):
        raise ValueError('El CSV preparado no tiene los campos requeridos por el tablero.')
    if datos.empty or datos.duplicated(['ano', 'c_digo_departamento']).any():
        raise ValueError('El CSV está vacío o tiene claves territorio-año duplicadas.')
    if (datos['desercion'].dropna() > 1).any() or (datos['desercion'].dropna() < 0).any():
        raise ValueError('La deserción debe estar almacenada como proporción entre 0 y 1.')
    records = json.loads(datos.to_json(orient='records', force_ascii=False, double_precision=10))
    assets = {}
    for key, path, mime in [
        ('original', ROOT / 'datos/datos_originales_men.csv', 'text/csv;charset=utf-8'),
        ('clean', csv, 'text/csv;charset=utf-8'),
        ('notebook', ROOT / 'Desercion-Escolar-Colombia.ipynb', 'application/x-ipynb+json'),
    ]:
        assets[key] = {'name': path.name, 'mime': mime, 'base64': base64.b64encode(path.read_bytes()).decode()}
    path = ROOT / 'Desercion-Escolar-Colombia.html'
    html = path.read_text(encoding='utf-8')
    payload = '<script>const DATA=' + json.dumps(records, ensure_ascii=False, allow_nan=False).replace('</', '<\\/')
    payload += ';\nconst ASSETS=' + json.dumps(assets) + ';</script>'
    html, count = re.subn(r'<script>const DATA=.*?;</script>', lambda _: payload, html, count=1, flags=re.S)
    if count != 1:
        raise ValueError('No se encontró el bloque de datos del tablero; no se modificó el archivo.')
    temporary = path.with_suffix('.html.tmp')
    temporary.write_text(html, encoding='utf-8')
    temporary.replace(path)
    print(f'Tablero actualizado: {len(records)} registros; notebook y CSV incorporados.')

if __name__ == '__main__':
    actualizar()
