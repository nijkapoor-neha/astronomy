from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        embeddings = self.model.encode(texts)
        return np.array(embeddings).astype("float32")

    def normalize(self, vectors):
        faiss.normalize_L2(vectors)
        return vectors