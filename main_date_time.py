from db.search import VectorSearch
from astrology.calculator import calculate_lagna
from query.mapper import build_lagna_query

def main():
    search_engine = VectorSearch()

    print("Enter your details:\n")

    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    time = input("Time of Birth (HH:MM): ")

    # For now manually input lat/lon
    lat = float(input("Latitude: "))
    lon = float(input("Longitude: "))

    # Step 1: Calculate Lagna
    lagna, degree = calculate_lagna(dob, time, lat, lon)

    print(f"\n🔮 Your Lagna: {lagna} ({degree:.2f}°)")

    # Step 2: Build query
    query = build_lagna_query(lagna)

    # Step 3: Search vector DB
    results = search_engine.search(query)

    print("\n📖 Interpretation:\n")
    for r in results:
        print(f"- {r['text']}\n")

if __name__ == "__main__":
    main()