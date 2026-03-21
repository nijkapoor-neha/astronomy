import swisseph as swe
from datetime import datetime, timedelta

# ✅ Set Lahiri Ayanamsa (Vedic astrology)
swe.set_sid_mode(swe.SIDM_LAHIRI)

swe.set_ephe_path("")

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def calculate_lagna(date_str, time_str, lat, lon):
    # Parse local time (IST)
    dt_local = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")

    # 🔥 Convert IST → UTC
    dt_utc = dt_local - timedelta(hours=5, minutes=30)

    # Convert to Julian Day (UTC!)
    jd = swe.julday(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0
    )
    flags = swe.FLG_SIDEREAL
    # Calculate houses (sidereal)
    houses, ascmc = swe.houses_ex(jd, lat, lon, b'W',flags)

    asc_degree = ascmc[0]

    lagna_sign = SIGNS[int(asc_degree // 30)]

    return lagna_sign, asc_degree