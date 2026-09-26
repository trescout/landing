# 465'ten fazla platformda OSINT kullanıcı analizi

Python tabanlı User-Scanner, tek bir kullanıcı adı veya e-posta üzerinden 465'ten fazla sosyal ağ, forum ve kod deposunda açık kaynak istihbaratı (OSINT) taraması gerçekleştirir.

- ★ 3.910
- Python
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 3.910, 465'ten fazla platform desteği ve asenkron HTTP tarama motoru güncellemesi.

## Ne kazandırır?
- Geniş platform kapsamı: GitHub, Reddit, Twitter, Steam, Telegram ve 465'i aşkın sitede tek seferde hesap varlığı doğrulama.
- Asenkron yüksek hızlı tarama: asyncio ve aiohttp tabanlı mimarisiyle yüzlerce hedefi saniyeler içinde paralel sorgulama.
- Yanlış pozitif filtreleme: HTTP durum kodlarının yanı sıra yanıt gövdesindeki hata metinlerini doğrulayan akıllı tespit mekanizması.
- JSON ve CSV rapor dışa aktarma: Analiz sonuçlarını adli bilişim ve güvenlik raporlarında kullanılmak üzere yapılandırılmış formatlarda kaydetme.
- Gizlilik ve yerel yürütme: Hiçbir sorguyu üçüncü taraf sunuculara göndermeden tamamen yerel makineden çalıştırma imkânı.

## Kurulum

**Depoyu klonlama ve bağımlılıkları yükleme**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```

## Çalıştırma

**Hedef kullanıcı adını ve e-postayı tarama**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```

## Teknik mimari ve çalışma prensibi

User-Scanner, modüler bir hedef eşleme ve asenkron tarama boru hattı üzerine kurulmuştur:
- Veritabanı Şablonları (JSON Site Manifestleri): 465+ platformun URL desenlerini, hata kodlarını ve profil regexlerini içeren modüler yapılandırma.
- Eşzamanlı İstek Havuzu (Connection Pooling): DNS çözümlemelerini ve TCP soketlerini önbelleğe alarak ağ bant genişliğini en verimli şekilde kullanma.
- Özel HTTP Başlıkları ve User-Agent Rotasyonu: WAF ve hız sınırı (rate limit) engellerine takılmamak için gerçekçi tarayıcı başlıkları simülasyonu.

## OSINT araştırma senaryoları ve veri analizi

Güvenlik uzmanları ve adli bilişim araştırmacıları için User-Scanner kritik senaryolar sunar:
- Kişisel Veri İhlali ve İz Takibi: Kullanıcı adı korelasyonu ile sızdırılmış profillerin hangi sosyal mecralarda etkin olduğunu haritalandırın.
- Kurumsal Güvenlik Denetimleri: Şirket çalışanlarının kurumsal e-posta adresleriyle harici platformlarda hesap açıp açmadığını tespit edin.
- Sosyal Mühendislik Savunması: Hedef odaklı oltalama (spear phishing) saldırılarına karşı yetkisiz taklit hesapları erkenden belirleyin.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bir güvenlik denetiminde User-Scanner aracını kullanarak tek bir kullanıcı adı üzerinden 465'ten fazla platformda nasıl tarama yapabileceğimi, elde edilen bulguları JSON formatında dışa aktarıp şüpheli profilleri nasıl listeleyeceğimi adım adım açıklar mısın?

- **Kimin için:** Siber güvenlik araştırmacıları, OSINT analistleri, adli bilişim uzmanları ve etik hackerlar. 
- **Lisans:** GPL-3.0 (Açık kaynak copyleft lisansı) 
- **Çatı:** Python Asenkron OSINT Tarayıcısı 
- **Platformlar:** Linux, macOS, Windows 

## Sıkça sorulan sorular
- User-Scanner kullanmak yasal mıdır? Evet. User-Scanner yalnızca kamuya açık web sayfalarında herkesin görebileceği hesap varlığı durumlarını sorgular; hiçbir yetkisiz sisteme erişim sağlamaz veya şifre kırmaz.
- Tor veya proxy desteği var mı? Evet. İstekleri SOCKS5 veya HTTP proxy zincirleri üzerinden yönlendirerek IP adresinizi maskeleyebilir ve hız sınırlarından kaçınabilirsiniz.
- Sonuçlar ne kadar sürede tamamlanır? Asenkron mimarisi sayesinde internet bağlantınıza bağlı olarak 465'ten fazla platformun taranması genellikle 20 ile 45 saniye arasında tamamlanır.
- E-posta araması nasıl çalışır? E-posta modunda, desteklenen servislerin şifre sıfırlama veya hesap kayıt uç noktalarında kamuya açık doğrulama sinyalleri incelenir.

## Bağlantılar
- [GitHub deposu →](https://github.com/kaifcodec/user-scanner)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CLI Açık Kaynak API Framework CI/CD

---
Kaynak: TreScout Keşif · https://trescout.com/discover/user-scanner/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
