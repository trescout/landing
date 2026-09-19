# Konteyner ve bulut güvenlik tarayıcısı

Trivy, konteynerler, Kubernetes kümeleri, kod depoları ve bulut altyapılarındaki güvenlik açıklarını, hatalı yapılandırmaları ve gizli anahtarları (secrets) saniyeler içinde tespit eden kapsamlı bir güvenlik tarama aracıdır. Yazılım malzeme listesi (SBOM) desteğiyle DevSecOps süreçlerini uçtan uca otomatize eder.

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Ne kazandırır?
- Çok katmanlı hedef taraması: Konteyner imajları (Docker, OCI), yerel dosya sistemleri, uzak Git depoları, sanal makine diskleri ve canlı Kubernetes kümelerini tek bir araçla denetler.
- Sıfır ek altyapı yükü: Harici bir veritabanı sunucusuna veya sürekli çalışan ağır ajanlara ihtiyaç duymaz; tek bir çalıştırılabilir ikili (binary) olarak saniyeler içinde analiz sunar.
- Hassas veri ve gizli anahtar (secrets) yakalama: Kaynak koda veya imaj katmanlarına yanlışlıkla gömülen API anahtarlarını, şifreleri ve özel sertifikaları sezgisel motoruyla tespit eder.
- Kod olarak altyapı (IaC) denetimi: Terraform, Dockerfile, Kubernetes YAML ve CloudFormation dosyalarındaki hatalı güvenlik yapılandırmalarını üretime geçmeden önce yakalar.
- SBOM ve açık kaynak lisans uyumluluğu: CycloneDX ve SPDX standartlarında yazılım malzeme listesi üreterek yazılım tedarik zinciri güvenliğini yasal düzenlemelerle uyumlu hale getirir.

## Kurulum

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Çalıştırma

**Konteyner imajını tara**

```
trivy image imaj-adi:etiket
```

**Yerel kaynak kodu ve sırları tara**

```
trivy fs --scanners vuln,secret,misconfig .
```

**CycloneDX formatında SBOM oluştur**

```
trivy image --format cyclonedx --output sbom.json imaj-adi:etiket
```

Kaynak: Resmî kaynak: https://github.com/aquasecurity/trivy

## Teknik mimari ve çalışma prensibi

Trivy, Aqua Security ve açık kaynak topluluğu tarafından geliştirilen, modern DevSecOps standartlarını karşılamak üzere tasarlanmış yüksek performanslı bir güvenlik motoruna sahiptir:
- Trivy DB ve yerel önbellek: NVD, GitHub Advisory Database, Red Hat, Debian, Ubuntu ve Alpine güvenlik bültenlerini içeren hafif bir veritabanı önbelleğini otomatik indirir. Taramalar bu yerel önbellek üzerinden yapıldığı için ağ kısıtlaması olan ortamlarda dahi ışık hızında çalışır.
- Statik katman analizi: Konteyner imajlarını çalıştırmadan veya Docker daemon'a ihtiyaç duymadan doğrudan OCI katmanlarını ayrıştırır. Bu yaklaşım tarama sürecinde sistem güvenliğini riske atmaz.
- IaC motoru ve Rego politikaları: Altyapı şablonlarını Open Policy Agent (OPA) uyumlu kurallarla denetler. Güvenli olmayan açık portlar veya root yetkisiyle çalışan servisler anında raporlanır.
- SBOM standartlaşması: Paket yöneticisi kilit dosyalarını (package-lock.json, poetry.lock, Cargo.lock vb.) tarayarak uygulamanızın bağımlılık haritasını eksiksiz çıkarır.

## DevSecOps ve CI/CD boru hattı entegrasyonu

Trivy, modern yazılım dağıtım süreçlerinde bir kalite kapısı (quality gate) olarak konumlandırılır. Güvenlik açıklarının üretime sızmasını engellemek için CI/CD aşamasında belirli ciddiyet eşikleri tanımlanabilir:

**Kritik açıklarda derlemeyi durdurma komutu**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH imaj-adi:etiket
```
- Erken aşama geri bildirimi: Geliştiriciler kodlarını uzak depoya göndermeden önce yerel ortamlarında Trivy çalıştırarak açık kaynak kütüphanelerindeki zafiyetleri anında görür.
- Otomatik SARIF raporlama: Üretilen SARIF çıktıları GitHub Code Scanning veya GitLab Security panolarına aktarılarak ekiplerin merkezi zafiyet takibi yapması sağlanır.
- Canlı küme denetimi (Trivy Operator): Kubernetes ortamında çalışan iş yüklerini sürekli izleyerek yeni keşfedilen sıfırıncı gün (0-day) açıklarını anlık olarak raporlar.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
GitHub Actions üzerinde her kod gönderiminde (push) ve çekme isteğinde (PR) Docker imajımı ve kaynak kodlarımı Trivy ile tarayan bir güvenlik iş akışı (workflow) kurmak istiyorum. Yalnızca CRITICAL ve HIGH seviyesindeki güvenlik açıklarında derlemeyi durduran (exit-code 1), bulguları SARIF formatında GitHub Security panosuna yükleyen ve CycloneDX formatında SBOM dosyası oluşturan eksiksiz bir .github/workflows/trivy.yml dosyası hazırlar mısın?

- **Kimin için:** Yazılım geliştirme ve dağıtım süreçlerinde güvenlik denetimlerini, gizli anahtar kontrollerini ve SBOM üretimini otomatize etmek isteyen mühendisler içindir. 
- **Lisans:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı) 
- **Geliştirici:** Aqua Security ve Açık Kaynak Topluluğu 
- **Çıktı Formatları:** Tablo, JSON, SARIF, CycloneDX, SPDX, Şablon 

## Sıkça sorulan sorular
- Trivy Docker daemon olmadan konteyner imajlarını tarayabilir mi? Evet. Trivy, Docker istemcisine veya arka plan servisine (daemon) ihtiyaç duymadan doğrudan uzaktaki imaj depolarından (Docker Hub, GitHub Container Registry, AWS ECR vb.) veya yerel tar arşivlerinden imajları indirip tarayabilir.
- İnternet bağlantısı olmayan (air-gapped) ortamlarda çalışır mı? Evet. Trivy veritabanı (trivy-db) önceden indirilerek kapalı ağdaki ortama taşınabilir. Trivy, internete çıkmadan yerel veritabanı önbelleği üzerinden tarama gerçekleştirebilir.
- SBOM nedir ve Trivy bu alanda neden tercih edilir? SBOM (Software Bill of Materials), yazılımınızın içerdiği tüm açık kaynak kütüphaneleri, sürümleri ve lisansları belgeleyen dijital içerik listesidir. Trivy, hem imaj düzeyinde hem de kaynak kod düzeyinde SBOM üretebilen az sayıdaki standart araçtan biridir.
- Yanlış pozitif veya kabul edilmiş riskler nasıl hariç tutulur? Proje kök dizinine bir .trivyignore dosyası ekleyerek göz ardı etmek istediğiniz CVE kodlarını satır satır listeleyebilirsiniz. Bu sayede CI/CD boru hatlarında gereksiz derleme kesintilerinin önüne geçilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/aquasecurity/trivy)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Secrets SBOM Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/trivy/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
