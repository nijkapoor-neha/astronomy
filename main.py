from db.search import VectorSearch

def main():
    search_engine = VectorSearch()

    while True:
        query = input("\nAsk astrology question: ")

        results = search_engine.search(query)

        print("\nTop Results:\n")
        for r in results:
            print(f"- {r['text']}\n")

if __name__ == "__main__":
    main()