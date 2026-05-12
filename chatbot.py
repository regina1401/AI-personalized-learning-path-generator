import os

from groq import Groq
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

# ---------------- LOAD ENV ---------------- #

load_dotenv()

# ---------------- GROQ CLIENT ---------------- #

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- GREETING LIST ---------------- #

GREETINGS = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
]

# ---------------- RESPONSE FUNCTION ---------------- #

def generate_response(
    user_question,
    subject,
    weak_topics
):

    lower_question = user_question.lower().strip()

    # -------- GREETING HANDLING -------- #

    if lower_question in GREETINGS:

        return (
            "Hello! 👋\n\n"
            "I am your AI Learning Assistant.\n"
            f"How may I help you with {subject} today?"
        )

    # -------- MAIN PROMPT -------- #

    prompt = f"""
    {SYSTEM_PROMPT}

    Subject:
    {subject}

    Weak Topics:
    {weak_topics}

    Student Question:
    {user_question}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return completion.choices[0].message.content

# ---------------- TEST ---------------- #

if __name__ == "__main__":

    response = generate_response(
        "Explain deadlock",
        "Operating System",
        "Deadlock"
    )

    print(response)
