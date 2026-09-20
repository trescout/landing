# Assembly nedir, ne demek ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Assembly, bilgisayar bilimlerinde iki temel kavrama karşılık gelir: Birincisi donanım işlemcisine (CPU) doğrudan hükmeden en düşük seviyeli sembolik programlama dili (Assembly Language); ikincisi ise derlenmiş yazılım modüllerinin (.NET assembly, CLI) dağıtılabilir tek bir paket haline getirilmesidir.

## 1. Düşük seviyeli programlama dili (Assembly Language)

Bilgisayar işlemcisi yalnızca `0` ve `1` ikili sinyallerinden (makine kodu / opcodes) anlar. Ancak insanların `01001000 10001001 11000011` gibi dizileri ezberlemesi imkânsızdır.

Assembly dili, bu ham makine kodlarına karşılık gelen insan tarafından okunabilir sembolik kısaltmalardan (**mnemonics**) oluşur:

- `MOV`: Veriyi bir kayıtçıdan (register) diğerine veya bellek adresine kopyalar.
- `ADD` / `SUB`: Matematiksel toplama ve çıkarma işlemlerini yürütür.
- `PUSH` / `POP`: Veriyi çağrı yığınına (call stack) ekler veya çeker.
- `JMP` / `JE` / `JNE`: Karşılaştırma sonucuna göre program akışını başka bir bellek adresine dallandırır (if-else / döngü mantığı).

Yazılan assembly kodları, **Assembler** (nasm, gas, masm) adı verilen hafif dönüştürücüler aracılığıyla 1'e 1 oranında doğrudan makine koduna çevrilir. Üst seviye dillerin aksine arada hiçbir yorumlayıcı veya sanal makine katmanı yoktur.

## 2. İşlemci kayıtçıları (Registers) ve x86-64 mimarisi

İşlemciler RAM'deki verilere doğrudan işlem yapamaz; verinin önce CPU içindeki ışık hızında çalışan ultra küçük bellek hücrelerine, yani **Kayıtçılara (Registers)** taşınması gerekir.

Modern bir 64-bit x86-64 işlemcide en kritik kayıtçılar şunlardır:

- **Genel Amaçlı Kayıtçılar:**
  - `RAX` (Accumulator): Aritmetik işlemlerin sonucu ve fonksiyon dönüş değerleri burada tutulur.
  - `RBX` (Base): Temel veri işaretçisi.
  - `RCX` (Counter): Döngü sayaçları için optimize edilmiştir.
  - `RDX` (Data): Giriş/çıkış ve çarpma/bölme işlemlerinde kullanılır.
  - `RDI` & `RSI`: Bellek bloklarını kopyalarken hedef (Destination) ve kaynak (Source) adreslerini gösterir.
- **Özel Amaçlı ve Durum Kayıtçıları:**
  - `RSP` (Stack Pointer): Çağrı yığınının (Call Stack) en üst noktasını işaret eder.
  - `RBP` (Base Pointer): Mevcut fonksiyon çerçevesinin (stack frame) taban adresini sabitler.
  - `RIP` (Instruction Pointer / Program Counter): İşlemcinin bir sonraki saat çevriminde çalıştıracağı makine komutunun bellek adresini tutar.
  - `RFLAGS`: İşlemlerin sonucunu kaydeden bayraklardır (Zero Flag `ZF`, Carry Flag `CF`, Overflow Flag `OF`).

## 3. CISC vs RISC: x86-64 ve ARM64 farkı

Günümüz bilişim dünyası iki baskın mimariye bölünmüştür:

| Kriter | x86-64 (Intel / AMD) | ARM64 / AArch64 (Apple Silicon, Mobil) |
| :--- | :--- | :--- |
| **Felsefe** | **CISC** (Karmaşık Komut Kümeli Bilgisayar) | **RISC** (İndirgenmiş Komut Kümeli Bilgisayar) |
| **Komut Boyutu** | Değişken uzunluklu (1 bayt ile 15 bayt arası). | Sabit 32-bit (4 bayt) komut uzunluğu. |
| **Bellek Erişimi** | Aritmetik komutlar doğrudan RAM adresleriyle çalışabilir. | **Load-Store mimarisi:** Yalnızca `LDR` ve `STR` belleğe erişir; hesaplamalar sadece register'larda yapılır. |
| **Güç Tüketimi** | Yüksek performans, yüksek enerji tüketimi. | Yüksek enerji verimliliği ve watt başına üstün performans. |

## 4. Sistem çağrıları (Syscall) ve Linux x86-64 örneği

Bir program ekrana yazı yazdırmak veya işletim sisteminden çıkmak istediğinde doğrudan donanıma erişemez; işletim sistemi çekirdeğinden (Kernel) bir **Sistem Çağrısı (Syscall)** talep eder:

```assembly
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; yazdırılacak metnin bellek adresi
    mov rdx, 8          ; metnin uzunluğu (bayt)
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0 (rdi = 0)
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. Yazılım mühendisliğinde .NET Assembly ve WebAssembly

Assembly terimi donanım dışında iki popüler modern yazılım bağlamında da kullanılır:

- **.NET Assembly:** C# veya F# ile yazılan kod derlendiğinde doğrudan makine koduna dönüşmez; Ortak Ara Dil (CIL/MSIL) bayt kodlarını, meta verileri ve kaynakları içeren `.dll` veya `.exe` formatında bir mantıksal birim (Assembly) oluşturulur.
- **WebAssembly (WASM):** C, C++ ve Rust kodlarının web tarayıcılarında JavaScript'in yanında yerel hıza yakın hızda çalışmasını sağlayan taşınabilir, yığın tabanlı bir sanal makine ikili kod formatıdır.

## Sıkça sorulanlar

**Assembly ne demek, ne işe yarar?**  
Assembly, bilgisayar işlemcisinin donanımsal komut kümesine (instruction set) 1'e 1 karşılık gelen en alt seviyeli sembolik programlama dilidir. Doğrudan CPU kayıtçılarını ve belleği kontrol etmek için kullanılır.

**Assembler ile Compiler (Derleyici) arasındaki fark nedir?**  
Derleyici (C, C++, Rust), karmaşık insan mantığını ve döngülerini analiz edip makine koduna optimize ederek çevirir. Assembler ise zaten makine kodunun sembolik hali olan assembly komutlarını doğrudan ikili bayt koduna dönüştürür.

**Assembly dili günümüzde hâlâ nerede kullanılır?**  
İşletim sistemi çekirdekleri (bootloader), donanım aygıt sürücüleri, tersine mühendislik (reverse engineering), kötü amaçlı yazılım analizi, siber güvenlik açığı tespiti ve gömülü sistemlerde (IoT/mikrodenetleyici) aktif olarak kullanılır.

**CISC ile RISC arasındaki fark nedir?**  
CISC (x86-64), tek bir komutta birden çok alt işlemi ve bellek erişimini yapabilen zengin komut kümesine sahiptir; RISC (ARM) ise her komutu tek bir saat çevriminde çalışacak şekilde basitleştirilmiş ve enerji verimliliği yüksek bir mimaridir.

## İlgili terimler

- [Memory Management](/dictionary/memory-management/)
- [Runtime](/dictionary/runtime/)
- [Compilation](/dictionary/compilation/)
- [Apple Silicon](/dictionary/apple-silicon/)
- [Emulator](/dictionary/emulator/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/assembly/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
