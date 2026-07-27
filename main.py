import time
import pygame
import gradio as gr

from speech_to_text import (
    record_audio,
    transcribe_with_groq
)

from ai_agent import ask_agent

from text_to_speech import (
    text_to_speech_with_elevenlabs
)

audio_filepath = "audio_question.mp3"
output_audio = "final.mp3"

def play_audio(file_path):

    try:

        pygame.mixer.init()

        pygame.mixer.music.load(file_path)

        pygame.mixer.music.play()

        print(f"\n🔊 Playing : {file_path}")

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()

    except Exception as e:

        print("Audio Error :", e)

def voice_chat():

    try:

        # Record Audio
        record_audio(audio_filepath)

        # Speech To Text
        user_text = transcribe_with_groq(audio_filepath)

        print("\n======================")
        print("YOU :", user_text)
        print("======================")

        if not user_text:

            return "", "No speech detected.", None

        # Ask AI
        response = ask_agent(user_text)

        print("\n======================")
        print("DORA :", response)
        print("======================")

        # Text To Speech
        text_to_speech_with_elevenlabs(
            response,
            output_audio
        )

        return (
            user_text,
            response,
            output_audio
        )

    except Exception as e:

        return "", str(e), None

# ==========================================================
# Gradio Frontend
# ==========================================================

with gr.Blocks(
    title="🤖 Dora AI Assistant",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown(
        """
# 🤖 Dora AI Assistant

### 🎤 Click **Start Recording** and ask your question.

- 💬 Short answers by default
- 📷 Webcam opens automatically for image questions
- 🔊 AI replies with voice
"""
    )

    with gr.Row():

        user_box = gr.Textbox(
            label="🎤 You",
            lines=3,
            interactive=False
        )

        ai_box = gr.Textbox(
            label="🤖 Dora",
            lines=5,
            interactive=False
        )

    audio_box = gr.Audio(
        label="🔊 AI Voice",
        autoplay=True
    )

    record_btn = gr.Button(
        "🎤 Start Recording",
        variant="primary",
        size="lg"
    )

    clear_btn = gr.Button(
        "🗑 Clear"
    )

    record_btn.click(
        fn=voice_chat,
        outputs=[
            user_box,
            ai_box,
            audio_box
        ]
    )

    clear_btn.click(
        lambda: ("", "", None),
        outputs=[
            user_box,
            ai_box,
            audio_box
        ]
    )

demo.launch(
    server_name="127.0.0.1",
    server_port=7860,
    share=False,
    inbrowser=True
) 


# import os
# from speech_to_text import record_audio, transcribe_with_groq
# from ai_agent import ask_agent
# from text_to_speech import text_to_speech_with_elevenlabs
# import pygame
# import time

# audio_filepath = "audio_question.mp3"

# def play_audio(file_path):
#     try:
#         pygame.mixer.init()
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#         print(f"🔊 Playing: {file_path}")
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.quit()
#     except Exception as e:
#         print(f"Could not play audio, but file saved: {e}")
#         print(f"Aap {file_path} ko manually open karke sun sakte ho")

# def process_audio_and_chat():
#     while True:
#         try:
#             record_audio(file_path=audio_filepath)
#             user_input = transcribe_with_groq(audio_filepath)

#             print(f"\nYou: {user_input}")
#             if not user_input:
#                 continue
#             if "goodbye" in user_input.lower():
#                 print("Goodbye!")
#                 break

#             response = ask_agent(user_query=user_input)
#             print(f"Doctor: {response}")

#             # Voice banao (ElevenLabs fail hoga to gTTS banega)
#             text_to_speech_with_elevenlabs(response, "final.mp3")
            
#             # Ab bajao
#             play_audio("final.mp3")

#         except Exception as e:
#             print(f"Error: {e}")


# #code for frontend
# import gradio as gr
# from speech_to_text import record_audio, transcribe_with_groq
# from ai_agent import ask_agent
# from text_to_speech import text_to_speech_with_elevenlabs

# audio_filepath = "audio_question.mp3"


# def chat():
#     # Record Audio
#     record_audio(file_path=audio_filepath)

#     # Speech To Text
#     user_input = transcribe_with_groq(audio_filepath)

#     if not user_input:
#         return "", "No speech detected.", None

#     # AI Response
#     response = ask_agent(user_input)

#     # Text To Speech
#     output_audio = text_to_speech_with_elevenlabs(
#         response,
#         "final.mp3"
#     )

#     return user_input, response, output_audio


# with gr.Blocks(title="🤖 Dora AI Assistant") as demo:

#     gr.Markdown(
#         """
#         # 🤖 Dora AI Assistant

#         Click **Start Recording** and ask anything.

#         Image-related questions will automatically open the webcam.
#         """
#     )

#     with gr.Row():

#         user_box = gr.Textbox(
#             label="🎤 You",
#             lines=3
#         )

#         ai_box = gr.Textbox(
#             label="🤖 Dora",
#             lines=5
#         )

#     audio = gr.Audio(
#         label="🔊 AI Voice",
#         autoplay=True
#     )

#     btn = gr.Button(
#         "🎤 Start Recording",
#         variant="primary"
#     )

#     btn.click(
#         fn=chat,
#         outputs=[
#             user_box,
#             ai_box,
#             audio
#         ]
#     )

# demo.launch()