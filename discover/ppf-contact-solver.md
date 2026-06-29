# Fizik Simülasyonlarında Temasları Yönetin

PPF Contact Solver , ZOZO'nun fizik motoru olarak fizik tabanlı simülasyonlarda kumaş, katı ve ip arasındaki temasları çözümlemek için tasarlanmıştır. Farklı geometrilerin etkileşimini hesaplayarak simülasyonlarda fiziksel tutarlılığı artırır. Blender eklentisi sayesinde uzaktan da çalıştırılabilir.

_Görsel: ppf-contact-solver · ZOZO (proje deposundan)_

- ★ 3.389
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

- **Kimin için:** Grafik/fizik simülasyonu yapan teknik kullanıcılar, araştırmacılar 
- **Zorluk:** İleri · teknik/araştırma odaklı 
- **Ne sunar:** Kumaş/katı/ip temas çözümü 
- **Çalışır:** Python + Blender eklentisi 
- **Ücret:** Ücretsiz · açık kaynak (Apache-2.0) 

## Ne işe yarar?
- Gerçekçi kumaş, katı cisim ve ip simülasyonları gerçekleştirir.
- Simülasyonlarda fiziksel tutarlılığı artırır.
- Blender üzerinden uzaktan çalıştırılabilir.
- Araştırma odaklı (ZOZO'nun kendi fizik motoru) bir çözümdür.

## Kimler için uygun değil?

Bu bir son-kullanıcı uygulaması değil. Kullanmak için programlama ve fizik simülasyonu bilgisi gerekir; daha çok grafik/araştırma alanına hitap eder.

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
ZOZO'nun ppf-contact-solver fizik temas çözücüsünü Docker ile çalıştır (NVIDIA GPU gerekir): aşağıdaki docker komutunu çalıştır, sonra tarayıcıda http://localhost:8080 adresini açıp hazır JupyterLab örneklerini dene.

**Docker ile başlat (NVIDIA GPU gerekir)**

```
docker run --rm -it --name ppf-contact-solver --gpus all \
-p 8080:8080 -p 9090:9090 -e WEB_PORT=8080 \
ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```

Lisans: Apache-2.0 · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz (patent koruması da içerir). 

## Bağlantılar
- [GitHub deposu →](https://github.com/st-tech/ppf-contact-solver)
- [Proje sayfası →](https://st-tech.github.io/ppf-contact-solver)

## İlgili sözlük terimleri
GPU Open Source Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ppf-contact-solver/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
