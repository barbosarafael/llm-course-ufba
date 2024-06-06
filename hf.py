import os
from langchain_community.llms import HuggingFaceEndpoint
import time

os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'XXXXXXXXXXXXXXX'

model = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Meta-Llama-3-8B-Instruct',
    task = 'text-generation'
    )

response = model.invoke('Hello world!')
print(response)

#---- 2. mudar um pouco o prompt para tentar gerar respostas menores, mais contextualizadas

model = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Meta-Llama-3-8B-Instruct',
    task = 'text-generation'
    )

start_time = time.time()
response = model.invoke('Oi, você pode gerar um JSON sobre qualquer informação? Gere o texto em uma quantidade de linhas reduzida')
end_time = time.time()

elapsed_time = end_time - start_time

print(f'Resposta do modelo LangChain: {response}')
print(f'Tempo de geração da resposta (invoke): {elapsed_time}')
print(f'Quantidade de caracteres gerados: {len(response)}')

#---- 1. usar outro modelo disponível no hugging face (comparação do mesmo prompt)

model = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mixtral-8x7B-Instruct-v0.1',
    task = 'text-generation'
    )

start_time = time.time()
response = model.invoke('Oi, você pode gerar um JSON sobre qualquer informação? Gere o texto em uma quantidade de linhas reduzida')
end_time = time.time()

print(f'Resposta do modelo LangChain: {response}')
print(f'Tempo de geração da resposta (invoke): {elapsed_time}')
print(f'Quantidade de caracteres gerados: {len(response)}')

