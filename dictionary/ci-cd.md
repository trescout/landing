# CI/CD nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

> Continuous Integration / Continuous Deployment

CI/CD (**Continuous Integration / Continuous Deployment**), kodun otomatik test edilip yayına alınmasıdır.

## Tanım ve Kelime Kökeni

Yazılan kodun hatasız kullanıcıya ulaşması için kurulan otomatik hattır. CI kodu sürekli birleştirip test eder, CD canlıya aktarır. El emeği yayın dönemi kapanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Ekip:** Her commit sonrası test.
**Mobil:** Mağazaya otomatik sürüm.
**Web:** Birleşince yayına alma.

## Teknik Derinlik ve Mimari

Hat aşamaları:

**Lint:** Stil denetimi.
**Test:** Birim ve uçtan uca.
**Derleme:** Paket üretimi.
**Yayın:** Kademeli açılış.

Örnek adım:

```
steps:
  - run: npm ci
  - run: npm test
```

Kritik yayında manuel onay kapısı konur. Delivery ile farkı: Delivery hazırlar, deployment basar. İlki bekler, ikincisi gider.

## Sık Karıştırılanlar

Manuel test sanılır. Oysa hat tamamen otomatiktir: Kod gelir, test koşar, sonuç çıkar. İnsan yalnızca kapıda bekler.

## Farklı Disiplinlerde Kullanımı

**Mutfak bandı:** Hazırlık, tadım ve servis.
**Montaj hattı:** Parça, denetim ve paket.
**Bagaj bandı:** Kayıt, tarama ve yükleme.

*Restoran mutfağında yemeğin hazırlanıp tadım testinden geçip müşteriye servis edilmesini sağlayan bant gibidir.*

## Sıkça Sorulanlar

**Neden bu kadar önemli?**

Hatalı kodu canlıdan çevirir, hızı artırır. Güvenle sık yayın yapılır.

**Her zaman otomatik mi olmalı?**

Genellikle evet, kritik yayında manuel kapı eklenir.

**Delivery ile farkı nedir?**

Delivery hazırlar ve bekler, deployment basar ve gider. İlki onaylı, ikincisi tam otomatiktir.

**Bozulursa ne olur?**

Hat durur, yayın kesilir. Yedek plan ve hızlı geri alma bu yüzden şarttır.

## İlgili terimler

- [Continuous Integration](https://trescout.com/dictionary/continuous-integration/)
- [Continuous Deployment](https://trescout.com/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/dictionary/deployment/)
- [QA](https://trescout.com/dictionary/qa/)

## İlgili araçlar

- [Free for Dev](https://trescout.com/discover/free-for-dev/)
- [Strix](https://trescout.com/discover/strix/)
- [Googletest](https://trescout.com/discover/googletest/)
- [Trivy](https://trescout.com/discover/trivy/)
- [Openship](https://trescout.com/discover/openship/)
- [Ipatool](https://trescout.com/discover/ipatool/)
- [Checkstyle](https://trescout.com/discover/checkstyle/)
- [Flue](https://trescout.com/discover/flue/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ci-cd/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
