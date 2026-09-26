# Kişisel bilgisayarınızı yerel yapay zekâ sunucusuna dönüştürün

Açık kaynaklı Osmantic/ODS, kişisel donanımınız üzerinde çalışan yerel büyük dil modeli çıkarımı, vektör arama tabanlı RAG boru hatları ve otonom ajan iş akışları kurmanızı sağlar.

- ★ 5.181
- Python
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 5.181, yerel RAG boru hattı ve multimodal model desteği güncellemesi.

## Ne kazandırır?
- Tam veri gizliliği ve yerel yürütme: Verilerinizi harici bulut sunucularına göndermeden yerel GPU ve CPU üzerinde güvenli yapay zekâ işletimi.
- Entegre RAG (Arama Destekli Üretim): Kişisel notlarınızı, şirket belgelerinizi ve kod depolarınızı vektörize ederek anında anlamsal arama yapma.
- Çok modlu (Multimodal) yetenekler: Metin üretimi, konuşma tanıma (Whisper), ses sentezi ve görsel üretimi tek çatı altında buluşturma.
- OpenAI uyumlu yerel API: Mevcut yapay zekâ istemcilerinizi ve araçlarınızı tek bir URL değişikliğiyle yerel ODS sunucunuza yönlendirme.
- Kapsamlı ajan orkestrasyonu: Yerel araçları çağıran ve çok adımlı görevleri otonom olarak çözen akıllı ajan zincirleri.

## Kurulum

**Depoyu klonlama ve ortamı kurma**

```
git clone https://github.com/Osmantic/ODS.git
cd ODS
pip install -e .
```

## Çalıştırma

**Yerel yapay zekâ sunucusunu başlatma**

```
python -m ods.server --port 8000
# Web paneline http://localhost:8000 adresinden erişin
```

## Teknik mimari ve çalışma prensibi

Osmantic/ODS, modüler bir mikro-servis mimarisiyle model çıkarımını ve vektör dizinlemeyi koordine eder:
- Yerel Çıkarım Çekirdeği (llama.cpp & vLLM): GGUF ve saf GPU formatlarındaki modelleri minimum bellek ayak iziyle hızlıca yükleme ve çalıştırma.
- Gömülü Vektör Veritabanı: ChromaDB ve SQLite tabanlı hafif vektör saklama ile belgeleri parçalayıp (chunking) dizinleme.
- Görev Kuyruğu ve Ajan Durum Makinesi: Çok adımlı sorguları ve araç çağırma (tool calling) akışlarını yöneten asenkron işleyiciler.

## Yerel RAG iş akışları ve özel ajan boru hatları

ODS, kurumsal veri gizliliğini koruyarak güçlü yapay zekâ entegrasyonları kurmayı mümkün kılar:
- Gizli Şirket Belgeleriyle Çalışma: Sözleşmeler, finansal tablolar ve kurum içi yazışmaları buluta çıkarmadan yerel RAG ile sorgulayın.
- Yerel Kod Analizi ve Geliştirme Asistanı: Özel yazılım projelerinizi indeksleyerek VS Code veya Cursor üzerinde yerel yapay zekâ kod tamamlaması sağlayın.
- Otonom Veri İşleme Ajanları: Yerel dosya sistemindeki raporları okuyup özetleyen ve format dönüştüren arka plan görevleri tanımlayın.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Kişisel bilgisayarımda ODS sunucusunu kurarak şirketimin PDF belgelerini yerel vektör veritabanına nasıl aktaracağımı, ardından yerel bir Llama 3 modeli üzerinden bu belgelere dayalı RAG soru-cevap sorguları nasıl yapacağımı kod ve terminal adımlarıyla açıklar mısın?

- **Kimin için:** Veri gizliliğine önem veren şirketler, yerel yapay zekâ geliştiricileri ve sistem yöneticileri. 
- **Lisans:** MIT (Özgür açık kaynak lisansı) 
- **Çatı:** Python & llama.cpp Yerel Yapay Zekâ Sunucusu 
- **Platformlar:** Linux, macOS, Windows 

## Sıkça sorulan sorular
- İnternet bağlantısı olmadan tamamen çevrimdışı çalışır mı? Evet. Gerekli model ağırlıkları indirildikten sonra ODS hiçbir ağ bağlantısına ihtiyaç duymadan tamamen çevrimdışı (air-gapped) ortamlarda çalışabilir.
- Hangi model formatlarını destekliyor? GGUF formatındaki tüm açık modelleri (Llama 3, Mistral, Qwen, DeepSeek) ve saf HuggingFace ağırlıklarını destekler.
- Web arayüzü mevcut mu? Evet. ODS yerleşik bir web paneli ile gelir; modelleri yönetebilir, dosya yükleyebilir ve sohbet oturumları açabilirsiniz.
- GPU olmadan yalnızca CPU ile çalışır mı? Evet. llama.cpp çekirdeği sayesinde AVX2/AVX-512 komut setlerini kullanarak saf CPU üzerinde de yüksek verimle çalışabilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/Osmantic/ODS)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ LLM Açık Kaynak API CLI

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ods/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
