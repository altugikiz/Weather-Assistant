# weather_assistant/config.py

import os
from dotenv import load_dotenv

# .env dosyasındaki çevre değişkenlerini yükle
load_dotenv()

# API Anahtarları ve URL'ler
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Gelecekte kullanılabilir
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

# API Anahtarı kontrolü
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY çevre değişkeni tanımlı değil. Lütfen .env dosyasına ekleyin.")

# Sabitler
SONG_SUGGESTIONS = {
    "yağmur": ["Adele - Set Fire to the Rain", "Rihanna - Umbrella"],
    "güneş": ["The Beatles - Here Comes the Sun", "Katrina and the Waves - Walking on Sunshine"],
    "soğuk": ["Coldplay - Viva La Vida", "Dean Martin - Let It Snow"],
    "sıcak": ["Nelly - Hot in Herre", "The Lovin' Spoonful - Summer in the City"],
    "default": ["Pharrell Williams - Happy", "Louis Armstrong - What a Wonderful World"]
}

# Türkçe aylar için haritalama
TURKISH_MONTHS = {
    "ocak": 1, "şubat": 2, "mart": 3, "nisan": 4, "mayıs": 5, "haziran": 6,
    "temmuz": 7, "ağustos": 8, "eylül": 9, "ekim": 10, "kasım": 11, "aralık": 12
}