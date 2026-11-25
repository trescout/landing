# Uygulama mağazası retlerini önleme rehberi

mjmirza/app-store-compliance, uygulama mağazası inceleme süreçlerinde karşılaşılan 117 farklı ret desenini ve çözüm yollarını içeren açık bir rehber sunuyor. Yasal düzenleme takipleri ve gizlilik bildirimleri gibi araçlarla geliştiricilerin App Store ve Google Play onay süreçlerini kolaylaştırmayı hedefliyor.

- ★ 6.355
- Shell
- GitHub Trending · 2026-11-20

## Güncelleme

- **25 Kasım 2026:** Yıldız 6.296 → 6.355, son sürüm v2.5.2 (25 Kasım 2026).
- **25 Kasım 2026:** Yıldız 4.775 → 6.296, son sürüm v2.5.1 (22 Kasım 2026).
- **23 Kasım 2026:** Yıldız 3.762 → 4.775, son sürüm v2.5.1 (22 Kasım 2026).
- **22 Kasım 2026:** Yıldız 3.623 → 3.762, son sürüm v2.5.1 (22 Kasım 2026).

## Ne kazandırır?

- Uygulamanızı Apple ve Google onayına göndermeden önce tarayarak olası ret risklerini tespit edebilirsiniz.
- Karşılaşılan ret maddelerini doğrudan resmi inceleme kurallarıyla ve çözüm yöntemleriyle eşleştirebilirsiniz.
- Gizlilik bildirimleri ve test hesabı gereksinimlerini mağaza yüklemesi öncesinde doğrulayabilirsiniz.

## Kurulum

**Aracı yapay zekâ geliştirme araçlarına b**

```
git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/scripts/install.sh --tool all
```

## Çalıştırma

**Uygulama klasörünü tarama**

```
git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh "/path/to/your/app"
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Mobil uygulama projemi App Store ve Google Play inceleme kurallarına göre denetlemek ve ret alabilecek açıkları önceden bulmak istiyorum. Aracı indirip yapay zekâ araçlarına tanıtmak için "git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/scripts/install.sh --tool all" komutunu, ardından mobil uygulama klasörümü taramak için "/path/to/your/app" kısmını kendi uygulama yolumla değiştirerek "git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh "/path/to/your/app"" komutunu çalıştırın.

Depo: https://github.com/mjmirza/app-store-compliance. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Mobil uygulamalarını Apple App Store veya Google Play onayına hazırlayan ve mağaza incelemelerinden ret almak istemeyen ekipler içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/mjmirza/app-store-compliance)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Hooks](https://trescout.com/dictionary/hooks/)
- [Shell](https://trescout.com/dictionary/shell/)
- [Clone](https://trescout.com/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/app-store-compliance/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
