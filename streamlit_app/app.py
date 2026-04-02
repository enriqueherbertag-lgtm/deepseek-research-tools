import streamlit as st

st.set_page_config(
    page_title="DeepSeek Research Tools",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 DeepSeek Research Tools")
st.caption("Asistente gráfico para investigación asistida por IA")

st.markdown("""
### Bienvenido

Esta es una interfaz gráfica para las herramientas de investigación que utilizan DeepSeek AI.

**Herramientas disponibles:**
- **Analizador de Papers:** Extrae contribuciones clave, metodologías y limitaciones de papers académicos.
- **Asistente de Investigación:** Ayuda con revisión de literatura y generación de hipótesis.

Selecciona una herramienta en el menú lateral para comenzar.
""")

st.info("💡 Las herramientas utilizan la API de DeepSeek. Asegúrate de tener configurada tu clave de API en el archivo `.env` o como variable de entorno.")
