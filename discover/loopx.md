# Yapay zekâ ajanları için kalıcı hafıza

Loopx, uzun süreli çalışan yapay zekâ ajan ekipleri için geliştirilmiş hafif bir durum çekirdeği (state kernel). Kodlama ajanları (Codex, Claude Code) ile uyumlu çalışarak görev takibi, kota yönetimi ve doğrulanabilir iş devri gibi süreçleri standartlaştırıyor.

- ★ 5.864
- Python
- GitHub Trending · 2026-08-06

## Güncelleme

- **16 Eylül 2026:** Yıldız 5.853 → 5.864, son sürüm v1.0.5 (15 Eylül 2026).
- **15 Eylül 2026:** Yıldız 5.793 → 5.853, son sürüm v1.0.4 (15 Eylül 2026).
- **11 Eylül 2026:** Yıldız 5.751 → 5.793, son sürüm v1.0.3 (11 Eylül 2026).
- **9 Eylül 2026:** Yıldız 5.726 → 5.751, son sürüm v1.0.2 (9 Eylül 2026).

## Ne kazandırır?

- Uzun süreli görevlerde hedef takibini ve kota yönetimini standartlaştırır.
- Farklı yapay zekâ ajanları arasında doğrulanabilir iş devri sağlar.
- Görev geçmişini ve kanıtları düzenli bir yapıda saklar.

## Kurulum

**Doğrudan kurulum**

```
curl -fsSL https://raw.githubusercontent.com/huangruiteng/loopx/main/scripts/install-from-github.sh | bash
export PATH="$HOME/.local/bin:$PATH"
loopx doctor
```

## Çalıştırma

**Projeyi başlatma**

```
cd /path/to/your-project
loopx connect
loopx status
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Seninle uzun süreli bir proje üzerinde çalışacağız. Görevlerimizi, hedeflerimizi ve ilerleme kayıtlarımızı LoopX durum çekirdeği ile yönetmeni istiyorum. Çalışırken her adımda mevcut durumu kontrol et, tamamlanan işlerin kanıtlarını kaydet ve bir sonraki yapılacak işi (todo) belirleyerek kota sınırları içinde kal. Görev devri yaparken veya yeni bir aşamaya geçerken LoopX üzerinden doğrulanabilir bir iz bırak.

Depo: https://github.com/huangruiteng/loopx. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Günlerce süren yazılım geliştirme, araştırma veya veri analizi gibi karmaşık süreçleri yöneten yapay zekâ ajanları kullanan kişiler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/huangruiteng/loopx)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-06 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [State Kernel](https://trescout.com/dictionary/state-kernel/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/loopx/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
