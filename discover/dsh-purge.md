# Yapay zekâ modelleri için güvenlik testi

YuJunZhiXue/dsh-purge, farklı yapay zekâ modelleri için özelleştirilebilir komut istemleri (prompts) kullanarak güvenlik kısıtlamalarını aşmayı (jailbreak) hedefleyen bir JavaScript aracıdır. Proje, kullanıcıların farklı modeller için kendi komutlarını tanımlamasına ve varsayılan olarak yerel modellere odaklanmasına olanak tanır.

- ★ 6.492
- JavaScript
- GitHub Trending · 2026-10-19

## Güncelleme

- **23 Ekim 2026:** Yıldız 10.161 → 6.492, son sürüm v1.1.73 (23 Ekim 2026).
- **20 Ekim 2026:** Yıldız 7.527 → 10.161, son sürüm v1.1.71 (11 Ekim 2026).
- **19 Ekim 2026:** Yıldız 7.496 → 7.527, son sürüm v1.1.71 (11 Ekim 2026).

## Ne kazandırır?

- Yapay zekâ çalıştırma ortamı DeepSeek Harness üzerindeki güvenlik ve denetim kurallarını yerel ortamda test edebilirsiniz.
- Farklı modeller için özel komut istemleri tanımlayarak model yanıtlarını ve sistem filtrelerini doğrudan inceleyebilirsiniz.
- Geliştirici arayüzü üzerinden yapılan sistem yamalarını yönetebilir ve dilediğiniz an önceki duruma geri dönebilirsiniz.

## Kurulum

**Depoyu eklenti dizinine klonlama**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**İlgili profil dizinine geçip bağımlılıkl**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Çalıştırma

**Kod sözdizimini doğrulama**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ çalıştırma ortamı DeepSeek Harness üzerinde güvenlik değerlendirmesi yapabilmek için dsh-purge eklentisini kurup doğrulamak istiyorum. İlk olarak sürüm kontrol yazılımı Git ile depoyu indirmek adına git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" komutunu çalıştır. Ardından paket yöneticisi pnpm ile profil bağımlılıklarını kurmak için cd "$DSH_HOME/profiles/web" # 或 profiles/desktop\npnpm install adımını tamamla. Son işlem olarak JavaScript çalışma ortamı Node.js ile dosyaları denetlemek üzere node --check lib/index.js\nnode --check lib/core.js\nnode --check lib/rewind.js\nnode --check lib/skills.js\nnode --check client.js komutunu çalıştır.

Depo: https://github.com/YuJunZhiXue/dsh-purge. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ modellerinin güvenlik sınırlarını ve sistem filtrelerini kendi yerel ortamında denetlemek isteyen araştırmacılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/YuJunZhiXue/dsh-purge)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-19 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Jailbreak](https://trescout.com/dictionary/jailbreak/)
- [Harness](https://trescout.com/dictionary/harness/)
- [Clone](https://trescout.com/dictionary/clone/)
- [AI Skills](https://trescout.com/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/dsh-purge/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
