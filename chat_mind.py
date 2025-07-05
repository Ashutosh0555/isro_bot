print("is working")
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sentence_transformers import SentenceTransformer  # Optional for inference

def find_similar_paragraphs(query, ls, embeddings, model, top_k=3, threshold=0.5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = []
    for idx in top_indices:
        if similarities[idx] >= threshold:
            results.append((similarities[idx], ls[idx]))
    return results
