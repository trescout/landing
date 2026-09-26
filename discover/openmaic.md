# Çoklu yapay zekâ ajanlarıyla etkileşimli sınıf simülasyonu

Tsinghua Üniversitesi araştırmacıları tarafından geliştirilen OpenMAIC, öğretmen, öğrenci ve gözlemci rollerindeki çoklu yapay zekâ ajanlarını etkileşimli bir sınıf ortamında buluşturur.

- ★ 25.572
- TypeScript
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 25.572, çoklu ajan rol simülasyonu ve gerçek zamanlı sesli diyalog entegrasyonu.

## Ne kazandırır?
- Rol tabanlı çoklu ajan mimarisi: Öğretmen, soru soran öğrenci, tartışmacı ve özetleyici rollerindeki LLM ajanlarının dinamik etkileşimi.
- Görsel ve sesli sınıf arayüzü: Sanal tahta, anlık soru-cevap akışı ve ses sentezi (TTS) ile sürükleyici pedagojik deneyim.
- Özelleştirilebilir ders müfredatı: Kendi PDF dokümanlarınızı veya metin ders notlarınızı yükleyerek anında etkileşimli ders kurgulama.
- Tek tıkla simülasyon başlatma: Modern web arayüzü üzerinden karmaşık ajan orkestrasyonunu teknik kodlama bilmeden yönetme.
- Açık ağırlıklı model uyumluluğu: Ollama, vLLM veya bulut LLM sağlayıcıları üzerinden istediğiniz yapay zekâ modelini bağlama özgürlüğü.

## Kurulum

**Depoyu klonlama ve bağımlılıkları yükleme**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

## Çalıştırma

**Geliştirme sunucusunu başlatma**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```

## Teknik mimari ve çalışma prensibi

OpenMAIC, çoklu ajan koordinasyonunu yöneten olay tabanlı bir diyalog döngüsü üzerinde çalışır:
- Sohbet Orkestrasyon Motoru: Hangi ajanın ne zaman konuşacağını, söz hakkı sırasını ve tartışma bağlamını yöneten merkezi kontrolör.
- Bellek ve Bağlam Yönetimi: Ders boyunca paylaşılan ortak tahta içeriğini ve öğrenci sorularını kısa/uzun süreli hafızada saklama.
- WebSocket Üzerinden Gerçek Zamanlı Yayın: Frontend arayüzüne konuşma metinlerini, duygusal ifadeleri ve animasyonları gecikmesiz iletme.

## Çoklu ajan sınıf dinamikleri ve rol simülasyonları

OpenMAIC, eğitim teknolojilerinde ve yapay zekâ araştırmalarında yenilikçi uygulama alanları sağlar:
- Sokratik Tartışma Ortamları: Farklı bakış açılarına sahip ajanların bir konu üzerinde tartışarak kullanıcının eleştirel düşünmesini tetiklemesi.
- Kişiselleştirilmiş Öğretmen Desteği: Kullanıcının anlama hızına göre zorluk seviyesini otomatik ayarlayan özel yapay zekâ eğitmenleri.
- Ajanlar Arası Sosyal Etkileşim Araştırmaları: Büyük dil modellerinin kalabalık grup ortamlarında nasıl işbirliği yaptığını ve bilgi paylaştığını analiz etme.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenMAIC platformunda kendi ders notlarımı yükleyerek bir Sokratik tartışma ortamı simüle etmek istiyorum. Ajanların rollerini (öğretmen, meraklı öğrenci, eleştirel sorgulayıcı) nasıl tanımlayacağımı ve yerel bir Ollama modeliyle bu sınıfı nasıl ayağa kaldıracağımı adım adım açıklar mısın?

- **Kimin için:** Eğitimciler, yapay zekâ araştırmacıları, edtech girişimcileri ve öğrenciler. 
- **Lisans:** Apache-2.0 (Açık kaynak lisansı) 
- **Çatı:** TypeScript & Next.js Çoklu Ajan Simülatörü 
- **Platformlar:** Web tarayıcısı, Linux, macOS, Windows 

## Sıkça sorulan sorular
- OpenMAIC'i kullanmak için GPU gerekir mi? Kendi yerel modelinizi çalıştıracaksanız (Ollama/vLLM) GPU önerilir; ancak bulut API'leri (OpenAI, Gemini, Groq) üzerinden standart bir bilgisayarla doğrudan kullanılabilir.
- Kullanıcı simülasyona sesli olarak katılabilir mi? Evet. WebRTC ve ses tanıma modülü sayesinde kullanıcı mikrofonuyla konuşarak sınıftaki tartışmalara dahil olabilir.
- Kaç ajan aynı anda sınıfta bulunabilir? Varsayılan yapılandırmada 3 ile 8 ajan arasında ideal etkileşim sağlanır; sistem kaynaklarına göre daha kalabalık sınıflar kurgulanabilir.
- Ders içeriği hangi formatlarda yüklenebilir? Düz metin, Markdown ve PDF dokümanları doğrudan sistemin bilgi tabanına aktarılabilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/THU-MAIC/OpenMAIC)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ LLM Açık Kaynak API Framework

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openmaic/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
