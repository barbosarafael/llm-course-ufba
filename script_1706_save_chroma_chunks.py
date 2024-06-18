from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import chromadb
import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
import pickle

from dotenv import load_dotenv
load_dotenv()

# 4. Definir os documentos e salvando no Chroma        

with open('chunks_wikipedia_v2.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

print(mynewlist)
        
# docs = [Document(page_content = chunk) for chunk in chunks_to_save]        

# db = Chroma.from_documents(documents = docs, 
#                            embedding = OpenAIEmbeddings(),
#                            persist_directory = './tomorrow')


# TO-DO:

# Salvar os chunks no ChromaDB
# Avaliar a similaridade padrão com um loop for a sua query/prompt
# Utilizar o script rerank 
# Avaliar os chunks
# Enviar os principais chunks para o LLM