# weather_assistant/main.py

from weather_assistant.ui.interface import create_ui

if __name__ == "__main__":
    # Arayüzü oluştur
    demo = create_ui()
    
    # Uygulamayı başlat
    demo.launch()