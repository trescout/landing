# Localhost nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Localhost, bilgisayarınızın kendisini adresleyen özel ağ adıdır. Karşılığı 127.0.0.1 adresidir.

## Tanım ve Kelime Kökeni
"Local" **yerel**, "host" ise **ev sahibi bilgisayar** demektir. Yazılımcı siteyi hemen internete yüklemez, önce kendi bilgisayarında bu adresle test eder. Bilgisayarınız kendi kendine sunucu rolü oynar. Dışarıdan kimse göremez, yalnızca siz görürsünüz.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Web geliştirme:** `npm run dev` sonrası tarayıcıda açılan adres.
- **Veritabanı:** Yerelde kurulu Postgres veya Redis bağlantısı.
- **API deneme:** Henüz yayınlanmamış uçların test edilmesi.

## Teknik Derinlik ve Mimari
Bilmeniz gerekenler:
- **127.0.0.0/8:** Kendine dönüş (loopback) aralığı, genellikle 127.0.0.1 kullanılır.
- **Port:** Aynı bilgisayardaki kapı numarası. İki uygulama aynı portu kaparsa çakışır.
- **0.0.0.0 farkı:** Localhost yalnız size açıktır, 0.0.0.0 ağdaki herkese dinletir.

Sağlık denetimi örneği:

```
curl http://localhost:3000/api/health
```

Yanıt gelmiyorsa uygulama çalışmıyor veya port yanlıştır. Güvenlik duvarı localhost trafiğini genellikle serbest bırakır.

## Sık Karıştırılanlar
İnternet sitesi sanılır. Oysa localhost yalnızca sizin bilgisayarınıza özeldir, alan adı ve yayın gerektirmez.

## Farklı Disiplinlerde Kullanımı
- **Tiyatro:** Seyircisiz prova odası.
- **Müzik:** Kayıttan önce ses kontrolü.
- **Mutfak:** Servisten önce tadım.

## Bir benzetmeyle
Bir tiyatro oyununu sahneye koymadan önce boş bir odada yalnızca oyuncularla prova yapmak gibidir; seyirci henüz yoktur.

## Sıkça sorulanlar

**Neden localhost kullanıyoruz?**  
Hataları internete açmadan, güvenli şekilde kendi bilgisayarımızda düzeltmek için.

**127.0.0.1 nedir?**  
Localhost adının sayı karşılığıdır. Her bilgisayarda kendisini gösterir.

**Port nedir, neden gerekir?**  
Aynı bilgisayardaki uygulamaları ayıran kapı numarasıdır. Tarayıcı adresindeki iki nokta sonrasıdır.

**Dışarıdan erişilebilir mi?**  
Hayır. Başkalarının görmesi için yayın ve alan adı gerekir. Test bağlantısını paylaşmak için tünel araçları kullanılır.

## İlgili terimler
- [IDE](/dictionary/ide/)
- [Deployment](/dictionary/deployment/)
- [Network Stack](/dictionary/network-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/localhost/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
