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

    print("\n📖 Your Astrological Interpretation:\n")
    print("=" * 70)

    # 🔎 Step 3: Search Vector DB
    seen = set()
    result_count = 0

    for q in queries[:8]:  # limit to avoid overload
        results = search_engine.search(q, k=1)

        for r in results:
            if r["text"] not in seen:
                result_count += 1
                tags = r.get("metadata", {}).get("tags", [])
                
                print(f"\n{result_count}. {q}")
                print("-" * 70)
                print(f"   {r['text']}")
                
                if tags:
                    tag_str = ", ".join(tags[:5])  # Show first 5 tags
                    print(f"   📌 Keywords: {tag_str}")
                
                seen.add(r["text"])

    print("\n" + "=" * 70)
    print(f"✨ Showing {result_count} key interpretations from your chart\n")


if __name__ == "__main__":
    main()