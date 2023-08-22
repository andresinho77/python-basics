import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
  prompt="happy teenegers on a boat in the sea",
  n=2,
  size="1024x1024"
)
print(response)