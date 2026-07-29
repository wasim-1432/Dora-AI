from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import analyze_image_with_query

load_dotenv()

# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.2,
)

# =====================================================
# Vision Keywords
# =====================================================

VISION_KEYWORDS = [

    # Camera / Image
    "see",
    "look",
    "image",
    "photo",
    "picture",
    "camera",
    "webcam",

    # Counting
    "count",
    "how many",
    "number of",

    # Objects
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
    "glass",
    "cup",
    "chair",
    "table",

    # Holding
    "hand",
    "holding",
    "carry",

    # People
    "person",
    "people",
    "face",
    "shirt",
    "dress",
    "wearing",

    # Position
    "behind",
    "front",
    "around",

    # Vision Tasks
    "identify",
    "recognize",
    "detect",
    "describe",

    "visible"
]

# =====================================================
# Vision Detector
# =====================================================

def needs_vision(query: str):

    query = query.lower()

    print("\nTranscript :", query)

    for keyword in VISION_KEYWORDS:

        if keyword in query:

            print(f"📷 Vision Keyword Found : {keyword}")

            return True

    return False


# =====================================================
# Text LLM Prompt
# =====================================================

SYSTEM_PROMPT = """
You are Dora AI Assistant.

Rules:

1. Give short and direct answers.

2. Do NOT explain unless the user asks:
   explain
   why
   how
   details
   elaborate

3. Answer factual questions in one sentence.

Examples

User:
Who is the Prime Minister of India?

Assistant:
Narendra Modi.

User:
Capital of India?

Assistant:
New Delhi.

User:
Explain Python.

Assistant:
(Provide a detailed explanation.)

User:
What is AI?

Assistant:
Artificial Intelligence is the simulation of human intelligence by machines.
"""

# =====================================================
# Main AI Function
# =====================================================


# =====================================================
# Main Ask Agent Function
# =====================================================

def ask_agent(user_query: str, image_path: str = None):

    # Vision query
    if image_path and needs_vision(user_query):
        return analyze_image_with_query(user_query, image_path)

    # Normal text query
    prompt = f"""
You are Dora AI Assistant.

Reply naturally, clearly, and briefly.
Do not use markdown or bullet points unless necessary.

User: {user_query}
Assistant:
"""

    response = llm.invoke(prompt)

    return response.content.strip()



# def ask_agent(user_query: str, image_path=None):

#     print("=" * 60)
#     print("Question :", user_query)

#     # -------------------------------------------------
#     # Vision Question
#     # -------------------------------------------------

#     if needs_vision(user_query):

#         if image_path is None:

#             return (
#                 "Please capture or upload an image "
#                 "for this question."
#             )

#         print("📷 Using Browser Image")

#         return analyze_image_with_query(
#             user_query,
#             image_path
#         )

#     # -------------------------------------------------
#     # Text Question
#     # -------------------------------------------------

#     print("💬 Text Question")

#     messages = [

#         ("system", SYSTEM_PROMPT),

#         ("human", user_query)

#     ]

#     response = llm.invoke(messages)

#     return response.content.strip()


# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    while True:

        query = input("\nYou : ")

        if query.lower() == "exit":
            break

        print(
            ask_agent(
                query
            )
        )
