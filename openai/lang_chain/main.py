from click import prompt
from langchain import LLMChain
from langchain.llms import OpenAI
import os

davinci = OpenAI(model_name='text-davinci-003')
llm_chain = LLMChain(
    prompt=prompt,
    llm=davinci
)
print(llm_chain.run('Where is ibague located'))
