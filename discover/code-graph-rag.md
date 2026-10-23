# Kod deponuzu yapay zekâ ile sorgulayın

Code-graph-rag, büyük kod depolarındaki (monorepo) karmaşık yapıları anlamak ve sorgulamak için bilgi grafikleri (knowledge graphs) ile getirme destekli üretim (RAG) yöntemini birleştiriyor. Geliştiricilerin farklı dillerdeki kod tabanlarını yapay zekâ yardımıyla analiz etmelerine ve düzenlemelerine olanak tanıyor.

- ★ 5.278
- Python
- GitHub Trending · 2026-08-10

## Güncelleme

- **23 Ekim 2026:** Yıldız 5.264 → 5.278, son sürüm v0.2.19 (22 Ekim 2026).
- **18 Ekim 2026:** Yıldız 5.259 → 5.264, son sürüm v0.2.10 (18 Ekim 2026).
- **15 Ekim 2026:** Yıldız 5.189 → 5.259, son sürüm v0.2.0 (15 Ekim 2026).
- **29 Eylül 2026:** Yıldız 5.180 → 5.189, son sürüm v0.1.38 (29 Eylül 2026).

## Ne kazandırır?

- Kod tabanını bilgi grafiğine dönüştürerek karmaşık ilişkileri görün
- Doğal dilde sorular sorarak kod yapısı hakkında yanıtlar alın
- Yapısal arama ve düzenleme araçlarıyla kod üzerinde hassas değişiklikler yapın

## Kurulum

**Paket yöneticisi ile kurulum**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Alternatif kurulum yöntemi**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```

## Çalıştırma

**Veritabanını başlatma**

```
cgr daemon up
```

**Depoyu analiz etme ve sorgulama**

```
cgr start --repo-path /path/to/repo --update-graph
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Code-Graph-RAG aracını kullanarak kod depomu analiz et. Kod tabanındaki fonksiyonlar, sınıflar ve modüller arasındaki ilişkileri kullanarak sorduğum sorulara yanıt ver. Kod üzerinde yapmam gereken değişiklikleri veya optimizasyonları, aracın sağladığı yapısal analiz yeteneklerini kullanarak öner.

Depo: https://github.com/vitali87/code-graph-rag. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Büyük ve karmaşık kod depolarındaki yapısal ilişkileri anlamak, sorgulamak ve yapay zekâ yardımıyla güvenli değişiklikler yapmak isteyen yazılımcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/vitali87/code-graph-rag)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-10 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Monorepo](https://trescout.com/dictionary/monorepo/)
- [RAG](https://trescout.com/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/code-graph-rag/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
