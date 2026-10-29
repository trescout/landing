# Yazılım süreçlerini otomatize eden sunucu

Jenkins, yazılım geliştirme süreçlerini otomatize eden açık kaynaklı bir sürekli entegrasyon (continuous integration) ve sürekli dağıtım (continuous delivery) sunucusudur. Java tabanlı bu platform, yazılım projelerinin derleme, test ve dağıtım aşamalarını yönetmek için geniş bir eklenti ekosistemi sunar.

- ★ 26.703
- Java
- GitHub Trending · 2026-07-27

## Güncelleme

- **29 Ekim 2026:** Yıldız 26.682 → 26.703, son sürüm jenkins-2.580.2 (28 Ekim 2026).
- **20 Ekim 2026:** Yıldız 26.648 → 26.682, son sürüm jenkins-2.587 (20 Ekim 2026).
- **13 Ekim 2026:** Yıldız 26.620 → 26.648, son sürüm jenkins-2.586 (13 Ekim 2026).
- **6 Ekim 2026:** Yıldız 26.603 → 26.620, son sürüm jenkins-2.585 (6 Ekim 2026).

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

**Kaynak:** Homebrew formülü · Docker Hub jenkins/jenkins

## Nasıl başlanır?

Resmî web sitesi olan jenkins.io adresindeki indirme sayfasına giderek platformunuza uygun WAR dosyası, Docker imajı veya yerel paketlerden birini seçip kurulum adımlarını takip edebilirsiniz.

- [Resmî kaynak →](https://www.jenkins.io)

- **Kimin için:** Yazılım geliştirme süreçlerini otomatize etmek isteyen geliştiriciler ve teknik ekipler için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/jenkinsci/jenkins)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-27 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Continuous Integration](https://trescout.com/dictionary/continuous-integration/)
- [Localhost](https://trescout.com/dictionary/localhost/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/jenkins/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
