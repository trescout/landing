# Fizik simülasyonlarında temasları yönetin

**PPF Contact Solver**, ZOZO'nun fizik motoru olarak fizik tabanlı simülasyonlarda **kumaş, katı ve ip** arasındaki temasları çözümlemek için tasarlanmıştır. Farklı geometrilerin etkileşimini hesaplayarak simülasyonlarda fiziksel tutarlılığı artırır. Blender eklentisi sayesinde uzaktan da çalıştırılabilir.

- ★ 4.560
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## Kurulum

**GPU container’ını başlat**

```
docker run --rm -it --name ppf-contact-solver --gpus all -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEB_PORT=8080 ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```

**Kaynak:** Resmî kaynak: https://github.com/st-tech/ppf-contact-solver

## Güncelleme

- **19 Ekim 2026:** Yıldız 4.552 → 4.560, son sürüm addon-2026-10-19-0917 (19 Ekim 2026).
- **13 Ekim 2026:** Yıldız 4.514 → 4.552, son sürüm addon-2026-10-13-1345 (13 Ekim 2026).
- **1 Ekim 2026:** Yıldız 4.513 → 4.514, son sürüm addon-2026-10-01-2043 (1 Ekim 2026).
- **1 Ekim 2026:** Yıldız 4.507 → 4.513, son sürüm addon-2026-10-01-0946 (1 Ekim 2026).

- **Kimin için:** Grafik/fizik simülasyonu yapan teknik kullanıcılar, araştırmacılar
- **Zorluk:** İleri · teknik/araştırma odaklı
- **Ne sunar:** Kumaş/katı/ip temas çözümü
- **Çalışır:** Python + Blender eklentisi
- **Ücret:** Ücretsiz · açık kaynak (Apache-2.0)

## Ne işe yarar?

- Gerçekçi **kumaş, katı cisim ve ip simülasyonları** gerçekleştirir.
- Simülasyonlarda fiziksel tutarlılığı artırır.
- Blender üzerinden uzaktan çalıştırılabilir.
- Araştırma odaklı (ZOZO'nun kendi fizik motoru) bir çözümdür.

## Kimler için uygun değil?

Bu bir son-kullanıcı uygulaması değil. Kullanmak için programlama ve fizik simülasyonu bilgisi gerekir; daha çok grafik/araştırma alanına hitap eder.

## Nasıl kurulur, nasıl kullanılır?

Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

ZOZO'nun ppf-contact-solver fizik temas çözücüsünü Docker ile çalıştır (NVIDIA GPU gerekir): aşağıdaki docker komutunu çalıştır, sonra tarayıcıda http://localhost:8080 adresini açıp hazır JupyterLab örneklerini dene.

Depo: https://github.com/st-tech/ppf-contact-solver. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

**Lisans:** Apache-2.0 · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz (patent koruması da içerir).

## Bağlantılar

- [GitHub deposu →](https://github.com/st-tech/ppf-contact-solver)
- [Proje sayfası →](https://st-tech.github.io/ppf-contact-solver)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Container](https://trescout.com/dictionary/container/)
- [Localhost](https://trescout.com/dictionary/localhost/)
- [GPU](https://trescout.com/dictionary/gpu/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ppf-contact-solver/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
