"""
Enhanced Vedic Astrology Dataset Builder with Tags and Simple Language
Improve the quality and searchability of the knowledge base
"""

import json
import os

def enhance_data():
    """Generate improved entries for planet-house placements with tags and simple descriptions"""
    
    enhanced_entries = []
    
    # Planet meanings in simple terms
    planet_info = {
        "Sun": {
            "desc": "self, confidence, authority, leadership, success",
            "tags": ["identity", "power", "success", "career"]
        },
        "Moon": {
            "desc": "feelings, relationships, family, comfort, peace of mind",
            "tags": ["emotions", "family", "home", "mind"]
        },
        "Mars": {
            "desc": "energy, courage, action, competition, conflict",
            "tags": ["action", "courage", "conflict", "sports"]
        },
        "Mercury": {
            "desc": "communication, thinking, learning, business, writing",
            "tags": ["communication", "learning", "business", "intellect"]
        },
        "Jupiter": {
            "desc": "good luck, growth, wisdom, teaching, wealth",
            "tags": ["luck", "wisdom", "wealth", "growth", "teacher"]
        },
        "Venus": {
            "desc": "love, beauty, comfort, pleasure, relationships",
            "tags": ["love", "beauty", "pleasure", "romance", "arts"]
        },
        "Saturn": {
            "desc": "hard work, discipline, time, responsibility, lessons",
            "tags": ["discipline", "hard work", "duty", "delays", "lessons"]
        },
        "Rahu": {
            "desc": "desire, ambition, unconventional ways, sudden changes",
            "tags": ["ambition", "desire", "unusual", "obsession"]
        },
        "Ketu": {
            "desc": "spiritual path, letting go, past experiences, mystery",
            "tags": ["spirituality", "detachment", "mystical", "karma"]
        }
    }
    
    # House meanings in simple terms
    houses = {
        1: {
            "name": "Self",
            "desc": "your personality, looks, health, the way people see you",
            "tags": ["appearance", "personality", "health", "identity"]
        },
        2: {
            "name": "Money & Family",
            "desc": "earning money, family relationships, food, possessions",
            "tags": ["wealth", "money", "family", "food", "possessions"]
        },
        3: {
            "name": "Communication",
            "desc": "speaking, writing, siblings, short travels, courage",
            "tags": ["communication", "siblings", "travel", "writing", "courage"]
        },
        4: {
            "name": "Home & Mother",
            "desc": "home, mother, land, property, happiness at home",
            "tags": ["home", "mother", "property", "peace", "family"]
        },
        5: {
            "name": "Love & Children",
            "desc": "romance, fun, children, creativity, intelligence",
            "tags": ["love", "romance", "children", "creativity", "fun"]
        },
        6: {
            "name": "Work & Health",
            "desc": "job, enemies, health issues, service to others",
            "tags": ["work", "job", "health", "enemies", "service"]
        },
        7: {
            "name": "Marriage",
            "desc": "marriage, partner, business partnerships, public image",
            "tags": ["marriage", "partner", "business", "contracts"]
        },
        8: {
            "name": "Inheritance & Secrets",
            "desc": "inheritance, sudden changes, secrets, mysteries, long life",
            "tags": ["inheritance", "transformation", "mysteries", "sudden"]
        },
        9: {
            "name": "Luck & Travel",
            "desc": "luck, higher learning, spirituality, father, long travels",
            "tags": ["luck", "learning", "spirituality", "travel", "father"]
        },
        10: {
            "name": "Career",
            "desc": "job success, authority, reputation, public respect",
            "tags": ["career", "success", "authority", "reputation", "public"]
        },
        11: {
            "name": "Friendships & Gains",
            "desc": "friends, groups, earning money, wishes coming true",
            "tags": ["friends", "groups", "gains", "networking", "wishes"]
        },
        12: {
            "name": "Losses & Spirituality",
            "desc": "expenses, isolation, spirituality, foreign travel, letting go",
            "tags": ["spirituality", "isolation", "foreign", "spiritual"]
        }
    }
    
    # More descriptive interpretations
    interpretations = {
        "Sun": {
            1: "Strong personality, natural leader, confident. People notice you easily. Good for management jobs.",
            2: "Good income through hard work. Likes to spend on family. Can be bossy about money.",
            3: "Good at convincing others, brave in speaking opinion. May argue a lot. Good for sales, teaching.",
            4: "May have distance from mother. Works hard for home and family. Gains property slowly.",
            5: "Creative and romantic, lucky in love. Good with children. Can be proud or stubborn.",
            6: "Strong fighter against enemies. Good at solving problems. Can work too hard and hurt health.",
            7: "Partner may be strong-willed or important. Marriage brings status. Both partners ambitious.",
            8: "May inherit money or property. Lives long despite health worries. Interested in mysteries.",
            9: "Spiritual and lucky. Good teacher. Respected everywhere. May travel for belief/learning.",
            10: "Top career success, natural boss. Gets respect and power at work. Very good placement.",
            11: "Gains through friends and teamwork. Popular in groups. Money comes through hard work.",
            12: "Spiritual path calls you. May live or work alone. Interested in hidden knowledge."
        },
        "Moon": {
            1: "Emotional, sensitive, caring. Face changes with feelings. Good memory. May be moody.",
            2: "Beautiful voice and face. Likes good food and comfort. Money comes and goes easily.",
            3: "Good writer and storyteller. Close to siblings. Travels easily. Imagination is strong.",
            4: "Loves mother very much. Home is very important. Happy family life. Good for real estate.",
            5: "Romantic and creative. Good relationship with children. Can be emotional in love.",
            6: "Helps others with care. Worries about health too much. Good nurse or caregiver.",
            7: "Emotional in marriage. Partner is important. Business with family works well.",
            8: "Hidden feelings, psychic ability. May inherit. Interested in deep subjects.",
            9: "Spiritual and philosophical. Lucky in travels. Values faith and ethics.",
            10: "Popular at work. Shows emotions in public. May change jobs due to feelings.",
            11: "Popular with friends. Cares for group. Money comes through relationships.",
            12: "Spiritual, strange dreams. May move to foreign place. Sacrifice for spirituality."
        },
        "Mars": {
            1: "Brave and aggressive. Strong body. Quick to fight or argue. Good for sports, army.",
            2: "Spends money quickly. Talks harsh. May have teeth problems. Sharp with words.",
            3: "Good fighter, bold communication. May argue with siblings. Brave and independent.",
            4: "Fights with family. May leave home. Land or property disputes. Mother stress.",
            5: "Passionate in love. May have children trouble. Risk-taker. Loves sports.",
            6: "Excellent at beating enemies. Strong fight ability. Good health from exercise.",
            7: "Husband/partner is tough. Marriage has passion but fights. Business conflicts.",
            8: "Interested in forbidden things. Long life but accidents. Intense personality.",
            9: "Spiritual fighter. Fights for beliefs. May hurt people's feelings with words.",
            10: "Great career success. Engineer, doctor, soldier - all good. Boss material.",
            11: "Wins over friends. Leads groups. Money through hard effort and success.",
            12: "Fights with hidden enemy. May live alone. Spiritual warrior energy."
        },
        "Mercury": {
            1: "Smart, talkative, quick learner. Always busy with ideas. May jump between things.",
            2: "Good trader and businessman. Clever with money. Pretty voice. Good storyteller.",
            3: "Natural writer, teacher, speaker. Best placement for Mercury. Excellent communicator.",
            4: "Smart about property and land. Good brain for home business. Close to mother.",
            5: "Clever and creative. Good teacher. Children are smart. Can be over-talkative.",
            6: "Analytical mind, good for detailed work. Medical or technical field good.",
            7: "Partner is smart. Business partnership good. Marriage through communication.",
            8: "Loves uncovering secrets. Good detective or researcher. Mysterious communication.",
            9: "Excellent teacher and writer. Spiritual teacher good. Learning brings luck.",
            10: "Great career in communication field. Teacher, journalist, sales all good.",
            11: "Makes money through talking and learning. Friends help succeed. Network gains.",
            12: "Secret communication or hidden knowledge. Good researcher. Foreign language good."
        },
        "Jupiter": {
            1: "Very lucky, kind, wise. People trust you. Good health and happiness. Natural teacher.",
            2: "Rich and generous. Good food and comfort life. Clear speech. Family happy.",
            3: "Good communication and teaching. Lucky with travel. Siblings help succeed.",
            4: "Happy family life. Good mother. Property and land gains. Peace at home.",
            5: "Most lucky placement for Jupiter! Creative talent, good children, lucky love.",
            6: "Good doctor or helper. Overcomes enemies. Employer kind. Success through caring.",
            7: "Good marriage partner. Business success. Mutual understanding. Long-lasting.",
            8: "Inherits well. Interested in deep learning. Spirituality brings benefits.",
            9: "Ultimate luck placement! Spiritual, wise, good father. Teaching brings success.",
            10: "Career success through hard work. Authority comes naturally. Always grows.",
            11: "Money through friends and groups. Wishes come true. Many friends. Popular.",
            12: "Spiritual charity. May live abroad. Spiritual learning and growth."
        },
        "Venus": {
            1: "Beautiful and charming. Gets what wants. Artistic. Love comes easily. May be lazy.",
            2: "Beautiful face and voice. Loves luxury and good food. Rich through beauty.",
            3: "Sweet speaking. Good writer. Artistic talent. Charming communication.",
            4: "Beautiful home. Happy family. Mother is kind. Loves comfort and luxury.",
            5: "Most lucky for Venus! Romantic, artistic, creative. Love life very good.",
            6: "Service work is pleasant. Pets love you. May lack courage. Work happiness.",
            7: "Excellent marriage! Partner is beautiful or kind. Business success. Happiness.",
            8: "Secret love possible. Magnetic personality. May inherit through marriage.",
            9: "Loves travel and art. Spiritual beauty. Father kind. Teacher of beauty/arts.",
            10: "Success in beauty, entertainment, hospitality field. Public loves you.",
            11: "Money through friendship groups. Beautiful friends. Enjoyment through group.",
            12: "Hidden creative ability. May have secret relationship. Spiritual romanticism."
        },
        "Saturn": {
            1: "Serious, responsibility-loving. Looks older. Long hard work pays off. Careful.",
            2: "Slow money gain but solid. Saves carefully. Family may be distant. Talks slow.",
            3: "Hard work in learning and speaking. Siblings may be problems. Disciplined.",
            4: "Mother may be distant or sick. Home struggles early but gains later. Sad.",
            5: "Late children or few children. Takes relationships seriously. Hard work needed.",
            6: "Excellent at overcoming enemies. Strong discipline. Success through hard work.",
            7: "Late marriage but long-lasting. Serious partner. Business needs hard work.",
            8: "Long life despite worries. Slow inheritance. Interest in deep study.",
            9: "Spiritual but strict path. Travel is delayed. Father may be distant.",
            10: "Ultimate success! Slow climb to top but reaches very high. Very lucky placement.",
            11: "Slow gains but solid. Friends become mentor. Responsibility increases.",
            12: "Spiritual discipline. May isolate. Meditation and research good. Sacrifice."
        },
        "Rahu": {
            1: "Wants recognition badly. Unusual personality. Confused about identity.",
            2: "Wants money desperately. Deceptive in speech. Money comes and goes.",
            3: "Obsessed with talking and travel. Deceptive communication. Lies possible.",
            4: "Wants property badly. Mother problems. Home life unsettled. Adoption possible.",
            5: "Desperate for love. May not have children. Risky behavior. Gambling bad.",
            6: "Defeats enemies. May lie and cheat. Enemies through deception.",
            7: "Deceptive partner or foreign marriage. Multiple marriages possible. Drama.",
            8: "Inheritance disputes. Secrets and deception. Sudden life changes.",
            9: "Wrong spiritual path. Fake guru. Confusing beliefs. Travel for gain.",
            10: "Career success through manipulation. Reputation crises. Sudden rise and fall.",
            11: "Gains through deception. Wrong friends. Network works but with lies.",
            12: "Imprisonment or hospital possible. Addiction risk. Foreign settlement."
        },
        "Ketu": {
            1: "Spiritual but confused. Accidents possible. Not interested in worldly success.",
            2: "Hard to earn money. Loss and poverty. Poor speech. No family comfort.",
            3: "Not interested in communication. Spiritual learning. Sibling separation.",
            4: "Separated from mother. Moves often. Spiritual than family focus.",
            5: "No children or few. Not interested in romance. Spiritual expression.",
            6: "Detached from enemies. Healing ability. Mysterious illness possible.",
            7: "Separated from partner. Not interested in marriage. Spiritual union.",
            8: "Deep researcher. Occult knowledge. Long life with transformation.",
            9: "Spiritual wisdom from past. Father separation. Enlightenment seeking.",
            10: "Not interested in fame. Spiritual leadership. Career changes.",
            11: "No interest in social gains. Spiritual friends. Detached from group.",
            12: "Maximum spirituality. Monastery life possible. Healing through surrender."
        }
    }
    
    # Generate entries with better descriptions and tags
    for planet, planet_data in planet_info.items():
        for house_num, house_data in houses.items():
            interp = interpretations.get(planet, {}).get(house_num, 
                f"{planet} in {house_data['name']}: Brings combined effects of {planet_data['desc']} on {house_data['desc']}.")
            
            entry = {
                "id": f"{planet.lower()}_{house_num}h",
                "text": interp,
                "metadata": {
                    "planet": planet,
                    "house": house_num,
                    "house_name": house_data['name'],
                    "type": "planet_house_placement",
                    "tags": planet_data['tags'] + house_data['tags'],
                    "simple": True
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
    
    print(f"✓ Added {len(new_entries)} enhanced entries with tags and simple language")
    print(f"✓ Total merged dataset: {len(merged_data)} entries")
    print(f"✓ Saved to: {output_path}")
    
    return output_path

if __name__ == "__main__":
    print("🔮 Enhancing Vedic Astrology Dataset with Simple Language & Tags\n")
    
    # Generate enhanced entries
    enhanced = enhance_data()
    print(f"✓ Generated {len(enhanced)} enhanced planet-house entries")
    
    # Merge with existing data
    output_file = merge_with_existing(enhanced)
    
    print(f"\n✨ Enhancement complete!")
    print(f"\nNext steps:")
    print(f"  1. Run: python -m db.build-index")
    print(f"     (will auto-detect enhanced data)")


