# Deserción escolar en Colombia 2011 a 2024

Proyecto integrador de Business Intelligence. El tablero permite explorar la deserción intraanual del sector oficial mediante filtros de año, territorio y rango. Sus gráficos, indicadores y frases se actualizan con la selección.

## Archivos

| Archivo | Contenido |
| --- | --- |
| `app.py` | Aplicación de Streamlit que presenta el tablero HTML y las descargas. |
| `Desercion-Escolar-Colombia.html` | Tablero autónomo con Chart.js, datos y notebook incorporados; también abre sin conexión. |
| `Desercion-Escolar-Colombia.ipynb` | Notebook diseñado por el equipo, adaptado con rutas relativas para reproducir la preparación. |
| `Proyecto-BI-2026-2.docx` | Documento del proyecto con fuente, diccionario, transformaciones y trazabilidad. |
| `datos/datos_originales_men.csv` | CSV original del MEN sin modificaciones. |
| `datos/preparados/` | CSV limpio y evidencias generadas por el notebook. |
| `herramientas/actualizar_tablero.py` | Actualiza los datos y las descargas incorporados en el HTML después de ejecutar el notebook. |

## Ejecución local

Desde la raíz del repositorio, con Python 3.12:

```bash
python -m venv .venv
```

Activa el entorno: en Windows, `.venv\Scripts\activate`; en macOS o Linux, `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

El tablero lee el HTML incluido en este repositorio. No depende del alojamiento anterior ni ejecuta la limpieza durante cada visita.

## Reproducir la preparación

Instala las dependencias de preparación con `python -m pip install -r requirements-notebook.txt`. Abre `Desercion-Escolar-Colombia.ipynb` con Jupyter desde la raíz del proyecto y ejecuta todas las celdas en orden. La entrada está en `datos/datos_originales_men.csv` y los resultados se guardan en `datos/preparados/`.

Después de modificar o ejecutar la preparación, sincroniza el HTML:

```bash
python herramientas/actualizar_tablero.py
```

Versiona juntos el notebook, los CSV preparados y el HTML para que los datos publicados coincidan con la evidencia. `app.py` publica el tablero; el notebook realiza la transformación de datos.

## Publicación en Streamlit Community Cloud

1. Sube estos archivos y carpetas a `alejo262/Desercion-Escolar-Colombia`, conservando su estructura.
2. Entra en https://share.streamlit.io/ con la cuenta de GitHub que tenga acceso al repositorio.
3. Elige **Create app** y la opción para una aplicación existente.
4. Selecciona el repositorio `alejo262/Desercion-Escolar-Colombia`, la rama `main` y el archivo `app.py`.
5. En **Advanced settings**, selecciona Python 3.12. No se necesitan contraseñas ni secretos para consultar estos datos públicos.
6. Publica con **Deploy** y verifica el tablero y las descargas. El enlace asignado termina en `.streamlit.app`.

Documentación: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Fuente y alcance

Ministerio de Educación Nacional, conjunto `ji8i-4anb`:
https://www.datos.gov.co/resource/ji8i-4anb.csv?$limit=50000

El corte incluye 462 registros de 33 territorios, entre 2011 y 2024. Las tasas preparadas se almacenan como proporciones; `0.0665` equivale a `6.65 %`. La variación interanual se expresa en puntos porcentuales. Baja: menos de 3 %; Media: de 3 % a 6 % inclusive; Alta: más de 6 %. Son umbrales del proyecto.

Los promedios son simples entre territorios y no equivalen a la tasa nacional oficial. Se conservan los nulos y las coberturas superiores a 100 %; las asociaciones no demuestran causalidad. La fuente advierte cifras preliminares para 2020.

La inteligencia artificial apoyó la construcción del tablero HTML y la revisión del documento. El equipo revisa los datos, el funcionamiento y la coherencia del trabajo antes de su entrega.
