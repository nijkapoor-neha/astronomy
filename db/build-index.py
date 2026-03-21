import numpy as np
import faiss
from utils.loader import load_data
from embeddings.embedder import Embedder
from db.storage import save_index, save_pickle

DATA_PATH = "data/vedic_astrology_dataset.json"

def build():
    texts, ids, metadata = load_data(DATA_PATH)

    embedder = Embedder()

    vectors = embedder.encode(texts)
    vectors = embedder.normalize(vectors)

    dim = vectors.shape[1]

    index = faiss.IndexFlatIP(dim)  # cosine similarity
    index.add(vectors)

    # Create mappings
    id_map = {i: ids[i] for i in range(len(ids))}
    text_map = {ids[i]: texts[i] for i in range(len(ids))}
    meta_map = {ids[i]: metadata[i] for i in range(len(ids))}

    # Save everything
    save_index(index)
    save_pickle(id_map, "db/id_map.pkl")
    save_pickle(text_map, "db/text_map.pkl")
    save_pickle(meta_map, "db/meta_map.pkl")

    print("✅ FAISS index built successfully!")

if __name__ == "__main__":
    build()