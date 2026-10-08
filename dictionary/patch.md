# Patch nedir, ne demek ve nasıl çalışır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

**Patch** (Türkçe karşılığıyla **yama**), bir yazılımdaki hataları düzeltmek, güvenlik açıklarını kapatmak veya mevcut işlevleri geliştirmek amacıyla yayınlanan kod ve dosya güncellemesidir.

Bununla birlikte teknoloji dünyasında "patch" üç temel bağlamda kullanılır: Yazılım ve oyun sürümlerinde **hata/güvenlik yamaları**, sürüm kontrol sistemlerinde **diff/kod yamaları** ve web mimarilerinde **HTTP PATCH** metodu.

*Kıyafetinizdeki küçük bir söküğü onarmak için giysinin tamamını çöpe atmak yerine üzerine uygun bir kumaş parçası dikmek gibidir. Tüm yazılımı baştan indirmeden sadece kusurlu parçaları değiştirir.*

## 1. Yazılım ve Oyun Dünyasında Patch

Geleneksel olarak bir programda hata oluştuğunda tüm yazılımı sıfırdan indirip kurmak bant genişliği ve zaman açısından verimsizdir. Patch, sadece değişen baytları ya da dosyaları hedef sisteme uygular.

- **Güvenlik Yamaları (Security Patches):** Kritik güvenlik zafiyetlerini (CVE) ve sıfır gün (zero-day) açıklarını kapatmak için acil olarak dağıtılır.
- **Hata Düzeltme Yamaları (Bug Fixes):** Kararlılığı bozan veya beklenmedik çökmelere yol açan mantıksal hataları giderir.
- **Oyun Yamaları ve Dengelemeler:** Çevrim içi çok oyunculu oyunlarda karakter yeteneklerini dengeleyen, yeni içerik ekleyen ve performansı optimize eden güncellemelerdir. Genellikle detaylı "Yama Notları" (Patch Notes) ile birlikte sunulur.
- **Hotfix:** Test döngüsü beklenmeden üretim ortamındaki (production) yangını söndürmek için ivedilikle yayınlanan dar kapsamlı yama.

## 2. Geliştirici Araçlarında Patch: UNIX patch ve Git

Açık kaynak dünyasında ve sürüm kontrol sistemlerinde patch, iki dosya veya commit arasındaki farkı (diff) temsil eden düz metin belgesidir.

### UNIX patch Komutu ve Geçmişi

Tarihte delikli kartlardaki deliklerin bantla kapatılması veya kağıt şeritlerin onarılması metaforuna dayanan "patch", 1985 yılında Larry Wall tarafından yazılan `patch` komutuyla standartlaşmıştır. `diff -u eski.c yeni.c > duzeltme.patch` komutuyla üretilen yama, `patch < duzeltme.patch` ile karşı tarafta doğrudan kaynak koda uygulanabilir.

### Git Ortamında Patch Kullanımı

Git, yamaları e-posta listeleri veya çevrim dışı kanallar üzerinden taşımak için gelişmiş araçlar sunar:

- `git format-patch`: Belirli commit'leri yazar bilgisi, commit mesajı ve kod farkıyla birlikte e-posta dostu `.patch` dosyalarına dönüştürür.
- `git apply`: Bir yama dosyasını commit oluşturmadan doğrudan çalışma dizinine uygular.
- `git am`: E-posta biçimindeki yamaları okuyarak orijinal yazar ve tarih bilgisiyle otomatik commit oluşturur (özellikle Linux çekirdeği geliştirmesinde standarttır).

## 3. Web Mimarisi ve REST API'lerde HTTP PATCH

RESTful servislerde veri güncellenirken sıklıkla `PUT` ve `PATCH` metotları karşılaştırılır:

- **`PUT` (Tam Değiştirme):** Kaynağın tamamını yeniden gönderir. Belirtilmeyen alanlar genellikle varsayılana döner veya silinir. `PUT` işlemi **idempotent**'tir (aynı isteği defalarca göndermek aynı sonucu üretir).
- **`PATCH` (Kısmi Güncelleme - RFC 5789):** Yalnızca değişmesi istenen alanları içeren bir gövde gönderir. Örneğin bir kullanıcının sadece e-posta adresini güncellemek için tüm profil nesnesini göndermek yerine yalnızca ilgili alanı iletmek yeterlidir.
- **JSON Patch (RFC 6902):** Değişiklikleri standartlaştırmak için `add`, `remove`, `replace`, `move`, `copy` ve `test` gibi atomik operasyon dizileri tanımlayan yapıdır.

## Karşılaştırmalı Özet: Farklı Bağlamlarda "Patch"

| Bağlam | Ne Anlama Gelir? | Temel Amaç | Tipik Örnek |
|---|---|---|---|
| **Yazılım & İşletim Sistemi** | Güncelleme Paketi | Güvenlik açığı kapatma, kararlılık | Windows Update KB yaması, Sıfır-gün yaması |
| **Oyun Dünyası** | İçerik ve Denge Güncellemesi | Oynanış dengesi, performans, meta değişimi | Sezon yaması (Patch 14.2), Dengeleme güncellemesi |
| **Git & Versiyon Kontrolü** | Satır Bazlı Değişiklik Dosyası | Kod paylaşımı, kod incelemesi, katkı sağlama | `git format-patch HEAD~1`, `linux-kernel.patch` |
| **Web API / HTTP** | Kısmi Güncelleme Metodu | Ağ tasarrufu, kaynak üzerinde kısmi değişiklik | `PATCH /api/users/42` body: `{"status": "active"}` |

## Sıkça sorulanlar

**Patch ne demek, Türkçe karşılığı nedir?**

Türkçe karşılığı "yama" veya "hata düzeltme eki"dir. Bir sistemin veya yazılımın tümünü değiştirmeden belirli bir bölümünü onaran veya güncelleyen kod parçacıklarını ifade eder.

**Hotfix ile Patch arasındaki fark nedir?**

Patch genellikle planlı sürümlerle (örneğin aylık güvenlik bültenleri) kapsamlı testlerden sonra yayınlanır. Hotfix ise üretim ortamında ortaya çıkan acil bir çökme veya güvenlik zafiyetini derhal durdurmak için hazırlanan plansız, hızlı müdahale yamasıdır.

**HTTP PUT ve HTTP PATCH arasındaki temel fark nedir?**

PUT kaynağın bütünüyle değiştirilmesini (replace) hedefler ve aynı isteğin tekrarlanması durumunda aynı sonucu verir (idempotent). PATCH ise kaynağın sadece belirtilen alanlarını kısmi olarak değiştirir (partial update) ve her senaryoda idempotent olmak zorunda değildir.

**Git ortamında PR (Pull Request) varken neden hâlâ patch dosyaları kullanılır?**

Linux çekirdeği (kernel), Git'in kendi geliştirme süreci ve Postgres gibi köklü açık kaynak projeleri merkezi web platformlarına (GitHub vb.) bağımlı kalmamak adına e-posta tabanlı yama (patch) iş akışını sürdürmektedir.

**Patch Tuesday nedir?**

Microsoft'un her ayın ikinci salı günü Windows ve kurumsal ürünleri için düzenli olarak toplu güvenlik yamalarını dağıttığı sektörel takvime verilen addır.

## İlgili terimler

- [Vulnerability Scanning](https://trescout.com/dictionary/vulnerability-scanning/)
- [Security Scanner](https://trescout.com/dictionary/security-scanner/)
- [Deployment](https://trescout.com/dictionary/deployment/)
- [Git Push](https://trescout.com/dictionary/git-push/)

## İlgili araçlar

- [PLFM RADAR](https://trescout.com/discover/plfm-radar/)
- [PhotoGIMP](https://trescout.com/discover/photogimp/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/patch/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
