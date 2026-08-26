# TreScout kontrollü beta ölçüm planı

Bu belge, TreScout’un canlı rapor arşivinden erken erişim listesine uzanan akışı ölçmek için kullanılan **consent sonrası, sıfır-PII event sözleşmesini** tanımlar. Event’ler kullanıcı açıkça anonim ürün ölçümünü etkinleştirmeden gönderilmez. Bu belge hukuki uyumluluk görüşü değildir; provider veri işleme koşulları ve son privacy metni ayrıca onaylanmalıdır.

## 1. Event sözleşmesi

| Event | Anlamı | İzinli bağlam |
|---|---|---|
| `discovery_view` | Bir keşif detay sayfası görüntülendi | `pageType`, `contentSlug`, `placement`, `path`, `locale` |
| `report_preview_open` | Bir rapor detay sayfası açıldı | `pageType`, `contentSlug`, `placement`, `path`, `locale` |
| `beta_report_open` | PDF veya rapor aksiyon bağlantısı seçildi | `pageType`, `contentSlug`, `placement`, `path`, `locale` |
| `early_access_start` | Erken erişim formundaki e-posta alanına ilk odaklanma | `pageType`, `contentSlug`, `placement`, `path`, `locale` |
| `early_access_submit` | Form submit işlemi başarıyla sonuçlandı | `pageType`, `contentSlug`, `placement`, `isDuplicate`, `path`, `locale` |
| `beta_return_week_2` | Consent sonrası ilk görülmeden 7–30 gün aralığında geri dönüş sinyali | `pageType`, `contentSlug`, `placement`, `daysSinceFirstSeen`, `path`, `locale` |

Event payload’larına e-posta, isim, serbest metin, dış origin URL’si, referrer, UUID veya ham query parametreleri eklenmez. UTM değerleri yalnızca kısa identifier token’ları olarak kabul edilir. Consent verilmeden önce ne event gönderilir ne de retention amacıyla `localStorage` yazılır.

## 2. KPI tanımları

| KPI | Hesaplama | Yorum sınırı |
|---|---|---|
| **Keşif ilgisi** | `discovery_view` event sayısı | Kullanıcı tekilleştirmesi yapılmadığı için aggregate event hacmidir |
| **Rapor okuma ilgisi** | `beta_report_open / report_preview_open` | Aynı sayfa veya aynı ziyaret için tekrarlar olabilir |
| **Form başlatma oranı** | `early_access_start / report_preview_open` | Form görünürlüğü ve trafik kaynağı ayrıca izlenmelidir |
| **Form tamamlanma oranı** | `early_access_submit / early_access_start` | Submit event’i yalnız API başarılı yanıtından sonra üretilmelidir |
| **Tekrar dönüş sinyali** | `beta_return_week_2` teslim edilen event sayısı | `firstSeen` yalnız consent sonrası tutulur; kullanıcı kimliği yoktur |
| **Duplicate submit oranı** | `early_access_submit` içinde `isDuplicate=true` payı | Liste kalitesi ve tekrar denemeleri anlamak için kullanılır |

Mevcut sıfır-PII modelde **unique user, session, retention cohort veya gerçek dönüşüm oranı** iddiası yapılmamalıdır. Vercel Custom Events’in production panelinde gerçekten alındığı ve aggregation semantiği doğrulanmadan bu KPI’lar yalnızca yön gösteren aggregate sinyaller olarak kullanılmalıdır.

## 3. Production doğrulama checklist’i

1. Production’da `UPSTASH_REDIS_REST_URL` ve `UPSTASH_REDIS_REST_TOKEN` mevcut olmalıdır. Eksik veya erişilemez durumlarda subscribe endpoint’i fail-closed olarak `503` döndürür.
2. Bir test deployment’ında consent yokken provider scriptlerinin network isteği başlatmadığı, `ts_telemetry_consent`, `ts_first_seen` ve `ts_retention_w2` anahtarlarının yazılmadığı görülmelidir.
3. Consent verildikten sonra provider scriptleri yalnızca bir kez yüklenmeli; custom event’in provider panelinde göründüğü doğrulanmalıdır.
4. Submit smoke testi gerçek kişisel veri kullanmadan `example.invalid` gibi ayrılmış bir alan adıyla yapılmalıdır. Başarılı liste kaydı testi gerekiyorsa açıkça yetkilendirilmiş bir test adresi kullanılmalı ve sonrasında suppression/unsubscribe kontrol edilmelidir.
5. Provider, Resend ve Vercel loglarında e-posta, IP, referrer ve ham hata gövdesi gibi gereksiz kişisel veri bulunmadığı periyodik olarak kontrol edilmelidir.

## 4. Ürün kararları

E-posta teslimi, teslim saati seçimi ve konu filtreleri henüz erken erişim kapsamındadır. Bu nedenle landing sayfası bugün için canlı rapor arşivini, erken erişim formu ise gelecekteki ürün davetini temsil eder. Bu ayrım ürün kopyasında korunmalı; aktif olmayan özellikler “şu anda kullanılabilir” gibi sunulmamalıdır.

İptal/unsubscribe ve suppression akışı gerçek e-posta gönderimi başlamadan önce tamamlanmalıdır. Provider analytics’in consent kapsamı, lawful basis, veri lokasyonu ve saklama süresi için hukuk/ürün sahibi onayı alınmadan form veya privacy kopyasına resmî GDPR/KVKK uyumluluk iddiası eklenmemelidir.
