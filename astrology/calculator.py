import swisseph as swe
from datetime import datetime, timedelta

swe.set_sid_mode(swe.SIDM_LAHIRI)
swe.set_ephe_path("")

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini",
    "Mrigashira", "Ardra", "Punarvasu", "Pushya",
    "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha",
    "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,
    "Ketu": swe.MEAN_NODE
}

def get_nakshatra(degree):
    nak_size = 360 / 27  # 13°20′
    nak_index = int(degree / nak_size)
    return NAKSHATRAS[nak_index], nak_index


def get_pada(degree):
    nak_size = 360 / 27
    pada_size = nak_size / 4  # each nakshatra has 4 padas

    remainder = degree % nak_size
    pada = int(remainder / pada_size) + 1

    return pada


def calculate_full_chart(date_str, time_str, lat, lon):
    date_normalized = date_str.strip().replace("/", "-").replace(".", "-").replace(":", "-")
    time_normalized = time_str.strip().replace(".", ":")

    # Parse time
    parts = time_normalized.split(":")
    hour = int(parts[0])
    minute = int(parts[1]) if len(parts) > 1 else 0

    year, month, day = [int(x) for x in date_normalized.split("-")][:3]

    dt_local = datetime(year, month, day, hour, minute)

    # IST → UTC
    dt_utc = dt_local - timedelta(hours=5, minutes=30)

    jd = swe.julday(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0
    )

    flags = swe.FLG_SIDEREAL

    # 🔮 Lagna
    houses, ascmc = swe.houses_ex(jd, lat, lon, b'W', flags)
    asc_degree = ascmc[0]
    lagna_sign = SIGNS[int(asc_degree // 30)]

    chart = {
        "lagna": lagna_sign,
        "lagna_degree": asc_degree,
        "planets": {}
    }

    # 🌙 Moon (IMPORTANT for birth nakshatra)
    moon_deg = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
    moon_nak, _ = get_nakshatra(moon_deg)
    moon_pada = get_pada(moon_deg)

    chart["birth_nakshatra"] = moon_nak
    chart["birth_nakshatra_pada"] = moon_pada

    # 🌍 Planets
    for name, planet in PLANETS.items():
        pos = swe.calc_ut(jd, planet, swe.FLG_SIDEREAL)[0][0]

        if name == "Ketu":
            pos = (chart["planets"]["Rahu"]["degree"] + 180) % 360

        sign = SIGNS[int(pos // 30)]
        house = int(((pos - asc_degree) % 360) // 30) + 1

        nak, _ = get_nakshatra(pos)
        pada = get_pada(pos)

        chart["planets"][name] = {
            "degree": pos,
            "sign": sign,
            "house": house,
            "nakshatra": nak,
            "pada": pada
        }

    return chart