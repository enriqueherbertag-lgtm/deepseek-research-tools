import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

st.set_page_config(page_title="Asistente de Investigación", page_icon="💡")
st.title("💡 Asistente de Investigación")
st.caption("Ayuda con revisión de literatura, generación de hipótesis y diseño experimental")

# Inicializar historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola. Soy tu asistente de investigación. ¿En qué tema estás trabajando? Puedo ayudarte a revisar literatura, generar hipótesis o diseñar experimentos."}
    ]

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("Escribe tu pregunta o tema de investigación..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generar respuesta (placeholder - conectar con DeepSeek API)
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            # TODO: Conectar con la API real de DeepSeek
            # Por ahora, respuesta simulada
            respuesta = f"Estoy analizando tu consulta sobre: {prompt}\n\n[Esta es una respuesta simulada. Conecta con la API de DeepSeek para respuestas reales.]"
            st.markdown(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})
