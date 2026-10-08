# Sandboxing nedir?

*Sözlük · Geliştirme · Son güncelleme: 3 Ekim 2026*

Yazılımların veya şüpheli kodların ana sisteme ve çevreye zarar vermesini önlemek amacıyla izole bir ortamda çalıştırılması tekniği.

## Tanım

Sandboxing, güvenilmeyen ya da test aşamasındaki kod parçacıklarını sistem kaynaklarından tecrit ederek kontrollü bir alanda çalıştırma pratiğidir. Bu mekanizma, uygulamanın dosya sistemine, yerel ağa veya işletim sistemi çekirdeğine doğrudan erişmesini sınırlar. Güvenlik açıklarının sisteme yayılmasını engellemek ve zararlı yazılımların etkisini sıfıra indirmek için vazgeçilmez bir güvenlik katmanıdır.

*Tehlikeli olabilecek kimyasal bir deneyi odanın ortasında değil, patlamaya dayanıklı cam bir fanusun içinde yapmaya benzer.*

## Nasıl çalışır?

İşletim sistemi seviyesindeki kısıtlamalar veya sanallaştırma araçları kullanılarak korumalı bir bariyer kurulur. Kod çalıştırıldığında sadece kendisine izin verilen kısıtlı bellek ve disk alanını kullanabilir. Sistem çağrıları sürekli izlenir; izin verilmeyen bir işlem girişimi tespit edildiğinde yazılım anında durdurulur.

## Nerede kullanılır?

Web tarayıcılarında üçüncü taraf betikleri çalıştırmada, e-posta eklerindeki şüpheli dosyaları inceleyen güvenlik yazılımlarında ve yapay zekâ ajanlarının kod koşturduğu geliştirme ortamlarında kullanılır.

## Sık karıştırılanlar

Sandbox terimi tecrit edilmiş alanın kendisini tanımlarken; sandboxing bu güvenli ortamı oluşturma, yönetme ve sınırlandırma sürecini ifade eder.

## Sıkça sorulanlar

**Sandboxing sistem performansını belirgin şekilde düşürür mü?**

Sistem çağrılarının denetlenmesi küçük bir işlem yükü getirse de modern işletim sistemlerinde bu kayıp genellikle fark edilmeyecek kadar azdır.

**Yapay zekâ araçlarında sandboxing neden gereklidir?**

Yapay zekâ modellerinin ürettiği ve çalıştırdığı kodlar işletim sisteminde kritik dosyaları silme riski taşıyabileceğinden, bu işlemler güvenli bir izolasyon katmanında yürütülür.

## İlgili terimler

- [Sandbox](https://trescout.com/dictionary/sandbox/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Virtual Machines](https://trescout.com/dictionary/virtual-machines/)
- [Security Scanner](https://trescout.com/dictionary/security-scanner/)

## İlgili araçlar

- [Agent Governance Toolkit](https://trescout.com/discover/agent-governance-toolkit/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/sandboxing/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
