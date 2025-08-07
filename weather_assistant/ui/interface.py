# weather_assistant/ui/interface.py

import gradio as gr
from datetime import datetime
from gradio_calendar import Calendar

# Servisleri import et
from weather_assistant.services import weather_service, assistant_service, calendar_service, event_parser

def load_css() -> str:
    """CSS dosyasını okur ve string olarak döndürür."""
    with open("weather_assistant/ui/assets/style.css", "r", encoding="utf-8") as f:
        return f.read()

def create_ui():
    """Gradio arayüzünü oluşturur ve döndürür."""

    # --- Olay Yöneticisi Fonksiyonlar ---
    def handle_process_plan(text_input: str, city: str):
        """'Planla ve Kaydet' butonuna tıklandığında çalışır."""
        event = event_parser.EventParser.parse(text_input)
        
        weather_data = weather_service.get_weather(city, event.date)
        
        if "error" in weather_data:
            return weather_data["error"], "", "", "", None

        hourly_forecast = "### Saatlik Tahmin\n" + "\n".join(
            [f"⏰ {h['time'].split(' ')[1]}: {h['temp_c']}°C, {h['condition']['text']}" for h in weather_data.get('hourly', [])]
        )
        weather_output = (
            f"![Hava Durumu]({weather_data['icon']})\n"
            f"📅 **Tarih:** {weather_data['date']}\n"
            f"🌡️ **Sıcaklık:** {weather_data['temp']}°C\n"
            f"🌤️ **Hava Durumu:** {weather_data['condition']}\n\n{hourly_forecast}"
        )
        
        suitability = assistant_service.check_suitability(weather_data['condition'], event.name)
        clothing = assistant_service.suggest_clothing(weather_data['temp'], weather_data['condition'])
        calendar_result = calendar_service.save_to_calendar(event)
        
        return weather_output, suitability, clothing, calendar_result, None

    def handle_show_day_details(selected_date: datetime, city: str):
        """Takvimden bir tarih seçildiğinde çalışır."""
        if not selected_date:
            return "Tarih seçilmedi.", "", ""
        
        date_str = selected_date.strftime("%d.%m.%Y")
        weather_data = weather_service.get_weather(city, date_str)
        
        if "error" in weather_data:
            weather_info = weather_data["error"]
            clothing = "Hava durumu bilinmediği için öneri yapılamadı."
        else:
            hourly_forecast = "### Saatlik Tahmin\n" + "\n".join(
                [f"⏰ {h['time'].split(' ')[1]}: {h['temp_c']}°C, {h['condition']['text']}" for h in weather_data.get('hourly', [])]
            )
            weather_info = (
                f"![Hava Durumu]({weather_data['icon']})\n"
                f"📅 **Tarih:** {weather_data['date']}\n"
                f"🌡️ **Sıcaklık:** {weather_data['temp']}°C\n"
                f"🌤️ **Hava Durumu:** {weather_data['condition']}\n\n{hourly_forecast}"
            )
            clothing = assistant_service.suggest_clothing(weather_data['temp'], weather_data['condition'])
        
        plans = calendar_service.get_events_for_day(date_str)
        return weather_info, plans, clothing

    # --- Gradio Arayüz Tanımı ---
    with gr.Blocks(theme=gr.themes.Ocean(), css=load_css(), title="Planlama ve Takvim Asistanı") as demo:
        gr.Markdown("### Planınızı Girin ve Takvime Ekleyin")

        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(label="Plan", placeholder="örn: 20 Mart Sabo'yla tenis maçı")
                city_input = gr.Textbox(label="Şehir", value="Antalya")
                submit_btn = gr.Button("Planla ve Kaydet")

            with gr.Column(elem_classes="output"):
                weather_output = gr.Markdown(label="Hava Durumu")
                suitability_output = gr.Textbox(label="Plan Uygunluğu", interactive=False)
                clothing_output = gr.Textbox(label="Giyim Önerisi", interactive=False)
                calendar_output = gr.Textbox(label="Takvim Durumu", interactive=False)
        
        gr.Markdown("---")
        gr.Markdown("### Takvimi İncele")
        
        with gr.Row():
            date_calendar = Calendar(type="datetime", label="İncelemek için bir tarih seçin", value=datetime.now())
        
        with gr.Row():
            day_weather = gr.Markdown(label="Seçilen Günün Hava Durumu")
            with gr.Column():
                day_plans = gr.Textbox(label="Seçilen Günün Planları", interactive=False)
                day_clothing = gr.Textbox(label="Giyim Önerisi", interactive=False)

        # Olayları bağlama
        submit_btn.click(
            fn=handle_process_plan,
            inputs=[text_input, city_input],
            outputs=[weather_output, suitability_output, clothing_output, calendar_output]
        )
        date_calendar.change(
            fn=handle_show_day_details,
            inputs=[date_calendar, city_input],
            outputs=[day_weather, day_plans, day_clothing]
        )
    return demo