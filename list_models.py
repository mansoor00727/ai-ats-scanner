import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models for your key:")
for m in client.models.list():
    if "generateContent" in m.supported_actions:
        print(f"-> {m.name}")
