# Cloudflare üzerinde ücretsiz geçici e-posta

Cloudflare Temp Email, Cloudflare Workers, Pages ve D1/KV veritabanı altyapısını kullanarak tamamen ücretsiz, sunucusuz (serverless) ve kendi alan adınızla çalışan geçici e-posta (disposable email) servisi kurmanızı sağlayan açık kaynaklı bir platformdur. Gelen kutusu yönetimi, eklerin saklanması, Telegram botu entegrasyonu ve otomatik temizlik mekanizmalarıyla kişisel gizliliğinizi korur.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Güncelleme
- 13 Eylül 2026: Yıldız 11.391 → 11.734, son sürüm v1.12.0 (13 Eylül 2026).
- 23 Ağustos 2026: Yıldız 11.332 → 11.391, son sürüm v1.11.1 (22 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 11.156 → 11.332, son sürüm v1.11.0 (19 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 10.884 → 11.156, son sürüm v1.10.0 (31 Temmuz 2026).

## Ne kazandırır?
- Sıfır sunucu ve operasyon maliyeti: Cloudflare'in cömert ücretsiz tarifesi (günde 100.000 Workers isteği, ücretsiz Email Routing ve Pages barındırma) üzerinde harici bir sunucu kiralamadan çalışır.
- Özel alan adı ve engellenemeyen adresler: Genel geçici e-posta servislerinin aksine web sitelerinin kara listesine takılmayan kendi alan adınızla tek kullanımlık adresler üretir.
- Rust ve WASM ile hızlı e-posta ayrıştırma: Gelen karmaşık MIME, multipart ve HTML içerikli e-postaları Rust ile derlenmiş WebAssembly modülü sayesinde milisaniyeler içinde işler.
- Telegram botu ve anlık bildirimler: Yeni bir e-posta geldiğinde doğrudan Telegram üzerinden bildirim alın, mesaj içeriğini okuyun veya bot komutlarıyla anında yeni adres oluşturun.
- Otomatik temizlik ve güvenli erişim: Belirlenen süre sonunda eski iletileri ve ekleri otomatik temizler; admin parolasıyla yetkisiz erişimi engeller.

## Nasıl başlanır ve kurulum seçenekleri

Projeyi devreye almak için Cloudflare hesabınız ve Cloudflare DNS üzerinde yönetilen bir alan adınızın bulunması yeterlidir. İster Cloudflare Pages üzerinden GitHub deposunu tek tıkla bağlayarak grafiksel arayüzle dağıtabilir, isterseniz Wrangler CLI aracılığıyla yerel ortamınızdan D1 veritabanı ve Worker fonksiyonlarını yayına alabilirsiniz.
- [Resmî kurulum rehberi →](https://temp-mail-docs.awsl.uk)
- [Canlı demo arayüzü →](https://mail.awsl.uk)

## Teknik mimari ve çalışma prensibi

Cloudflare Temp Email, geleneksel SMTP sunucuları (Postfix, Dovecot) kurma ve yönetme yükünü tamamen ortadan kaldıran modern bir sunucusuz (serverless) mimari üzerine kuruludur:
- Cloudflare Email Routing entegrasyonu: Alan adınıza gelen tüm MX trafiği Cloudflare altyapısında karşılanır ve catch-all kuralıyla doğrudan yakalayıcı Worker fonksiyonuna yönlendirilir.
- Edge Worker ve Rust WASM ayrıştırıcı: Gelen e-posta akışı (raw stream), Worker içinde çalışan optimize edilmiş Rust WASM motoruna aktarılarak başlıklar, gövde, HTML ve ekler hızla ayrıştırılır.
- Cloudflare D1 ve R2 depolama: E-posta metinleri ve meta verileri kenar SQLite veritabanı olan Cloudflare D1 üzerinde saklanır. Dosya ekleri isteğe bağlı olarak Cloudflare R2 nesne depolamasına yazılır.
- Modern tek sayfa uygulama (SPA): Kullanıcı dostu web arayüzü Cloudflare Pages'in küresel CDN ağı üzerinden sıfır gecikmeyle servis edilir.
- REST API ve harici entegrasyonlar: Otomatik testler veya üçüncü taraf yazılımlar için REST API uç noktaları üzerinden yeni e-posta adresi türetme ve gelen kutusunu sorgulama imkânı sunar.

## Kurulum ve örnek dağıtım

```bash
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Cloudflare üzerinde çalışan dreamhunter2333/cloudflare_temp_email açık kaynaklı geçici e-posta projesini kendi alan adımla kurmak istiyorum. Cloudflare hesabım ve Cloudflare DNS'e bağlı bir alan adım var. Cloudflare panosu üzerinden Email Routing yönlendirmesini, D1 veritabanını ve Cloudflare Pages arayüzünü sıfırdan nasıl kuracağımı adım adım anlatır mısın? Ayrıca gelen e-postaları Telegram botuma yönlendirmek için hangi yapılandırma adımlarını izlemeliyim?

- **Kimin için:** Kendi alan adıyla ücretsiz, güvenli ve engelsiz geçici e-posta servisi barındırmak isteyen geliştiriciler, test ekipleri ve gizlilik odaklı kullanıcılar içindir. 
- **Lisans:** MIT (Özgür açık kaynak lisansı) 
- **Altyapı:** Cloudflare Workers, Pages, D1 (SQLite) ve Email Routing 
- **Diller ve Araçlar:** TypeScript, Rust (WASM), Vue 3, Wrangler 

## Sıkça sorulan sorular
- Cloudflare'in ücretsiz planı kişisel kullanım için yeterli mi? Evet. Cloudflare ücretsiz tarifesinde günlük 100.000 Worker isteği, ücretsiz Email Routing ve D1 veritabanı kotası sunar. Kişisel kullanımda ve küçük ekiplerde bu sınırların aşılması neredeyse imkansızdır; sistem tamamen sıfır maliyetle çalışır.
- Servisi kullanmak için özel bir alan adı (custom domain) şart mı? Evet. E-posta alabilmek için Cloudflare DNS üzerinde yönetilen bir alan adına (veya alt alan adına, örn. mail.alanadiniz.com) sahip olmanız gerekir. Bu sayede genel geçici e-posta servislerini engelleyen siteleri kolayca aşabilirsiniz.
- Gelen e-postalar kalıcı olarak saklanır mı? Hayır, bu bir geçici e-posta servisidir. Sistem yöneticisi olarak panelden e-postaların saklanma süresini (örneğin 1 saat, 24 saat veya 7 gün) belirleyebilirsiniz; süresi dolan kayıtlar D1 ve R2 depolama alanından otomatik silinir.
- Servis üzerinden dışarıya e-posta yanıtı gönderilebilir mi? Evet. Cloudflare Email Routing yalnızca e-posta alımını desteklese de; proje Resend, Brevo veya özel bir SMTP sunucusu API'si bağlandığında web panelinden dış dünyaya e-posta gönderme ve yanıtlama işlemlerini de destekler.

## Bağlantılar
- [GitHub deposu →](https://github.com/dreamhunter2333/cloudflare_temp_email)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-23 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Self-Hosted Cloud Computing Digital Privacy Open Source API Rust

---
Kaynak: TreScout Keşif · https://trescout.com/discover/cloudflare-temp-email/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
