# Intermediate CA nedir?

*Geliştirme · Son güncelleme: 21 Ekim 2026*

> Intermediate Certificate Authority

Güvenli web sitelerinin kimliğini doğrulayan kök sertifika ile son kullanıcı arasında yer alan ara yetkili.

## Tanım

Ara sertifika kuruluşu (intermediate CA), internet üzerindeki güvenli HTTPS bağlantılarının temelini oluşturan ve kök sertifika yetkilisi tarafından yetkilendirilmiş ara güven kurumudur. Kök sertifikanın doğrudan internete açık sunucularda kullanılması güvenlik riski yarattığı için bu görev ara sertifikalara devredilir. Böylece ana güven zinciri korunurken web sitelerine dijital güvenlik sertifikaları güvenli bir şekilde dağıtılabilir.

*Devletin doğrudan kendi mhrasından kimlik vermek yerine mahalle muhtarlığına yetki belgesi verip onay işlerini onun üzerinden yürütmesine benzer.*

## Nasıl çalışır?

Tarayıcınız bir web sitesine girdiğinde sunucu size bir sertifika zinciri sunar. Bu zincir son kullanıcı sertifikasından başlar, ara sertifika üzerinden geçerek cihazınızda önceden yüklü olan ana kök sertifikaya kadar ulaşır ve güven bağı kurulur.

## Nerede kullanılır?

SSL/TLS sertifika yönetiminde, web sunucu yapılandırmalarında ve kurumsal güvenlik altyapılarında aktif olarak yer alır.

## Sık karıştırılanlar

Doğrudan ana kök sertifikanın kendisi değildir, kök ile son nokta arasında güveni taşıyan köprü görevindeki ara basamaktır.

## Sıkça sorulanlar

**Ara sertifika neden doğrudan kök sertifika kullanılmaz?**

Kök sertifikanın gizli anahtarı tehlikeye girerse tüm internet güvenliği çökebilir; bu yüzden risk ara sertifikalarla sınırlandırılır.

**Tarayıcılar ara sertifikayı nasıl doğrular?**

Sunucu eksik ara sertifikaları tarayıcıya iletir ve tarayıcı yerleşik güven zincirini kullanarak doğrulamayı tamamlar.

## İlgili terimler

- [End-to-End Encryption](https://trescout.com/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/dictionary/identity-provider/)
- [OIDC](https://trescout.com/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/dictionary/vulnerability-scanning/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/intermediate-ca/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
