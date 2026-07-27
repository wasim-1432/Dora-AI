import os
import tempfile
import gradio as gr

from speech_to_text import transcribe_with_groq
from ai_agent import ask_agent
from text_to_speech import text_to_speech_with_elevenlabs


def chat(audio, image):

    if audio is None:
        return "", "Please record your voice.", None

    # audio is a filepath from browser
    user_text = transcribe_with_groq(audio)

    print("\nYOU :", user_text)

    if not user_text:
        return "", "No speech detected.", None

    response = ask_agent(
        user_query=user_text,
        image_path=image
    )

    print("\nDORA :", response)

    output_audio = "final.mp3"

    text_to_speech_with_elevenlabs(
        response,
        output_audio
    )

    return (
        user_text,
        response,
        output_audio
    )


with gr.Blocks(
    title="🤖 Dora AI Assistant",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown(
        """
# 🤖 Dora AI Assistant

### 🎤 Speak your question.

### 📷 Upload an image only if your question is about objects or surroundings.

Examples:

- Who is the Prime Minister of India?
- What is AI?
- How many pens are in my hand?
- What colour is my shirt?
"""
    )

    with gr.Row():

        audio = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="🎤 Microphone"
        )

        image = gr.Image(
            type="filepath",
            label="📷 Optional Image"
        )

    user_box = gr.Textbox(
        label="You",
        interactive=False
    )

    ai_box = gr.Textbox(
        label="Dora",
        lines=6,
        interactive=False
    )

    output_audio = gr.Audio(
        label="🔊 Dora Voice",
        autoplay=True
    )

    with gr.Row():

        submit = gr.Button(
            "🚀 Ask Dora",
            variant="primary"
        )

        clear = gr.Button("🗑 Clear")

    submit.click(
        fn=chat,
        inputs=[
            audio,
            image
        ],
        outputs=[
            user_box,
            ai_box,
            output_audio
        ]
    )

    clear.click(
        lambda: (
            None,
            None,
            "",
            "",
            None
        ),
        outputs=[
            audio,
            image,
            user_box,
            ai_box,
            output_audio
        ]
    )

demo.launch()
