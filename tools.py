import os
import re
import base64

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


# ==========================================
# Image to Base64
# ==========================================

def image_to_base64(image_path: str) -> str:
    """
    Converts image file into Base64 string.
    """

    if image_path is None:
        return None

    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")


# ==========================================
# Vision
# ==========================================

def analyze_image_with_query(query: str, image_path: str) -> str:

    if image_path is None:
        return "Please upload or capture an image."

    img_b64 = image_to_base64(image_path)

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    print("\n📷 Sending image to Groq Vision...")

    messages = [
        {
            "role": "system",
            "content": """
You are Dora AI Vision Assistant.

Rules:

1. Reply ONLY to the user's question.

2. Never explain your reasoning.

3. Never generate <think>.

4. Never describe the whole image unless asked.

5. Maximum answer length: 12 words.

6. Give direct answers.

7. Count objects accurately.

8. If unsure, simply say:
"I am not sure."

Examples

User:
How many pens are in my hand?

Assistant:
2 pens.

User:
How many people are there?

Assistant:
3 people.

User:
What am I holding?

Assistant:
2 pens.

User:
What colour is my shirt?

Assistant:
Blue.

User:
Is there anyone behind me?

Assistant:
Yes, one person.

User:
Describe the image.

Assistant:
(Only then briefly describe.)
"""
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_b64}"
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model="qwen/qwen3.5-vl-32b-instruct",
        messages=messages,
        temperature=0
    )

    answer = response.choices[0].message.content

    answer = re.sub(
        r"<think>.*?</think>",
        "",
        answer,
        flags=re.DOTALL
    ).strip()

    print("\nVision Response:")
    print(answer)

    return answer


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    image = input("Image Path : ").strip()
    question = input("Question   : ").strip()

    print(
        analyze_image_with_query(
            question,
            image
        )
    )
