from db.search import VectorSearch
from astrology.calculator import calculate_full_chart
from query.builder import build_queries

def main():
    search_engine = VectorSearch()

    print("Enter your details:\n")

    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    time = input("Time of Birth (HH:MM): ")

    # For now manually input lat/lon
    lat = float(input("Latitude: "))
    lon = float(input("Longitude: "))

    # 🔮 Step 1: Calculate Full Chart
    chart = calculate_full_chart(dob, time, lat, lon)

    print("\n🔮 Your Chart Summary:\n")
    print(f"Lagna: {chart['lagna']} ({chart['lagna_degree']:.2f}°)")

    moon = chart["planets"]["Moon"]
    print(f"Moon Nakshatra: {moon['nakshatra']}")

    print("\n🪐 Planet Positions:")
    for planet, info in chart["planets"].items():
        print(f"{planet}: {info['sign']} | House {info['house']} | {info['nakshatra']}")

    # 🔍 Step 2: Build Queries
    queries = build_queries(chart)

    print("\n📖 Interpretation:\n")

    # 🔎 Step 3: Search Vector DB
    seen = set()

    for q in queries[:8]:  # limit to avoid overload
        results = search_engine.search(q, k=1)

        for r in results:
            if r["text"] not in seen:
                print(f"🔹 {q}")
                print(f"   → {r['text']}\n")
                seen.add(r["text"])


if __name__ == "__main__":
    main()