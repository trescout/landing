# CI/CD nedir, ne demek?

> Continuous Integration / Continuous Deployment

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

CI/CD (**Continuous Integration / Continuous Deployment**), kodun otomatik test edilip yayına alınmasıdır.

## Tanım ve Kelime Kökeni
Yazılan kodun hatasız kullanıcıya ulaşması için kurulan otomatik hattır. CI kodu sürekli birleştirip test eder, CD canlıya aktarır. El emeği yayın dönemi kapanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Ekip:** Her commit sonrası test.
- **Mobil:** Mağazaya otomatik sürüm.
- **Web:** Birleşince yayına alma.

## Teknik Derinlik ve Mimari
Hat aşamaları:
- **Lint:** Stil denetimi.
- **Test:** Birim ve uçtan uca.
- **Derleme:** Paket üretimi.
- **Yayın:** Kademeli açılış.

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
- **Mutfak bandı:** Hazırlık, tadım ve servis.
- **Montaj hattı:** Parça, denetim ve paket.
- **Bagaj bandı:** Kayıt, tarama ve yükleme.

## Bir benzetmeyle
Restoran mutfağında yemeğin hazırlanıp tadım testinden geçip müşteriye servis edilmesini sağlayan bant gibidir.

## Sıkça sorulanlar

**Neden bu kadar önemli?**  
Hatalı kodu canlıdan çevirir, hızı artırır. Güvenle sık yayın yapılır.

**Her zaman otomatik mi olmalı?**  
Genellikle evet, kritik yayında manuel kapı eklenir.

**Delivery ile farkı nedir?**  
Delivery hazırlar ve bekler, deployment basar ve gider. İlki onaylı, ikincisi tam otomatiktir.

**Bozulursa ne olur?**  
Hat durur, yayın kesilir. Yedek plan ve hızlı geri alma bu yüzden şarttır.

## İlgili terimler
- [Continuous Integration](/dictionary/continuous-integration/)
- [Continuous Deployment](/dictionary/continuous-deployment/)
- [Deployment](/dictionary/deployment/)
- [QA](/dictionary/qa/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ci-cd/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
