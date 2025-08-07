# weather_assistant/services/assistant_service.py

import random
from weather_assistant.config import SONG_SUGGESTIONS

def suggest_clothing(temp: float, condition: str) -> str:
    """Hava durumuna göre giyim ve şarkı önerisi yapar."""
    song_key = "default"
    if temp <= 5:
        clothing_advice = "❄️ Çok soğuk! Kalın bir mont, atkı, bere ve eldiven önerilir."
        song_key = "soğuk"
    elif 5 < temp <= 15:
        clothing_advice = "🧥 Hava serin. Bir hırka veya hafif bir mont giyebilirsin."
    elif 15 < temp <= 25:
        clothing_advice = "👕 Hava ılık. Hafif bir tişört veya gömlek yeterli."
    else:
        clothing_advice = "☀️ Hava sıcak! Şort, tişört veya hafif bir elbise tercih edebilirsin."
        song_key = "sıcak"

    condition_lower = condition.lower()
    if "yağmur" in condition_lower:
        clothing_advice += "\n☔ Yağmur var. Şemsiye ve su geçirmez ayakkabı almayı unutma!"
        song_key = "yağmur"
    elif "güneş" in condition_lower:
        song_key = "güneş"

    song = random.choice(SONG_SUGGESTIONS.get(song_key, SONG_SUGGESTIONS["default"]))
    return f"{clothing_advice}\n\n🎵 Günün Şarkısı: {song}"

def check_suitability(condition: str, event_name: str) -> str:
    """Hava durumunun planlanan etkinlik için uygunluğunu kontrol eder."""
    condition_lower = condition.lower()
    if "yağmur" in condition_lower or "kar" in condition_lower:
        if "toplantı" in event_name.lower() or "sinema" in event_name.lower():
            return "Hava kapalı mekan etkinliği için uygun, dışarıda dikkatli ol."
        return "❌ Hava açık hava etkinlikleri için uygun değil, planı gözden geçir."
    return "✅ Hava plan için uygun görünüyor."