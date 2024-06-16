# 0) Libs

from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import chromadb
import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

from dotenv import load_dotenv
load_dotenv()

# 1) Definindo o caminho para o repositório

path_to_files = 'leetcode-master/'

# 2) Criação de funções:

# a) Lê todos os arquivos da pasta, inclusive sub-diretórios

def list_files_walk(start_path = '.'):
    
    l = []
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            
            files = os.path.join(root, file)
            l.append(files)
            
    return l

# b) Identifica a extensão do arquivo 

def identify_language(file: str):
    
    try:
    
        regex = r'\.[^.]+$'

        string = re.search(regex, file).group()
        
    except:
        
        string = ''
    
    return string

# c) Lê o conteúdo do arquivo:

def read_files(file: str):
    
    with open(file, 'r', encoding = 'utf-8') as src:
        content = src.read()
    
    return content

# d) Exclui as linhas com comentários 

def remove_comments(file: str, extension_file: str):
    
    lines = file.strip().split('\n')
    
    if extension_file == '.py':    
        
        uncommented_lines = [line for line in lines if not line.strip().startswith('#')]
    
    elif extension_file in ('.java', '.cpp'):    
        
        uncommented_lines = [line for line in lines if not line.strip().startswith('//')]
    
    else: 
        
        print('Não reconhecido')
        
    rows = '\n'.join(uncommented_lines)
    
    return rows

# e) Aplica o spliter/chunk por linguagens:

def text_splitter_by_language(
    doc: str,
    extension_file: str,
    chunk_size: int = 200,
    chunk_overlap: int = 20
    ):
    
    if extension_file == '.py':
        
        lang = Language.PYTHON
        
    elif extension_file == '.java':
        
        lang = Language.JAVA
        
    elif extension_file == '.cpp':
        
        lang = Language.CPP
        
    else: 
        
        lang = None    
        
    text_splitter = RecursiveCharacterTextSplitter.from_language(
            language = lang,
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = len
            )
    
    split_doc = text_splitter.split_text(doc)
    
    return split_doc

# f) Seleciona os chunks similares

def select_similar_chunks(user_query):
       
    client = chromadb.PersistentClient(path = "./tomorrow")
    
    col = client.get_or_create_collection("langchain", 
                                          embedding_function = OpenAIEmbeddingFunction(api_key = os.getenv('OPENAI_API_KEY')))
    
    results =  col.query(query_texts = [user_query], n_results = 5)
    
    return "\n".join(results['documents'][0])

# g) Consulta os chunks a partir de uma query

def prompt_llm(user_query, chunks):
    
    model = ChatOpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'))
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Gostaria que você atuasse como um especialista em três linguagens de programação: Cpp, Java e Python"),
        ("user", "{user_query}"),
        ("system", "Responda em até 50 palavras."),
    ])

    chain = prompt | model 

    response = chain.invoke({
        "user_query" : user_query,
        "cdd_info" : chunks
    })
    
    return response.content

# 3) Aplicação da função:

# a) Lendo todos os arquvios e separando seus caminhos relativos

all_files = list_files_walk(start_path = path_to_files)

# b) Mantendo na lista somente os que nos interessam: .py, .cpp, .java

official_files = [x for x in all_files if identify_language(x) in ('.py', '.cpp', '.java')]

# c) Loop para todos os arquivos:

chunks_to_save = []

for file in official_files:
    
    print(f'\n>>>>>>>>>> Nome do arquivo: {file}')
    
    # Lendo o conteúdo
    
    content = read_files(file = file)
    
    # Pegando a extensão
    
    extension = identify_language(file = file)
    
    # Excluindo linhas com comentários
    
    content_preprocess = remove_comments(file = content, extension_file = extension)
    
    # Aplicando o chunk
    
    chunk = text_splitter_by_language(doc = content_preprocess, extension_file = extension)
    
    count = 0
    for doc in chunk: 
        count += 1
        print(f'\n {count}º chunk: > ', doc)
        
        chunks_to_save.append(doc)
        
        
# 4. Definir os documentos e salvando no Chroma        
        
docs = [Document(page_content = chunk) for chunk in chunks_to_save]        

db = Chroma.from_documents(documents = docs, 
                           embedding = OpenAIEmbeddings(),
                           persist_directory = './tomorrow')

# 5. Iniciando a conversa dinâmica com os chunks do banco

conversation_history = []
model = ChatOpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'))

while True:

    user_query = input('>>>>>>>>>>>> Digite algo \n')
    
    conversation_history.append(user_query)
    
    chunks = select_similar_chunks(user_query)
    response = model.invoke(chunks)
    
    conversation_history.append(response)
    
    print(f'{response}\n')
    
    
    
#----------------------- Código do gradio

# import time
# import gradio as gr
# import chromadb
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
# import os
# from langchain.schema import AIMessage, HumanMessage

# from dotenv import load_dotenv

# load_dotenv()

# def echo(message, history):
    
#     llm = ChatOpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'))
    
#     history_langchain_format = []
    
#     for human, ai in history:
        
#         history_langchain_format.append(HumanMessage(content = human))
#         history_langchain_format.append(AIMessage(content=ai))
        
#     history_langchain_format.append(HumanMessage(content=message))
    
#     gpt_response = llm(history_langchain_format)
    
#     return gpt_response.content 
    
    
# demo = gr.ChatInterface(fn = echo, 
#                         title = 'Te ajudo em Python, Cpp e Java',
#                         theme = 'soft',
#                         description = 'Me pergunte sobre sintaxe e também posso traduzir de uma linguagem para outra',
#                         cache_examples = True,
#                         multimodal = False
#                         )

# demo.launch(share = True)    
    