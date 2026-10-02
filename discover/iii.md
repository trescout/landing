# Servislerinizi Gerçek Zamanlı Yönetin

iii , backend yığınınızdaki tüm servisleri (kuyruk, cron, HTTP, state, gözlemlenebilirlik, ajanlar, sandbox) gerçek zamanlı oluşturma, genişletme ve izleme yöntemidir. Normalde ayrı entegrasyon zorlukları çıkaran parçaları tek bir noktadan yönetilebilir kılar.

- ★ 18.824
- Rust
- Lisans: yok
- GitHub Trending · 28 May 2026

## Güncelleme
- 2 Ekim 2026: Yıldız 18.809 → 18.824, son sürüm iii/v0.24.4 (2 Ekim 2026).
- 27 Eylül 2026: Yıldız 18.767 → 18.809, son sürüm iii/v0.24.3 (25 Eylül 2026).
- 18 Eylül 2026: Yıldız 18.662 → 18.767, son sürüm iii/v0.24.0 (17 Eylül 2026).
- 2 Eylül 2026: Yıldız 18.570 → 18.662, son sürüm iii/v0.23.0 (1 Eylül 2026).

- **Kimin için:** Backend / altyapı geliştiren ekipler 
- **Zorluk:** İleri · geliştirici aracı 
- **Ne sunar:** Servis kompozisyonu + observability 
- **Ücret:** Açık kaynak (lisans notuna bakın) 
- **Lisans:** Belirtilmemiş · ayrıntı aşağıda 

## Ne kazandırır?
- Kuyruk, cron, HTTP ve durum yönetimi tek yerde .
- Gerçek zamanlı izlenebilirlik imkanı.
- Ajan ve sandbox desteği.
- Entegrasyon süreçlerindeki karmaşayı azaltır.

## Nasıl başlanır?

Başlangıç yapmak ve dokümantasyona ulaşmak için iii.dev adresini ziyaret edebilirsiniz.

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
iii'yi denemek için önce 'iii project init myapp' ile bir proje oluştur, 'cd myapp' yapıp 'iii' komutuyla motoru başlat, ardından 'iii worker add queue' gibi komutlarla yetenekler ekleyerek hepsini aynı canlı sistemde birbirine bağla; SDK gerekirse 'npm install iii-sdk' kur.

**Proje oluştur**

```
iii project init myapp
```

**Motoru başlat**

```
cd myapp
iii
```

**Worker (yetenek) ekle**

```
iii worker add queue
```

**Node.js SDK kur**

```
npm install iii-sdk
```

Lisans: ⚠️ Repo'da bir lisans belirtilmemiş; bu varsayılan olarak 'tüm hakları saklı' demektir. Denemek için bakabilirsiniz, ancak net bir lisans eklenene kadar kod yeniden kullanımı ve ticari kullanım için yazarın açık izni gerekir.

## Bağlantılar
- [GitHub deposu →](https://github.com/iii-hq/iii)
- [Ana sayfa →](https://iii.dev)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Observability Backend Sandbox SDK Rust Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/iii/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
