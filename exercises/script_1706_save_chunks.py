# 0) Libs

import wikipedia
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle

# 1) Funções:

# a) Lista de N páginas do Wikipedia

def get_wikipedia_pages(page_name: str, results: int = 100, suggestion = False):
    
    wiki_pages = wikipedia.search(query = page_name, results = results, suggestion = True)[0]
    
    wiki_pages = [x for x in wiki_pages if "disambiguation" not in x]
        
    return wiki_pages


# b) Extração somente o texto da página da wikipedia

def extract_only_text_wikipedia(title: str):
    
    # title = f'^{title}$'
    
    try:

        wiki = wikipedia.page(title = title, auto_suggest = False)
        
    except wikipedia.DisambiguationError as e:
        
        wiki = wikipedia.page(e.options[0], auto_suggest = False)
        
    text = wiki.content        
    
    return text


# c) Pré-processamento de texto da wikipedia

def preprocess_text_wikipedia(page: str):
    
    page = page.replace('==', '')

    page = page.replace('\n', '')[:-12]
    
    return page


# 2) Código:

# a) Extraindo as páginas da wikipedia:

print('Iniciando a extração')

wiki_pages = get_wikipedia_pages(page_name = 'Brasil', results = 1000)

# b) Extraindo somente os textos das páginas e já os tratando

print('Extraindo somente os textos das páginas e já os tratando')

content_pages = [extract_only_text_wikipedia(x) for x in wiki_pages]

# c) Fazendo o pré-processamento do texto

content_pages = [preprocess_text_wikipedia(x) for x in content_pages]

# d) Aplicando o textsplitter para criar os chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 250,
    chunk_overlap = 20,
    length_function = len
    )

# e) Salvando os chunks em uma lista

chunks_to_save = []

for file in content_pages:
    
    # Aplicando o chunk
    
    chunk = text_splitter.split_text(file)
    
    # count = 0
    for doc in chunk: 
        # count += 1
        # print(f'\n {count}º chunk: > ', doc)
        
        chunks_to_save.append(doc)
        
print(len(chunks_to_save))

# Salvando a lista em pickle

with open('chunks_wikipedia_brasil.pkl', 'wb') as f:
    pickle.dump(chunks_to_save, f)