# Yapay zekâ modellerini tek merkezden yönetin

LiteLLM, 100'den fazla büyük dil modeli (LLM) arayüzünü tek bir standart formatta birleştiren bir yapay zekâ ağ geçidi (AI gateway). Yazılım geliştiricilere maliyet takibi, yük dengeleme ve güvenlik duvarı (guardrails) gibi özellikler sunarak farklı model sağlayıcıları arasında geçiş yapmayı kolaylaştırıyor.

- ★ 61.984
- Python
- GitHub Trending · 2026-10-09

## Güncelleme

- **25 Ekim 2026:** Yıldız 61.793 → 61.984, son sürüm v1.106.3 (24 Ekim 2026).
- **22 Ekim 2026:** Yıldız 61.715 → 61.793, son sürüm v1.106.2 (21 Ekim 2026).
- **21 Ekim 2026:** Yıldız 61.706 → 61.715, son sürüm v1.107.0 (21 Ekim 2026).
- **21 Ekim 2026:** Yıldız 61.464 → 61.706, son sürüm v1.106.1 (20 Ekim 2026).

## Ne kazandırır?

- Yüzden fazla LLM (Büyük Dil Modeli) sağlayıcısını tek bir standart biçimde birleştirerek kod karmaşasını önler.
- Yapay zekâ modelleri arasında geçiş yaparken kod tabanınızı yeniden yazma ihtiyacını ortadan kaldırır.
- Sanal anahtarlar, bütçe takibi ve yük dengeleme gibi araçlarla kurumsal düzeyde bir yönetim altyapısı sunar.

## Kurulum

**programlama dili Python kütüphanesini yü**

```
uv add litellm
```

## Çalıştırma

**Geçit sunucusunu başlatma**

```
uv tool install 'litellm[proxy]'
litellm --model gpt-4o
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Sen bir yazılım geliştirme yardımcısısın. Projemizde farklı yapay zekâ modellerini tek bir merkezden yönetmek için LiteLLM aracını kullanmak istiyoruz. Öncelikle terminalde 'uv add litellm' komutunu çalıştırarak kütüphaneyi yüklememi sağla. Ardından, 'uv tool install 'litellm[proxy]'' ve 'litellm --model gpt-4o' komutlarıyla büyük dil modeli gpt-4o için yerel bir geçit sunucusunu nasıl başlatacağımı ve bu sunucu üzerinden modelleri nasıl yönlendirebileceğimi adım adım açıkla.

Depo: https://github.com/BerriAI/litellm. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Farklı yapay zekâ modellerini tek bir standart arayüz üzerinden bütçe takibi ve yük dengeleme özellikleriyle yönetmek isteyen yazılım geliştiriciler içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/BerriAI/litellm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-09 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [AI Gateway](https://trescout.com/dictionary/ai-gateway/)
- [Guardrails](https://trescout.com/dictionary/guardrails/)
- [Gateway](https://trescout.com/dictionary/gateway/)
- [Proxy](https://trescout.com/dictionary/proxy/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/litellm/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
