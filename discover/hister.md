# Kişisel Sayfa ve Dosyalar İçin Özel Arama Motoru

Kullanıcının ziyaret ettiği sayfalar ve sakladığı dosyalar için AGPLv3 lisanslı özel bir arama motorudur. Tam metin indeksleme, gelişmiş sorgu filtreleri ve isteğe bağlı anlamsal arama sunar.

- ★ 2.620
- Go
- GitHub Trending · 2026-08-25

## Bu araç ne yapar?

Hister yerel olarak veya kontrol ettiğiniz altyapıda çalışabilir; zorunlu bir bulut servisi ve telemetri gerektirmez. Chrome ve Firefox eklentileriyle sayfaları indeksler, web sitesi tarama ve tarayıcı geçmişi içe aktarma seçenekleri sunar. Anlamsal arama etkinleştirilirse metin, seçilen embeddings uç noktasına gönderilir.

## Kimin için?

Web sayfalarını ve kişisel dosyaları kendi kontrolündeki bir arama altyapısında sorgulamak isteyenler.

## Ne beklememeli?

Zorunlu bulut hizmeti veya telemetri isteyen kullanım senaryoları ya da içeriğin yapılandırılmış Hister sunucusuna gönderilmesine izin verilmeyen tarayıcı indeksleme akışları.

## Öne çıkanlar
- Yerel veya kontrol edilen altyapıda, telemetri ve zorunlu bulut hizmeti olmadan çalışma
- Tam metin, alan filtreleri, ifadeler, joker karakterler, olumsuzlama ve önceliklerle sorgulama
- Web, terminal, TUI, CLI ve MCP istemcileri ile isteğe bağlı anlamsal arama

## İlk kullanım akışı
- Platformunuza uygun ikili dosyayı indirin ve Linux veya macOS'ta çalıştırılabilir yapın
- Hister sunucusunu yerel dinleme modunda başlatın
- Yerel web arayüzünü açın
- Chrome veya Firefox eklentisini kurup indekslenecek sayfaları seçin

## Güvenli başlangıç

Tarayıcı eklentisi, favicon indirme dışında indekslenen sayfa içeriğini yapılandırılmış Hister sunucusuna gönderir. İsteğe bağlı anlamsal arama, doküman metnini seçilen embeddings uç noktasına gönderir.

## İlk görev istemi
İlk adım için hazır istem
Yerel arayüzü açıp tarayıcı eklentisiyle seçtiğim sayfaları indeksle ve sorgu filtrelerini kullanarak aramayı doğrula.

## Kurulum

**Binary’yi çalıştırılabilir yap**

```
chmod +x hister
```

## Çalıştırma

**Hister sunucusunu başlat**

```
./hister listen
```

**Yerel arayüze eriş**

```
http://127.0.0.1:4433
```

Kaynak: Resmî README ve dokümantasyon kaynakları: https://hister.org/docs/quickstart, https://github.com/asciimoo/hister, https://hister.org/posts/how-i-use-hister

## Bağlantılar
- [GitHub deposu →](https://github.com/asciimoo/hister)
- [Quickstart →](https://hister.org/docs/quickstart)
- [Privacy ve kullanım README →](https://github.com/asciimoo/hister)
- [Kullanım akışı →](https://hister.org/posts/how-i-use-hister)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-25 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/hister/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
