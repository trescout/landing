# C++ projeleri için hızlı günlük kaydı

spdlog, C++ programlama dili için geliştirilmiş, yalnızca başlıklardan (header-only) veya derlenmiş kütüphane olarak kullanılabilen ultra hızlı bir günlük kaydı (logging) kütüphanesidir. Modern C++ standartlarını kullanarak yazılım projelerinde gecikmesiz ve yüksek performanslı çıktı yönetimi sunar.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Güncelleme
- 6 Ağustos 2026: Yıldız 29.402 → 29.437, son sürüm v1.17.0 (4 Ocak 2026).

## Ne kazandırır?
- Saniyede milyonlarca satır loglama performansı: Sıfır bellek tahsisi yaklaşımı ve derleme zamanı optimizasyonlarıyla ana uygulama iş parçacığında mikrosaniye düzeyinde gecikme yaratır.
- Asenkron ve kilitsiz (lock-free) halka kuyruk: Log yazma işlemlerini arka plan havuzuna devrederek dosya veya ağ G/Ç darboğazlarını çağrı hattından tamamen yalıtır.
- Zengin hedef (sink) çeşitliliği: Renkli konsol çıktısı, boyuta göre dönen (rotating) dosyalar, günlük tarihli arşivler, syslog ve Android logcat hedeflerine eşzamanlı yazım imkanı.
- Entegre fmt biçimlendirme gücü: C++20 format standardının temeli olan {fmt} kütüphanesini kullanarak güvenli, hızlı ve Python tarzı esnek metin biçimlendirme sağlar.
- Header-only veya derlenmiş kullanım esnekliği: Projenize tek bir dizin kopyalayarak dahil edebilir veya derleme sürelerini düşürmek için statik kütüphane olarak bağlayabilirsiniz.

## Kurulum

**macOS (Homebrew)**

```
brew install spdlog
```

**vcpkg ile paket kurulumu**

```
vcpkg install spdlog
```

**CMake FetchContent entegrasyonu**

```
include(FetchContent)
FetchContent_Declare(
spdlog
GIT_REPOSITORY https://github.com/gabime/spdlog.git
GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(projem PRIVATE spdlog::spdlog)
```

Kaynak: Homebrew formülü

## Nasıl başlanır ve temel kullanım

spdlog kütüphanesini kullanmaya başlamak son derece zahmetsizdir. Başlık dosyasını projenize dahil ettikten sonra doğrudan küresel loglama fonksiyonlarını çağırabilir veya özelleştirilmiş logger nesneleri oluşturabilirsiniz:

**Temel C++ Kullanım Örneği**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
// Standart konsol loglaması
spdlog::info("spdlog basariyla baslatildi.");
spdlog::warn("Dikkat: Bellek kullanimi yukseliyor!");
spdlog::error("Hata kodu: {:d}, aciklama: {}", 404, "Sayfa bulunamadi");

// Boyuta gore donen (rotating) dosya logger'i (maksimum 5MB, 3 dosya)
auto file_logger = spdlog::rotating_logger_mt("dosya_log", "logs/uygulama.txt", 1024 * 1024 * 5, 3);
file_logger->info("Bu mesaj hem thread-safe hem de otomatik arsivlenen dosyaya yazilir.");

return 0;
}
```

## Teknik mimari ve çalışma prensibi

spdlog kütüphanesinin benzersiz hızı, modüler ve sıfır ek yük (zero-overhead) odaklı yazılım mimarisine dayanır:
- Logger ve Sink ayrımı: Logger nesnesi gelen günlüğü filtreler (trace, debug, info, warn, err, critical). Kabul edilen iletiler bir veya birden fazla Sink nesnesine aktarılır. Örneğin tek bir logger aynı anda konsola renkli basarken dosyaya JSON formatında yazabilir.
- İş parçacığı güvenliği (_mt vs _st): spdlog tüm sink sınıflarını iki biçimde sunar: Çok iş parçacıklı güvenli muteks kilitlemeli (_mt) ve tek iş parçacığına özel kilitsiz (_st) sürümler. Tek iş parçacıklı modda muteks maliyeti tamamen sıfırlanır.
- Asenkron halka kuyruk (Ring Buffer): spdlog::init_thread_pool ile tahsis edilen bellek bloğu, arka planda çalışan iş parçacığı tarafından tüketilir. Ana uygulama log kaydını kuyruğa bırakıp derhal yoluna devam eder.
- Akıllı tampon boşaltma (Flush): Performans için veriler işletim sistemi tamponunda bekletilir; ancak kritik hata anlarında veri kaybını önlemek için spdlog::flush_on(spdlog::level::err) mekanizması tetiklenebilir.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Modern bir C++ projesinde CMake kullanarak spdlog kütüphanesini asenkron mimariyle yapılandırmak istiyorum. Günlük 10MB boyuta ulaştığında dosyayı döndüren (rotating file), aynı zamanda konsola renkli çıktı veren ve hata (error) seviyesinde anında diske yazan (flush) örnek bir C++ başlatma fonksiyonu ile birlikte CMakeLists.txt dosyasını hazırlar mısın?

- **Kimin için:** Yazılım projelerinde hata ayıklama, izleme ve denetim süreçlerini sıfır gecikmeyle hızlandırmak isteyen C++ geliştiricileri, oyun motoru ve gömülü sistem mimarları içindir. 
- **Lisans:** MIT Lisansı (Ticari ve açık kaynak projelerde tamamen serbest) 
- **Standart:** C++11, C++14, C++17, C++20 ve C++23 uyumlu 
- **Kütüphane Tipi:** Header-only veya önceden derlenmiş (Compiled) statik/dinamik bağlama 

## Sıkça sorulan sorular
- spdlog header-only olarak mı yoksa derlenerek mi kullanılmalı? Küçük ve orta ölçekli projelerde yalnızca include dizinini ekleyerek header-only kullanmak büyük pratiklik sağlar. Ancak yüzlerce kaynak dosyasından oluşan büyük C++ projelerinde derleme süresini optimize etmek için SPDLOG_COMPILED bayrağıyla kütüphaneyi derleyip bağlamak tavsiye edilir.
- Loglama ana uygulamanın çalışma hızını etkiler mi? Senkron modda dahi mikrosaniye seviyesinde çalışan spdlog, asenkron logger mimarisi kullanıldığında ana iş parçacığı üzerindeki G/Ç yükünü neredeyse sıfıra indirir. Mesaj kuyruğa kopyalanır ve disk yazımı arka planda gerçekleşir.
- Dönen dosya (rotating file) mekanizması nasıl çalışır? Belirtilen azami dosya boyutuna (örneğin 10MB) ulaşıldığında aktif dosya arşivlenir (uygulama.1.txt, uygulama.2.txt) ve sıfırdan yeni dosya açılır. Belirlenen maksimum dosya adedi aşıldığında ise en eski log dosyası otomatik olarak temizlenir.
- Harici fmt kütüphanesi ile çakışma yaşanır mı? Hayır. spdlog varsayılan olarak dahili paketlenmiş fmt sürümünü kullanır. Dilerseniz SPDLOG_FMT_EXTERNAL makrosunu tanımlayarak sisteminizdeki mevcut bağımsız fmt kütüphanesini doğrudan spdlog ile entegre edebilirsiniz.

## Bağlantılar
- [GitHub deposu →](https://github.com/gabime/spdlog)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Logging Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/spdlog/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
