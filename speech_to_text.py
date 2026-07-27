import os
import time
import logging
from io import BytesIO

import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
from dotenv import load_dotenv
from groq import Groq

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================================
# FFmpeg Setup
# ==========================================

ffmpeg = which("ffmpeg")
ffprobe = which("ffprobe")

if ffmpeg is None:
    ffmpeg = r"C:\Users\Acer\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"

if ffprobe is None:
    ffprobe = r"C:\Users\Acer\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin\ffprobe.exe"

AudioSegment.converter = ffmpeg
AudioSegment.ffprobe = ffprobe

print("FFmpeg :", AudioSegment.converter)
print("FFprobe:", AudioSegment.ffprobe)

# ==========================================
# Record Audio
# ==========================================

def record_audio(
    file_path="audio_question.mp3",
    timeout=10,
    phrase_time_limit=15
):

    recognizer = sr.Recognizer()

    # Better microphone settings
    recognizer.energy_threshold = 150
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.7
    recognizer.non_speaking_duration = 0.4

    try:

        with sr.Microphone(sample_rate=16000) as source:

            print("\n🎤 Adjusting microphone...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("✅ Speak now...\n")

            # Small delay to avoid cutting first words
            time.sleep(0.5)

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

            print("✅ Recording Finished")

            wav_data = audio.get_wav_data()

            audio_segment = AudioSegment.from_wav(
                BytesIO(wav_data)
            )

            print(
                f"Recorded Length : {len(audio_segment)/1000:.2f} seconds"
            )

            audio_segment.export(
                file_path,
                format="mp3",
                bitrate="128k"
            )

            if os.path.exists(file_path):
                logging.info(f"Saved : {file_path}")
                return file_path

            raise Exception("Audio file not created.")

    except sr.WaitTimeoutError:
        print("❌ No speech detected.")
        return None

    except Exception as e:
        print("Recording Error :", e)
        return None


# ==========================================
# Speech To Text (Groq Whisper)
# ==========================================

def transcribe_with_groq(audio_path):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise Exception("❌ GROQ_API_KEY not found")

    client = Groq(api_key=api_key)

    with open(audio_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            language="en",
            temperature=0,
            prompt=(
                "This is an English voice assistant. "
                "Accurately recognize complete questions. "
                "Do not omit words like who, what, where, when, why, how, current."
            ),
            response_format="text"
        )

    print("\n==============================")
    print("RAW TRANSCRIPT:")
    print(repr(transcription))
    print("==============================\n")

    return transcription.strip()


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    audio = record_audio()

    if audio:

        print("\nUploading to Groq...\n")

        text = transcribe_with_groq(audio)

        print("\nRecognized Text:")
        print(text)