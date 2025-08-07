# weather_assistant/services/weather_service.py

import requests
from datetime import datetime
from weather_assistant.config import BASE_URL, WEATHER_API_KEY

def get_weather(city: str, date_str: str) -> dict:
    """Belirtilen şehir ve tarih için hava durumu verisini çeker."""
    try:
        event_date = datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        return {"error": f"Tarih formatı desteklenmiyor: {date_str}"}

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    delta_days = (event_date - today).days

    if delta_days < 0:
        return {"error": f"Geçmiş tarihler için tahmin yapılamaz: {date_str}"}
    if delta_days > 6:
        return {"error": f"Sadece 7 günlük tahminler destekleniyor. ({date_str} geçersiz)."}

    params = {"q": city, "key": WEATHER_API_KEY, "days": 7, "lang": "tr"}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        data = response.json()
        if "error" in data:
            return {"error": data["error"]["message"]}
    except requests.exceptions.RequestException as e:
        return {"error": f"API'ye ulaşılamadı: {e}"}

    forecast = data["forecast"]["forecastday"][delta_days]
    return {
        "date": forecast["date"],
        "condition": forecast["day"]["condition"]["text"],
        "temp": forecast["day"]["avgtemp_c"],
        "icon": "https:" + forecast["day"]["condition"]["icon"],
        "hourly": forecast["hour"][::4]  # Her 4 saatte bir veri alarak sadeleştir
    }