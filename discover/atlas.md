# Yapay zekâ ajanları için kaynak kontrolü

Atlas, yazılım geliştirme süreçlerinde kullanılan yapay zekâ ajanları için bir kaynak kontrolü (source control) sistemi. Birden fazla kodlama ajanının yaptığı değişiklikleri tek bir merkezden izlemeye ve sorgulamaya olanak tanıyor.

- ★ 3.058
- Rust
- GitHub Trending · 2026-09-03

## Güncelleme
- 3 Eylül 2026: Yıldız 3.056 → 3.058, son sürüm alpha-0.3.0 (25 Ağustos 2026).

## Ne kazandırır?
- Farklı kodlama ajanlarının yaptığı değişiklikleri tek merkezden izler.
- Ajanlar arası ortak hafıza ile görev geçişlerinde kaldığınız yerden devam etmenizi sağlar.
- Her kod değişikliğini, o değişikliği yapan ajanın gerekçesi ve komutlarıyla eşleştirir.

## Kurulum

**Gerekli bağımlılıkların yüklenmesi**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Uygulamanın kaynak koddan derlenmesi**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sen bir yazılım geliştirme asistanısın. Atlas kullanarak yaptığın tüm kod değişikliklerini, aldığın kararları ve kullandığın araçları oturum geçmişiyle birlikte kaydet. Çalışırken Claude Code veya Codex gibi farklı ajanlar arasında geçiş yapman gerekirse, önceki oturumdaki planları ve mimari notları ortak hafızadan oku. Kod tabanındaki dosyaları, klasörleri veya geçmiş oturumları '@' işaretiyle çağırarak bağlamı koru ve yaptığın her değişikliğin nedenini, ilgili oturumun gerekçeleriyle birlikte belgele.

- **Kimin için:** Birden fazla yapay zekâ ajanıyla çalışan ve kodlama süreçlerinde yapılan değişikliklerin mantıksal gerekçelerini takip etmek isteyen yazılım geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/pacifio/atlas)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Source Control Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/atlas/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
