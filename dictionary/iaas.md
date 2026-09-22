# IaaS nedir, ne demek?

> Infrastructure as a Service

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

IaaS (**Infrastructure as a Service**, hizmet olarak altyapı), donanımın kiralanmasıdır.

## Tanım ve Kelime Kökeni
Güç yetmeyince dev veri merkezinden parça kiralanır. İşletim sistemi ve yazılım sizde, donanım sorumluluğu sağlayıcıdadır. Boş arsa benzetmesi yerindedir: Altyapı hazır, bina sizindir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Site:** Trafiğe göre makine.
- **Yedek:** Uzak disk.
- **Test:** Geçici ortam.

## Teknik Derinlik ve Mimari
Katmanlar:
- **Sanal makine:** İşlemci ve bellek dilimi.
- **Depolama:** Blok ve nesne alanı.
- **Ağ:** Sanal ağ ve adres.

Kodla makine:

```
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}
```

Maliyet kuralı: Açık unutulan makine yazar. Etiket ve alarm disiplini şarttır.

## Sık Karıştırılanlar
PaaS sanılır. IaaS donanım verir, PaaS hazır ortam sunar. Biri arsa, diğeri mobilyalı dairedir.

## Farklı Disiplinlerde Kullanımı
- **Arsa:** Altyapılı boş arazi.
- **Depo:** Rafı hazır ambar.
- **Tarla:** Sürülü toprak kiralama.

## Bir benzetmeyle
Boş arsa kiralamaya benzer; altyapı hazırdır, bina size aittir.

## Sıkça sorulanlar

**IaaS güvenli mi?**  
Altyapı güvenlidir, iç güvenlik sizdedir. Yama ve erişim disiplini şarttır.

**PaaS farkı nedir?**  
IaaS donanım verir, PaaS ortam sunar. Kontrol sizdeyse ilki, hız istenirse ikincisi seçilir.

**Maliyet nasıl tutulur?**  
Kullanılmayan kapatılır, doğru boyut seçilir, alarm kurulur.

**Ne zaman seçilir?**  
Tam kontrol ve özel kurulum gerektiğinde. Standart işte PaaS yeterlidir.

## İlgili terimler
- [SaaS](/dictionary/saas/)
- [PaaS](/dictionary/paas/)
- [Virtual Machines](/dictionary/virtual-machines/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/iaas/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
