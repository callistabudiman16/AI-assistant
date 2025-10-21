import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = 'AIzaSyC4ioUQI4FaleKIYojxIFHybg8zhDCpS8o'
if not api_key:
    print("Please set your GOOGLE_API_KEY in a .env file or as an environment variable")
    print("You can get an API key from: https://ai.google.dev/gemini-api/docs/api-key")
    exit(1)

genai.configure(api_key=api_key)

# List available models first
print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")

# Create the model with a proper text generation model
model_name = "gemini-2.5-flash"  # Use a stable model
print(f"\nUsing model: {model_name}")
model = genai.GenerativeModel(model_name)

# Generate content using the prompt template
with open('prompt_template_test.txt', 'r', encoding='utf-8') as file:
    prompt_content = file.read()

response = model.generate_content(prompt_content)
print(f"\nResponse: {response.text}")