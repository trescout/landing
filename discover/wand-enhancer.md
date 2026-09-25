# Wand uygulaması için gelişmiş arayüz özelleştirme

> Wand-enhancer · C# · ★ 27.333

Wand-Enhancer, WeMod oyun yöneticisi için kullanıcı deneyimini optimize eden ve birlikte çalışabilirliği artıran C# tabanlı açık kaynaklı bir eklentidir. Arayüz düzenini esnetir, kısayol tuşlarını merkezileştirir ve yerel oyun içi paneller üzerinde tam kontrol sağlar.

## Ne kazandırır?
- Gelişmiş Arayüz Esnekliği: Varsayılan masaüstü istemcisinin katı arayüz sınırlarını aşarak panelleri ve kısayolları dilediğiniz gibi yapılandırın.
- Hızlı Tuş Atamaları ve Makrolar: Oyun esnasında dikkatinizi dağıtmadan araçları etkinleştiren özelleştirilebilir kısayol mimarisi.
- Düşük Sistem Yükü: C# .NET üzerinde yerel derlenen hafif yapısıyla oyun kare hızına (FPS) etki etmeyen bellek dostu mimari.
- Açık Kaynak Şeffaflığı: Kapalı kutu üçüncü taraf yazılımlara kıyasla kod tabanı topluluk tarafından denetlenebilir ve genişletilebilir.

## Teknik mimari ve çalışma prensibi
Wand-Enhancer, istemci çalışma zamanına (runtime) kanca (hook) atarak kullanıcı arayüzü olaylarını yönetir:1. Çalışma Zamanı Enjeksiyonu ve Kancalar: İstemci penceresinin WPF / WinForms olay döngüsüne bağlanarak tuş vuruşlarını ve pencere durumlarını yakalar.2. Yapılandırma ve Durum Yönetimi: Kullanıcı tercihlerini yerel JSON dosyalarında saklar; bellek üzerinde anlık okuma yaparak gecikmesiz tepki verir.3. Modül Ayrımı: Çekirdek mantık ile görsel temalandırma katmanlarını bağımsız kütüphaneler halinde tutar, böylece istemci güncellemelerinde çökme riskini en aza indirir.

## Kurulum ve eklenti entegrasyonu
Wand-Enhancer'ı yerel ortamınızda kaynak koddan derleyip istemciye dahil etmek için aşağıdaki adımları izleyin:

### Depoyu klonlama ve bağımlılıkları hazırlama
```bash
git clone https://github.com/the1andonlych33s3/wand-enhancer.git
cd wand-enhancer
dotnet restore
```

### Projeyi derleme ve eklentiyi yerleştirme
```bash
dotnet build -c Release
# Oluşan derleme çıktısını eklenti dizinine kopyalayın
```

## Kod bilmeyenler için yapay zekâ istemi
Wand-Enhancer eklentisinin C# mimarisini analiz et. İstemci penceresine bağlanan kanca mekanizmasını, olay dinleyicilerini ve yapılandırma dosya yapısını özetle. Yeni bir klavye kısayolu eklemek için gereken sınıf ve metot yapısını gösteren örnek bir kod şablonu hazırla.

## Kritik uyarılar ve sınırlar
- İstemci Sürüm Uyumluluğu: Ana WeMod istemcisine gelen büyük güncellemeler API kancalarını geçici olarak kırabilir. Eklentinin sürüm notlarını takip edin.
- Güvenlik Yazılımları Bildirimleri: Bellek enjeksiyonu ve kanca teknikleri kullanan tüm açık kaynak araçlar gibi yerel antivirüs yazılımlarınca yanlış pozitif (false positive) olarak işaretlenebilir.
- Yalnızca Masaüstü: Araç yalnızca yerel Windows masaüstü istemcisi üzerinde çalışır; mobil veya web arayüzleri kapsanmaz.

## Sıkça sorulan sorular

### Wand-Enhancer resmi bir WeMod ürünü müdür?
Hayır, topluluk tarafından geliştirilmiş bağımsız ve açık kaynaklı bir eklentidir.

### Kullanırken sistem performansım düşer mi?
Hayır, .NET Core üzerinde optimize edildiği için arka planda minimum CPU ve bellek tüketir.

### Eklenti ayarlarımı nasıl sıfırlarım?
Kullanıcı dizinindeki <code>config.json</code> dosyasını silerek varsayılan ayarlara anında dönebilirsiniz.

### Kendi özel temalarımı geliştirebilir miyim?
Evet, arayüz stilleri XAML/CSS tabanlı şablonlarla yapılandırılabilir.

## Bağlantılar
- [GitHub deposu (the1andonlych33s3/wand-enhancer) →](https://github.com/the1andonlych33s3/wand-enhancer)

## İlgili sözlük terimleri
- [Runtime](/dictionary/runtime/)
- [Customization](/dictionary/customization/)
- [Assets](/dictionary/assets/)

---
Source: TreScout Discovery · https://trescout.com/discover/wand-enhancer/
