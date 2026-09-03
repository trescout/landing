# Yazılım süreçlerini otomatize eden sunucu

Jenkins, yazılım geliştirme süreçlerini otomatize eden açık kaynaklı bir sürekli entegrasyon (continuous integration) ve sürekli dağıtım (continuous delivery) sunucusudur. Java tabanlı bu platform, yazılım projelerinin derleme, test ve dağıtım aşamalarını yönetmek için geniş bir eklenti ekosistemi sunar.

- ★ 26.526
- Java
- GitHub Trending · 2026-07-27

## Güncelleme
- 3 Eylül 2026: Yıldız 26.504 → 26.526, son sürüm jenkins-2.568.3 (2 Eylül 2026).
- 27 Ağustos 2026: Yıldız 26.467 → 26.504, son sürüm jenkins-2.579 (25 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 26.444 → 26.467, son sürüm jenkins-2.578 (18 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 26.422 → 26.444, son sürüm jenkins-2.577 (11 Ağustos 2026).

## Ne kazandırır?
- Yazılım projelerinin derleme ve test süreçlerini otomatikleştirir
- Geniş eklenti desteğiyle süreçleri özelleştirme imkânı sunar
- Hata tespiti ve dağıtım aşamalarını hızlandırır

## Kurulum

**macOS (Homebrew)**

```
brew install jenkins
```

**Docker imajı**

```
docker pull jenkins/jenkins:lts
```

## Çalıştırma

**Docker ile başlat (http://localhost:8080)**

```
docker run -p 8080:8080 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

Kaynak: Homebrew formülü · Docker Hub jenkins/jenkins

## Nasıl başlanır?

Resmî web sitesi olan jenkins.io adresindeki indirme sayfasına giderek platformunuza uygun WAR dosyası, Docker imajı veya yerel paketlerden birini seçip kurulum adımlarını takip edebilirsiniz.
- [Resmî kaynak →](https://www.jenkins.io)

- **Kimin için:** Yazılım geliştirme süreçlerini otomatize etmek isteyen geliştiriciler ve teknik ekipler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/jenkinsci/jenkins)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-27 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Continuous Integration

---
Kaynak: TreScout Keşif · https://trescout.com/discover/jenkins/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
