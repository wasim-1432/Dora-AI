import os
from gtts import gTTS


def text_to_speech_with_gtts(text, output_filepath):
    """Free fallback voice"""
    print("Using gTTS fallback...")
    tts = gTTS(text=text, lang="en")
    tts.save(output_filepath)
    return output_filepath


def text_to_speech_with_elevenlabs(text, output_filepath):
    """Use ElevenLabs if API key exists, otherwise use gTTS."""

    api_key = os.environ.get("ELEVENLABS_API_KEY")

    # If API key is missing
    if not api_key:
        print("No ElevenLabs API key found.")
        return text_to_speech_with_gtts(text, output_filepath)

    try:
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(api_key=api_key)

        VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel

        audio_stream = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            text=text,
            model_id="eleven_multilingual_v2",
            output_format="mp3_22050_32"
        )

        with open(output_filepath, "wb") as f:
            for chunk in audio_stream:
                if chunk:
                    f.write(chunk)

        print(f"Audio saved with ElevenLabs: {output_filepath}")
        return output_filepath

    except Exception as e:
        print(f"ElevenLabs Error: {e}")
        print("Falling back to gTTS...")
        return text_to_speech_with_gtts(text, output_filepath)
