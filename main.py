
import os
import tempfile
import gradio as gr

from speech_to_text import transcribe_with_groq
from ai_agent import ask_agent
from text_to_speech import text_to_speech_with_elevenlabs


def chat(audio, image):

    # No audio provided
    if audio is None:
        return "", "Please record your voice.", None

    try:
        # Speech to text
        user_text = transcribe_with_groq(audio)

        print("\\nYOU:", user_text)

        if not user_text:
            return "", "No speech detected.", None

        # Ask AI agent
        response = ask_agent(
            user_query=user_text,
            image_path=image
        )

        print("\\nDORA:", response)

        # Temporary MP3 file (important for Render)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            output_audio = tmp.name

        # Text to speech
        text_to_speech_with_elevenlabs(
            response,
            output_audio
        )

        return user_text, response, output_audio

    except Exception as e:
        print("ERROR:", e)
        return "", f"Error: {str(e)}", None


with gr.Blocks(
    title="🤖 Dora AI Assistant",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown(
        """
# 🤖 Dora AI Assistant

### 🎤 Speak your question

### 📷 Upload an image only if your question is about objects or surroundings

**Examples:**

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
            sources=["upload", "webcam"],
            type="filepath",
            label="📷 Upload or Capture Image"
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
        inputs=[audio, image],
        outputs=[user_box, ai_box, output_audio]
    )

    clear.click(
        lambda: (None, None, "", "", None),
        outputs=[audio, image, user_box, ai_box, output_audio]
    )


# IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False
    )
