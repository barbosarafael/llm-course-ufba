from sentence_transformers import SentenceTransformer

model = SentenceTransformer(model_name_or_path = 'all-MiniLM-L6-v2')

sentences = ['pizza',
             'man', 
             'king', 
             'google',
             'ufba',
             'lasagna', 
             'what kind of food i eat in italy?']

embeddings = model.encode(sentences = sentences)

# for sent, emb in zip(sentences, embeddings):
    
#     print(f'Sentença: {sent}\n')
    
#     print(f'Embedding: {emb}')

similaridade = model.similarity(embeddings, embeddings)

print(similaridade)