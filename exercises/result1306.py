# 0) Lib

from sentence_transformers import SentenceTransformer

# 1) Definição dos 3 modelos

model1 = SentenceTransformer(model_name_or_path = 'all-MiniLM-L6-v2')
model2 = SentenceTransformer(model_name_or_path = 'all-mpnet-base-v2')
model3 = SentenceTransformer(model_name_or_path = 'all-distilroberta-v1')

# 2) Simulação dos chunks (sim, feitos a partir do Chat-GPT)

sentences = [
    "O céu estava azul claro e as nuvens flutuavam suavemente.",
    "As crianças brincavam alegremente no parque.",
    "O sol brilhava intensamente no meio do dia.",
    "A chuva começou a cair de repente, molhando tudo ao redor.",
    "Os pássaros cantavam nas árvores próximas ao rio.",
    "A lua iluminava a noite escura com seu brilho prateado.",
    "O vento soprava forte, balançando as árvores.",
    "As estrelas brilhavam no céu noturno, formando constelações.",
    "O mar estava calmo, com ondas suaves quebrando na areia.",
    "A montanha se erguia majestosa no horizonte, coberta de neve."
]

# 3) Embedding dos chunks

embeddings = model1.encode(sentences = sentences)

# 4) Pesquisa e embedding do pesquisa

user_query = ['Quantas montanhas temos no Brasil?']
user_query_emb = model1.encode(user_query)

# 5) Resultado da similaridade para o modelo 1

for i in range(len(embeddings)):
    
    print(f'>>>>>>>>> Pesquisa: {user_query[0]}\n')
    
    print(f'Chunk: {sentences[i]}\n')
    
    sim = model1.similarity(user_query_emb[0], embeddings[i])
    
    print(f'Similaridade: {sim}\n')
    
# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O céu estava azul claro e as nuvens flutuavam suavemente.

# Similaridade: tensor([[0.4035]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As crianças brincavam alegremente no parque.

# Similaridade: tensor([[0.4953]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O sol brilhava intensamente no meio do dia.

# Similaridade: tensor([[0.5117]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A chuva começou a cair de repente, molhando tudo ao redor.

# Similaridade: tensor([[0.5114]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: Os pássaros cantavam nas árvores próximas ao rio.

# Similaridade: tensor([[0.5098]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A lua iluminava a noite escura com seu brilho prateado.

# Similaridade: tensor([[0.5423]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O vento soprava forte, balançando as árvores.

# Similaridade: tensor([[0.4227]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As estrelas brilhavam no céu noturno, formando constelações.

# Similaridade: tensor([[0.5598]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O mar estava calmo, com ondas suaves quebrando na areia.

# Similaridade: tensor([[0.4815]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A montanha se erguia majestosa no horizonte, coberta de neve.

# Similaridade: tensor([[0.5563]])


# 6) Resultado da similaridade para o modelo 2

for i in range(len(embeddings)):
    
    print(f'>>>>>>>>> Pesquisa: {user_query[0]}\n')
    
    print(f'Chunk: {sentences[i]}\n')
    
    sim = model2.similarity(user_query_emb[0], embeddings[i])
    
    print(f'Similaridade: {sim}\n')
    
    
# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O céu estava azul claro e as nuvens flutuavam suavemente.

# Similaridade: tensor([[0.4035]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As crianças brincavam alegremente no parque.

# Similaridade: tensor([[0.4953]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O sol brilhava intensamente no meio do dia.

# Similaridade: tensor([[0.5117]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A chuva começou a cair de repente, molhando tudo ao redor.

# Similaridade: tensor([[0.5114]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: Os pássaros cantavam nas árvores próximas ao rio.

# Similaridade: tensor([[0.5098]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A lua iluminava a noite escura com seu brilho prateado.

# Similaridade: tensor([[0.5423]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O vento soprava forte, balançando as árvores.

# Similaridade: tensor([[0.4227]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As estrelas brilhavam no céu noturno, formando constelações.

# Similaridade: tensor([[0.5598]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O mar estava calmo, com ondas suaves quebrando na areia.

# Similaridade: tensor([[0.4815]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A montanha se erguia majestosa no horizonte, coberta de neve.

# Similaridade: tensor([[0.5563]])    


# 7) Resultado da similaridade para o modelo 3

for i in range(len(embeddings)):
    
    print(f'>>>>>>>>> Pesquisa: {user_query[0]}\n')
    
    print(f'Chunk: {sentences[i]}\n')
    
    sim = model3.similarity(user_query_emb[0], embeddings[i])
    
    print(f'Similaridade: {sim}\n')
    
# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O céu estava azul claro e as nuvens flutuavam suavemente.

# Similaridade: tensor([[0.4035]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As crianças brincavam alegremente no parque.

# Similaridade: tensor([[0.4953]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O sol brilhava intensamente no meio do dia.

# Similaridade: tensor([[0.5117]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A chuva começou a cair de repente, molhando tudo ao redor.

# Similaridade: tensor([[0.5114]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: Os pássaros cantavam nas árvores próximas ao rio.

# Similaridade: tensor([[0.5098]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A lua iluminava a noite escura com seu brilho prateado.

# Similaridade: tensor([[0.5423]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O vento soprava forte, balançando as árvores.

# Similaridade: tensor([[0.4227]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: As estrelas brilhavam no céu noturno, formando constelações.

# Similaridade: tensor([[0.5598]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: O mar estava calmo, com ondas suaves quebrando na areia.

# Similaridade: tensor([[0.4815]])

# >>>>>>>>> Pesquisa: Quantas montanhas temos no Brasil?

# Chunk: A montanha se erguia majestosa no horizonte, coberta de neve.

# Similaridade: tensor([[0.5563]])    