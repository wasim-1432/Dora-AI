import os
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Rachel

def text_to_speech_with_elevenlabs(text, output_filepath):
    try:
        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            text=text,
            model_id="eleven_multilingual_v2",
            output_format="mp3_22050_32"
        )
        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        print(f"Audio saved: {output_filepath}")
        return output_filepath
    except Exception as e:
        print(f"ElevenLabs Error (402 ayega to gTTS use hoga): {e}")
        # Agar 402 Payment error aaye to gTTS se kaam chalao
        return text_to_speech_with_gtts(text, output_filepath)

def text_to_speech_with_gtts(text, output_filepath):
    from gtts import gTTS
    print("Using gTTS (Free)...")
    tts = gTTS(text=text, lang='en')
    tts.save(output_filepath)
    return output_filepath



# import os
# import subprocess
# import platform

# from dotenv import load_dotenv
# from elevenlabs.client import ElevenLabs
# from elevenlabs import save
# from gtts import gTTS

# load_dotenv()

# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")


# # -----------------------------
# # Play Audio
# # -----------------------------
# def play_audio(file_path):

#     os_name = platform.system()

#     try:

#         if os_name == "Windows":

#             # ffplay (FFmpeg) required
#             subprocess.run(
#                 [
#                     "ffplay",
#                     "-nodisp",
#                     "-autoexit",
#                     file_path
#                 ],
#                 stdout=subprocess.DEVNULL,
#                 stderr=subprocess.DEVNULL,
#             )

#         elif os_name == "Darwin":

#             subprocess.run(["afplay", file_path])

#         elif os_name == "Linux":

#             subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path])

#         else:

#             print("Unsupported OS")

#     except Exception as e:

#         print("Unable to play audio:", e)


# # -----------------------------
# # ElevenLabs TTS
# # -----------------------------
# def text_to_speech_with_elevenlabs(text, output_file):

#     if not ELEVENLABS_API_KEY:
#         raise Exception(
#             "ELEVENLABS_API_KEY not found in .env file."
#         )

#     client = ElevenLabs(
#         api_key=ELEVENLABS_API_KEY
#     )

#     audio = client.text_to_speech.convert(

#         VOICE_ID = "21m00Tcm4TlvDq8ikWAM" ,

#         model_id="eleven_multilingual_v2",

#         text=text,

#         output_format="mp3_22050_32",

#     )

#     save(audio, output_file)

#     print("Saved :", output_file)

#     play_audio(output_file)


# # -----------------------------
# # Google TTS
# # -----------------------------
# def text_to_speech_with_gtts(text, output_file):

#     tts = gTTS(

#         text=text,

#         lang="en",

#         slow=False,

#     )

#     tts.save(output_file)

#     print("Saved :", output_file)

#     play_audio(output_file)


# # -----------------------------
# # Main
# # -----------------------------
# if __name__ == "__main__":

#     input_text = input("Enter Text : ")

#     output_file = "output.mp3"

#     try:

#         print("\nUsing ElevenLabs...\n")

#         text_to_speech_with_elevenlabs(

#             input_text,

#             output_file,

#         )

#     except Exception as e:

#         print("\nElevenLabs Error:")

#         print(e)

#         print("\nSwitching to Google TTS...\n")

#         text_to_speech_with_gtts(

#             input_text,

#             output_file,

#         )