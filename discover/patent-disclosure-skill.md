# Yapay zekâ ile patent buluş açıklamalarını otomatikleştirin

Python tabanlı Patent Disclosure Skill, teknik buluş taslaklarını analiz ederek resmi patent formatına uygun teknik açıklamalar, istemler (claims) ve önceki teknik (prior art) karşılaştırmaları üretir.

- ★ 6.058
- Python
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 6.058, otomatik istem (claim) ağacı üretimi ve önceki teknik analiz desteği.

## Ne kazandırır?
- Yapılandırılmış patent metni üretimi: Buluşun teknik alanı, arka planı, özeti ve detaylı açıklama bölümlerini standart patent normlarına uygun oluşturma.
- Bağımsız ve bağımlı istem (Claim) ağacı: Hukuki koruma kapsamını maksimize eden hiyerarşik patent istem listelerini otomatik formüle etme.
- Önceki teknik (Prior Art) fark analizi: Mevcut teknolojilerle buluş arasındaki teknik farkları ve yenilik basamağını net vurgulama.
- Patent vekilleriyle işbirliğini hızlandırma: Mühendislerin taslaklarını patent vekillerine hazır, düzenli teknik dokümanlara dönüştürerek maliyet ve zaman tasarrufu.
- Çok dilli patent terminolojisi desteği: İngilizce, Türkçe ve uluslararası patent kurumlarının (WIPO, EPO, USPTO) terminolojisine uyum.

## Kurulum

**Depoyu klonlama ve bağımlılıkları yükleme**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```

## Çalıştırma

**Patent analiz ve açıklama üretimini başlatma**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```

## Teknik mimari ve çalışma prensibi

Patent Disclosure Skill, teknik belgeleri patent kurallarına göre ayrıştıran aşamalı bir ajan iş akışı işletir:
- Teknik Buluş Ayrıştırma Motoru: Yazılım, donanım veya kimyasal proses açıklamalarındaki anahtar girdileri, çıktıları ve metodolojiyi tespit eder.
- İstem (Claim) Sentaks Doğrulayıcı: İstemlerdeki belirsiz (vague) ifadeleri ve biçimsel hataları denetleyen hukuki dil analizörü.
- Şablon ve Markdown Dışa Aktarımı: Resmi patent başvurularında kullanılmak üzere dokümanı standart bölümlere ayrılmış Markdown formatında kaydetme.

## Patent analiz iş akışları ve istem hazırlama

Ar-Ge ekipleri ve patent uzmanları bu aracı fikri mülkiyet süreçlerini hızlandırmak için kullanır:
- Yazılım Algoritmalarını Patentlenebilir Biçime Çevirme: Kod ve mimari şemalarından patent otoritelerinin kabul edeceği yöntem ve sistem açıklamaları türetme.
- Ofis Aksiyonlarına (Office Actions) Karşı Savunma: Patent inceleme uzmanlarının itirazlarına karşı buluşun ayırt edici özelliklerini listeleyen yanıt taslakları oluşturma.
- Fikri Mülkiyet Portföyü Denetimi: Şirket içi teknolojik projelerin patent potansiyeli taşıyan buluş basamaklarını erkenden haritalandırma.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Geliştirdiğim dağıtık bir veritabanı önbellekleme algoritması için patent disclosure skill kullanarak resmi bir buluş bildirim metni hazırlamak istiyorum. Algoritmanın akışını girdi olarak verip bağımsız istemleri, buluşun teknik alanını ve önceki teknikle olan farkları nasıl üreteceğimi adım adım açıklar mısın?

- **Kimin için:** Patent vekilleri, fikri mülkiyet yöneticileri, Ar-Ge mühendisleri ve mucitler. 
- **Lisans:** MIT (Özgür açık kaynak lisansı) 
- **Çatı:** Python Tabanlı Patent Ajanı Yeteneği 
- **Platformlar:** Linux, macOS, Windows 

## Sıkça sorulan sorular
- Bu araç resmi bir patent vekilinin yerini tutar mı? Hayır. Patent Disclosure Skill mühendislerin buluş taslaklarını düzenleyip vekillere hazır hale getiren bir ön hazırlık ve verimlilik aracıdır; hukuki başvuru vekille yapılmalıdır.
- Hangi LLM modelleriyle çalışır? Claude 3.5 Sonnet, GPT-4o veya yerel açık ağırlıklı modellerle (Qwen, Llama 3) çalışacak şekilde yapılandırılabilir.
- Gizli teknik sırlarım internete sızar mı? Yerel bir LLM (Ollama veya vLLM) ile çalıştırıldığında tüm patent analizleri tamamen yerel bilgisayarınızda yapılır, hiçbir veri dışarı çıkmaz.
- Patent çizimleri ve akış şemalarını yorumlayabilir mi? Multimodal modeller bağlandığında sistem mimarisi ve blok diyagram görsellerini de analiz ederek metne dökebilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/handsomestWei/patent-disclosure-skill)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ LLM Açık Kaynak CLI API

---
Kaynak: TreScout Keşif · https://trescout.com/discover/patent-disclosure-skill/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
