# Yapay zekâ ajanları için bilgisayar kontrolü

CUA, bilgisayar kullanım yeteneğine sahip yapay zekâ ajanları için açık kaynaklı bir altyapı sunuyor. Masaüstü işletim sistemlerini kontrol edebilen ajanların eğitimi ve değerlendirilmesi amacıyla kum havuzu (sandbox), yazılım geliştirme kiti (SDK) ve kıyaslama (benchmark) araçlarını tek bir çatı altında topluyor.

- ★ 30.335
- HTML
- GitHub Trending · 2026-06-16

## Güncelleme

- **20 Ekim 2026:** Yıldız 30.189 → 30.335, son sürüm cua-spaces-v0.11.0 (20 Ekim 2026).
- **19 Ekim 2026:** Yıldız 30.064 → 30.189, son sürüm agent-v0.9.1 (19 Ekim 2026).
- **18 Ekim 2026:** Yıldız 29.921 → 30.064, son sürüm cua-spaces-v0.9.4 (18 Ekim 2026).
- **16 Ekim 2026:** Yıldız 29.802 → 29.921, son sürüm cua-spaces-v0.9.3 (16 Ekim 2026).

## Ne kazandırır?

- Masaüstü uygulamalarını arka planda kontrol etme
- Farklı işletim sistemleri için izole kum havuzları
- Ajan performansını ölçmek için kıyaslama araçları

## Kurulum

**Sürücü kurulumu (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Sandbox SDK kurulumu**

```
pip install cua
```

## Çalıştırma

**macOS sanal makine başlatma**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

CUA altyapısını kullanarak bir bilgisayar kullanım ajanı geliştirmek istiyorum. Ajanımın masaüstü uygulamalarıyla arka planda etkileşime girmesini, fare tıklamaları yapmasını ve klavye girdileri göndermesini sağlayacak temel Python yapısını kurmama yardımcı ol. CUA Sandbox SDK kullanarak bir Linux ortamında komut çalıştıran ve ekran görüntüsü alan örnek bir kod taslağı oluştur.

Depo: https://github.com/trycua/cua. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Bilgisayar üzerinde otonom görevler gerçekleştiren yapay zekâ ajanları geliştiren yazılımcılar ve araştırmacılar için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/trycua/cua)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Benchmark](https://trescout.com/dictionary/benchmark/)
- [Sandbox](https://trescout.com/dictionary/sandbox/)
- [SDK](https://trescout.com/dictionary/sdk/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/cua/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
