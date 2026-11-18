# Kodlama ajanlarınız için yönetilebilir iş akışları

Tencent tarafından geliştirilen LoopForge, kodlama ajanlarının teslimat süreçlerini yönetmek için kullanılan kendi sunucunuzda barındırabileceğiniz (self-hosted) bir iş akışı aracıdır. CodeBuddy, Codex ve Claude Code gibi yazılımları betikler ve insan onay mekanizmalarıyla düzenleyerek yerel kodlama asistanı süreçlerini destekler.

- ★ 3.785
- Go
- GitHub Trending · 2026-11-15

## Güncelleme

- **18 Kasım 2026:** Yıldız 2.090 → 3.785, son sürüm v0.4.0 (17 Kasım 2026).
- **16 Kasım 2026:** Yıldız 986 → 2.090, son sürüm v0.3.8 (12 Kasım 2026).
- **15 Kasım 2026:** Yıldız 983 → 986, son sürüm v0.3.8 (12 Kasım 2026).

## Ne kazandırır?

- Yapay zekâ kodlama araçlarını korumalı çalışma alanlarında güvenle çalıştırır.
- Standart süreçler ve insan onay adımlarıyla tekrarlanabilir teslimatlar sağlar.
- Sohbet arayüzünden rollere görev atar veya adım adım iş akışlarını yürütür.

## Kurulum

**Depoyu klonlama ve sistemi başlatma**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Alternatif imaj kaynağı ile başlatma**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Çalıştırma

**Proje içine kodlama asistanı kurma**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Kodlama ajanlarının teslimat süreçlerini kendi sunucumda yönetebilmek için LoopForge sistemini kurmak istiyorum. İlk olarak `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh` komut dizisini çalıştırarak depoyu klonlayıp sistemi başlatın. İndirme aşamasında takılma yaşanırsa `MIRROR=ghcr.nju.edu.cn ./start.sh` komutunu kullanarak alternatif sunucudan imajları çekip başlatmayı tamamlayın. Hedef projeniz içerisinde kodlama asistanını kurmak için `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude` komutunu çalıştırın.

Depo: https://github.com/Tencent/LoopForge. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ destekli kodlama ajanlarını kendi altyapısında insan onayı ve standart iş akışlarıyla yönetmek isteyen ekipler için uygundur.

## Bağlantılar

- [GitHub deposu →](https://github.com/Tencent/LoopForge)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-15 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Self-hosted](https://trescout.com/dictionary/self-hosted/)
- [Clone](https://trescout.com/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/loopforge/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
