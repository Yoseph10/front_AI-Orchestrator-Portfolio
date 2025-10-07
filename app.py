import gradio as gr
import requests
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_GENAI")

conversation_history = []

def chat_web(user_input, usuario=None):
    global conversation_history
    if not user_input.strip():
        return conversation_history, ""

    params = {"user_input": user_input}
    if usuario:
        params["usuario"] = usuario

    try:
        response = requests.post(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        assistant_message = data["response"]

        user_avatar = f"👤 {usuario if usuario else 'Tú'}"
        ia_avatar = "🤖 IA"

        conversation_history.append((user_avatar, user_input))
        conversation_history.append((ia_avatar, assistant_message))

        return conversation_history, ""
    except Exception as e:
        return conversation_history, f"Error: {str(e)}"

def clear_history():
    global conversation_history
    conversation_history = []
    return [], ""

# CSS actualizado con un fondo más claro en el chat
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
body { font-family: 'Roboto', sans-serif; }

.gradio-container {
    background: #1e1e1e;
    color: #f5f5f5;
}

#main-title {
    color: #1e1e1e !important; /* Color de texto oscuro para que se vea sobre el fondo blanco */
    background-color: #ffffff; /* Fondo blanco para el recuadro */
    padding: 10px 20px; /* Espacio interior para que el texto no toque los bordes */
    border: 2px solid #607d8b; /* Borde del recuadro, puedes cambiar el color */
    border-radius: 8px; /* Esquinas redondeadas */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra sutil para darle profundidad */
    text-shadow: none; /* Eliminar la sombra de texto que ya no es necesaria */
    display: inline-block; /* Asegura que el recuadro se ajuste al contenido */
    font-size: 12px !important; /* Título más pequeño */
}

#chatbot {
    height: 550px !important;
    border-radius: 12px;
    background: #b6c7e3; /* Fondo del chat más claro */
    padding: 10px;
}

#instructions {
    background-color: #ffffff !important; /* Fondo blanco */
    color: #333333 !important; /* Texto oscuro */
    padding: 12px;
    border-radius: 8px;
    font-size: 10px; /* Letra más pequeña */
    line-height: 1.4;
}

.message.user {
    background-color: #ffffff !important;
    color: #ffffff !important;
    border-radius: 18px 18px 4px 18px !important;
    padding: 12px !important;
}

.message.bot {
    background-color: #ffffff !important;
    color: #ffffff !important;
    border-radius: 18px 18px 18px 4px !important;
    padding: 12px !important;
}

.gradio-textbox {
    border: 1px solid #444;
    background: #333;
    color: #f5f5f5;
    border-radius: 8px;
}

.gradio-button {
    border-radius: 8px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

.gradio-button.primary {
    background-color: #ff5722 !important;
    color: #ffffff !important;
}

.gradio-button.secondary {
    background-color: #607d8b !important;
    color: #ffffff !important;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("# 🤖⚡ Asistente de Portafolio IA de Yoseph Ayala", elem_id="main-title")

    # Caja de instrucciones inicial
    with gr.Group():
        gr.Markdown(
        """
        📱 ¡Bienvenido a mi Portafolio Inteligente usando IA!
        Según tu rol, puedes interactuar de diferentes formas:

        - 👔 **Reclutador**: Pregunta sobre mi experiencia, habilidades y proyectos.
          También puedes solicitar mi CV.

        - 💼 **Cliente**: Consulta sobre mis servicios profesiones
        y cómo puedo ayudarte a resolver tus necesidades. Además, puedes agendarme una reunión.

        - 🎓 **Alumno**: Explora los cursos en Ciencia de Datos e IA que ofrezco.
        """,
        elem_id="instructions"
        )

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label=" ", elem_id="chatbot", show_label=False)
        with gr.Column(scale=1):
            user_input = gr.Textbox(
                label="Mensaje",
                placeholder="Escribe tu mensaje...",
                lines=2,
            )
            usuario = gr.Textbox(
                label="Usuario (opcional)",
                placeholder="Tu nombre o ID",
                lines=1,
            )
            with gr.Row():
                submit_btn = gr.Button("Enviar ➡️", variant="primary")
                clear_btn = gr.Button("Limpiar 🗑️", variant="secondary")

    submit_btn.click(chat_web, inputs=[user_input, usuario], outputs=[chatbot, user_input])
    clear_btn.click(clear_history, outputs=[chatbot, user_input])

#demo.launch(share=True)

# Integrar Gradio con FastAPI
app = FastAPI()
app = gr.mount_gradio_app(app, demo, path="/")
