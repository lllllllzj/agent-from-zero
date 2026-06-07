import os

from dotenv import load_dotenv
from google import genai
from openai import OpenAI

load_dotenv()

client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat_gemini = client_gemini.chats.create(model="gemini-2.5-flash")

client_groq = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
