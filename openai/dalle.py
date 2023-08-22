import openai
import os

response = openai.Image.create(
  prompt="Holocausto",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)