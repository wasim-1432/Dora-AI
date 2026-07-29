import os
import re
from PIL import Image
import google.generativeai as genai


# ==========================================
# Gemini Configuration
# ==========================================

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# ==========================================
# Vision Analysis
# ==========================================

def analyze_image_with_query(query: str, image_path: str) -> str:

    if image_path is None:
        return "📷 Please keep the object visible to the camera."

    try:
        print("\\n📷 Sending image to Gemini Vision...")

        image = Image.open(image_path)

        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are Dora AI Vision Assistant.

Rules:
- Reply only to the user's question.
- Maximum 12 words.
- Do not explain reasoning.
- Count objects carefully.
- If unsure, say: I am not sure.

User question: {query}
"""

        response = model.generate_content([prompt, image])

        answer = response.text.strip() if response.text else "I am not sure."

        # Remove markdown if any
        answer = re.sub(r"[*_#]", "", answer).strip()

        print("\\nVision Response:")
        print(answer)

        return answer

    except Exception as e:
        print(f"❌ Vision Error: {e}")
        return f"❌ Vision error: {str(e)}"


