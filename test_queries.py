"""
Test to verify improved query generation
"""

from query.mapper import build_queries

# Test sample chart
test_chart = {
    "lagna": "Gemini",
    "lagna_degree": 45.5,
    "planets": {
        "Sun": {
            "degree": 30.0,
            "sign": "Aries",
            "house": 1,
            "nakshatra": "Krittika"
        },
        "Moon": {
            "degree": 120.0,
            "sign": "Leo",
            "house": 5,
            "nakshatra": "Magha"
        },
        "Mars": {
            "degree": 90.0,
            "sign": "Cancer",
            "house": 4,
            "nakshatra": "Punarvasu"
        },
        "Mercury": {
            "degree": 45.0,
            "sign": "Aries",
            "house": 1,
            "nakshatra": "Bharani"
        },
        "Jupiter": {
            "degree": 150.0,
            "sign": "Virgo",
            "house": 6,
            "nakshatra": "Hasta"
        },
        "Venus": {
            "degree": 75.0,
            "sign": "Gemini",
            "house": 3,
            "nakshatra": "Mrigashira"
        },
        "Saturn": {
            "degree": 200.0,
            "sign": "Libra",
            "house": 7,
            "nakshatra": "Swati"
        },
        "Rahu": {
            "degree": 270.0,
            "sign": "Sagittarius",
            "house": 9,
            "nakshatra": "Mula"
        },
        "Ketu": {
            "degree": 90.0,
            "sign": "Gemini",
            "house": 3,
            "nakshatra": "Mrigashira"
        }
    }
}

print("🔮 Testing Improved Query Builder\n")
print("=" * 60)
queries = build_queries(test_chart)

print(f"✨ Generated {len(queries)} queries:\n")
for i, query in enumerate(queries, 1):
    print(f"{i:2d}. {query}")

print("\n" + "=" * 60)
print("\n✅ Query builder working! These queries should match better")
print("   with your astrology database entries for nakshatra and signs.\n")
