# Criando aplicações baseadas em LLMs

## Sobre

Notas, códigos e recursos do curso "Criando aplicações baseadas em LLMs". O curso foca no desenvolvimento de aplicações utilizando Modelos de Linguagem de Grande Escala (LLMs).

> **Observação**: Como são notas de aulas, fui adicionando as anotações não me preocupando com estrutura de arquivos. Agora no fim do curso que estruturei os arquivos de uma forma que faz sentido. Logo, quando você replicar esse código, talvez tenha algo quebrado.

## Estrutura do Projeto


```
.
├── chunks-pks # Arquivos .pkl com as listas de chunks criadas durante o curso

├── exercises # Exercícios em .py ou .txt enviados no final de cada aula (eu faltei alguma, não lembro o dia)

├── leetcode-master # repositório baixado para um dos exercícios
   ├── cpp # Arquivos em extensão .cpp
   ├── java # Arquivos em extensão .java
   ├── python # Arquivos em extensão .python

├── notes # Anotações das aulas

├── notes_py # Anotações dos scripts das aulas

```

## Pré-requisitos 

- Python 3.10.12
- Bibliotecas instaladas. Utilize um `pip install -r requirements.txt`

## Como executar os scripts

Utilizando como exemplo um dos script do último exercício realizado. 

- Carrega textos de N (parâmetro) páginas de um determinado assunto (parâmetro) na Wikipedia
- Faz um pré-processamento do texto
- Cria os chunks
- Salva os chunks em um arquivo `.pkl`

```
python exercises/script_1706_save_chunks.py
```

## Contato

Se deseja tirar dúvida sobre algo, pode mandar mensagem no [LinkedIn](https://www.linkedin.com/in/rafael-barbosa0) ou [Twitter](https://x.com/rafaelbarbosa_s)