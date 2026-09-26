# 34 ücretsiz LLM sağlayıcısını tek API'de birleştirin

FreeLLMAPI, 34 farklı ücretsiz büyük dil modeli sağlayıcısını OpenAI formatında tek bir REST API altında toplayarak akıllı yönlendirme ve arıza toleransı sunar.

- ★ 21.410
- TypeScript
- GitHub Trending · 2026-08-28

## Güncelleme
- 28 Ağustos 2026: Yıldız 21.410, 34 ücretsiz yapay zekâ sağlayıcısı ve streaming yanıt desteği.

## Ne kazandırır?
- 34 ücretsiz model sağlayıcısı: Google Gemini, Groq, Cloudflare Workers AI ve HuggingFace dahil onlarca ücretsiz sağlayıcıya tek noktadan erişim.
- OpenAI REST API uyumluluğu: /v1/chat/completions uç noktası sayesinde LangChain, LlamaIndex ve mevcut yapay zekâ uygulamalarıyla kod değiştirmeden çalışma.
- Akıllı yönlendirme ve arıza kurtarma: Bir sağlayıcı hız sınırına (rate limit) ulaştığında veya hata verdiğinde otomatik olarak alternatif sağlayıcıya geçiş.
- Streaming (Server-Sent Events) desteği: Model çıktılarını gerçek zamanlı kelime kelime akış olarak alabilme imkânı.
- Hafif ve kolay dağıtım: Docker veya Node.js ile saniyeler içinde yerel bilgisayarda ya da sunucuda ayağa kaldırılabilen mimari.

## Kurulum

**Depoyu klonlama ve bağımlılıkları yükleme**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Çalıştırma

**Servisi başlatma ve model sorgulama**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Teknik mimari ve çalışma prensibi

FreeLLMAPI, istemciden gelen OpenAI formatındaki istekleri sağlayıcıya özel imzalara çeviren bir ters proxy katmanı uygular:
- Sağlayıcı Adaptör Katmanı: Farklı REST ve WebSocket API'lerini ortak bir JSON yanıt formatında normalize eden genişletilebilir mimari.
- Dinamik Yük Dengeleme ve Kota İzleme: Her sağlayıcının anlık hız sınırlarını izleyerek istekleri en hızlı yanıt veren aktif modele yönlendirme.
- Yerleşik Önbellek ve Hata Yönetimi: Tekrarlanan sorguları önbelleğe alıp zaman aşımlarında otomatik yeniden deneme (retry) mekanizması.

## Model yönlendirme ve arıza toleransı mekanizması

Geliştiriciler FreeLLMAPI ile maliyet oluşturmadan üretim ortamına yakın testler gerçekleştirebilir:
- Çoklu Model Karşılaştırma: Aynı kullanıcı girdisini farklı açık kaynak modellerine göndererek yanıt kalitesini ve gecikme sürelerini ölçümleyin.
- Geliştirme ve Prototipleme Aşamasında Tasarruf: Ücretli API anahtarları tanımlamadan yapay zekâ destekli prototipleri ve MVP projelerini hızlıca ayağa kaldırın.
- Yedekleme Stratejisi (Fallback Pipeline): Birincil sağlayıcı kapandığında sisteminizin kesintiye uğramadan ikincil modellere yönlenmesini sağlayın.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
FreeLLMAPI aracını Docker ile yerel sunucumda nasıl çalıştıracağımı, OpenAI Node.js SDK'sını bu yerel uç noktaya nasıl yönlendireceğimi ve bir sağlayıcı hata verdiğinde otomatik yedek model kullanımını nasıl sağlayacağımı kod örnekleriyle açıklar mısın?

- **Kimin için:** Yapay zekâ geliştiricileri, açık kaynak araştırmacıları, full-stack mühendisler ve prototip geliştirenler. 
- **Lisans:** MIT (Özgür açık kaynak lisansı) 
- **Çatı:** TypeScript / Node.js Ters Proxy 
- **Platformlar:** Docker, Linux, macOS, Windows 

## Sıkça sorulan sorular
- FreeLLMAPI kullanmak için API anahtarı satın almam gerekir mi? Hayır. Sistem, ücretsiz katman sunan veya kamuya açık ücretsiz çıkarım sağlayan 34 yapay zekâ modelini bir araya getirir.
- Hangi büyük dil modelleri destekleniyor? Llama 3, Mistral, Gemma, Claude benzeri açık ağırlıklı modeller ve Google Gemini ücretsiz katmanı gibi popüler modeller desteklenmektedir.
- Kurumsal gizlilik için uygun mudur? FreeLLMAPI açık kaynaklıdır ve yerel ağınızda çalışır, ancak arkadaki ücretsiz sağlayıcıların kendi kullanım şartları ve gizlilik politikaları geçerlidir.
- LangChain veya CrewAI ile uyumlu mudur? Evet. Tam bir OpenAI REST API emülasyonu sağladığı için baseURL adresini localhost:3000/v1 yaparak tüm LLM çatılarıyla doğrudan kullanılabilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/tashfeenahmed/freellmapi)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-28 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ API LLM Açık Kaynak CLI

---
Kaynak: TreScout Keşif · https://trescout.com/discover/freellmapi/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
