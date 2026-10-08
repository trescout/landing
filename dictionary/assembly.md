# Assembly nedir, ne demek ve nasıl çalışır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

Assembly, bilgisayar bilimlerinde iki temel kavrama karşılık gelir: Birincisi donanım işlemcisine (CPU) doğrudan hükmeden en düşük seviyeli sembolik programlama dili (Assembly Language); ikincisi ise derlenmiş yazılım modüllerinin (.NET assembly) dağıtılabilir tek bir paket haline getirilmesidir.

## 1. Düşük seviyeli programlama dili (Assembly Language)

Bilgisayar işlemcisi yalnızca 0 ve 1 ikili sinyallerinden (makine kodu / opcodes) anlar. Assembly dili, bu ham makine kodlarına karşılık gelen insan tarafından okunabilir sembolik kısaltmalardan (**mnemonics**) oluşur:

- `MOV`: Veriyi bir kayıtçıdan (register) diğerine veya bellek adresine kopyalar.
- `ADD` / `SUB`: Matematiksel toplama ve çıkarma işlemlerini yürütür.
- `PUSH` / `POP`: Veriyi çağrı yığınına (call stack) ekler veya çeker.
- `JMP` / `JE` / `JNE`: Karşılaştırma sonucuna göre program akışını başka bir bellek adresine dallandırır.

Yazılan assembly kodları, **Assembler** (nasm, gas) adı verilen dönüştürücüler aracılığıyla doğrudan makine koduna çevrilir; arada sanal makine katmanı yoktur.

## 2. İşlemci kayıtçıları (Registers) ve x86-64 mimarisi

Modern bir 64-bit x86-64 işlemcide en kritik kayıtçılar şunlardır:

- **Genel Amaçlı Kayıtçılar:** `RAX` (akümülatör ve fonksiyon dönüşü), `RBX` (temel veri işaretçisi), `RCX` (döngü sayacı), `RDX` (giriş/çıkış verisi), `RDI` ve `RSI` (hedef ve kaynak göstericileri).
- **Özel Amaçlı Kayıtçılar:** `RSP` (Stack Pointer - yığının en üst noktası), `RBP` (Base Pointer - fonksiyon çerçevesi tabanı), `RIP` (Instruction Pointer - bir sonraki çalıştırılacak komutun adresi) ve `RFLAGS` (Zero, Carry bayrakları).

## 3. CISC vs RISC: x86-64 ve ARM64 farkı

x86-64 mimarisi **CISC** (Karmaşık Komut Kümeli) felsefesiyle çalışır; değişken komut boyutlarına ve doğrudan bellek üzerinde işlem yapabilen zengin komutlara sahiptir. ARM64 (Apple Silicon, Mobil) ise **RISC** (İndirgenmiş Komut Kümeli) tabanlıdır; sabit 32-bit komut uzunluğu ve Load-Store mimarisi ile enerji verimliliğinde büyük üstünlük sağlar.

## 4. Sistem çağrıları (Syscall) ve Linux x86-64 örneği

```
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; metnin bellek adresi
    mov rdx, 8          ; metin uzunluğu
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. .NET Assembly ve WebAssembly (WASM)

- **.NET Assembly:** C# kodu derlendiğinde CIL/MSIL bayt kodlarını ve meta verileri içeren `.dll` veya `.exe` biçiminde mantıksal bir montaj paketi (Assembly) oluşturulur.
- **WebAssembly (WASM):** C, C++ ve Rust kodlarının tarayıcı içinde yerel hıza yakın performansla çalışmasını sağlayan taşınabilir bir yığın sanal makinesi bayt kodudur.

*Assembly dili, bir saatin içindeki çarkları, yayları ve milleri mikroskop altında cımbızla tek tek yerleştirmeye benzer; en yüksek hassasiyet ve performansı sağlar ama büyük dikkat ister. Yazılım montajı ise üretilen bu hassas mekanizmayı kasanın içine oturtup çalışır bir kol saati olarak kutulamaktır.*

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

- [Memory Management](https://trescout.com/dictionary/memory-management/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Compilation](https://trescout.com/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/dictionary/emulator/)

## İlgili araçlar

- [Ghidra](https://trescout.com/discover/ghidra/)
- [Apollo-11](https://trescout.com/discover/apollo-11/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/assembly/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
