def build_lagna_query(lagna_sign):
    return f"{lagna_sign} lagna personality traits and life effects"

def build_queries(chart):
    queries = []

    # 🔮 Lagna - core identity
    lagna = chart['lagna']
    queries.append(f"{lagna} Ascendant rising sign personality")
    queries.append(f"{lagna} Lagna native character traits")

    # 🌙 Moon Nakshatra (most important for emotional nature)
    moon = chart["planets"]["Moon"]
    moon_nak = moon['nakshatra']
    queries.append(f"{moon_nak} Moon nakshatra emotional nature")
    queries.append(f"{moon_nak} nakshatra psychology behavior")
    
    # 🔥 Sun position - core essence
    sun = chart["planets"]["Sun"]
    queries.append(f"{sun['sign']} Sun sign ego identity purpose")
    queries.append(f"{sun['nakshatra']} Sun nakshatra vitality")

    # 💫 Key planet placements with house meaning
    important_planets = ["Jupiter", "Saturn", "Venus", "Mars"]
    for planet in important_planets:
        if planet in chart["planets"]:
            info = chart["planets"][planet]
            house = info['house']
            nak = info['nakshatra']
            # Query by nakshatra + significance
            queries.append(f"{nak} {planet} influence life")
            queries.append(f"{planet} in house {house} effects")

    # 🌙 Moon sign - emotional expression
    moon_sign = moon['sign']
    queries.append(f"{moon_sign} Moon sign emotional response")

    return queries