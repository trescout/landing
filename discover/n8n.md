# Görsel İş Akışları ve AI Otomasyonu

n8n, görsel canvas, özel kod, AI ajanları ve iş akışlarını bir araya getiren fair-code bir otomasyon platformudur. Self-host veya cloud dağıtım seçenekleriyle çalışabilir; farklı model sağlayıcılarını iş akışlarınıza dahil etmenizi destekler.

- ★ 202.576
- GitHub Trending · 2026-08-23

## Kurulum

**Veri volume’ünü oluşturun**

```
docker volume create n8n_data
```

## Çalıştırma

**n8n Docker container’ını başlatın**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Kaynak: Komutlar n8n resmî README’sinden 24 Ağustos 2026’da kontrol edildi; editör 5678 portunda açılır.

## Güncelleme
- 27 Ağustos 2026: Yıldız 201.895 → 202.576, son sürüm n8n@2.36.7 (25 Ağustos 2026).
- 23 Ağustos 2026: Yıldız 201.890 → 201.895, son sürüm n8n@2.35.7 (21 Ağustos 2026).

## Bu araç ne yapar?

n8n ile iş akışlarını görsel canvas üzerinde oluşturabilir, JavaScript, Python ve npm paketleriyle genişletebilirsiniz. Resmî kaynaklar OpenAI, Anthropic, Google ve açık kaynak modelleriyle model esnekliğini; ayrıca insan onayı, gözlemlenebilirlik, rol tabanlı erişim ve audit trail özelliklerini listeler. Platform self-host veya cloud olarak dağıtılabilir.

## Kimin için?

İş akışlarında görsel tasarımı özel kod ve AI ajanlarıyla birleştirmek isteyen ekipler.

## Ne beklememeli?

Yalnızca kapalı kaynak lisanslı ürünler arayan veya iş akışlarını kod ya da yapılandırma ile genişletmek istemeyen kullanıcılar.

## Öne çıkanlar
- Görsel canvas, özel kod ve AI ajanlarını aynı iş akışında birleştirme
- JavaScript, Python ve npm paketleriyle genişletilebilir yapı
- Self-host veya cloud dağıtım seçenekleri
- İnsan onayı, gözlemlenebilirlik, rol tabanlı erişim ve audit trail özellikleri

## İlk kullanım akışı
- Docker ile resmî hızlı başlangıç yönergelerini izleyerek n8n’i çalıştırın.
- Tarayıcınızda 5678 portundan editörü açın.
- Görsel canvas üzerinde ilk iş akışınızı oluşturun.
- Gereksiniminize göre özel kod veya desteklenen bir model sağlayıcısı ekleyin.

## Güvenli başlangıç

n8n, Sustainable Use License altında source-available olarak dağıtılır. Kullanım ve dağıtım koşullarını resmî lisans metninden inceleyin; self-host kurulumunuzun erişim ve işletim ayarlarını kendi gereksinimlerinize göre yapılandırın.

## İlk görev istemi
İlk adım için hazır istem 
Görsel canvas üzerinde, bir girdiyi alan, bir AI modeliyle işleyen ve sonucu sonraki adıma aktaran örnek bir iş akışı tasarlamama yardımcı olun.

## Bağlantılar
- [GitHub deposu →](https://github.com/n8n-io/n8n)
- [n8n resmî GitHub deposu →](https://github.com/n8n-io/n8n)
- [n8n resmî belgeleri →](https://docs.n8n.io/)
- [n8n belgeleri deposu →](https://github.com/n8n-io/n8n-docs)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-23 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Self-hosting Container Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/n8n/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
