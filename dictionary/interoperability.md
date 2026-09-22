# Interoperability nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Interoperability (Türkçe karşılığıyla **birlikte çalışabilirlik**), farklı sistemlerin ortak standartlarla veri alışverişi yapabilmesidir.

## Tanım ve Kelime Kökeni
Sözcük, Latince **inter** (arası) ve **operate** (çalışmak) köklerinden gelir. Farklı dillerde veya farklı teknolojilerle yazılmış iki sistemin ortak bir dil konuşarak anlaşmasıdır. Örneğin bir muhasebe programının banka sistemleriyle otomatik konuşabilmesi bu yetenek sayesindedir. Teknolojilerin birbirine bağımlı kalmadan bir ekosistem oluşturmasını sağlar.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Muhasebe ve banka:** Hesap hareketlerinin programa otomatik düşmesi.
- **Şarj aletleri:** USB-C standardı sayesinde tek kabloyla birçok cihazın şarj olması.
- **Akıllı ev:** Farklı markaların Matter standardıyla aynı evde çalışması.
- **e-Fatura:** Türkiye'de firmaların UBL-TR formatıyla birbirine fatura gönderebilmesi.

## Teknik Derinlik ve Mimari
Birlikte çalışabilirlik şu katmanlarda sağlanır:
- **Veri biçimi:** JSON veya XML gibi herkesin okuyabildiği formatlar.
- **Arayüz (API):** Sistemlerin birbirine açtığı tanımlı kapılar.
- **Protokol:** Verinin nasıl taşınacağının kuralları (ör. HTTPS).
- **Kimlik doğrulama:** Kimin hangi veriye erişebileceği (ör. OAuth 2.0).
- **Sürümleme:** Arayüz değişince eskisinin bir süre daha çalışması.

Kural basittir: Ne kadar çok özel (proprietary) format, o kadar az birlikte çalışabilirlik.

## Farklı Disiplinlerde Kullanımı
- **Dil:** Farklı ülkelerden insanların ortak dille anlaşması.
- **Demiryolu:** Hat genişliği standardı sayesinde trenlerin ülke değiştirebilmesi.
- **Elektrik:** Priz ve voltaj standartlarının cihazları uyumlu kılması.

## Bir benzetmeyle
Farklı ülkelerden gelen insanların ortak bir dil kullanarak birbirini anlaması gibidir.

## Sıkça sorulanlar

**Neden her sistemde bu özellik yok?**  
Bazen şirketler sistemlerini bilerek kapalı tutar, bazen de farklı teknolojiler teknik olarak eşleşemez. Açık standart seçmek genellikle uzun vadede kazandırır.

**Birlikte çalışabilirlik nasıl sağlanır?**  
Açık format, belgeli API, standart protokol ve sürüm disipliniyle. Yeni entegrasyon için önce mevcut standartlara bakmanız gerekir.

**Tek standarda bağlı kalmak riskli midir?**  
Tek tedarikçiye kilitlenmek risklidir, açık standarda yaslanmak riski dağıtır. Standardın arkasında geniş topluluk olmasına dikkat edin.

**Güvenliği nasıl etkiler?**  
Kapı açmak saldırı yüzeyini büyütür. Bu yüzden kimlik doğrulama, yetki ve kayıt (log) olmadan arayüz açılmamalıdır.

## İlgili terimler
- [API](/dictionary/api/)
- [API Gateway](/dictionary/api-gateway/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/interoperability/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
