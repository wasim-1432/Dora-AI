import cv2
import base64
from dotenv import load_dotenv

load_dotenv()

def capture_image() -> str:
    """
    Captures one frame from the default webcam, resizes it,
    encodes it as Base64 JPEG (raw string) and returns it.
    """
    print("Trying to open webcam...")
    for idx in range(4):
        cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
        if cap.isOpened():
            for _ in range(10):  # Warm up
                cap.read()
            ret, frame = cap.read()
            print("Image captured successfully.")
            cap.release()
            if not ret:
                continue
            cv2.imwrite("sample.jpg", frame)  # Optional
            ret, buf = cv2.imencode('.jpg', frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')
    raise RuntimeError("Could not open any webcam (tried indices 0-3)")


from groq import Groq

def analyze_image_with_query(query: str) -> str:
    """
    Expects a string with 'query'.
    Captures the image and sends the query and the image to
    to Groq's vision chat API and returns the analysis.
    """
    img_b64 = capture_image()
    model="qwen/qwen3.6-27b"
    
    if not query or not img_b64:
        return "Error: both 'query' and 'image' fields required."

    client=Groq()  
    messages = [
        {
            "role": "system",
            "content": """
    You are a camera vision assistant.

    STRICT RULES:
    1. Answer ONLY the user's question.
    2. Never explain your reasoning.
    3. Never output <think>, reasoning, analysis, or chain of thought.
    4. Never describe the whole image unless the user explicitly asks.
    5. Keep every answer under 10 words.
    6. Give direct answers only.
    7. If counting objects, reply only with the count.
    8. If uncertain, say "I am not sure."

    Examples:

    User: How many pens are in my hand?
    Assistant: 2 pens.

    User: How many people are there?
    Assistant: 3 people.

    User: What am I holding?
    Assistant: 2 pens.

    User: What color is my shirt?
    Assistant: Blue.

    User: Is anyone behind me?
    Assistant: Yes, one person.

    User: Is my laptop open?
    Assistant: Yes.

    User: Describe the image.
    Assistant: (Only then give a brief description.)
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
    print("Sending image to Groq Vision...")
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    import re

    response = chat_completion.choices[0].message.content

    response = re.sub(
        r"<think>.*?</think>",
        "",
        response,
        flags=re.DOTALL
    ).strip()

    return response

if __name__ == "__main__":
    query = "How many people do you see?"
    print(analyze_image_with_query(query))