import json

def load_data(path):
    with open(path, "r") as f:
        data = json.load(f)

    texts = [item["text"] for item in data]
    ids = [item["id"] for item in data]
    metadata = [item.get("metadata", {}) for item in data]

    return texts, ids, metadata