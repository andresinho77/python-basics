import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def cost_a(response):
    json_obj = json.loads(response)
    print(json_obj['choices'])
    print(json_obj['usage'])

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="hacer un guion de una pelicula sobre un plan para robar un banco" ,
  temperature=0.5,
  max_tokens=1500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

cost_a(str(response))
