import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="Juego de Preguntas y Respuestas",
    page_icon="❓",
    layout="centered"
)

# Estilo personalizado para tema oscuro
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-message {
        color: #4CAF50;
        font-size: 1.2em;
        font-weight: bold;
    }
    .question-container {
        background-color: #2D2D2D;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

def obtener_pregunta():
    """Retorna una pregunta aleatoria de cultura general"""
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "respuesta": "paris"
        },
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "respuesta": "1939"
        },
        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "respuesta": "amazonas"
        },
        {
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "respuesta": "leonardo da vinci"
        },
        {
            "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
            "respuesta": "jupiter"
        }
    ]
    return random.choice(preguntas)

def main():
    st.title("🎮 Juego de Preguntas y Respuestas")
    st.markdown("""
    ### ¡Bienvenido al juego!
    Por cada respuesta correcta ganarás premios en pesos argentinos.
    ¡Buena suerte!
    """)

    # Inicializar el estado de la sesión
    if 'preguntas_usadas' not in st.session_state:
        st.session_state.preguntas_usadas = []
    if 'premio_total' not in st.session_state:
        st.session_state.premio_total = 0
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = obtener_pregunta()
    if 'mostrar_respuesta' not in st.session_state:
        st.session_state.mostrar_respuesta = False

    # Mostrar la pregunta actual
    with st.container():
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.write(f"**Pregunta:** {st.session_state.pregunta_actual['pregunta']}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Input para la respuesta
    respuesta = st.text_input("Tu respuesta:", key="respuesta_input").strip().lower()

    # Botón para verificar la respuesta
    if st.button("Verificar respuesta"):
        if respuesta == st.session_state.pregunta_actual['respuesta']:
            premio = 1000 * (len(st.session_state.preguntas_usadas) + 1)
            st.session_state.premio_total += premio
            st.markdown(f'<div class="success-message">¡Correcto! Has ganado {premio} pesos argentinos</div>', unsafe_allow_html=True)
        else:
            st.error(f"Incorrecto. La respuesta correcta era: {st.session_state.pregunta_actual['respuesta']}")

        # Obtener nueva pregunta
        st.session_state.preguntas_usadas.append(st.session_state.pregunta_actual)
        st.session_state.pregunta_actual = obtener_pregunta()
        st.experimental_rerun()

    # Mostrar premio total
    st.markdown(f"### Premio total acumulado: {st.session_state.premio_total} pesos argentinos")

if __name__ == "__main__":
    main() 