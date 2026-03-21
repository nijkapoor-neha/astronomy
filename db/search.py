import numpy as np

from embeddings.embedder import Embedder
from db.storage import load_index, load_pickle

class VectorSearch:
    def __init__(self):
        self.index = load_index()
        self.id_map = load_pickle("db/id_map.pkl")
        self.text_map = load_pickle("db/text_map.pkl")
        self.meta_map = load_pickle("db/meta_map.pkl")

        self.embedder = Embedder()

    def search(self, query, k=3):
        q_vec = self.embedder.encode([query])
        q_vec = self.embedder.normalize(q_vec)

        distances, indices = self.index.search(q_vec, k)

        results = []
        for idx in indices[0]:
            doc_id = self.id_map[idx]
            results.append({
                "id": doc_id,
                "text": self.text_map[doc_id],
                "metadata": self.meta_map[doc_id]
            })

        return results