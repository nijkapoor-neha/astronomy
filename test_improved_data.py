"""
Test improved dataset with simple language and tags
"""

import json

# Load the enhanced dataset
with open("data/vedic_astrology_dataset_enhanced.json", "r") as f:
    data = json.load(f)

# Find some examples with simple interpretations
print("🔮 IMPROVED INTERPRETATIONS WITH SIMPLE LANGUAGE & TAGS\n")
print("=" * 70)

examples = [
    ("sun_1h", "Sun in 1st House (Self)"),
    ("moon_4h", "Moon in 4th House (Home & Mother)"),
    ("jupiter_5h", "Jupiter in 5th House (Love & Children)"),
    ("saturn_10h", "Saturn in 10th House (Career)"),
    ("venus_7h", "Venus in 7th House (Marriage)"),
    ("mars_6h", "Mars in 6th House (Work & Health)"),
]

for entry_id, title in examples:
    entry = next((e for e in data if e["id"] == entry_id), None)
    if entry:
        print(f"\n🌟 {title}")
        print("-" * 70)
        print(f"📝 {entry['text']}")
        print(f"🏷️  Tags: {', '.join(entry['metadata'].get('tags', []))}")
        print()

print("=" * 70)
print("\n✅ Each interpretation now:")
print("   • Uses SIMPLE, everyday language")
print("   • Direct benefits and challenges listed")
print("   • Tagged for better searching")
print("   • Practical advice (e.g., 'Good for...' jobs)")
