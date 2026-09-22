# Script nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Script (Türkçe karşılığıyla **betik**), tek işi otomatik yapan kısa komut dizisidir.

## Tanım ve Kelime Kökeni
Büyük proje yerine tek iş çözülür: Dosya adı değiştirme, veri temizleme, program başlatma. Metin dosyasına komut yazılır, yorumlayıcı çalıştırır. Derleme gerekmez, yaz-çalıştır düzenidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sistem:** Yedekleme ve temizlik.
- **Veri:** Toplu dosya işlemleri.
- **Tarayıcı:** Sayfa otomasyon eklentileri.

## Teknik Derinlik ve Mimari
Çalışma düzeni:
- **Shebang:** Dosyanın ilk satırı yorumlayıcıyı gösterir.
- **İzin:** Çalıştırma bayrağı verilir.
- **Parametre:** Dosya ve seçenek dışarıdan alınır.

Örnek:

```
#!/bin/bash
for dosya in *.log; do
  gzip "$dosya"
done
```

Kural: Yıkıcı komut önce kuru çalışmayla denenir, yedek alınır.

## Sık Karıştırılanlar
Uygulama sanılır. Uygulama büyük ve derlemelidir, betik hafif ve anlıktır. İkisi farklı ölçeğin aracıdır.

## Farklı Disiplinlerde Kullanımı
- **Liste:** Adım adım iş tarifi.
- **Tarif kartı:** Ölçülü kısa talimat.
- **Otomat:** Jetona basınca çalışan düzenek.

## Bir benzetmeyle
Uzun uzun anlatmak yerine adım adım iş listesi vermeye benzer.

## Sıkça sorulanlar

**Herkes yazabilir mi?**  
Evet. Temel mantıkla basit betikler yazılır, karmaşık işler pratikle gelir.

**Hangi dil seçilmeli?**  
Sistem işinde Bash, genel işte Python pratik başlangıçlardır.

**Nasıl çalıştırılır?**  
Yorumlayıcı adıyla veya çalıştırma izniyle doğrudan. Windows tarafında WSL veya PowerShell kullanılır.

**Güvenli mi?**  
Kaynağı belli betikler evet. İnternetten alınan betik okunmadan çalıştırılmaz.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [Tools](/dictionary/tools/)
- [Shell](/dictionary/shell/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/script/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
