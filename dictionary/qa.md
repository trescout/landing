# QA nedir, ne demek?

> Quality Assurance

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

QA (Quality Assurance - Kalite Güvence), yazılım geliştirme yaşam döngüsünün her aşamasında hataları ortaya çıkmadan önlemeyi, mühendislik standartlarını kurgulamayı ve nihai ürünün güvenilirliğini garanti altına almayı hedefleyen sistematik kalite yönetimi disiplinidir.

## Kavramsal köken: Deming döngüsü ve üretim hatlarından yazılıma
Kalite Güvence kavramı yazılımdan çok önce, 20. yüzyılın ortalarında endüstriyel üretimde doğmuştur. W. Edwards Deming ve Walter Shewhart'ın temellerini attığı Toplam Kalite Yönetimi (TQM) ve PDCA döngüsü (Plan-Do-Check-Act / Planla-Uygula-Kontrol Et-Önlem Al), kalitenin sonradan denetlenemeyeceğini, ürünün içine bizzat inşa edilmesi gerektiğini savunur. Toyota Üretim Sistemi'ndeki *Jidoka* (kusurlu ürün üretildiğinde hattı anında durdurma) prensibi de bugünkü modern sürekli entegrasyon (CI) ve QA felsefesinin atasıdır.

Yazılım dünyasında ise Barry Boehm'in ünlü "Yazılım Mühendisliği Ekonomisi" araştırması, tasarım aşamasında fark edilen bir hatayı düzeltmenin maliyeti 1 birimken, canlıya (production) çıktıktan sonra düzeltmenin maliyetinin 100 katına çıkabildiğini kanıtlamıştır. QA, bu devasa maliyeti ve itibar kaybını önlemek için vardır.

## Kritik ayrım: QA vs QC vs Testing
Bu üç kavram sıklıkla birbiri yerine kullanılsa da aralarında net metodolojik sınırlar bulunur:
- **Test (Testing):** Yazılımın belirli bir sürümündeki somut hataları (bug) bulmak için senaryoların çalıştırılmasıdır (ürün odaklı ve reaktiftir).
- **Kalite Kontrol (QC - Quality Control):** Ürünün yayına çıkmadan önce belirlenen teknik şartnamelere ve kabul kriterlerine uygun olup olmadığını doğrulayan denetim kapısıdır (ürün odaklı ve reaktiftir).
- **Kalite Güvence (QA - Quality Assurance):** Hataların hiç ortaya çıkmaması için geliştirme metodolojilerini, test altyapısını, mimari standartları ve CI/CD süreçlerini tasarlayan şemsiye disiplindir (süreç odaklı ve proaktiftir).

## Modern QA paradigması: Shift-Left ve Shift-Right
Geleneksel şelale (waterfall) modelinde geliştiriciler kodu yazar, ardından test edilmesi için QA departmanına "duvarın üzerinden atardı". Modern çevik (Agile) ve DevOps dünyasında bu yaklaşım yerini iki tamamlayıcı yöne bırakmıştır:

1. **Shift-Left (Sola Kayma):** Kalite kontrolünü geliştirmenin en başına çeker. Geliştirici daha kod yazarken statik analiz (ESLint, SonarQube), tip denetimi (TypeScript), birim testleri (Jest, pytest) ve TDD (Test-Driven Development) uygular. QA mühendisi burada test koşan kişi değil, test altyapısını ve çerçevelerini (framework) inşa eden bir platform mimarıdır.
2. **Shift-Right (Sağa Kayma):** Kod canlıya çıktıktan sonra kalitenin korunmasıdır. Sentetik izleme, kanarya dağıtımları, hata takibi (Sentry), kaos mühendisliği (Chaos Engineering) ve canlı trafik analitiği ile gerçek kullanıcı deneyimi denetlenir.

## Test piramidi ve otomasyon katmanları
Sağlam bir QA mimarisi Mike Cohn'un Test Piramidi prensibine dayanır:
- **Birim Testleri (Unit Tests):** Tabanı oluşturur; bağımsız fonksiyonları izole olarak test eder, milisaniyeler içinde çalışır ve maliyeti en düşüktür.
- **Entegrasyon ve Sözleşme Testleri (Integration & Contract Tests):** Veritabanı, önbellek ve mikroservisler arası API sözleşmelerini (ör. Pact) doğrular.
- **Uçtan Uca Testler (E2E Tests):** Cypress veya Playwright gibi araçlarla gerçek bir kullanıcının tarayıcıdaki adımlarını simüle eder; kapsamı geniştir ancak bakımı daha maliyetlidir.
- **Fonksiyonel Olmayan Testler:** Yük ve stres testleri (k6, Locust), güvenlik açığı taramaları (SAST/DAST) ve erişilebilirlik (WCAG / a11y) denetimlerini içerir.

## Bir benzetmeyle: Koruyucu hekimlik
Hata ayıklamak (debugging) ameliyat masasında müdahale etmek, yazılım testi yapmak ise laboratuvar tahlili almaktır. QA ise toplum sağlığı ve koruyucu hekimlik protokolüdür: Sağlıklı beslenme rehberleri, aşı takvimleri ve hijyen kuralları koyarak hastalanma riskini baştan yok etmeyi hedefler.

## Yapay zeka ve LLM çağında QA
Büyük dil modelleri (LLM) gibi olasılıksal (non-deterministic) sistemlerin yaygınlaşmasıyla QA disiplini yeni bir evreye girmiştir:
- **LLM Değerlendirmeleri (Evals):** Model yanıtlarının halüsinasyon, doğruluk, toksisite ve alaka düzeyini puanlayan otomatik denetimler (DeepEval, Ragas).
- **Semantik Regresyon Testleri:** Prompt şablonlarında yapılan bir değişikliğin önceki yanıt kalitesini bozup bozmadığını ölçen kıyaslama kümeleri (benchmarks).
- **Yapay Zeka Destekli Test Üretimi:** Test senaryolarının ve görsel arayüz regresyon farklarının yapay zeka modelleriyle otomatik tespiti.

## Sıkça sorulanlar

**QA ne anlama gelir ve açılımı nedir?**  
Quality Assurance ifadesinin kısaltmasıdır; Türkçede Kalite Güvence anlamına gelir. Yazılım süreçlerinin baştan sona hatasız işlemesini sağlayan mühendislik disiplinidir.

**QA ile QC (Kalite Kontrol) ve Test arasındaki fark nedir?**  
Test ve QC mevcut koddaki hataları bulmaya odaklanan reaktif adımlardır. QA ise hataların baştan hiç meydana gelmemesi için geliştirme süreçlerini, standartlarını ve araçlarını tasarlayan proaktif süreçtir.

**Shift-Left ve Shift-Right test yaklaşımları ne demektir?**  
Shift-Left test süreçlerini geliştirmenin en başına (kod yazım anına) çekmeyi; Shift-Right ise canlı ortamdaki sistem sağlığını ve kullanıcı davranışlarını anlık izlemeyi ifade eder.

**Yapay zeka ve LLM tabanlı uygulamalarda QA nasıl yapılır?**  
Geleneksel testlerin yanı sıra halüsinasyon oranları, semantik benzerlik, prompt regresyonu ve RAG doğruluk metriklerini ölçen özel değerlendirme (evals) çerçeveleri kullanılır.

## İlgili terimler
- [Unit Testing](/dictionary/unit-testing/)
- [End-to-End Testing](/dictionary/end-to-end-testing/)
- [Testing Framework](/dictionary/testing-framework/)
- [Production Pipeline](/dictionary/production-pipeline/)
- [Benchmarks](/dictionary/benchmark/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/qa/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
