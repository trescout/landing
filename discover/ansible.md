# Ajansız IT Otomasyon Platformu

Ansible; sistem yapılandırması, yazılım dağıtımı ve IT otomasyonunu basit YAML dosyaları üzerinden gerçekleştiren ajansız bir araçtır.

- ★ 70.299
- GitHub Trending · 2026-07-04

## Güncelleme
- 11 Ağustos 2026: Yıldız 70.171 → 70.299, son sürüm v2.21.3 (10 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 69.245 → 70.171, son sürüm v2.21.2 (13 Temmuz 2026).

## Bu araç ne yapar?

Ansible; sistem yapılandırması, yazılım dağıtımı ve IT otomasyonunu basit, okunabilir YAML dosyaları üzerinden gerçekleştiren ajansız bir araçtır. Altyapınızı kod olarak yönetmenizi ve karmaşık görevleri standartlaştırmanızı sağlar.

## Kimin için?

Birden fazla sunucuyu aynı anda yapılandırmak ve yönetim süreçlerini güvenilir şekilde otomatize etmek isteyenler.

## Ne beklememeli?

Sadece tek bir yerel makinede basit görevler yürütmek isteyen ve otomasyon altyapısına ihtiyaç duymayanlar.

## Öne çıkanlar
- Hedef sunucularda ajan (agent) kurulumu gerektirmez.
- Yapılandırmaları okunması ve yazılması kolay YAML formatında tutar.
- Binlerce hazır modül ile geniş bir entegrasyon desteği sunar.

## İlk kullanım akışı
- Kontrol düğümünüze Ansible paketini yükleyin.
- Yöneteceğiniz sunucuların IP adreslerini yapılandırma dosyasına (inventory) ekleyin.
- Hedef sunucularla SSH erişimini sağlamak için anahtar tabanlı kimlik doğrulamasını ayarlayın.
- Bağlantıyı doğrulamak için tüm sunuculara ping testi çalıştırın.

## Güvenli başlangıç

Ansible yapılandırma dosyalarında hassas verileri düz metin olarak saklamamalı, bu verileri şifrelemek için yerleşik Vault özelliğini kullanmalısınız.

## İlk görev istemi
İlk adım için hazır istem 
Ansible ile tüm web sunucularına Nginx nasıl kurulur?

## Kurulum

**pip ile (PyPI)**

```
pip install ansible
```

**macOS (Homebrew)**

```
brew install ansible
```

## Çalıştırma

**Ansible playbook betiğini çalıştır**

```
ansible-playbook site.yml
```

Kaynak: PyPI (ansible) · Homebrew (ansible) · resmî Ansible dokümantasyonu (docs.ansible.com)

## Bağlantılar
- [GitHub deposu →](https://github.com/ansible/ansible)
- [Ansible resmî README →](https://github.com/ansible/ansible)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ansible/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
