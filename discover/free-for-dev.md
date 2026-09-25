# Ücretsiz geliştirici araçları kaynak listesi

free-for-dev, yazılım geliştiricilerin, girişimcilerin ve altyapı mühendislerinin sıfır sermaye ile MVP ve projeler inşa edebilmesi için kalıcı ücretsiz katman (free tier) sunan binden fazla SaaS, PaaS ve IaaS servisini listeleyen açık kaynaklı devasa bir kaynak kütüphanesidir.

- ★ 137.565
- HTML
- GitHub Trending · 2026-06-27

## Güncelleme
- 16 Eylül 2026: Yıldız 137.565, topluluk onaylı yeni nesil sunucusuz veritabanları (serverless DB) ve yapay zekâ çıkarım API'leri listeye eklendi.

## Ne kazandırır?
- Sıfır altyapı maliyeti ile MVP geliştirme: Fikirlerinizi kredi kartı riski veya aylık sabit sunucu faturası ödemeden gerçek kullanıcılarla test etme.
- Binden fazla kategorize edilmiş servis: Bulut barındırma, sunucusuz mimariler, veritabanları, CDN, kimlik doğrulama, CI/CD ve izleme araçları.
- Yalnızca gerçek ücretsiz katmanlar: Geçici 14 günlük deneme sürümleri elenir; yalnızca kalıcı (Always Free) plan sunan platformlar kabul edilir.
- Topluluk denetimi ve güncellik: Binlerce açık kaynak katkıcısı tarafından sürekli test edilen ve kapanan servisleri temizleyen canlı ekosistem.
- Mimari esneklik: Farklı bulut sağlayıcıların ücretsiz kotalarını birleştirerek kurumsal seviyede hibrit altyapı tasarlama.

## Öne çıkan kategoriler ve ücretsiz altyapılar

free-for-dev rehberi modern bir web veya mobil uygulamanın tüm ihtiyaçlarını kapsayan ana başlıklara ayrılmıştır:
- Sunucu ve Bulut Hesaplama (IaaS/PaaS): Oracle Cloud (Always Free 4 çekirdek ARM / 24 GB RAM), Cloudflare Workers, Fly.io ve Render.
- Veritabanı ve Depolama (DBaaS): Supabase (PostgreSQL), Neon (Serverless Postgres), Cloudflare D1/R2 ve Upstash (Redis).
- Kimlik Doğrulama ve Güvenlik (Auth & Sec): Clerk, Auth0, Stytch ve Let's Encrypt SSL sertifikaları.
- Sürekli Entegrasyon ve Test (CI/CD): GitHub Actions (2000 dk/ay), GitLab CI ve Codecov kod kapsama analizleri.
- Gözlemlenebilirlik ve Log Yönetimi: Grafana Cloud, Better Stack, Sentry (hata takibi) ve Axiom.

## Topluluk kuralları ve ücretsiz katman kriterleri

Rehbere eklenecek her servisin katı topluluk kalite standartlarını karşılaması zorunludur:
- Gerçek ücretsiz plan şartı: Sadece süre sınırı olmayan kalıcı ücretsiz kullanım hakkı sunan servisler listelenir.
- Kredi kartı zorunluluğu kısıtı: Kayıt aşamasında kredi kartı talep etmeyen veya sadece kimlik doğrulama amaçlı sıfır çekim yapanlar açıkça belirtilir.
- Otomatik link kontrolü: Depoya gönderilen her Pull Request, GitHub Actions botları tarafından kırık bağlantı testinden geçirilir.

## Mimari yaklaşım ve başlangıç rehberi

free-for-dev listesini kullanarak sıfır maliyetli modern bir web uygulaması kurmak için önerilen mimari:
- Statik Ön Yüz ve Dağıtım: Vercel veya Cloudflare Pages üzerinde React/Next.js uygulaması.
- Veritabanı Katmanı: Supabase üzerinde 500 MB ücretsiz PostgreSQL ve yerleşik satır bazlı güvenlik (RLS).
- E-posta ve Bildirimler: Resend üzerinden ayda 3.000 adet ücretsiz işlem e-postası (transactional email).

## Maliyet optimizasyonu ve kota aşımı stratejileri

Ücretsiz katmanlarda sürpriz faturalarla karşılaşmamak için izlenmesi gereken adımlar:
- Bütçe ve harcama limitleri tanımlama: Platform panellerinde harcama tavanını (spend limit) kesin olarak 0 USD olarak ayarlayın.
- Önbellekleme (Caching) kullanımı: Cloudflare ücretsiz CDN ile statik ve dinamik varlıkları önbelleğe alarak API çağrılarını %80 azaltın.
- Veri tabanı bağlantı havuzlama (Pooling): Sunucusuz ortamlarda bağlantı sınırlarına takılmamak için PgBouncer veya yerleşik pooler kullanın.

## Kod bilmiyorsanız
🤖 Kod bilmiyorsanız
Yeni bir web girişimi için tamamen ücretsiz servislerden oluşan modern bir bulut altyapısı kurmak istiyorum. free-for-dev listesindeki en popüler ücretsiz sağlayıcıları (barındırma, veritabanı, kimlik doğrulama ve e-posta servisi) birleştiren, kota sınırlarını aşmayacak sıfır maliyetli bir mimari planı ve kurulum adımlarını açıklar mısın?

- **Kimin için:** Girişimciler, bağımsız geliştiriciler, öğrenciler ve altyapı maliyetini sıfırlamak isteyen mühendisler.
- **Lisans:** CC BY 4.0 (Açık içerik lisansı)
- **Küratör:** R.I. Pienaar ve 1000'den fazla açık kaynak katkıcısı
- **Servis Sayısı:** 1.000'den fazla doğrulanmış ücretsiz servis

## Sıkça sorulan sorular
- Ücretsiz katman ile deneme sürümü (Free Trial) arasındaki fark nedir? Deneme sürümleri genellikle 7 ila 30 gün sonra sona erer ve ödeme ister. free-for-dev listesindeki servisler ise belirli kotalar dahilinde süresiz olarak ücretsizdir.
- Kredi kartı girmeden kullanılabilecek servisler var mı? Evet. Listedeki birçok servis (Supabase, Vercel, Cloudflare, Fly.io) kayıt sırasında kredi kartı talep etmez.
- Ücretsiz kotalar dolduğunda ne olur? Harcama limiti konulmuşsa servis geçici olarak istekleri reddeder (HTTP 429 veya 503) ancak kartınızdan para çekilmez.
- Büyük ölçekli projeler için bu servisler yeterli midir? MVP, ilk kullanıcılar ve orta ölçekli trafik için fazlasıyla yeterlidir; ürün gelir üretmeye başladığında aynı platformlar üzerinde tek tıkla ücretli planlara geçilebilir.

## Bağlantılar
- [GitHub →](https://github.com/ripienaar/free-for-dev)

## İlgili sözlük terimleri
SaaS PaaS IaaS Cloud Computing Open Source API

---
Source: TreScout Discover · https://trescout.com/discover/free-for-dev/
