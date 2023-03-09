import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def cost_a(response):
    json_obj = json.loads(response)
    a = json_obj['usage']
    print(a['prompt_tokens']*100)
    print(a['total_tokens']*30)
    # print(a[''])

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
