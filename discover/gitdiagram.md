# GitHub depolarını etkileşimli mimari şemalara dönüştürün

> Gitdiagram · TypeScript · ★ 16.568

Gitdiagram, GitHub depolarındaki karmaşık dosya yapılarını ve kod ilişkilerini saniyeler içinde görselleştiren açık kaynaklı bir araçtır. URL'deki tek bir harfi değiştirerek devasa kod tabanlarının sistem mimarisini interaktif diyagramlar halinde sunar.

## Ne kazandırır?
- Saniyeler İçinde Kod Haritası: Binlerce satırlık yabancı bir depoda kaybolmadan sistem mimarisini, ana modülleri ve veri akışını kuşbakışı görün.
- Tek Tıkla URL Kısayolu: Herhangi bir GitHub repo URL'sindeki github.com kısmını gitdiagram.com yaparak kurulumsuz anında şema üretin.
- İnteraktif Düğümler: Şema üzerindeki kutulara tıklayarak doğrudan GitHub'daki ilgili kaynak kod dosyasına veya klasörüne gidin.
- Dışa Aktarma Desteği: Oluşturulan mimari şemaları dokümantasyon veya sunumlar için PNG, SVG veya metin biçiminde indirin.

## Tek tıkla kullanım: URL değiştirme kısayolu
Gitdiagram'ın en pratik yanı hiçbir kurulum gerektirmeden tarayıcı üzerinden çalışmasıdır. İncelemek istediğiniz herhangi bir açık kaynaklı deponun adresindeki hub kelimesini silip yerine diagram yazmanız yeterlidir:URL Kısayolu ÖrneğiKopyala# Orijinal GitHub adresi:
https://github.com/facebook/react

# Gitdiagram etkileşimli şema adresi:
https://gitdiagram.com/facebook/reactBu bağlantıya girdiğiniz anda Gitdiagram arkaplanda depoyu tarar, dosya ağacını analiz eder ve interaktif şemayı tarayıcınızda açar.

## Teknik mimari ve çalışma mantığı
Gitdiagram, kod tabanını salt metin olarak değil, ilişkisel bir sistem grafı olarak ele alır:

1. Ağaç Çıkarma (Tree Ingestion): GitHub REST ve GraphQL API'lerini kullanarak deponun dosya ağacını, paket yöneticisi tanımlarını (package.json, Cargo.toml, go.mod) ve dizin hiyerarşisini çeker.

2. Semantik Analiz ve İlişkilendirme: Modüller arasındaki import zincirlerini ve servis sınırlarını tespit eder. LLM entegrasyonu (OpenAI / Claude API) ile bileşenlerin rollerini (API Gateway, Controller, Database Adapter) etiketler.

3. Vektörel Çizim Motoru: Elde edilen grafı React Flow ve SVG tabanlı bir sanal tuvale dönüştürür. Düğümler arası veri akışı yönlü oklarla görselleştirilir.

## Kurulum ve yerel dağıtım
Kendi API anahtarlarınızla çalıştırmak veya özel (private) depolarınızı kendi sunucunuzda görselleştirmek için Gitdiagram'ı yerel ortamınızda başlatabilirsiniz:

### Yerel ortamı hazırlama ve bağımlılıkları kurma
```bash
git clone https://github.com/ahmedkhaleel2004/gitdiagram.git
cd gitdiagram
bun install
cp .env.example .env
```

### Geliştirme sunucusunu başlatma
```bash
# .env içine GITHUB_TOKEN ve OPENAI_API_KEY ekleyin
bun run dev
```

## Kod bilmiyorsanız: Yapay zekâ ajanı istemi
Gitdiagram mimarisini temel alarak incelediğim GitHub deposunun sistem şemasını oluştur. Depodaki ana bileşenleri, veri akış yönlerini, giriş noktalarını (entry points) ve harici bağımlılıkları tespit et. Mimariyi Mermaid.js formatında bir flowchart olarak çiz ve her bileşenin işlevini ikişer cümleyle açıkla.

## Kritik uyarılar ve sınırlar
- Devasa Monorepolar: On binlerce dosya içeren monorepolarda GitHub API hız limitine (rate limit) takılabilir. Kişisel GitHub token kullanmak sınırları genişletir.
- Özel (Private) Depolar: Bulut sürümü yalnızca herkese açık (public) depoları destekler. Şirket içi kapalı depolar için aracı yerel sunucunuzda kendi token'ınızla çalıştırmalısınız.
- LLM Token Maliyeti: Kendi sunucunuzda çalıştırırken büyük repolarda harcanan LLM API token miktarını optimize etmek için dosya filtreleme kurallarını yapılandırmalısınız.

## Sıkça sorulan sorular

### Gitdiagram'ı kullanmak ücretli mi?
Hayır, Gitdiagram açık kaynaklıdır (MIT lisansı). Web sürümü herkese açık repolar için ücretsizdir, yerel sürümü de kendi donanımınızda bedelsiz çalıştırabilirsiniz.

### Özel (private) GitHub depolarımda kullanabilir miyim?
Evet. Bunun için projeyi GitHub'dan klonlayıp kendi makinenizde çalıştırmalı ve özel deponuza erişim yetkisi olan bir GitHub Personal Access Token (PAT) tanımlamalısınız.

### Büyük projelerde şema karmaşıklaşır mı?
Gitdiagram derinlik filtreleri sunar. Çok katmanlı projelerde ana dizin seviyesinde özet şema alabilir veya ilgilendiğiniz alt modülü seçip detayına inebilirsiniz.

### Oluşturulan şemayı sunumuma ekleyebilir miyim?
Evet, arayüz üzerinden tek tıkla şemanın yüksek çözünürlüklü PNG veya SVG çıktısını alabilir, doğrudan tasarım ve dokümantasyon araçlarınıza yapıştırabilirsiniz.

## Bağlantılar
- [GitHub deposu (ahmedkhaleel2004/gitdiagram) →](https://github.com/ahmedkhaleel2004/gitdiagram)
- [Gitdiagram Canlı Web Uygulaması →](https://gitdiagram.com)

## İlgili sözlük terimleri
- [Software Architecture](/dictionary/software-architecture/)
- [AI Agent](/dictionary/ai-agent/)
- [Runtime](/dictionary/runtime/)
- [Artificial Intelligence](/dictionary/artificial-intelligence/)

---
Source: TreScout Discovery · https://trescout.com/discover/gitdiagram/
