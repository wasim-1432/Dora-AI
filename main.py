
import os
import tempfile
import gradio as gr

from speech_to_text import transcribe_with_groq
from ai_agent import ask_agent, needs_vision
from text_to_speech import text_to_speech_with_elevenlabs


# =====================================================
# Main Chat Function
# =====================================================

def process_query(audio, webcam_image):

    if audio is None:
        return "", "🎤 Listening... please speak.", None

    # Speech → Text
    user_text = transcribe_with_groq(audio)

    if not user_text:
        return "", "❌ No speech detected.", None

    print(f"\\nYOU: {user_text}")

    # Decide whether image is needed
    use_vision = needs_vision(user_text)

    if use_vision:
        if webcam_image is None:
            response = "📷 Please allow camera access and keep the object visible."
        else:
            response = ask_agent(
                user_query=user_text,
                image_path=webcam_image
            )
    else:
        response = ask_agent(
            user_query=user_text,
            image_path=None
        )

    print(f"\\nDORA: {response}")

    # Temporary audio output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        audio_path = tmp.name

    text_to_speech_with_elevenlabs(response, audio_path)

    return user_text, response, audio_path


# =====================================================
# Gradio UI
# =====================================================

with gr.Blocks(
    title="🤖 Dora AI Assistant",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown(
        """
# 🤖 Dora AI Assistant

### 🎙️ Just speak naturally

- **Who is the current Prime Minister of India?** → direct answer
- **What is AI?** → direct answer
- **How many pens are in my hand?** → camera image analysed automatically
- **What colour is my shirt?** → camera image analysed automatically

⚠️ Allow **Microphone** and **Camera** permissions when the browser asks.
        """
    )

    with gr.Row():

        # Microphone
        mic = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="🎤 Dora is Listening",
        )

        # Hidden webcam component
        webcam = gr.Image(
            sources=["webcam"],
            type="filepath",
            label="📷 Auto Camera",
            visible=True
        )

    user_box = gr.Textbox(
        label="🧑 You",
        interactive=False
    )

    ai_box = gr.Textbox(
        label="🤖 Dora",
        lines=5,
        interactive=False
    )

    voice_output = gr.Audio(
        label="🔊 Dora Voice",
        autoplay=True
    )

    # Auto-process when recording stops
    mic.stop_recording(
        fn=process_query,
        inputs=[mic, webcam],
        outputs=[user_box, ai_box, voice_output]
    )

    gr.Button("🗑️ Clear").click(
        lambda: (None, None, "", "", None),
        outputs=[mic, webcam, user_box, ai_box, voice_output]
    )


# =====================================================
# Render Deployment
# =====================================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False
    )

