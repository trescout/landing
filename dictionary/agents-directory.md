# Agents Directory nedir?

*Yapay Zekâ · Son güncelleme: 11 Ekim 2026*

Yazılım projelerinde yapay zekâ ajanlarının davranışlarını, araçlarını ve kurallarını bir arada tutan özel klasör yapısıdır.

## Tanım

Agents directory, bir kod tabanında farklı görevler için tasarlanmış yapay zekâ ajanlarının talimatlarını ve araç bağlantılarını barındıran dizindir. Projenizde çalışan birden fazla otonom yardımcının görev sınırlarını ve davranış kalıplarını tek bir standart yerde organize etmenizi sağlar. Geliştirme araçları ve orkestrasyon motorları bu dizini tarayarak projenize özel ajanları otomatik olarak tanır.

*Bir şirkette her bir uzman çalışanın görev tanımının, yetkilerinin ve rehber kitapçıklarının düzenli tutulduğu insan kaynakları klasörüne benzer.*

## Nasıl çalışır?

Geliştiriciler proje kök dizininde genellikle .agents veya agents adında bir klasör oluşturur. Bu klasörün içine test yazan, kod inceleyen veya dokümantasyon hazırlayan her bir ajan için yapılandırma dosyaları eklenir. Ajan destekli geliştirme araçları bu dosyaları okuyarak ajanın hangi rolleri üstleneceğini ve hangi fonksiyonları çağırabileceğini belirler.

## Nerede kullanılır?

Ajan tabanlı yazılım geliştirme ortamlarında, yapay zekâ orkestrasyon platformlarında ve modern kod editörlerinde sıkça kullanılır.

## Sık karıştırılanlar

Genel 'agent workspace' kavramıyla karıştırılabilir: Çalışma alanı ajanın iş yaparken kullandığı geçici belleği ve geçici dosyaları ifade ederken, agents directory ajanların kaynak kod ve kural tanımlarının saklandığı kalıcı dosya dizinidir.

## Sıkça sorulanlar

**Bu klasör olmadan yapay zekâ ajanları çalışamaz mı?**

Çalışabilir ancak her ajanın sistem talimatlarını ve kullanabileceği araçları tek tek manuel belirtmeniz gerekir; dizin yapısı bu süreci otomatikleştirir ve standartlaştırır.

**Klasördeki ajanlar birbirleriyle otomatik iletişim kurabilir mi?**

Kurabilir: Çoklu ajan mimarisine sahip sistemler bu dizindeki ajanları listeleyerek bir görevi diğer ajana devretmek için rehber olarak kullanır.

## İlgili terimler

- [AI Agent](https://trescout.com/dictionary/ai-agent/)
- [Agent Workspace](https://trescout.com/dictionary/agent-workspace/)
- [Agentic AI](https://trescout.com/dictionary/agentic-ai/)
- [Prompt as Code](https://trescout.com/dictionary/prompt-as-code/)
- [System Prompts](https://trescout.com/dictionary/system-prompts/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/agents-directory/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
