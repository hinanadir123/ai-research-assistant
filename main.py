import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SYSTEM_PROMPT

# Load variables from .env
load_dotenv()

# Create the client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

messages = [
    {
        "role": "system",
        "content": "SYSTEM_PROMPT"
    }
]

# Ask the user for a question
while True:
    question = input("\nYou: ")
    if not question.strip():
       print("Please enter a question.")
       continue
    if question.lower() == "quit":
       print("Goodbye!")
       break
    messages.append(
    {
        "role": "user",
        "content": question
    }
)

# Send the question to the AI
    response = client.chat.completions.create(
        model="cohere/north-mini-code:free",
        messages=messages
    )

# Print the AI's answer
    ai_reply = response.choices[0].message.content

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    print("\nAI:")
    print(ai_reply)