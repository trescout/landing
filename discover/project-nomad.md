# İnternetsiz hayatta kalma bilgisayarı

**Project N.O.M.A.D**; internet bağlantısı gerektirmeyen, kritik araçlar, bilgi kaynakları ve yapay zekâ ile donatılmış **kendi kendine yeten, çevrimdışı bir bilgisayar** kurma projesidir. Acil durumlar ve internetin olmadığı senaryolar için özel olarak tasarlanmıştır.

- ★ 41.177
- TypeScript
- Apache-2.0
- GitHub Trending · 30 May 2026

## Güncelleme

- **29 Ekim 2026:** Yıldız 39.138 → 41.177, son sürüm v1.35.1 (5 Ekim 2026).
- **6 Ekim 2026:** Yıldız 38.739 → 39.138, son sürüm v1.35.1 (5 Ekim 2026).
- **29 Eylül 2026:** Yıldız 38.519 → 38.739, son sürüm v1.35.0 (29 Eylül 2026).
- **27 Eylül 2026:** Yıldız 36.474 → 38.519, son sürüm v1.34.1 (2 Eylül 2026).

- **Kimin için:** Çevrimdışı/acil durum hazırlığı yapan herkes
- **Zorluk:** Orta · kurmak için biraz teknik bilgi
- **Ne sunar:** Çevrimdışı araç + bilgi + AI paketi
- **Ücret:** Ücretsiz · açık kaynak (Apache-2.0)
- **Lisans:** Apache-2.0 · ayrıntı aşağıda

## Ne kazandırır?

- İnternet gerektirmeyen kritik araçlar ve bilgi sunar.
- Yerel (offline) yapay zekâ desteği sağlar.
- Acil durum ve çevrimdışı senaryolara hazırlık imkânı tanır.

## Nasıl kurulur, nasıl kullanılır?

Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Debian tabanlı bir sistemde (Ubuntu önerilir) aşağıdaki kurulum komutunu terminale yapıştırıp çalıştır, sonra tarayıcıdan http://localhost:8080 adresini açarak çevrimdışı bilgi sunucusunu kullanmama yardım et.

Depo: https://github.com/Crosstalk-Solutions/project-nomad. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

**Hızlı kurulum (Debian/Ubuntu)**

```
curl -fsSL https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/install_nomad.sh -o install_nomad.sh
sudo bash install_nomad.sh
```

**Başlat**

```
sudo bash /opt/project-nomad/start_nomad.sh
```

**Lisans:** Apache-2.0 · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz (patent koruması da içerir).

## Bağlantılar

- [GitHub deposu →](https://github.com/Crosstalk-Solutions/project-nomad)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Offline](https://trescout.com/dictionary/offline/)
- [Localhost](https://trescout.com/dictionary/localhost/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/project-nomad/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
