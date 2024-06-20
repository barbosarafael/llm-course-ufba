# 0) Libs

import pickle
from sentence_transformers import CrossEncoder
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# 1) Carrega o pickle dos chunks como lista

with open('chunks-pkl/chunks_wikipedia_brasil.pkl', 'rb') as f:
    chunks_to_save = pickle.load(f)
    
# 2) Define o modelo de rerank

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# 3) Define a query

user_query = "Qual o time de futebol mais famoso no Brasil?" 

# 4) Cria o rankeamento e salva em uma lista de dicionários

ranks = model.rank(user_query, chunks_to_save)
case_list = []

for rank in ranks:
    
    chunk = [chunks_to_save[rank['corpus_id']]]
    score = [rank['score']]
    
    x = dict(zip(chunk, score))
    case_list.append(x)
    
# 5) Ordena o dicionário a partir da similaridade
    
best_chunks = sorted(case_list, key = lambda x: list(x.values())[0], reverse = True)

# 6) Print dos 10 melhores chunks

for x in best_chunks[:10]:
    
    print()
    
    print(f'User query: {user_query}')
    print(f'Chunk: {list(x.keys())[0]}')
    print(f'Similaridade: {list(x.values())[0]}')    
    
    
# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: "O mais querido do Brasil" ("the most beloved of Brazil"). In 1933 the team went on its first tour outside Brazil (to Montevideo and Buenos Aires) and on 14 May of the same year played its final match as an amateur team, defeating River Futebol
# Similaridade: 3.790598154067993

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: created an exhibit entitled O Negro no Futebol Brasileiro – A arte e os Artistas (The black man in Brazilian soccer - The art and its artists). This exhibit highlighted the presence of soccer players of African ancestry, such as Pelé, Garrincha,
# Similaridade: 2.5939791202545166

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: modified to "O brasileiro/desta vez no Chile/mostrou o futebol como é que é/ganhou o Bicampeonato/Sambando com a bola no pé/Goool!" (The Brazilian this time in Chile/Showed football the way it is/Won the Bichampionship/Dancing the samba with the
# Similaridade: 2.3298943042755127

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 100 anos de seleção brasileira de futebol. Rio de Janeiro: Folha Seca. ISBN 978-85-87199-29-4. External links Official website  (in Portuguese)Brazil FIFA profileBrazil CONMEBOL profileBrazilian Football – Guide to Football in BrazilRSSSF BrazilAll
# Similaridade: 1.6387391090393066

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: do Brasil (2): 2021, 2024Torneio Rio – São Paulo (1): 1955Campeonato Paulista de Futebol (27): 1917, 1919, 1921, 1922, 1923, 1931, 1935, 1937, 1939, 1949, 1951, 1953, 1954, 1961, 1964, 1965, 1969, 1970, 1971, 1973, 1986, 1992, 1995, 1999, 2015,
# Similaridade: 1.5595710277557373

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 1981, 1989, 1990, 2014Copa do Brasil (1): 2000Copa dos Campeões da Copa Brasil (1): 1978Copa dos Campeões (1): 2001Torneio Rio – São Paulo (5): 1933, 1962, 1966, 1998, 2002Campeonato Paulista de Futebol (25): 1930, 1932, 1933, 1934, 1938, 1941,
# Similaridade: 0.841048002243042

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 1968Campeonato Gaúcho de Atletismo Feminino (8): 1951, 1953, 1959, 1960, 1961, 1965, 1966, 1972 Campeonato Brasileiro record  References = Websites == Books =Enciclopédia do Futebol Brasileiro, Volume 1 – Lance, Rio de Janeiro: Aretê Editorial S/A,
# Similaridade: 0.583226203918457

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: Brasileiro de Futebol Feminino: 12016Campeonato Carioca de Futebol Feminino: 52015, 2016, 2017, 2018, 2019= Women's basketball =The Flamengo women's basketball team won back-to-back Brazilian championships in 1954 and 1955. Ten years later with some
# Similaridade: 0.5676404237747192

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: The Superliga Nacional de Futebol Americano (National American Football League, previously Liga Brasileira de Futebol Americano, Brazilian American Football League) is an American football league in Brazil. It was created by eight teams which played
# Similaridade: 0.1905982792377472

# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: Olé Brasil Futebol Clube, usually known as Olé Brasil, is a currently inactive Brazilian football club based in Ribeirão Preto, a city in the state of São Paulo. History The club was founded on September 21, 2006 by entrepreneurs Eduardo Zanello,
# Similaridade: 0.1300414353609085
    
def prompt_llm(user_query, chunks):
    model = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um especialista em um país chamado Brasil"),
        ("user", "{user_query}"),
        ("system", "Responda em até 100 palavras."),
    ])

    chain = prompt | model 

    response = chain.invoke({
        "user_query" : user_query,
        "cdd_info" : chunks
    })
    return response.content

# 6) Passa os 1000 melhores chunks, a partir do rerank, para o GPT-4 gerar a resposta

response = prompt_llm(user_query, best_chunks[:10])

print(f'\n>>>>>>>>>>>>>>>> Query: {user_query}\n')

print(response) 

# >>>>>>>>>>>>>>>> Query: Qual o time de futebol mais famoso no Brasil? -> Em outro teste ele apontou o Paysandu. Brincadeira, foi o Flamengo!

# O time de futebol mais famoso e tradicional no Brasil é o Sport Club Corinthians Paulista, conhecido como Corinthians. 
# Fundado em 1910, o clube tem uma das maiores torcidas do país e conquistou diversos títulos, incluindo o Campeonato Brasileiro,
# a Copa do Brasil e a Copa Libertadores da América. O Corinthians também é conhecido pela sua fanática torcida,
# chamada de "Fiel Torcida", que comparece em peso aos jogos e manifesta uma paixão intensa pelo clube.