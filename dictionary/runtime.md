# Runtime ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Runtime (çalışma zamanı), bir programın derleme evresinden sonra bilgisayar işlemcisinde ve belleğinde fiilen çalıştırıldığı anı ve bu süreci yöneten yürütme ortamını ifade eder.

## Tanım ve çalışma zamanı ortamları
Runtime kavramı yazılımda iki temel anlamı barındırır:
1. **Zaman Dilimi Olarak (Runtime):** Kodun yazıldığı (authoring) ve makine diline çevrildiği (compile-time) aşamadan sonra; kullanıcının programı başlattığı ve programın donanım kaynaklarını tüketerek çalıştığı 'çalışma zamanı' evresidir.
2. **Yürütme Ortamı Olarak (Runtime Environment):** Yazılan kodun işletim sistemi üzerinde doğrudan çalışabilmesi için gereken motor, kütüphaneler ve yardımcı katmandır. Örneğin tarayıcı dışındaki JavaScript için Node.js, Deno veya Bun; Java için JVM (Java Virtual Machine); C# için .NET CLR birer runtime'dır.

## Bir benzetmeyle
Bir yemek tarifinin kağıda dökülüp kontrol edilmesi derleme (compile-time) ise; o yemeğin ocakta fiilen pişmesi, kokusunun yayılması ve servis edilmesi çalışma zamanıdır (runtime). Mutfağın kendisi ve kullanılan aletler ise yürütme ortamıdır (runtime environment).

## Nasıl çalışır?
Program başlatıldığında işletim sistemi bellekte (RAM) yer açar, runtime motoru kod parçacıklarını yürütür, fonksiyon çağrılarını (call stack) yönetir ve veri akışını koordine eder.

## Nerede kullanılır?
Tüm yazılım geliştirme, hata ayıklama (debugging), performans izleme (APM) ve konteyner (Docker, Kubernetes) ortamlarında temel kavramdır.

## Sık karıştırılanlar
- **Runtime vs Compile-time:** Compile-time derleme anıdır; sözdizimi ve tip hataları bu aşamada yakalanır. Runtime ise programın çalıştığı andır; mantıksal hatalar veya bellek sorunları bu aşamada ortaya çıkar.

## Sıkça sorulanlar

**Runtime ne demek ve Türkçe karşılığı nedir?**  
Türkçede 'çalışma zamanı' veya 'çalışma ortamı' olarak kullanılır. Kodun aktif olarak işlem gördüğü süreci temsil eder.

**Runtime Error (Çalışma Zamanı Hatası) ne anlama gelir?**  
Derleme aşamasında fark edilmeyen ancak program çalışırken beklenmedik bir girdi, sıfıra bölme veya bellek yetersizliği gibi nedenlerle programın aniden durmasına (çökmesine) yol açan hatalardır.

**JavaScript runtime'ları (Node.js, Bun, Deno) arasındaki fark nedir?**  
Hepsi JavaScript kodunu çalıştırmak için V8 veya JavaScriptCore motorunu kullanır; ancak dosya sistemi erişimi, paket yöneticisi hızı ve TypeScript desteği gibi alanlarda farklı performans ve mimari optimizasyonları sunar.

## İlgili terimler
- [Compile-time](/dictionary/compile-time/)
- [State Management](/dictionary/state-management/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/runtime/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
