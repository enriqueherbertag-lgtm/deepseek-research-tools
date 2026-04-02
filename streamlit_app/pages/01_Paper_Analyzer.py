import streamlit as st
import sys
import os

# Agregar el directorio raíz al path para importar deepseek_tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from deepseek_tools.paper_analyzer import analyze_paper

st.set_page_config(page_title="Analizador de Papers", page_icon="📄")
st.title("📄 Analizador de Papers Académicos")
st.caption("Extrae contribuciones clave, metodologías y limitaciones usando DeepSeek")

# Entrada de texto
st.subheader("Texto del paper")
texto = st.text_area(
    "Pega el resumen (abstract) o el texto completo del paper",
    height=250,
    placeholder="Ejemplo: En este estudio investigamos el efecto de...",
    help="Puedes pegar el abstract, la introducción o cualquier sección que quieras analizar."
)

# URL opcional
st.subheader("URL (opcional)")
url = st.text_input(
    "Ingresa la URL del paper (PDF o página)",
    placeholder="https://arxiv.org/abs/xxxx.xxxxx",
    help="Funcionalidad en desarrollo. Por ahora solo funciona con texto pegado."
)

# Botón de análisis
if st.button("🔍 Analizar paper", type="primary"):
    if texto.strip():
        with st.spinner("Analizando con DeepSeek... Esto puede tomar unos segundos."):
            try:
                resultado = analyze_paper(texto)
                
                st.success("Análisis completado")
                
                # Mostrar resultados
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📌 Contribuciones clave")
                    st.write(resultado.get("contribuciones", "No se detectaron"))
                    
                    st.subheader("🔬 Metodología")
                    st.write(resultado.get("metodologia", "No se detectó"))
                
                with col2:
                    st.subheader("⚠️ Limitaciones")
                    st.write(resultado.get("limitaciones", "No se detectaron"))
                    
                    st.subheader("🏷️ Palabras clave")
                    st.write(resultado.get("keywords", "No se detectaron"))
                
                # Mostrar JSON completo en expander
                with st.expander("Ver respuesta completa (JSON)"):
                    st.json(resultado)
                    
            except Exception as e:
                st.error(f"Error al analizar: {e}")
                st.info("Verifica que la API key de DeepSeek esté configurada correctamente.")
    elif url.strip():
        st.info("Funcionalidad de análisis por URL está en desarrollo. Por ahora, pega el texto directamente.")
    else:
        st.warning("Por favor, ingresa el texto del paper o una URL para analizar.")

st.divider()
st.caption("Herramienta basada en `deepseek_tools.paper_analyzer`. Los resultados son generados por IA y deben ser verificados.")
