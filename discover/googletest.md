# C++ projelerinde endüstri standardı birim testleri

GoogleTest ve GoogleMock, modern C++ projelerinde birim testleri, sahte nesneler (mock) ve parametrik testler çalıştırmanızı sağlayan endüstri standardı açık kaynak test çatısıdır.

- ★ 38.987
- C++
- GitHub Trending · 2026-08-27

## Güncelleme
- 27 Ağustos 2026: Yıldız 38.987, v1.15.2 sürümü ile C++20 konseptleri ve gelişmiş mock doğrulama desteği.

## Ne kazandırır?
- Zengin doğrulama makroları: ASSERT_* (kritik hata, testi sonlandırır) ve EXPECT_* (hatayı kaydeder, test akışını devam ettirir) makroları ile net hata teşhisi.
- Gelişmiş Mock altyapısı (GoogleMock): Bağımlılıkları izole etmek için MOCK_METHOD ile arayüzleri kolayca taklit edebilme ve çağrı beklentilerini tanımlama.
- Parametrik test yeteneği: Aynı test mantığını onlarca farklı girdi ve veri kümesi üzerinde tek bir şablonla otomatik olarak tekrarlayabilme.
- Çoklu platform ve thread güvenliği: Linux, macOS ve Windows ortamlarında thread-safe mimari ve ölüm testleri (death tests) ile çökme senaryolarını doğrulama.
- CI/CD ve raporlama entegrasyonu: JUnit uyumlu XML ve JSON çıktı formatları ile GitHub Actions, Jenkins ve GitLab CI boru hatlarıyla kusursuz entegrasyon.

## Kurulum

**CMake FetchContent ile projeye ekleme**

```
include(FetchContent)
FetchContent_Declare(
googletest
URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```

## Çalıştırma

**Testi derleme ve CTest ile yürütme**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```

## Teknik mimari ve çalışma prensibi

GoogleTest, modüler bir C++ mimarisi üzerine inşa edilmiştir ve modern derleyicilerle doğrudan optimize edilir:
- Test Fixture ve Yaşam Döngüsü Yönetimi: SetUp ve TearDown yordamları ile her test öncesinde ve sonrasında bellek kaynakları güvenle yönetilir.
- Ölüm Testleri (Death Tests) için Süreç İzolasyonu: Programın beklenmedik şekilde çökmesini veya assert üretmesini fork mekanizmasıyla izole çocuk süreçlerde yakalar.
- Tip Parametreli Test Şablonları: Şablonlu sınıfları (C++ templates) farklı veri tipleriyle tek seferde test etmek için Type-Parameterized test altyapısı sunar.

## Test senaryoları ve GoogleMock entegrasyonu

Modern C++ projelerinde sahte nesnelerle bağımlılıkları yalıtarak test yazımı pratik avantajlar sağlar:
- Veritabanı ve Ağ Çağrılarını Soyutlama: MOCK_METHOD kullanarak gerçek ağ bağlantısı kurmadan beklenen API yanıtlarını ve gecikmeleri simüle edin.
- Çağrı Sayısı ve Parametre Doğrulama: EXPECT_CALL makrosu ile bir fonksiyonun kaç kez, hangi argümanlarla ve hangi sırayla çağrıldığını denetleyin.
- Hata Fırlatma Senaryolarını İnceleme: İstisna fırlatan (throw) kod bloklarını EXPECT_THROW makrolarıyla test ederek dayanıklılığı garanti altına alın.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Modern bir C++ projesinde GoogleTest ve GoogleMock kullanarak bir veri ayrıştırıcı (parser) sınıfı için birim testleri yazmak istiyorum. CMakeLists.txt dosyamı nasıl yapılandıracağımı, örnek bir TEST_F test fikstürünü ve MOCK_METHOD ile sahte nesne oluşturup çağrı beklentilerini nasıl doğrulayacağımı kod örnekleriyle açıklar mısın?

- **Kimin için:** C++ yazılım mühendisleri, gömülü sistem geliştiricileri ve sistem mimarları. 
- **Lisans:** BSD 3-Clause (Esnek açık kaynak lisansı) 
- **Çatı:** C++ Test ve Mock Kütüphanesi 
- **Platformlar:** Linux, macOS, Windows, Android, iOS 

## Sıkça sorulan sorular
- GoogleTest'i projeye dahil etmenin en modern yolu nedir? Modern CMake projelerinde FetchContent mekanizması en çok önerilen yaklaşımdır. Harici bir paket yöneticisine ihtiyaç duymadan kaynak kodu indirir ve hedef derleme sürecine bağlar.
- EXPECT_* ile ASSERT_* arasındaki temel fark nedir? EXPECT_* makroları başarısız olduğunda hatayı günlüğe kaydeder ancak fonksiyonun geri kalanının çalışmasına izin verir. ASSERT_* ise hatada derhal mevcut test fonksiyonundan çıkar.
- GoogleMock ayrı bir kütüphane midir? GoogleMock başlangıçta ayrı bir projeydi ancak uzun süredir GoogleTest deposuyla tek bir çatı altında birleştirilmiştir; ikisi birlikte kurulur ve kullanılır.
- Thread güvenliği sunuyor mu? Evet. GoogleTest, pthreads destekleyen sistemlerde ve Windows üzerinde thread-safe olarak çalışır; birden fazla thread üzerinden gelen eşzamanlı bildirimleri doğru şekilde senkronize eder.

## Bağlantılar
- [GitHub deposu →](https://github.com/google/googletest)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-27 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CI/CD Açık Kaynak CLI API Framework

---
Kaynak: TreScout Keşif · https://trescout.com/discover/googletest/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
