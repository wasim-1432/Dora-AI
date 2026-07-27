from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import analyze_image_with_query

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.2,
)

# Words which usually need vision
VISION_KEYWORDS = [

    "see",
    "look",
    "image",
    "photo",
    "picture",
    "camera",
    "webcam",

    "count",
    "how many",
    "number of",

    "pen",
    "pens",
    "pencil",
    "bottle",
    "book",
    "mobile",
    "phone",
    "laptop",
    "mouse",
    "keyboard",
    "wallet",
    "bag",

    "hand",
    "holding",

    "person",
    "people",
    "face",
    "shirt",
    "dress",
    "wearing",

    "behind",
    "front",
    "around",

    "identify",
    "recognize",
    "detect",
    "describe",

    "visible"
]


def needs_vision(query: str):

    query = query.lower()

    print("Transcript :", query)

    for keyword in VISION_KEYWORDS:

        if keyword in query:
            print(f"Vision Keyword Found : {keyword}")
            return True

    return False


SYSTEM_PROMPT = """
You are Dora AI Assistant.

Answer briefly.

Do not explain unless the user asks.

Examples:

Q: Who is the Prime Minister of India?

A: Narendra Modi.

Q: Capital of India?

A: New Delhi.

Q: Explain Python.

A: (Detailed explanation)
"""


def ask_agent(user_query: str):

    print("=" * 60)
    print("Question :", user_query)

    if needs_vision(user_query):

        print("📷 Opening Webcam...")

        return analyze_image_with_query(user_query)

    print("💬 Text Question")

    messages = [

        ("system", SYSTEM_PROMPT),

        ("human", user_query)

    ]

    response = llm.invoke(messages)

    return response.content.strip()


if __name__ == "__main__":

    while True:

        q = input("You : ")

        if q.lower() == "exit":
            break

        print(ask_agent(q))