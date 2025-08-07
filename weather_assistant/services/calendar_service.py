# weather_assistant/services/calendar_service.py

from pydantic import BaseModel
from typing import List

# Calendar Event Modeli
class CalendarEvent(BaseModel):
    name: str
    date: str  # Format: DD.MM.YYYY
    time: str  # Format: HH:MM
    participants: list[str]

# Hafızada etkinlikleri tutan liste (Veritabanı yerine geçici çözüm)
events: List[CalendarEvent] = []

def save_to_calendar(event: CalendarEvent) -> str:
    """Yeni bir etkinliği hafızadaki listeye ekler."""
    events.append(event)
    return f"Takvime kaydedildi: {event.name} - {event.date} {event.time} - Katılımcılar: {', '.join(event.participants)}"

def get_events_for_day(date_str: str) -> str:
    """Belirli bir tarihteki etkinlikleri listeler."""
    day_events = [e for e in events if e.date == date_str]
    if not day_events:
        return "Bu tarihte plan yok."
    return "\n".join([f"{e.time} - {e.name} (Katılımcılar: {', '.join(e.participants)})" for e in day_events])