import pickle
import faiss

def save_index(index, path="db/faiss_index.bin"):
    faiss.write_index(index, path)

def load_index(path="db/faiss_index.bin"):
    return faiss.read_index(path)

def save_pickle(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)