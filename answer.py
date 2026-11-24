
import os
from dotenv import load_dotenv
from groq import Groq
from retrieve import retrieve

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

question = "What are the main steps involved in the RAG pipeline?"

top_chunks = retrieve(question)
context = "\n\n".join(top_chunks)

prompt = f"""Answer using ONLY the context below.
If the answer isn't in the context, say so.

Context:
{context}

Question: {question}"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
)

print("Question:", question)
print("Answer:", response.choices[0].message.content)

