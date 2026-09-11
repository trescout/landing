# Yapay zekâ ajanları için gizli tarayıcı

Camofox, yapay zekâ ajanlarının bot algılama sistemlerini ve veri kazıma engellerini aşmasını sağlayan gizli bir tarayıcıdır (stealth headless browser). Tarayıcı otomasyon araçları Puppeteer ve Playwright ile doğrudan uyumlu çalışarak bu kütüphanelere alternatif bir çözüm sunar.

- ★ 10.915
- JavaScript
- GitHub Trending · 2026-09-08

## Güncelleme
- 11 Eylül 2026: Yıldız 10.066 → 10.915, son sürüm v1.15.0 (10 Eylül 2026).
- 8 Eylül 2026: Yıldız 10.058 → 10.066, son sürüm camoufox-backup-380139564 (6 Eylül 2026).

## Ne kazandırır?
- Bot algılama sistemlerini ve veri kazıma engellerini C++ seviyesinde aşar.
- Erişilebilirlik anlık görüntüleri ile standart HTML'e göre %90 daha az veri tüketir.
- Oturum yalıtımı sayesinde kullanıcı bazlı çerez ve depolama yönetimi sağlar.

## Kurulum

**Doğrudan çalıştırma**

```
npx @askjo/camofox-browser
```

**Kaynak koddan kurulum**

```
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install
npm start # downloads Camoufox on first run (~300MB)
```

## Çalıştırma

**Yerel sunucuyu başlatma**

```
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sen bir web tarayıcı yöneticisisin. Camofox-browser kullanarak hedef web sitelerine erişim sağla. Bot tespitine takılmamak için C++ seviyesinde gizlenen bu tarayıcıyı kullan. Web sayfalarından veri çekerken ham HTML yerine daha hafif olan erişilebilirlik anlık görüntülerini (accessibility snapshots) tercih et. Etkileşim kurman gereken öğeler için kararlı tanımlayıcıları kullan ve oturumları kullanıcı bazlı yalıtarak yönet.

- **Kimin için:** Web sitelerinden veri kazıması gereken veya internet üzerinde işlem yapan yapay zekâ ajanları geliştiren yazılımcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/jo-inc/camofox-browser)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Stealth Headless Browser Headless Browser Web Scraping Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/camofox-browser/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
