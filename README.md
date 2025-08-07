# Weather Assistant 🌤️

Türkçe destekli hava durumu asistanı uygulaması. Bu proje, hava durumu verilerini çekip kullanıcıya görsel bir arayüz ile sunan ve hava durumuna göre müzik önerileri yapan bir web uygulamasıdır.

## 🚀 Özellikler

- **Hava Durumu Sorgulama**: Şehir adına göre güncel hava durumu bilgisi
- **Türkçe Destek**: Tam Türkçe arayüz ve dil desteği
- **Müzik Önerileri**: Hava durumuna göre otomatik müzik önerileri
- **Gradio Arayüzü**: Modern ve kullanıcı dostu web arayüzü
- **API Entegrasyonu**: WeatherAPI.com servisi ile entegrasyon
- **Çevre Değişken Yönetimi**: Güvenli API anahtarı yönetimi

## 🛠️ Teknolojiler

- **Python 3.x**
- **Gradio** - Web arayüzü framework'ü
- **Requests** - HTTP istekleri için
- **Python-dotenv** - Çevre değişkenleri yönetimi
- **Pydantic** - Veri validasyonu
- **Gradio-calendar** - Takvim widget'ı

## 📁 Proje Yapısı

```
Weather-Assistant/
├── weather_assistant/
│   ├── __init__.py
│   ├── main.py              # Ana uygulama dosyası
│   ├── config.py            # Konfigürasyon ve sabitler
│   ├── requirements.txt     # Bağımlılıklar
│   ├── .env                 # Çevre değişkenleri (GİT'e dahil değil)
│   ├── .env.example         # Örnek çevre değişkenleri dosyası
│   ├── .gitignore          # Git ignore kuralları
│   └── ui/
│       └── interface.py     # Gradio arayüz tanımlaması
└── README.md
```

## ⚡ Hızlı Başlangıç

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/your-username/Weather-Assistant.git
cd Weather-Assistant
```

### 2. Sanal Ortam Oluşturun ve Aktifleştirin
```bash
# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktifleştir (Windows)
venv\Scripts\activate

# Sanal ortamı aktifleştir (macOS/Linux)
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
cd weather_assistant
pip install -r requirements.txt
```

### 4. API Anahtarlarını Yapılandırın
```bash
# .env.example dosyasını kopyalayın
copy .env.example .env
```

`.env` dosyasını düzenleyip kendi API anahtarlarınızı girin:
```env
WEATHER_API_KEY="your_weather_api_key_here"
OPENAI_API_KEY="your_openai_api_key_here_if_needed"
```

### 5. Uygulamayı Çalıştırın
```bash
python main.py
```

Uygulama varsayılan olarak `http://localhost:7860` adresinde çalışacaktır.

## 🔑 API Anahtarı Alma

### WeatherAPI.com
1. [WeatherAPI.com](https://www.weatherapi.com/) adresine gidin
2. Ücretsiz hesap oluşturun
3. API anahtarınızı alın
4. `.env` dosyasındaki `WEATHER_API_KEY` değişkenine ekleyin

### OpenAI (Opsiyonel)
Gelecekteki özellikler için OpenAI API anahtarı gerekebilir:
1. [OpenAI Platform](https://platform.openai.com/) hesabı oluşturun
2. API anahtarınızı alın
3. `.env` dosyasındaki `OPENAI_API_KEY` değişkenine ekleyin

## 🎵 Müzik Önerileri

Uygulama hava durumuna göre otomatik müzik önerileri yapar:

- **☔ Yağmur**: Adele - Set Fire to the Rain, Rihanna - Umbrella
- **☀️ Güneşli**: The Beatles - Here Comes the Sun, Walking on Sunshine
- **❄️ Soğuk**: Coldplay - Viva La Vida, Dean Martin - Let It Snow
- **🔥 Sıcak**: Nelly - Hot in Herre, Summer in the City
- **🎶 Varsayılan**: Pharrell Williams - Happy, What a Wonderful World

## 🌍 Türkçe Destek

Uygulama tam Türkçe destek sağlar:
- Türkçe ay isimleri
- Türkçe hava durumu açıklamaları
- Türkçe kullanıcı arayüzü

## 🔧 Konfigürasyon

### Sabitler ([config.py](weather_assistant/config.py))
- `SONG_SUGGESTIONS`: Hava durumuna göre müzik önerileri
- `TURKISH_MONTHS`: Türkçe ay isimleri haritalama
- `BASE_URL`: WeatherAPI.com temel URL'i

## 🚨 Güvenlik

- `.env` dosyası Git'e dahil edilmemiştir
- API anahtarları çevre değişkenleri olarak saklanır
- `.gitignore` dosyası hassas bilgileri korur

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🐛 Bilinen Sorunlar ve Çözümler

### Sanal Ortam Aktivasyonu Sorunu (Windows PowerShell)
Eğer PowerShell'de sanal ortam aktivasyonu çalışmıyorsa:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### API Anahtarı Hatası
Eğer "WEATHER_API_KEY çevre değişkeni tanımlı değil" hatası alıyorsanız:
1. `.env` dosyasının doğru konumda olduğundan emin olun
2. API anahtarının doğru formatta olduğunu kontrol edin
3. Uygulamayı yeniden başlatın

## 📞 Destek

Herhangi bir sorun yaşarsanız:
- Issue oluşturun
- Projeyi yıldızlamayı unutmayın ⭐

## 🔄 Gelecek Özellikler

- [ ] Haftalık hava durumu tahmini
- [ ] Grafik ve chart desteği
- [ ] Konum tabanlı otomatik hava durumu
- [ ] Push notification desteği
- [ ] Mobil uygulama versiyonu
- [ ] AI destekli hava durumu yorumları

---

**Not**: Bu proje eğitim ve öğrenme amaçlı geliştirilmiştir. Ticari kullanım için API limitlerini kontrol edin.