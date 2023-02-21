import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
  prompt="festival gay de perros y gatos en africa",
  n=2,
  size="1024x1024"
)
print(response)