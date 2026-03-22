def build_lagna_query(lagna_sign):
    return f"{lagna_sign} lagna personality traits and life effects"

def build_queries(chart):
    queries = []

    # 🔮 Lagna
    queries.append(f"{chart['lagna']} lagna personality traits")

    # 🌙 Moon Nakshatra (very important)
    moon = chart["planets"]["Moon"]
    queries.append(f"{moon['nakshatra']} nakshatra personality and life effects")

    # 🪐 Planets in houses
    for planet, info in chart["planets"].items():
        queries.append(
            f"{planet} in {info['house']} house in {info['sign']} sign effects"
        )

    return queries