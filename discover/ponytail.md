# Yapay Zekâ Kodlama Aracıları İçin Kural Seti

Yapay zekâ kodlama aracıları için MIT lisanslı bir kural seti ve eklenti sistemidir. Amaç, görev için gereken kodu yazarken doğrulama, hata yönetimi, güvenlik ve erişilebilirliği korumaktır.

- ★ 119.108
- JavaScript
- GitHub Trending · 2026-08-25

## Kurulum

**Claude Code marketplace’ini ekle**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Claude Code eklentisini kur**

```
/plugin install ponytail@ponytail
```

## Çalıştırma

**Ponytail düzeyini seç**

```
/ponytail full
```

**Diff incelemesini başlat**

```
/ponytail-review
```

Kaynak: Resmî README ve dokümantasyon kaynakları: https://github.com/DietrichGebert/ponytail, https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md

## Güncelleme
- 1 Eylül 2026: Yıldız 113.377 → 119.108, son sürüm v4.9.0 (7 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 110.483 → 113.377, son sürüm v4.9.0 (7 Ağustos 2026).

## Bu araç ne yapar?

Kural merdiveni, değişiklikten etkilenen kod okunduktan sonra uygulanır. Düzeltilmiş agentic benchmark, gerçek bir FastAPI ve React deposundaki 12 görevde Haiku 4.5 ile no-skill temel çizgisine göre ortalama yüzde 54 daha az kod satırı, yüzde 22 daha az token, yüzde 20 daha düşük maliyet ve yüzde 27 daha kısa süre bildirmiştir. Bu sonuçlar belirli test koşullarıyla sınırlıdır.

## Kimin için?

Claude Code, Codex, Gemini CLI ve desteklenen diğer agent host'larında kodlama akışına doğrulama, güvenlik ve erişilebilirlik kuralları eklemek isteyenler.

## Ne beklememeli?

Belirli benchmark sonuçlarını tüm projelere genellemek veya kritik üretim değişikliklerini insan incelemesi olmadan uygulamak.

## Öne çıkanlar
- Gereksiz kodu azaltmayı hedefleyen görev odaklı kurallar
- Doğrulama, hata yönetimi, güvenlik ve erişilebilirliği koruyan inceleme yaklaşımı
- Claude Code, Codex, Gemini CLI ve diğer host'lar için eklenti veya talimat adaptörleri

## İlk kullanım akışı
- Kullandığınız agent host için Ponytail entegrasyonunu kurun
- Kurulumun host içinde etkin olduğunu doğrulayın
- Uygun Ponytail düzeyini seçin
- Değişiklikler üzerinde inceleme veya denetim akışını çalıştırın

## Güvenli başlangıç

Yüzdeler, gerçek bir FastAPI ve React deposundaki 12 görev, Haiku 4.5 ve n=4 koşullarındaki düzeltilmiş agentic benchmark ortalamalarıdır. Ayrı adversarial katmanda yüzde 100 güvenlik bildirilmiştir. Eski tek atımlı yüzde 80 ile 94 aralığı genel ortalama değildir.

## İlk görev istemi
İlk adım için hazır istem 
Görevin gerektirdiği kadar kod yaz, ardından değişiklikleri doğrulama, hata yönetimi, güvenlik ve erişilebilirlik açısından incele.

## Bağlantılar
- [GitHub deposu →](https://github.com/DietrichGebert/ponytail)
- [Resmî README →](https://github.com/DietrichGebert/ponytail)
- [Agentic benchmark yöntemi →](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-25 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Benchmark Agentic Token Agent CLI Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ponytail/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
