# Yapay zekâ modellerini tek merkezden yönetin

LiteLLM, 100'den fazla büyük dil modeli (LLM) arayüzünü tek bir standart formatta birleştiren bir yapay zekâ ağ geçidi (AI gateway). Yazılım geliştiricilere maliyet takibi, yük dengeleme ve güvenlik duvarı (guardrails) gibi özellikler sunarak farklı model sağlayıcıları arasında geçiş yapmayı kolaylaştırıyor.

- ★ 60.449
- Python
- GitHub Trending · 2026-10-09

## Güncelleme

- **9 Ekim 2026:** Yıldız 60.446 → 60.449, son sürüm v1.104.2 (8 Ekim 2026).

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

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Sen bir yazılım geliştirme yardımcısısın. Projemizde farklı yapay zekâ modellerini tek bir merkezden yönetmek için LiteLLM aracını kullanmak istiyoruz. Öncelikle terminalde 'uv add litellm' komutunu çalıştırarak kütüphaneyi yüklememi sağla. Ardından, 'uv tool install 'litellm[proxy]'' ve 'litellm --model gpt-4o' komutlarıyla büyük dil modeli gpt-4o için yerel bir geçit sunucusunu nasıl başlatacağımı ve bu sunucu üzerinden modelleri nasıl yönlendirebileceğimi adım adım açıkla.

- **Kimin için:** Farklı yapay zekâ modellerini tek bir standart arayüz üzerinden bütçe takibi ve yük dengeleme özellikleriyle yönetmek isteyen yazılım geliştiriciler içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/BerriAI/litellm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-09 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [AI Gateway](https://trescout.com/dictionary/ai-gateway/)
- [Guardrails](https://trescout.com/dictionary/guardrails/)
- [Gateway](https://trescout.com/dictionary/gateway/)
- [Proxy](https://trescout.com/dictionary/proxy/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/litellm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
