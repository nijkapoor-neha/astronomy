"""
Enhanced Vedic Astrology Dataset Builder
Improve the quality and searchability of the knowledge base
"""

import json
import os

def enhance_data():
    """Generate improved entries for planet-house placements"""
    
    enhanced_entries = []
    
    # Planet descriptions
    planets = {
        "Sun": "ego, vitality, authority, father, career, public image",
        "Moon": "emotions, mind, mother, family, comfort, intuition",
        "Mars": "action, courage, conflict, siblings, energy, passion",
        "Mercury": "communication, intellect, commerce, learning, writing",
        "Jupiter": "expansion, wisdom, wealth, luck, spirituality, teaching",
        "Venus": "love, beauty, comfort, luxury, arts, pleasure",
        "Saturn": "restriction, duty, time, discipline, karma, delays",
        "Rahu": "obsession, worldly desires, illusion, unconventional",
        "Ketu": "detachment, spirituality, loss, mysticism, transformation"
    }
    
    # House meanings
    houses = {
        1: "personality, appearance, health, life direction",
        2: "wealth, family, speech, possessions, food",
        3: "communication, siblings, short travels, courage",
        4: "home, mother, property, peace, foundation",
        5: "children, romance, creativity, intelligence, speculation",
        6: "enemies, health issues, service, competition",
        7: "marriage, partnership, business relations, public",
        8: "inheritance, transformation, death, mysteries, shared wealth",
        9: "father, spirituality, higher learning, travel, dharma",
        10: "career, reputation, authority, public image",
        11: "friendship, gains, aspirations, groups, elder siblings",
        12: "loss, seclusion, spirituality, foreign lands, isolation"
    }
    
    # Enhanced planet-house combinations
    for planet, planet_desc in planets.items():
        for house_num, house_desc in houses.items():
            entry = {
                "id": f"{planet.lower()}_{house_num}h",
                "text": f"{planet} in House {house_num} impacts {house_desc}, bringing effects related to {planet_desc}. The house themes are influenced by {planet}'s intrinsic nature and strength in the chart.",
                "metadata": {
                    "planet": planet,
                    "house": house_num,
                    "type": "planet_house_placement",
                    "themes": house_desc,
                    "planet_nature": planet_desc
                }
            }
            enhanced_entries.append(entry)
    
    return enhanced_entries

def merge_with_existing(enhanced_entries):
    """Merge enhanced entries with existing dataset"""
    
    original_path = "data/vedic_astrology_dataset.json"
    output_path = "data/vedic_astrology_dataset_enhanced.json"
    
    # Load existing data
    try:
        with open(original_path, "r") as f:
            existing_data = json.load(f)
        print(f"✓ Loaded {len(existing_data)} existing entries")
    except FileNotFoundError:
        print(f"⚠ {original_path} not found, starting fresh")
        existing_data = []
    
    # Merge: add enhanced entries, avoiding duplicates by ID
    existing_ids = {entry.get("id") for entry in existing_data}
    new_entries = [e for e in enhanced_entries if e["id"] not in existing_ids]
    
    merged_data = existing_data + new_entries
    
    # Save merged dataset
    with open(output_path, "w") as f:
        json.dump(merged_data, f, indent=2)
    
    print(f"✓ Added {len(new_entries)} enhanced entries")
    print(f"✓ Total merged dataset: {len(merged_data)} entries")
    print(f"✓ Saved to: {output_path}")
    
    return output_path

if __name__ == "__main__":
    print("🔮 Enhancing Vedic Astrology Dataset\n")
    
    # Generate enhanced entries
    enhanced = enhance_data()
    print(f"✓ Generated {len(enhanced)} enhanced planet-house entries")
    
    # Merge with existing data
    output_file = merge_with_existing(enhanced)
    
    print(f"\n✨ Enhancement complete!")
    print(f"\nNext steps:")
    print(f"  1. Run: python -m db.build-index data/{os.path.basename(output_file)}")
    print(f"  2. Or just: python -m db.build-index")
    print(f"     (will auto-detect enhanced data)")

