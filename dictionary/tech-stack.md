# Tech Stack nedir ve nasıl seçilir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Tech stack (Türkçe karşılığıyla **teknoloji yığını**), bir yazılım uygulamasını geliştirmek, çalıştırmak, ölçeklemek ve izlemek için bir araya getirilen programlama dilleri, kütüphaneler, veritabanları, API'lar ve bulut altyapılarının bütünüdür.

## Kavramsal çerçeve, yığın metaforu ve tarihsel evrim
Tech stack (Technology Stack), Türkçede **teknoloji yığını** olarak adlandırılır. "Yığın" (stack) metaforu, bilgisayar bilimlerindeki katmanlı soyutlama prensibine dayanır: Tıpkı bir binanın zemin etüdü, temeli, taşıyıcı kolonları ve dış cephesi gibi; yazılım dünyasında da her teknoloji katmanı kendisinden bir önceki katmanın sunduğu imkânların üzerine inşa edilir.

Tarihsel olarak teknoloji yığınları yazılım endüstrisinin paradigmalarıyla birlikte evrilmiştir:
- **2000'lerin Başı (LAMP Çağı):** Web 2.0 devrimini sırtlayan monolitik mimaridir: Linux (işletim sistemi), Apache (web sunucusu), MySQL (ilişkisel veritabanı) ve PHP/Perl/Python (arka uç dili). Basit, dayanıklı ve tek sunucuda çalışan bu model internetin ilk devlerini doğurdu.
- **2010'lar (Full-Stack JavaScript Devrimi):** Node.js'in ortaya çıkışıyla tarayıcı ve sunucu arasındaki dil bariyeri yıkıldı. MEAN (MongoDB, Express, Angular, Node.js) ve ardından MERN (Angular yerine React) yığını, JSON veri formatını istemciden veritabanına kadar kesintisiz taşıyarak tek dille tam yığın geliştirme dönemini başlattı.
- **Günümüz (Dağıtık, Jamstack ve Modern AI Yığını):** Statik üretim (SSG), sunucusuz uç bilişim (Edge Computing) ve yapay zekânın sisteme entegre olduğu çağdır. Artık monolitik yığınlar yerini mikroservislere, olay güdümlü kuyruklara ve vektör tabanlı yapay zekâ boru hatlarına bırakmıştır.

## Bir benzetmeyle
Çok katlı bir gökdelen inşaatına benzer. Zemin etüdü ve betonarme temel işletim sistemi ve bulut altyapınızdır (AWS, Linux); elektrik ve su tesisatı veri akışını sağlayan API'lar ve veritabanıdır (PostgreSQL, Redis); binanın taşıyıcı çelik iskeleti iş mantığını yürüten arka uçtur (Go, Python); dairelerin kapıları, pencereleri ve iç tasarımı ise kullanıcının dokunduğu ön yüzdür (React, Tailwind CSS).

## Bir teknoloji yığınının anatomisi (Temel katmanlar)
Kapsamlı bir kurumsal teknoloji yığını beş ana katmandan meydana gelir:

1. **İstemci Katmanı (Frontend):** Kullanıcının doğrudan etkileşime girdiği görsel ve mantıksal arayüzdür. HTML5, CSS3, JavaScript/TypeScript temelinde; React, Next.js, Vue.js, Svelte gibi modern çerçeveler ve Tailwind CSS gibi tasarım sistemleriyle şekillenir. İstemci tarafı durum yönetimi (State Management) ve sunucu tarafı işleme (SSR) bu katmanın sorumluluğundadır.
2. **Sunucu ve İş Mantığı Katmanı (Backend):** Güvenlik kontrolleri, iş kuralları, veri işleme ve üçüncü parti entegrasyonların gerçekleştiği motordur. Go, Rust, Python (FastAPI/Django), Node.js (Express/NestJS) veya Java (Spring Boot) yaygın diller arasındadır. İletişim RESTful API, GraphQL veya yüksek hızlı gRPC protokolleriyle sağlanır.
3. **Veri ve Kalıcılık Katmanı (Database & Cache):** Verinin güvenle saklandığı ve sorgulandığı katmandır. Yapılandırılmış veriler için ilişkisel veritabanları (PostgreSQL, MySQL); esnek şemalar için NoSQL (MongoDB); milisaniyelik önbellekleme ve oturum yönetimi için bellek içi veritabanları (Redis, Dragonfly) kullanılır.
4. **Altyapı, DevOps ve Dağıtım Katmanı:** Yazılımın hayata geçtiği çalışma ortamıdır. Docker konteynerleri, Kubernetes küme yönetimi, Terraform (IaC), CI/CD boru hatları (GitHub Actions, GitLab) ve bulut sağlayıcıları (AWS, Google Cloud, Cloudflare) bu katmanı oluşturur.
5. **Modern Yapay Zekâ Katmanı (AI Stack):** Günümüz modern sistemlerine eklenen yeni katmandır. Temel modeller (Claude, GPT, Llama), semantik arama için Vektör Veritabanları (pgvector, Qdrant, Milvus), bağlam yönetimi için RAG hatları ve model servis motorları (vLLM, Ollama) bu katmanda yer alır.

## Mimari karar matrisi ve seçim kriterleri
Yanlış bir teknoloji yığını seçmek, bir girişimi aylar süren yeniden yazım (rewrite) felaketine sürükleyebilir. Doğru seçim için dört temel ilke gözetilmelidir:

- **"Sıkıcı Teknoloji" İlkesi (Choose Boring Technology):** Dan McKinley'nin ünlü tezine göre her şirketin yalnızca sınırlı sayıda "inovasyon jetonu" vardır. Rekabet avantajı sağlamayacak altyapı bileşenlerinde (örneğin henüz test edilmemiş deneysel bir veritabanı) bu jetonları harcamak yerine; PostgreSQL, Linux ve Go gibi kendini kanıtlamış, öngörülebilir "sıkıcı" teknolojiler seçilmelidir.
- **İşe Alım Yoğunluğu (Hiring Density):** Dünyanın en hızlı dili projeniz için en iyi dil olmayabilir. Şirketinizin bulunduğu pazarda o dili bilen mühendis bulma kolaylığı, kütüphane zenginliği ve Stack Overflow topluluk büyüklüğü geliştirme hızınızı doğrudan belirler.
- **Performans ve Geliştirme Hızı Ödünleşimi (Trade-off):** Erken aşama bir girişimde (MVP) hızlı pazar doğrulaması için geliştirici dostu Python (FastAPI) veya Next.js mükemmelken; saniyede yüz binlerce finansal işlem yapan bir sistemde bellek güvenliği ve mikro saniye gecikme için Rust veya Go tercih edilir.
- **Conway Yasası:** Yazılım sistemlerinin mimarisi, o sistemi üreten organizasyonun iletişim yapısını kopyalar. Dağınık ve otonom ekipler mikroservis yığınlarında verimliyken, küçük ve sıkı bağlı ekipler monolitik yığınlarda çok daha hızlı ürün çıkarır.

## Popüler teknoloji yığını kombinasyonları
| Yığın Adı | Ön Yüz | Arka Uç | Veritabanı | İdeal Senaryo |
| :--- | :--- | :--- | :--- | :--- |
| **MERN / PERN** | React | Node.js (Express) | MongoDB / PostgreSQL | Hızlı prototipleme, dinamik web uygulamaları |
| **Modern AI Stack** | Next.js / TypeScript | Python (FastAPI) | PostgreSQL + pgvector + Redis | Üretken yapay zekâ, LLM ve RAG tabanlı ürünler |
| **Yüksek Performans Dağıtık** | Svelte / React | Go veya Rust | PostgreSQL + Kafka + ClickHouse | Fintek, yüksek hacimli veri akışları ve IoT |
| **Boring Monolith** | Blade / ERB / SSR | Laravel veya Ruby on Rails | MySQL / PostgreSQL + Redis | Az kişilik ekiplerle maksimum ürün geliştirme hızı |

## Sık karıştırılanlar
- **Tech Stack vs Sadece Framework:** "Bizim stack React" ifadesi eksiktir; React yalnızca ön yüz kütüphanesidir. Teknoloji yığını sunucudan veritabanına, işletim sisteminden CDN'e kadar tüm zinciri kapsar.
- **En Popüler = En İyisi:** Hacker News veya sosyal medyada trend olan her yeni araç projeniz için doğru araç değildir. İhtiyaç duyulmayan karmaşık mikroservis veya Kubernetes kurulumları erken aşamada aşırı mühendislik (over-engineering) tuzağıdır.

## Sıkça sorulanlar

**Tech stack ne demek, Türkçe karşılığı nedir?**  
Türkçe karşılığı teknoloji yığınıdır. Bir yazılım uygulamasını geliştirmek, çalıştırmak, ölçeklemek ve canlıda tutmak için birlikte kullanılan yazılım dilleri, çatıları (framework), veritabanları ve altyapı araçlarının bütünüdür.

**Bir teknoloji yığını seçerken yapılan en büyük hata nedir?**  
Gereksiz aşırı mühendislik (over-engineering) yapmak ve projenin ihtiyacı yokken en son trend araçları veya karmaşık mikroservis mimarilerini seçerek geliştirme sürecini kilitlemektir.

**Popüler tech stack kombinasyonları nelerdir?**  
LAMP (Linux, Apache, MySQL, PHP), MERN (MongoDB, Express, React, Node.js), Django/FastAPI + PostgreSQL ve modern Next.js + Supabase + Tailwind kombinasyonları en yaygın örneklerdendir.

**Yapay zekâ (AI) uygulamaları için modern tech stack neleri içerir?**  
Ön yüzde React/Next.js, model servis katmanında Python (FastAPI) veya vLLM, veri saklama ve anlamsal aramada pgvector veya Qdrant, orkestrasyonda ise LlamaIndex/LangChain bileşenlerini içerir.

## İlgili terimler
- [Framework](/dictionary/framework/)
- [Database](/dictionary/database/)
- [Frontend Stack](/dictionary/frontend-stack/)
- [Cloud Computing](/dictionary/cloud-computing/)
- [Deployment](/dictionary/deployment/)
- [Runtime](/dictionary/runtime/)
- [Memory Management](/dictionary/memory-management/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tech-stack/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
