import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Read the API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Make sure it's set in the .env file.")

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)

# Let user optionally set temperature
try:
    temperature = float(input("Set temperature (e.g. 0.2 for focused, 0.9 for creative): ") or "0.7")
except ValueError:
    temperature = 0.7
    print("Invalid input, using default temperature = 0.7")

# Start Gemini chat session
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat(history=[])

print("\nGemini Chat Started! Type 'exit' to quit.\n")

turn = 1
while True:
    user_input = input(f"User ({turn}): ")
    if user_input.strip().lower() == "exit":
        break

    response = chat.send_message(user_input, generation_config={"temperature": temperature})
    print(f"\nGemini ({turn}): {response.text}\n")
    turn += 1
