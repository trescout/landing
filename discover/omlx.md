# Mac bilgisayarlar için yapay zekâ sunucusu

Omlx, Apple Silicon (M1/M2/M3/M4) işlemcili Mac bilgisayarlar için sürekli yığınlama (continuous batching) ve SSD önbellekleme (SSD caching) yetenekleri sunan yeni nesil bir yerel büyük dil modeli (LLM) çıkarım sunucusudur. Apple MLX altyapısını OpenAI uyumlu API ve macOS menü çubuğu arayüzüyle birleştirir.

- ★ 21.147
- Python
- GitHub Trending · 2026-08-18

## Güncelleme
- 31 Ağustos 2026: Yıldız 20.793 → 21.147, son sürüm v0.6.4 (29 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 20.069 → 20.793, son sürüm v0.6.3rc3 (24 Ağustos 2026).
- 20 Ağustos 2026: Yıldız 19.758 → 20.069, son sürüm v0.6.3rc2 (20 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 19.519 → 19.758, son sürüm v0.6.3rc1 (19 Ağustos 2026).

## Ne kazandırır?
- Apple MLX ve Metal donanım ivmesi: Apple Silicon işlemcilerin Birleşik Bellek Mimarisi'ni (UMA) doğrudan kullanarak CPU ile GPU arasındaki bellek kopyalama darboğazını tamamen ortadan kaldırır.
- Sürekli yığınlama (Continuous Batching): Eşzamanlı gelen çok sayıda kullanıcı ve ajan istemini tek bir hesaplama döngüsünde birleştirerek sunucu verimini 3 kata kadar artırır.
- SSD önbellekleme ve parça ön dolumu (Chunked Prefill): Uzun bağlam pencerelerinde (context window) anahtar-değer (KV) önbelleğini NVMe SSD üzerinde saklayarak bellek yetersizliği (OOM) kilitlenmelerini önler.
- OpenAI uyumlu standart API: /v1/chat/completions ve /v1/models uç noktaları sayesinde Cursor, Open WebUI, Continue ve LangChain araçlarıyla sıfır konfigürasyonla çalışır.
- macOS menü çubuğu kontrolü: Terminale girmeden sunucuyu başlatma, durdurma, model seçme ve bellek tüketimini canlı grafiklerle izleme pratikliği sunar.

## Kurulum

**Homebrew ile kurulum**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Çalıştırma

**Arka plan servisini başlatma**

```
omlx start
```

**Belirli bir modeli indirme ve sunma**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Teknik mimari ve çalışma prensibi

Omlx, Apple araştırmacıları tarafından geliştirilen MLX makine öğrenimi çatısı üzerine inşa edilmiştir. Geleneksel çıkarım araçlarının (llama.cpp veya Ollama gibi) Mac üzerindeki sınırlarını aşmak için tasarlanmış üç temel mimari sütuna dayanır:
- Birleşik bellekten (UMA) tam yararlanma: Ayrık ekran kartına sahip PC'lerin aksine Apple Silicon Mac'lerde 128 GB veya 192 GB RAM doğrudan GPU çekirdekleri tarafından adreslenebilir. Omlx, Metal Shading Language (MSL) çekirdekleriyle bu devasa bellek havuzunu sıfır gecikmeyle işler.
- Dinamik KV önbellek yönetimi (PagedAttention): Çoklu oturumlarda bellek parçalanmasını engellemek için anahtar-değer tensörlerini sayfalanmış bloklar halinde tahsis eder. İstem bittiğinde kullanılan bellek derhal serbest bırakılır.
- SSD'ye taşan önbellek katmanı: 32K ve 128K gibi devasa bağlam pencerelerinde KV önbelleği RAM'i aştığında, Omlx otomatik olarak Apple'ın yüksek hızlı tümleşik SSD diskine sayfalama (paging) yapar. Böylece model çökmeden çıkarıma devam eder.

## OpenAI uyumlu yerel API entegrasyonu

Omlx başlatıldığında yerel makinenizde (varsayılan olarak http://localhost:8000 portunda) OpenAI uyumlu bir REST API sunar. Bu sayede kod editörlerinizi ve yapay zekâ uygulamalarınızı yerel modellerle besleyebilirsiniz:

**cURL ile API Testi**

```
curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "default",
"messages": [{"role": "user", "content": "Apple Silicon mimarisinin temel avantajı nedir?"}],
"temperature": 0.7
}'
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Apple Silicon Mac bilgisayarımda Omlx sunucusunu kullanarak yerel bir büyük dil modelini çalıştırmak istiyorum. Homebrew ile kurulumu tamamladıktan sonra sunucuyu arka planda çalıştıracak, menü çubuğundan model seçimini yönetecek ve Cursor kod editörü veya Python openai kütüphanesi üzerinden bu yerel modele nasıl bağlanacağımı adım adım açıklar mısın?

- **Kimin için:** Apple Silicon işlemcili Mac bilgisayarlarında büyük dil modellerini (LLM) en yüksek hızda ve yerel gizlilikle çalıştırmak isteyen yapay zekâ geliştiricileri içindir. 
- **Lisans:** Apache-2.0 (Açık kaynak lisansı) 
- **Çatı:** Apple MLX ve Python tabanlı yerel çıkarım motoru 
- **Donanım:** Apple Silicon M1, M2, M3, M4 serisi (Pro, Max, Ultra destekli) 

## Sıkça sorulan sorular
- Omlx ile Ollama arasındaki temel fark nedir? Ollama genel olarak C++ tabanlı llama.cpp altyapısını kullanırken, Omlx doğrudan Apple tarafından geliştirilen MLX çerçevesi üzerinde çalışır. Bu sayede Apple Silicon çiplerinin Metal ve nöral motor birimleriyle daha derin entegrasyon kurarak özellikle sürekli yığınlama ve uzun bağlamlarda daha yüksek token üretim hızı sağlar.
- 16 GB veya 24 GB RAM ile hangi modeller çalıştırılabilir? 4-bit kuantize edilmiş 8B parametreli modeller (Llama 3, Qwen 2.5, Mistral) yaklaşık 5-6 GB bellek kaplar ve 16 GB Mac'lerde son derece akıcı çalışır. 24 GB veya 36 GB birleşik belleğe sahip cihazlarda ise 14B veya 32B modeller rahatlıkla yüklenebilir.
- SSD önbellekleme Mac'in disk ömrünü yıpratır mı? Hayır. Omlx önbelleğe alma işlemlerinde gereksiz yazma döngülerini engellemek için akıllı tamponlama algoritmaları kullanır. Yalnızca bağlam belleği RAM sınırına yaklaştığında devreye girer ve disk aşınmasını minimumda tutar.
- Intel tabanlı eski Mac bilgisayarlarda çalışır mı? Hayır. Omlx, Apple Silicon (ARM mimarisi) ve Apple MLX çatısına özel optimize edilmiştir. Intel tabanlı Mac'lerde veya Windows/Linux x86 bilgisayarlarda çalışmaz.

## Bağlantılar
- [GitHub deposu →](https://github.com/jundot/omlx)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Apple Silicon Continuous Batching LLM Local Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/omlx/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
