# Yazılım tersine mühendislik ve analiz çerçevesi

Ghidra, Ulusal Güvenlik Ajansı (NSA) tarafından geliştirilen ve açık kaynak olarak paylaşılan kapsamlı bir yazılım tersine mühendislik (SRE) çerçevesidir. Java ve C++ çekirdeğiyle geliştirilen platform; derlenmiş ikili (binary) dosyaları kaynak koda dönüştürür, güvenlik araştırmacılarına gelişmiş dekompiler, simbolik analiz ve çoklu mimari desteği sunar.

- ★ 78.142
- Java
- GitHub Trending · 2026-08-28

## Güncelleme
- 17 Eylül 2026: Yıldız 78.142, son kararlı sürüm Ghidra_12.1.3_build (Java 21 desteği, RISC-V ve ARM64 dekompiler optimizasyonları).

## Ne kazandırır?
- Yerleşik güçlü C dekompileri: Makine kodlarını ve assembly yönergelerini okunabilir, yüksek seviyeli C benzeri sözdizimine dönüştürme.
- Geniş işlemci ve mimari yelpazesi: x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC ve yüzlerce gömülü mikrodenetleyici mimarisi desteği.
- İşbirlikçi çok kullanıcılı analiz: Ghidra Server altyapısıyla aynı ikili dosya üzerinde eşzamanlı açıklama ekleme, fonksiyon isimlendirme ve sürüm kontrolü.
- Otomasyon ve Headless analiz: Grafik arayüze girmeden sunucu üzerinde binlerce zararlı yazılımı komut satırından otomatik tarama.
- Java ve Python ile genişletilebilirlik: Özel scriptler, eklentiler ve veri tipi kütüphaneleriyle analizi kişiselleştirme.

## Kurulum ve sistem gereksinimleri

**JDK 21 ve Ghidra kurulumu**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Çalıştırma ve headless komut satırı analizi

**Grafik arayüzü başlatma**

```
./ghidraRun
```

**Headless otomatik analiz çalıştırma**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```

## Teknik mimari: Sleigh ve dekompiler motoru

Ghidra'nın endüstri standardı haline gelmesini sağlayan çekirdek mimari şu bileşenlerden oluşur:
- Sleigh işlemci modelleme dili: Yeni bir işlemci veya komut seti mimarisini (ISA) Ghidra'ya tanıtmak için kullanılan deklaratif tanımlama dili.
- P-Code ara temsil katmanı (IR): Tüm işlemci yönergelerini ortak bir ara dile (P-Code) çevirerek mimariden bağımsız veri akışı ve kontrol akışı analizi yapma.
- C++ tabanlı dekompiler motoru: Kontrol akış grafiklerini basitleştiren, değişken tiplerini çıkaran ve karmaşık döngüleri C koduna indirgeyen yüksek performanslı yerel motor.

## Tersine mühendislik ve zafiyet analizi iş akışları

Ghidra, karmaşık siber güvenlik ve yazılım denetim süreçlerinde temel araç olarak konumlanır:
- Zararlı yazılım analizi (Malware Triage): Şüpheli yürütülebilir dosyaları izole ortamda açıp gizli API çağrılarını, C2 alan adlarını ve şifreleme anahtarlarını ortaya çıkarma.
- İkili dosya karşılaştırma (Program Diff): Güvenlik yaması öncesi ve sonrasındaki iki dosya arasındaki farkları görselleştirerek kapatılan zafiyeti tespit etme.
- Gömülü yazılım (Firmware) analizi: IoT cihazlarından alınan ham flash bellek dökümlerini bellek haritasına oturtup bootloader ve çekirdek fonksiyonlarını çözümleme.

## Kod bilmiyorsanız
🤖 Kod bilmiyorsanız
Şüpheli bir ikili (binary) dosyayı Ghidra kullanarak incelemek istiyorum. Ghidra'da yeni bir proje açma, dosyayı içe aktarma, otomatik analizi (Auto Analysis) çalıştırma, Decompiler penceresinde fonksiyonları inceleme ve dışarıya çağrılan şüpheli API fonksiyonlarını tespit etme adımlarını adım adım açıklar mısın?

- **Kimin için:** Zararlı yazılım araştırmacıları, zafiyet avcıları, tersine mühendislik uzmanları ve gömülü sistem geliştiricileri.
- **Lisans:** Apache-2.0 (Açık kaynak lisansı)
- **Geliştirici:** National Security Agency (NSA) ve Açık Kaynak Topluluğu
- **Gereksinim:** Java Development Kit (JDK) 21 64-bit

## Sıkça sorulan sorular
- Ghidra ile IDA Pro arasındaki temel farklar nelerdir? IDA Pro ticari ve yüksek lisans bedellerine sahipken, Ghidra tamamen ücretsiz ve açık kaynaklıdır. Ghidra, tüm mimariler için yerleşik dekompiler sunar ve çok kullanıcılı işbirliği sunucusu içerir.
- Zararlı yazılım analizi yaparken Ghidra güvenli midir? Evet, statik analiz sırasında dosya çalıştırılmaz, yalnızca kodları çözümlenir. Ancak analizin izole bir sanal makinede (VM) yapılması güvenlik açısından esastır.
- Ghidra Server nasıl kurulur? Ghidra paketinde yer alan server dizinindeki svrAdmin betiğiyle yerel ağda birkaç dakika içinde bir takım sunucusu açılabilir ve kullanıcı yetkileri atanabilir.
- Python 3 betikleri Ghidra içinde çalıştırılabilir mi? Ghidra varsayılan olarak Jython (Python 2.7) ile gelse de, PyGhidra eklentisi sayesinde modern Python 3 ortamları ve harici kütüphaneler (NumPy, Capstone) doğrudan kullanılabilir.

## Bağlantılar
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## İlgili sözlük terimleri
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/discover/ghidra/
