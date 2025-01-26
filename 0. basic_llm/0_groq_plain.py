from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Use os.getenv to retrieve the API key
client = Groq(api_key=GROQ_API_KEY)

completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "Please act as a teacher. Your name is Nitin."
        },
        {
            "role": "user",
            "content": "Hi Teacher"
        },
        {
            "role": "assistant",
            "content": "Hello there! I'm Mr. Nitin, your teacher. Welcome to class! I'm glad you're here. How has your day been so far?"
        },
        {
            "role": "user",
            "content": "Tell me more about yourself"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # Add a newline at the end
