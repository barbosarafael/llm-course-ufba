from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
import os
load_dotenv()

def get_cdd_info():
    loader = PyPDFLoader("https://arxiv.org/pdf/2210.07342")
    pages = loader.load() # devolve um Document, envelopando a string
    pages =  [page.page_content for page in pages] # tiro a string de dentro do document

    return "\n".join(pages) # converto a lista de strings para uma unica string

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        ".",
        "!",
        "?",
        ";",
        " ",
        "",
    ],
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

docs = text_splitter.split_text(get_cdd_info())
for doc in docs: 
    print("->", doc)