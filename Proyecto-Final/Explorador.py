# Dashboard_IMDb.py (en la raíz de tu proyecto)
import streamlit as st
import pandas as pd
import os

# --- Configuración de la página principal ---
st.set_page_config(
    page_title="Explorador General IMDb",
    page_icon="images/IMDB_Logo_2016.svg.png", # Puedes seguir usando un icono pequeño aquí
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función para cargar el CSS
def load_css(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))  # ruta absoluta del script actual
    file_path = os.path.join(current_dir, file_name)          # une la ruta con el nombre del archivo
    with open(file_path, encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Llama a la función para cargar tu archivo CSS
load_css("style.css")

with open("images/IMDB_Logo_2016.svg.png", "rb") as img_file:
    st.image(img_file, width=450)


st.title("Bienvenido al Explorador de IMDb")

st.header("¿Que es IMDb?")
st.markdown("""
IMDb (Internet Movie Database) es una plataforma en línea que ofrece información detallada y actualizada sobre películas, series de televisión, actores, directores y otros profesionales del entretenimiento. Reconocida mundialmente, permite a los usuarios consultar sinopsis, reparto, calificaciones, tráilers, críticas y listas de popularidad, siendo una herramienta clave tanto para cinéfilos como para profesionales de la industria audiovisual.
""")
st.markdown("---")
# --- Texto de Finalidad y Problemática ---
st.markdown("""
### **Propósito del Proyecto**

En la era digital, donde la oferta de películas y series es abrumadora, tomar decisiones informadas sobre qué ver puede ser un desafío. 
Este dashboard interactivo nace con la **finalidad de resolver estas interrogantes**, transformando una vasta cantidad de datos de IMDb en **conocimiento accesible y visual**. Nuestro objetivo es proporcionar una herramienta intuitiva que permita a los usuarios:

* **Explorar tendencias históricas:** Observar la evolución de las calificaciones y la popularidad de géneros específicos a lo largo de las décadas.
* **Comparar formatos:** Entender las diferencias en la recepción crítica y del público entre películas y series en un vistazo.
* **Identificar lo más destacado:** Descubrir rápidamente los títulos mejor valorados o con mayor impacto.

En resumen, este proyecto busca **democratizar el análisis de datos cinematográficos**, ofreciendo una perspectiva clara y dinámica para que cualquier persona pueda navegar por el universo de IMDb con mayor facilidad y obtener ideas para sus próximas noches de entretenimiento.
""")
st.markdown("---")
st.markdown("""
    #### **Para proceder a ver las visualizaciones, utiliza el menú lateral para navegar entre las diferentes secciones de análisis de datos de películas y series.**
    Aquí podrás encontrar:
    - **Visión General de Calificaciones:** Un vistazo a cómo se distribuyen las valoraciones.
    - **Episodios de series:** Un vistazo a la cantidad de episodios y temporadas de las series junto a su calificacion.
    - **Tendencias Temporales:** Cómo han cambiado las cosas a lo largo de los años.
""")
# Luego, el enlace a IMDb
st.sidebar.image("images/IMDB_Logo_2016.svg.png", width=280) # Ajusta el 'width' según necesites
st.sidebar.markdown("¡Explora más en la [Página Oficial de IMDb](https://www.imdb.com/)!")
# Nota: No hay código de visualización pesado aquí. Las visualizaciones van en las páginas.
