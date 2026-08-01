# GitHub iş akışlarında depo kopyalama

GitHub tarafından geliştirilen actions/checkout, yazılım geliştirme süreçlerinde depo kopyalama (repository checkout) işlemlerini otomatize eden bir araçtır. Sürekli entegrasyon (continuous integration) iş akışlarında kaynak kodun çalışma ortamına aktarılmasını sağlar.

- ★ 8.197
- TypeScript
- GitHub Trending · 2026-07-03

## Ne kazandırır?
- Kaynak kodun çalışma ortamına aktarılması
- Otomatik depo kopyalama işlemleri
- Güvenli kimlik bilgisi yönetimi

## Nasıl başlanır?

GitHub Actions iş akışı dosyanızın (workflow) steps kısmına - uses: actions/checkout@v7 satırını ekleyerek aracın deponuzu çalışma alanına indirmesini sağlayabilirsiniz. İhtiyacınıza göre fetch-depth veya submodules gibi parametreleri with bloğu altında tanımlayarak kopyalama davranışını özelleştirebilirsiniz.
- [Resmî kaynak →](https://github.com/features/actions)

- **Kimin için:** GitHub Actions kullanarak sürekli entegrasyon süreçlerini otomatize eden yazılım geliştiriciler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/actions/checkout)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Repository Checkout Checkout Continuous Integration

---
Kaynak: TreScout Keşif · https://trescout.com/discover/checkout/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
