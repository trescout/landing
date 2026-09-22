# SQL Client nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

SQL Client (Türkçe karşılığıyla **SQL istemcisi**), ilişkisel veritabanlarına bağlanıp SQL sorgusu çalıştırmanızı sağlayan uygulamadır.

## Tanım ve Kelime Kökeni
SQL, **Structured Query Language** (Yapılandırılmış Sorgu Dili) ifadesinin kısaltmasıdır. **Client** ise hizmeti kullanan taraf demektir: Veritabanı sunucusu veriyi tutar, istemci ona bağlanıp soru sorar. DBeaver, DataGrip, TablePlus ve komut satırındaki `psql` yaygın örneklerdir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Veri analisti:** Satış tablosundan son ayın raporunu çeker.
- **Geliştirici:** Uygulamasının okuduğu kayıtları gözle denetler.
- **Veritabanı yöneticisi:** Yedekleri, kullanıcıları ve izinleri yönetir.

Tipik bir kullanım, adresi girip bağlanmak ve şu tür bir soru yazmaktır:

```
SELECT ad, eposta FROM musteriler WHERE sehir = 'İstanbul' LIMIT 10;
```

## Teknik Derinlik ve Mimari
Bir SQL istemcisinin arka planında şunlar çalışır:
- **Bağlantı ve sürücü:** İstemci, adres, port, kullanıcı adı ve parola ile sunucuya bağlanır. Her veritabanının kendi iletişim kuralı ve sürücüsü vardır.
- **Sorgu gönderimi:** Yazdığınız SQL metni sunucuya iletilir, sonuç satırlar halinde geri döner.
- **Hazır ifadeler (Prepared Statements):** Tekrarlanan sorgular önceden derlenir. Bu, hem hız kazandırır hem de zararlı girdi enjeksiyonuna karşı korur.
- **İşlemler (Transactions):** Birden çok yazma adımı tek bir bütün olarak işlenir. Hata olursa hiçbiri uygulanmaz.
- **Güvenli bağlantı:** Parola ve veriler şifreli kanaldan taşınır. Herkesin eriştiği ağlarda şifresiz bağlantı kullanılmamalıdır.

## ORM ile İstemci Farkı
ORM (Object-Relational Mapping), SQL yazmadan kod içinden veritabanıyla konuşmanızı sağlayan katmandır. SQL istemcisi ise SQL yazdığınız penceredir. ORM üretkenliği artırır, istemci ise neyin gerçekten çalıştığını görmenizi sağlar. İkisi birbirinin rakibi değil, tamamlayıcısıdır.

## Farklı Disiplinlerde Kullanımı
- **Kütüphanecilik:** Danışma görevlisi rafların yerini bilir, istediğiniz kaydı bulur.
- **Muhasebe:** Defterdeki kalemleri tek tek inceleyen denetçi.
- **Lojistik:** Depodaki ürünleri listeleyen el terminali.

## Bir benzetmeyle
Devasa bir kütüphanenin danışma görevlisi gibidir: Rafların (tabloların) yerini bilir, istediğiniz kitabı (kaydı) bulur, yenilerini rafa yerleştirir.

## Sıkça sorulanlar

**SQL bilmek şart mı?**  
Temel komutları (SELECT, WHERE, JOIN) bilmeniz gerekir. Grafiksel araçlar yardımcı olur, ancak karmaşık sorular için SQL şarttır.

**Ücretsiz istemci var mı?**  
Evet. DBeaver Community ve psql ücretsizdir. Birçok veritabanının kendi resmi aracı da ücretsiz sunulur.

**İstemci veriyi saklar mı?**  
Hayır. İstemci yalnızca bağlantı penceresidir. Veri sunucuda durur, istemciyi silmeniz veriyi silmez.

**Bağlantıyı nasıl güvenli tutarım?**  
Şifreli bağlantı kullanın, güçlü parola belirleyin, erişimi IP ile sınırlayın ve bağlantı bilgilerini kimseyle paylaşmayın.

## İlgili terimler
- [Database](/dictionary/database/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [ORM](/dictionary/orm/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/sql-client/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
