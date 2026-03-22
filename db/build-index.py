import numpy as np
import faiss
import json
import sys
import os
from utils.loader import load_data
from embeddings.embedder import Embedder
from db.storage import save_index, save_pickle

# Allow dynamic data path - check for enhanced data first
def get_data_path():
    # Check if enhanced entries exist
    if os.path.exists("data/enhanced_entries.json"):
        return "data/enhanced_entries.json"
    # Check if merged file exists
    if os.path.exists("data/vedic_astrology_dataset_enhanced.json"):
        return "data/vedic_astrology_dataset_enhanced.json"
    # Fallback to original
    return "data/vedic_astrology_dataset.json"

DATA_PATH = get_data_path()

def build(data_path=None):
    # Allow override via function parameter or command line
    if data_path is None:
        data_path = DATA_PATH
    
    print(f"📚 Building index from: {data_path}")
    
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found!")
        print(f"   Available files: vedic_astrology_dataset.json, enhanced_entries.json")
        return
    
    texts, ids, metadata = load_data(data_path)

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
    print(f"   Indexed {len(ids)} entries from {data_path}")

if __name__ == "__main__":
    data_file = sys.argv[1] if len(sys.argv) > 1 else None
    build(data_file)