import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt= str(input('Escriba la pregunta para Chat GPT:'))


def cost_a(response):
    json_obj = json.loads(response)

    ans = json_obj['choices']
    a = json_obj['usage']

    print('Prompt_tokens:',a['prompt_tokens'])
    print('Completion_tokens:' , a['completion_tokens'])
    print('Total_tokens:', a['total_tokens'])
    
    print('Answer:', ans[0]['text'])
    


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.5,
  max_tokens=1500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

cost_a(str(response))
