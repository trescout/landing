# Local ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Local (yerel), bilişimde yazılımların, verilerin veya hesaplama işlemlerinin uzak bir bulut sunucusu yerine doğrudan kullanıcının kendi fiziksel cihazında (bilgisayar, telefon, yerel sunucu) çalıştırılması ve depolanmasıdır.

## Tanım ve Türkçe Karşılığı
"Local" kelimesi Türkçede **yerel** anlamına gelir. Yazılım mühendisliğinde ve bilişim dünyasında `localhost`, yerel geliştirme ortamı (local environment) ve son yıllarda hızla yayılan **local-first** mimarisinin temel yapı taşıdır. Bulut (Cloud/SaaS) sistemlerinin aksine, tüm veri işleme adımları cihazınızın yerel işlemcisi (CPU/GPU), belleği ve diski üzerinde kapalı devre olarak gerçekleşir.

## Bir benzetmeyle
Her akşam dışarıdan yemek sipariş etmek (bulut servisleri) yerine kendi mutfağınızda kendi malzemelerinizle yemek pişirmek gibidir. İnternetiniz veya elektrik dağıtım hattınız kopsa bile kendi kilerinizdeki erzakla karnınızı doyurabilirsiniz; ne yediğinizi de sizden başka kimse göremez.

## Local Çalışmanın ve Local-First Mimarisinin Avantajları
- **Tam Veri Gizliliği:** Veriler internet üzerinden dış sunuculara aktarılmaz, izleme (tracking) veya veri madenciliği riski sıfıra iner (KVKK ve GDPR uyumlu).
- **Çevrimdışı Kullanılabilirlik (Offline-First):** İnternet bağlantısı kesildiğinde, uçakta veya seyahat halindeyken uygulamalar kesintisiz çalışmayı sürdürür.
- **Sıfır Ağ Gecikmesi (Ultra Düşük Gecikme):** Sunucuya gidiş-dönüş (ping/latency) süreleri ortadan kalkar; veriler yerel disk ve bellek hızında anında okunur.
- **Abonelik Bağımsızlığı:** Sürekli artan bulut API kotaları ve sunucu faturaları yerine tek seferlik donanım yatırımıyla maliyet kontrolü sağlanır.

## Nerede ve Hangi Alanlarda Kullanılır?
- **Yerel Yapay Zekâ Modelleri:** Ollama, LM Studio, llama.cpp gibi araçlarla internet olmadan çalışan büyük dil modelleri (LLM).
- **Yerel Not ve Bilgi Yönetimi:** Obsidian ve Logseq gibi veriyi kullanıcının kendi bilgisayarında düz Markdown dosyalarında tutan sistemler.
- **Yazılım Geliştirme (Localhost):** Kodların canlıya alınmadan önce yerel makinede test edildiği geliştirme ortamları (`localhost:3000`).
- **Gömülü Veritabanları:** SQLite veya DuckDB gibi sunucusuz, tek dosya halinde yerel diskte çalışan veritabanı motorları.

## Sık karıştırılanlar
Self-hosted ile Local kavramları sıklıkla karıştırılır. Self-hosted yaklaşımında yazılım bir ağ sunucusunda (ev laboratuvarında bir sunucu veya kiralanan VPS) barındırılır ve cihazlar ağ üzerinden bu sunucuya bağlanır. Local ise yazılımın doğrudan kullanıcının elindeki bilgisayarda veya telefonda çalışmasıdır.

## Sıkça sorulanlar

**Local ne demek (Türkçe anlamı)?**  
Bilişimde "yerel" anlamına gelir; işlemlerin, dosyaların ve programların internetteki uzak bir sunucuda değil, kullanıcının doğrudan kendi cihazında yer almasıdır.

**Localhost nedir?**  
Bir bilgisayarın ağ üzerinde kendisini işaret etmek için kullandığı standart yerel geri döngü adresidir (`127.0.0.1`).

**Local-first yazılım yaklaşımı nedir?**  
Verinin asıl sahibinin kullanıcının yerel cihazı olduğu, bulutun ise yalnızca yedekleme ve cihazlar arası senkronizasyon için ikincil bir katman olarak kullanıldığı modern yazılım felsefesidir.

**Yapay zekâyı local çalıştırmak için ne gerekir?**  
Yeterli sistem belleği (RAM), tercihen güçlü bir grafik kartı (VRAM) veya Apple Silicon birleşik belleği ile Ollama gibi açık kaynaklı bir model yürütücüsü yeterlidir.

## İlgili terimler
- [Self-hosted](/dictionary/self-hosted/)
- [Offline](/dictionary/offline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/local/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
