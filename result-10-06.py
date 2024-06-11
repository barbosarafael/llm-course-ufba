# 0) Libs

import os
import glob
import pathlib


# 1) Repositório do github: https://github.com/qiyuangong/leetcode

path_to_files = 'leetcode-master/'

# 2) Criando uma função para ler todos os arquivos da pasta

def list_files_walk(start_path = '.'):
    
    l = []
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            
            files = os.path.join(root, file)
            l.append(files)
            
    return l
            
all_files = list_files_walk(start_path = path_to_files)

# 3) Lendo um arquivo python:

def read_files(file: str):
    
    with open(file, 'r', encoding = 'utf-8') as src:
        content = src.read()
    
    return content

file = 'leetcode-master/python/110_Balanced_Binary_Tree.py'

doc = read_files(file = file)

# 4) Excluindo as linhas com comentários em python

def remove_comments(file: str):
    
    lines = file.strip().split('\n')
    
    uncommented_lines = [line for line in lines if not line.strip().startswith('#')]
    
    rows = '\n'.join(uncommented_lines)
    
    return rows

doc_preprocess = remove_comments(file = doc)

print(doc_preprocess)

# 4) Aplicando o chunk

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 20,
    length_function = len
)

docs = text_splitter.split_text(doc_preprocess)

for doc in docs: 
    print("\n->", doc)
    
# 5) Para amanhã: automatizar para todos