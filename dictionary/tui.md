# TUI nedir ve nasıl çalışır?

> Text User Interface

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

TUI (Text User Interface / Metin Kullanıcı Arayüzü), terminal ekranlarında grafik kartına ihtiyaç duymadan metin ve karakter bloklarıyla çalışan klavye odaklı kullanıcı arayüzüdür.

## Kavramsal çerçeve, etimoloji ve terminalin evrimi
TUI terimi, İngilizce **Text User Interface** (veya zaman zaman *Terminal User Interface*) ifadesinin kısaltmasıdır. Bilgisayar arayüzleri tarihinde CLI (Komut Satırı Arayüzü) ile GUI (Grafik Kullanıcı Arayüzü) arasında köprü kuran hibrit bir görsel paradigmadır:

- **CLI (Command-Line Interface):** Kullanıcının tek satırlık bir komut girdiği ve sistemin bu komuta metin çıktısıyla yanıt verdiği tek boyutlu akıştır.
- **GUI (Graphical User Interface):** Pikseller, pencereler, fare imleçleri ve grafik hızlandırıcı kartlar (GPU) kullanan zengin görsel arayüzdür.
- **TUI (Text User Interface):** Pikseller yerine terminal ekranındaki satır ve sütunlardan oluşan iki boyutlu karakter ızgarasını (character grid) kullanan; pencereler, butonlar, durum çubukları ve formlar barındıran menülü arayüzdür.

TUI'nin kökleri 1970'li yılların TeleType (TTY) ve DEC VT100 gibi fiziksel metin terminallerine dayanır. Bu terminallerde ekranın belirli koordinatlarına renkli metin yazdırmak ve imleci taşımak için **ANSI Kaçış Dizileri** (ANSI Escape Sequences - örneğin `\033[2J` ekranı temizler, `\033[31m` metni kırmızı yapar) geliştirilmiştir.

## Bir benzetmeyle
Modern bir akıllı telefonun dokunmatik yüksek çözünürlüklü OLED ekranı (GUI) yerine; havaalanlarındaki mekanik açılır-kapanır harf panoları (split-flap display) veya dijital karakterli skorbordlar gibidir. Her kutucukta yalnızca tek bir harf veya sembol yer alabilir ancak bu sembollerin organize dizilimiyle kusursuz ve anında tepki veren bir kontrol paneli ortaya çıkar.

## Teknik mimari: Raw mode, ANSI kaçış dizileri ve çift tamponlama
Bir TUI uygulamasının arka planda nasıl çalıştığı işletim sistemi düzeyinde üç temel mekanizmaya dayanır:

1. **Terminalin Ham Modu (Raw Mode):** Standart terminal ortamı "Cooked Mode"da çalışır; yani işletim sistemi kullanıcı Enter tuşuna basana kadar karakterleri bekletir ve tamponlar. Bir TUI uygulaması başladığında terminali `termios` çağrısıyla "Raw Mode"a alır. Böylece kullanıcının bastığı her tuş (`j`, `k`, `Ctrl+C`, yön tuşları) Enter beklenmeden anında yakalanır.
2. **Alternatif Ekran Tamponu (Alternate Screen Buffer):** `htop` veya `vim` açtığınızda terminal geçmişinizin kaybolmaması ve program kapandığında eski komut satırınıza geri dönebilmeniz, alternatif tampon (`tput smcup / rmcup`) sayesinde gerçekleşir. TUI kendine ait sanal bir tuval açar ve çıkışta ana ekrana geri döner.
3. **Çift Tamponlama ve Fark Çizimi (Diff Rendering):** Ekrandaki titremeyi (flickering) önlemek için modern TUI motorları bellekte iki karakter matrisi tutar: O anki ekran ve sonraki ekran. Yalnızca değişen hücreler hesaplanır ve terminale sadece bu farklar (diff) ANSI kodlarıyla basılır; böylece 60 FPS akıcılıkta animasyonlar çalıştırılabilir.

## Modern TUI rönesansı ve geliştirici araçları
Son yıllarda web teknolojilerinin (Electron tabanlı şişkin uygulamalar) devasa bellek tüketmesine tepki olarak geliştirici ekosisteminde muazzam bir TUI rönesansı yaşanmıştır:

- **Düşük Kaynak Tüketimi:** Bir grafik arayüz yüzlerce megabayt bellek tüketirken, bir TUI uygulaması yalnızca birkaç megabayt RAM harcar.
- **SSH Üzerinden Sıfır Gecikme:** Buluttaki uzaktaki bir sunucuyu yönetirken grafik aktarmak (VNC / RDP) yüksek bant genişliği gerektirir; TUI ise düşük hızlı mobil bağlantılarda bile SSH tüneli içinde ışık hızında akar.
- **Klavye Akış Hali (Flow State):** Fareden elinizi kaldırmadan, Vim tuş dizilimleriyle (h, j, k, l) çalışmak mühendislerin odaklanmasını ve üretkenliğini katlar.

### Öne Çıkan Modern Çerçeveler ve Araçlar
- **Rust Dünyası:** `ratatui` (eski adıyla tui-rs) ve `crossterm` kütüphaneleri, bellek güvenliği ve ultra yüksek performansıyla modern TUI projelerinin temel standardı haline gelmiştir.
- **Go Dünyası:** Charm ekibinin geliştirdiği `bubbletea` (The Elm Architecture desenini terminale uyarlayan reaktif framework), `lipgloss` (stil motoru) ve `bubbles`.
- **Python Dünyası:** Will McGugan tarafından yazılan `Textual` ve `rich`.
- **Kült TUI Araçları:** Git yönetimi için `lazygit`, Kubernetes kümeleri için `k9s`, Docker için `lazydocker`, sistem izleme için `btop` ve `htop`, disk analizi için `ncdu`.

## Sık karıştırılanlar
- **CLI vs TUI:** CLI tek satırlık soru-cevap modelidir (`git status`, `ls -la`). TUI ise terminal penceresini kaplayan, sekmeleri, listeleri ve klavye kısayolları olan iki boyutlu görsel bir paneldir (`lazygit`, `k9s`).
- **TUI Sadece İlkel Metinden İbaret Değildir:** Modern terminaller Nerd Fonts (ikonlar), 24-bit TrueColor desteği, UTF-8 kutu çizim karakterleri ve hatta Kitty Graphics / Sixel protokolleriyle terminal içinde gerçek görsel çizimini destekler.

## Sıkça sorulanlar

**TUI ne anlama gelir ve açılımı nedir?**  
TUI, Text User Interface (Metin Kullanıcı Arayüzü) veya Terminal User Interface ifadesinin kısaltmasıdır. Grafik pencere yöneticisi olmadan terminal karakter ızgarası üzerinde çalışan görsel ve etkileşimli arayüzleri tanımlar.

**CLI, GUI ve TUI arasındaki temel farklar nelerdir?**  
CLI tek satırlık metin komutlarıyla çalışır; GUI pikseller, pencereler ve fare ile yönetilir; TUI ise terminal içinde klavye odaklı menüler, paneller ve kutularla çalışan hibrit bir formattır.

**Terminal kullanıcı arayüzleri ekranı nasıl çizer?**  
ANSI kaçış dizileri (Escape Sequences) ve terminal kontrol kodları aracılığıyla imleç ekranın istenen satır ve sütununa taşınır, renk kodları atanır ve Unicode kutu karakterleri çizilir.

**Modern TUI geliştirmek için en popüler kütüphaneler hangileridir?**  
Rust ekosisteminde `ratatui`, Go dilinde `bubbletea` ve `lipgloss`, Python tarafında ise `Textual` ve `rich` kütüphaneleri sektör standardıdır.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [Terminal](/dictionary/terminal/)
- [Terminal Control](/dictionary/terminal-control/)
- [Runtime](/dictionary/runtime/)
- [Assembly](/dictionary/assembly/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tui/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
