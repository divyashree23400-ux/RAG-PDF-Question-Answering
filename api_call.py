
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a concise coding assistant."
        },
        {
            "role": "user",
            "content": "Explain what a REST API is in 2 lines."
        }
    ],
    temperature=0.3
)

print(response.choices[0].message.content)
