# Jogo de estratégia leve e de código aberto

O Unciv é uma recriação de código aberto, minimalista e multiplataforma de Civilization V para desktop e Android. Desenvolvido com Kotlin e LibGDX, o projeto oferece as mecânicas originais de estratégia 4X com carga zero de hardware e amplo suporte a mods.

- ★ 11.285
- Kotlin
- GitHub Trending · 2026-06-18

## Atualizações
- 18 de setembro de 2026: Estrelas 11.276 → 11.285, versão mais recente 4.22.1 (17 de setembro de 2026).
- 15 de setembro de 2026: Estrelas 11.257 → 11.276, versão mais recente 4.22.0 (14 de setembro de 2026).
- 10 de setembro de 2026: Estrelas 11.241 → 11.257, versão mais recente 4.21.19 (9 de setembro de 2026).
- 8 de setembro de 2026: Estrelas 11.223 → 11.241, versão mais recente 4.21.18 (7 de setembro de 2026).

## O que você ganha
- Arquitetura leve e amiga da bateria: Gráficos 2D que rodam fluidos mesmo nos aparelhos mais básicos sem aquecimento.
- Mecânicas fiéis de Civilization V: Gestão de cidades, árvore tecnológica, políticas sociais e combates hexagonais preservados.
- Saves multiplataforma e multijogador: Transfira seu progresso entre Android e PC ou jogue partidas por turnos.
- Ecossistema de mods da comunidade: Baixe civilizações, unidades e cenários com um clique no menu do jogo.
- Experiência livre e sem anúncios: Licença MPL-2.0, sem compras no app, rastreamento ou anúncios.

## Como começar e opções de instalação

Unciv está disponível para múltiplas plataformas. No Android, instale pela Google Play Store ou F-Droid. No PC (Windows, Linux, macOS), use os arquivos compactados, Flatpak ou itch.io.
- [Página na Google Play Store →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [Repositório de código aberto no F-Droid →](https://f-droid.org/packages/com.unciv.app/)
- [Versões de desktop no itch.io →](https://yairm210.itch.io/unciv)

## Arquitetura técnica e funcionamento interno

Construído sobre LibGDX e Kotlin, o Unciv foca em uma lógica de estado leve e determinística:
- Motor orientado a estado: Tabuleiro, unidades e cidades são serializados como JSON puro, gerando arquivos de save de poucos kilobytes.
- Motor de mods declarativo: Regras e custos são descritos em JSON sem necessidade de recompilar código-fonte.
- Resolução de turnos determinística: Decisões da IA e combates calculados com precisão evitam perdas de sincronia.
- Compilação multiplataforma: Código Kotlin único roda nativamente no desktop (JVM) e no Android.

## Estratégias de jogabilidade e dinâmica 4X

Unciv executa com maestria o ciclo 4X: eXplore, eXpand, eXploit e eXterminate:
- Exploração no início da partida: Envie guerreiros e batedores para recolher ruínas antigas e lucrar com cidades-estado.
- Equilíbrio de felicidade e alimento: Funde cidades perto de recursos de luxo para sustentar o crescimento populacional.
- Planejamento científico: Pesquise tecnologias alinhadas com as forças estratégicas da sua civilização.
- Aproveitamento de terreno: Posicione defensores em colinas e rios para repelir exércitos muito maiores.

## Se você não programa
🤖 Se você não programa
Quero criar um mod em JSON válido para o Unciv. Você pode criar um modelo com um líder que dá bônus de ciência e cultura, uma unidade de cavalaria especial e uma biblioteca única? Explique a estrutura de pastas e como testar no Mod Manager do jogo.

- **Para quem:** Jogadores e criadores de mods que buscam estratégia 4X clássica em formato leve e open-source.
- **Licença:** MPL-2.0 (Mozilla Public License 2.0)
- **Motor de jogo:** LibGDX (Kotlin multiplataforma)
- **Plataformas:** Android, Windows, Linux, macOS

## Perguntas frequentes
- O Unciv é parecido com o Civilization V? Sim, as mecânicas, árvore tecnológica e regras reproduzem fielmente Civ V e suas expansões com visual 2D.
- É preciso internet para jogar? Não, o modo single-player roda 100% offline. Internet só é necessária para baixar mods e multijogador.
- Como instalar mods? Acesse o menu Mods dentro do próprio jogo para baixar centenas de modificações em um clique.
- Posso passar o save do PC para o celular? Sim, basta copiar o código do save no menu do jogo e importar na outra plataforma pela área de transferência.

## Links
- [GitHub →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

## Termos relacionados do glossário
Open Source Offline

---
Source: TreScout Discover · https://trescout.com/pt/discover/unciv/
