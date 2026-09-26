# Java kodlarında kurumsal stil ve kalite denetimi

Checkstyle, Java projelerinde Google Java Style ve Sun kod kurallarına uyumu otomatik denetleyen, CI/CD boru hatlarına entegre edilebilen öncü bir statik analiz aracıdır.

- ★ 9.288
- Java
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 9.288, sürüm v10.18.0 ile Java 23 dil özellikleri ve gelişmiş AST kural denetimi.

## Ne kazandırır?
- Kurumsal standartlara uyum: Google Java Style ve Sun Code Conventions şablonları ile ekip genelinde sıfır biçimlendirme tartışması.
- Soyut sözdizim ağacı (AST) analizi: Yalnızca metin araması değil, Java kodunun anlamsal gramer yapısını derinlemesine denetleyebilme.
- Zengin dahili kural kütüphanesi: İsimlendirme standartları, boşluk düzeni, iç içe blok derinliği, javadoc eksiklikleri ve karmaşıklık metrikleri.
- Derleme aracı ekosistemi: Maven (maven-checkstyle-plugin) ve Gradle eklentileri ile derleme adımında otomatik kalite kapısı.
- Özelleştirilebilir XML yapılandırması: Ekip gereksinimlerine göre kuralları esnetme, dışlama (suppression) ve uyarı/hata seviyelerini yönetme.

## Kurulum

**Bağımsız CLI jar dosyasını indir**

```
curl -sSL -O https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.18.0/checkstyle-10.18.0-all.jar
```

## Çalıştırma

**Google Java Style kurallarıyla analiz et**

```
java -jar checkstyle-10.18.0-all.jar -c /google_checks.xml src/
# veya Maven ile:
./mvnw checkstyle:check
```

## Teknik mimari ve çalışma prensibi

Checkstyle, Java kaynak dosyalarını AST ağaçlarına dönüştürerek kural tabanlı gezinen bir denetim mimarisi kullanır:
- Java Parser ve ANTLR Altyapısı: ANTLR tabanlı gramer çözümleyici ile her sınıfı, metodu ve ifadeyi ağaç düğümlerine ayırır.
- Olay Tabanlı Ziyaretçi (Visitor) Deseni: Her kural denetleyicisi yalnızca ilgilendiği AST düğümlerine abone olarak yüksek performanslı tarama sağlar.
- SuppressionFilter ve Yorum İhlal İstisnaları: CHECKSTYLE:OFF etiketleri veya XML filtreleriyle belirli satır ve sınıfları denetim dışı bırakabilme.

## Kural setleri ve CI/CD entegrasyonu

Checkstyle'ı yazılım geliştirme döngüsünün parçası haline getirmek kod kalitesini kalıcı olarak güvenceye alır:
- GitHub Actions ile Pull Request Kapısı: Her PR açıldığında checkstyle denetimini çalıştırarak standart dışı kodların ana dala girmesini engelleyin.
- IDE Entegrasyonu (IntelliJ & Eclipse): Geliştiricilerin kod yazarken gerçek zamanlı stil uyarıları almasını sağlayarak geri bildirim döngüsünü hızlandırın.
- HTML ve XML Raporları Üretimi: Kod tabanındaki teknik borcu ve stil ihlallerini grafik ve tablolar halinde raporlayarak arşivleyin.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Mevcut bir Spring Boot projesinde Maven ile Checkstyle eklentisini nasıl yapılandıracağımı, Google Java Style kurallarını nasıl temel alacağımı ve ekip standartlarımıza göre satır uzunluğu sınırını 120 karaktere nasıl güncelleyeceğimi pom.xml ve checkstyle.xml örnekleriyle açıklar mısın?

- **Kimin için:** Java geliştiricileri, yazılım mimarları, kalite güvence ekipleri ve teknik liderler. 
- **Lisans:** LGPL-2.1 (Açık kaynak kütüphane lisansı) 
- **Çatı:** Java Statik Kod Analiz Aracı 
- **Platformlar:** JVM (Java Virtual Machine), Linux, macOS, Windows 

## Sıkça sorulan sorular
- Checkstyle kodumu otomatik olarak düzeltir mi? Hayır. Checkstyle kurallara uymayan satırları tespit eden bir analiz aracıdır (linter). Otomatik kod yeniden biçimlendirme için Spotless veya google-java-format gibi araçlarla birlikte kullanılır.
- Google Java Style ile Sun standartları arasındaki fark nedir? Sun standartları 1999 yılındaki orijinal Java kurallarını (4 boşluk girinti, 80 karakter satır) temel alır. Google Java Style ise 2 boşluk girinti ve 100 karakter sınırıyla modern endüstriyel pratiği yansıtır.
- Checkstyle derlemeyi durdurabilir mi? Evet. Maven veya Gradle üzerinde failOnViolation veya maxAllowedViolations parametreleriyle stil hatası bulunan kodların derlenmesi engellenebilir.
- Büyük projelerde performansı nasıldır? Checkstyle soyut sözdizim ağacı (AST) üzerinde çalıştığı için yüz binlerce satırlık projeleri dahi saniyeler içinde tarayabilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/checkstyle/checkstyle)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CI/CD Açık Kaynak CLI Framework API

---
Kaynak: TreScout Keşif · https://trescout.com/discover/checkstyle/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
