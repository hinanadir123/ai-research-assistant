import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Create the client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Ask the user for a question
question = input("Ask me anything: ")

# Send the question to the AI
response = client.chat.completions.create(
    model="cohere/north-mini-code:free",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

# Print the AI's answer
print("\nAI Response:\n")
print(response.choices[0].message.content)