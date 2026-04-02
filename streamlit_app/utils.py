"""
Utilidades comunes para la interfaz Streamlit.
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_api_key():
    """Obtiene la API key de DeepSeek desde variables de entorno."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        # Intentar desde streamlit secrets
        try:
            import streamlit as st
            api_key = st.secrets.get("DEEPSEEK_API_KEY")
        except:
            pass
    return api_key

def check_api_key():
    """Verifica si la API key está configurada."""
    api_key = get_api_key()
    if not api_key:
        return False
    return True
