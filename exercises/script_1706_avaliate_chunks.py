# 0) Libs

import pickle
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# 1) Carrega o pickle dos chunks como lista

with open('chunks_wikipedia_brasil.pkl', 'rb') as f:
    chunks_to_save = pickle.load(f)
    
# 2) Define o modelo para embeddings
    
model = SentenceTransformer("all-MiniLM-L6-v2")    
embeddings = model.encode(chunks_to_save)

# 3) Define a query e passa o embedding

user_query = "Qual o time de futebol mais famoso no Brasil?" 
query = model.encode([user_query])

# 4) Aplica o embedding nos chunks e avalia a similaridade

case_list = []

for i in range(len(embeddings)):
    
    similarities = model.similarity(query[0], embeddings[i])
    
    similarities = [similarities.numpy()[0][0]]
    
    chunk_temp = [chunks_to_save[i]]

    x = dict(zip(chunk_temp, similarities))
    
    case_list.append(x)
    
# 5) Rankeia os chunks pela maior similaridade    
    
sorted_data = sorted(case_list, key = lambda x: list(x.values())[0], reverse = True)

# 6) Print dos chunkks com suas maiores similaridades

for x in sorted_data[:10]:
    
    print()
    
    print(f'User query: {user_query}')
    print(f'Chunk: {list(x.keys())[0]}')
    print(f'Similaridade: {list(x.values())[0]}')
    
    print()
    
    
# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: Futebol - Brazilian Football ConfederationTaça Brasil at RSSSF BrasilEternal matches: Cruzeir
# Similaridade: 0.6524105072021484


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 1981, 1989, 1990, 2014Copa do Brasil (1): 2000Copa dos Campeões da Copa Brasil (1): 1978Copa dos Campeões (1): 2001Torneio Rio – São Paulo (5): 1933, 1962, 1966, 1998, 2002Campeonato Paulista de Futebol (25): 1930, 1932, 1933, 1934, 1938, 1941,
# Similaridade: 0.6393712759017944


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: do Brasil (2): 2021, 2024Torneio Rio – São Paulo (1): 1955Campeonato Paulista de Futebol (27): 1917, 1919, 1921, 1922, 1923, 1931, 1935, 1937, 1939, 1949, 1951, 1953, 1954, 1961, 1964, 1965, 1969, 1970, 1971, 1973, 1986, 1992, 1995, 1999, 2015,
# Similaridade: 0.632185697555542


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: estreará em 31 de março.Nicolazzi, Fernando (7 de abril de 2019). 2019 – O Brasil Paralelo entre o passado histórico e a picanha de papelão (por Fernando Nicolazzi) Sul 21. Cópia arquivada em 8 de abril de 2019. Estamos diante de uma
# Similaridade: 0.5664962530136108


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 100 anos de seleção brasileira de futebol. Rio de Janeiro: Folha Seca. ISBN 978-85-87199-29-4. External links Official website  (in Portuguese)Brazil FIFA profileBrazil CONMEBOL profileBrazilian Football – Guide to Football in BrazilRSSSF BrazilAll
# Similaridade: 0.5619381070137024


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: BrazilAll about Brazilian Football – S
# Similaridade: 0.561937689781189


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: A fundação do Villa Nova, Arquivo Campeões do Futebol, 2012-06-28.Centro de Memória Morro Velho: Respeito ao passado, referência para o presente e inspiração para inovações futuras., AngloGold As
# Similaridade: 0.5588362812995911


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: The Superliga Nacional de Futebol Americano (National American Football League, previously Liga Brasileira de Futebol Americano, Brazilian American Football League) is an American football league in Brazil. It was created by eight teams which played
# Similaridade: 0.5560070276260376


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 2021Copa do Brasil (4): 1992, 1997, 1999 , 2018Copa dos Campeões: 2002Torneio Rio – São Paulo (9): 1950, 1954, 1959, 1961, 1962, 1964, 1997, 1998, 2002Campeonato Paulista (38): 1928, 1929, 1930, 1938, 1941, 1943, 1945, 1952, 1955, 1956, 1957, 1958,
# Similaridade: 0.5464392304420471


# User query: Qual o time de futebol mais famoso no Brasil?
# Chunk: 1968Campeonato Gaúcho de Atletismo Feminino (8): 1951, 1953, 1959, 1960, 1961, 1965, 1966, 1972 Campeonato Brasileiro record  References = Websites == Books =Enciclopédia do Futebol Brasileiro, Volume 1 – Lance, Rio de Janeiro: Aretê Editorial S/A,
# Similaridade: 0.5436076521873474    