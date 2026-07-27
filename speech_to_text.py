import os
from dotenv import load_dotenv
from groq import Groq

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()


# ==========================================
# Speech To Text (Groq Whisper)
# ==========================================

def transcribe_with_groq(audio_path: str) -> str:
    """
    Transcribes an audio file using Groq Whisper.

    Parameters:
        audio_path (str): Path to the audio file received from Gradio.

    Returns:
        str: Transcribed text.
    """

    if audio_path is None:
        return ""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise Exception("❌ GROQ_API_KEY not found in .env")

    client = Groq(api_key=api_key)

    print("\n🎤 Uploading audio to Groq Whisper...")
    print("Audio File:", audio_path)

    with open(audio_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            language="en",
            temperature=0,
            prompt=(
                "This is a voice assistant. "
                "Recognize English accurately. "
                "Return only the spoken words. "
                "Do not add explanations."
            ),
            response_format="text",
        )

    text = transcription.strip()

    print("\n==============================")
    print("Recognized Text:")
    print(text)
    print("==============================\n")

    return text


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    audio_file = input("Enter audio file path: ").strip()

    if os.path.exists(audio_file):

        result = transcribe_with_groq(audio_file)

        print("\nFinal Text:")
        print(result)

    else:
        print("❌ File not found.")
