# weather_assistant/services/event_parser.py

from datetime import datetime
from weather_assistant.services.calendar_service import CalendarEvent
from weather_assistant.config import TURKISH_MONTHS

class EventParser:
    @staticmethod
    def parse(text_input: str) -> CalendarEvent:
        """Kullanıcı metnini analiz ederek bir takvim etkinliği oluşturur."""
        text_lower = text_input.lower()
        today = datetime.now()
        event_date = today

        # Metinden tarih ve ay ayıklama
        for month_tr, month_num in TURKISH_MONTHS.items():
            if month_tr in text_lower:
                try:
                    # Ay isminden önceki kelimenin sayısal kısmını al
                    day_str = text_lower.split(month_tr)[0].strip().split()[-1]
                    day = int(''.join(filter(str.isdigit, day_str)))
                    # Yıl olarak 2025 varsayıyoruz, projenize göre değiştirebilirsiniz
                    event_date = datetime(2025, month_num, day)
                    # Etkinlik adını ayıkla
                    name = text_input.split(f"{day} {month_tr.capitalize()}")[1].strip()
                    participants = [name.split("'")[0]] if "'" in name else ["Katılımcılar"]
                    
                    return CalendarEvent(
                        name=name,
                        date=event_date.strftime("%d.%m.%Y"),
                        time="12:00",  # Varsayılan saat
                        participants=participants
                    )
                except (ValueError, IndexError):
                    # Eğer tarih ayrıştırılamazsa, bugünü varsayarak devam et
                    pass
        
        # Eğer metinden tarih çıkarılamazsa, bugünü varsay ve tüm metni isim olarak al
        return CalendarEvent(
            name=text_input if text_input else "Genel Etkinlik",
            date=today.strftime("%d.%m.%Y"),
            time="09:00",
            participants=["Ben"]
        )