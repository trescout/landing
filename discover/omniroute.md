# 230'dan fazla yapay zekâ sağlayıcısını tek ağ geçidinde birleştirin

> Omniroute · Python / Go · ★ 65.889

OmniRoute, 230'u aşkın büyük dil modeli ve yapay zekâ sağlayıcısını tek bir OpenAI uyumlu uç noktada (API gateway) toplayan açık kaynaklı bir altyapı aracıdır. Otomatik hata telafisi (fallback), yük dengeleme ve jeton sıkıştırmasıyla kurumsal yapay zekâ maliyetlerini düşürür.

## Ne kazandırır?
- Evrensel API Uyumluluğu: OpenAI, Anthropic, Gemini, Mistral ve yerel modelleri tek bir /v1/chat/completions uç noktasından çağırın.
- Akıllı Hata Telafisi (Fallback): Ana sağlayıcı hız sınırına (rate limit) takıldığında veya kesinti yaşadığında istekleri milisaniyeler içinde alternatif modele yönlendirin.
- Jeton ve Maliyet Optimizasyonu: Dahili prompt sıkıştırma algoritmalarıyla gereksiz bağlam şişkinliğini önleyin ve API harcamalarınızı düşürün.
- Kapsamlı Telemetri ve Gözlemlenebilirlik: Sağlayıcılar arası yanıt sürelerini, hata oranlarını ve harcanan bütçeyi tek kontrol panelinden izleyin.

## Teknik mimari ve çalışma prensibi
OmniRoute, istemci ile yapay zekâ sağlayıcıları arasında yüksek verimli bir ters vekil (reverse proxy) gibi çalışır:1. Protokol Standardizasyonu: Gelen farklı istek formatlarını dahili bir şemaya çevirir ve hedef sağlayıcının beklediği JSON yapısına dönüştürür.2. Yönlendirme ve Sağlık Kontrolü (Health Checking): Sağlayıcıların gecikme sürelerini ve HTTP durum kodlarını sürekli denetler; yanıt vermeyen sunucuları geçici olarak havuzdan çıkarır.3. Akıllı Önbellekleme (Semantic Caching): Benzer veya yinelenen kullanıcı istemlerini önbellekten yanıtlayarak model çağrısı maliyetini sıfıra indirir.

## Kurulum ve dağıtım adımları
OmniRoute'u Docker Compose ile birkaç saniye içinde yerel veya bulut sunucunuzda ayağa kaldırabilirsiniz:

### Docker Compose ile hızlı başlatma
```bash
git clone https://github.com/danielfrg/omniroute.git
cd omniroute
cp .env.example .env
docker compose up -d
```

### Uç noktayı test etme
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Merhaba!"}]}'
```

## Kod bilmeyenler için yapay zekâ istemi
OmniRoute yapay zekâ ağ geçidini kullanarak OpenAI, Anthropic ve yerel Ollama modellerini içeren bir yönlendirme konfigürasyonu hazırla. Ana model yanıt vermezse otomatik olarak ikinci modele geçiş sağlayan bir fallback kuralı oluştur ve Docker Compose ile çalıştırma adımlarını listele.

## Kritik uyarılar ve sınırlar
- API Anahtarı Güvenliği: Ağ geçidi sunucusunun ortam değişkenlerindeki API anahtarlarını güvenceye alın; ağ geçidini genel internete açarken mutlaka yetkilendirme (Bearer Token) uygulayın.
- Model Parametre Farklılıkları: Sağlayıcıların desteklediği maksimum bağlam pencereleri (context window) ve sıcaklık (temperature) sınırları farklıdır; isteklerde ortak parametreler kullanın.
- Ağ Gecikmesi: Ağ geçidinin konumu ile sağlayıcı veri merkezleri arasındaki coğrafi mesafe ek birkaç milisaniyelik gecikme yaratabilir.

## Sıkça sorulan sorular

### OmniRoute kendi modellerini mi barındırıyor?
Hayır, OmniRoute mevcut yapay zekâ sağlayıcıları arasında akıllı yönlendirme yapan bir ağ geçididir (gateway).

### OpenAI SDK'sı ile doğrudan çalışır mı?
Evet, OpenAI istemci kütüphanelerinde sadece <code>base_url</code> adresini OmniRoute sunucunuza yönlendirmeniz yeterlidir.

### Yerel modelleri (Ollama, vLLM) bağlayabilir miyim?
Evet, ağ geçidine hem bulut sağlayıcıları hem de yerel sunucunuzdaki LLM uç noktalarını ekleyebilirsiniz.

### Kullanıcı isteklerini kaydediyor mu?
Veri gizliliği sizin kontrolünüzdedir; günlükleme (logging) seviyesini ve veri saklama kurallarını konfigürasyondan belirleyebilirsiniz.

## Bağlantılar
- [GitHub deposu (danielfrg/omniroute) →](https://github.com/danielfrg/omniroute)

## İlgili sözlük terimleri
- [Cloud Computing](/dictionary/cloud-computing/)
- [AI Agent](/dictionary/ai-agent/)
- [Runtime](/dictionary/runtime/)
- [Foundation Model](/dictionary/foundation-model/)

---
Source: TreScout Discovery · https://trescout.com/discover/omniroute/
