# Jogo de estratégia leve e de código aberto

Unciv é uma adaptação de código aberto, minimalista e multiplataforma para desktop e Android do Civilization V. Desenvolvido com infraestrutura Kotlin e LibGDX, o projeto oferece mecânica de estratégia 4X original com carga zero de hardware e alto suporte a mod.

- ★ 11.376
- Kotlin
- GitHub Trending · 2026-06-18

## O que você ganha
- Arquitetura de hardware baixo e compatível com bateria: funciona com aquecimento zero, mesmo nos dispositivos móveis mais básicos, usando vetores 2D e gráficos de pixel em vez de mecanismos pesados ​​de renderização 3D.
- Mecânica original de Civilization V: planejamento urbano, árvore tecnológica, políticas sociais, diplomacia e sistema tático de combate hexadecimal são totalmente preservados.
- Salvamento multiplataforma e suporte multijogador: você pode mover arquivos salvos diretamente entre o desktop e o Android ou jogar partidas multijogador round-robin baseadas em e-mail/servidor.
- Rico ecossistema de mods orientado pela comunidade: Novas civilizações, unidades, cenários de fantasia e temas gráficos podem ser instalados e ativados com um único clique na interface do jogo.
- Experiência totalmente gratuita e sem anúncios: Distribuída sob licença MPL-2.0; não contém compras no aplicativo, publicidade, rastreamento ou coleta de dados.

## Como começar e opções de instalação
- Página da Google Play Store →
- Repositório de código aberto F-Droid →
- Versões para desktop do itch.io →

## Arquitetura técnica e princípio de funcionamento
- Mecanismo de jogo orientado pelo estado: cada bloco hexadecimal, unidade, cidade e relação diplomática no tabuleiro de jogo é armazenado como objetos JSON puros. Essa estrutura mantém o tamanho dos arquivos de log em apenas algumas centenas de kilobytes.
- Mecanismo de modding declarativo: recursos de civilização, árvores tecnológicas e custos de construção são definidos por meio de arquivos JSON sem tocar no código-fonte. Desta forma, os desenvolvedores de mod não precisam de um compilador externo.
- Cálculo de rodadas determinísticas: movimentos de IA e resultados de batalha são calculados com algoritmos previsíveis. Isso evita interrupções de sincronização em jogos multijogador assíncronos.
- Compilação multiplataforma: graças ao LibGDX, uma única base de código Kotlin é empacotada com desempenho nativo para desktop (JVM) e dispositivos móveis (tempo de execução Android).

## Estratégias de jogo e dinâmica 4X
- Exploração do mapa nas primeiras rodadas: Distribua suas unidades de guerreiros e batedores pelo mapa com antecedência para coletar artefatos antigos, fazer o primeiro contato com cidades-estado e obter renda em ouro.
- Felicidade e equilíbrio alimentar: Ao estabelecer novas cidades, tome cuidado para estar ao alcance dos recursos de luxo. Quando a sua taxa de felicidade cai para negativo, o crescimento populacional e a produção desaceleram significativamente.
- Roteiro tecnológico: concentre-se nos pontos fortes da sua civilização em vez de pesquisas aleatórias; Siga os caminhos da ferraria e da pólvora para a vitória militar, da filosofia e da educação para a vitória cultural.
- Usando vantagens de terreno: Repelir grandes exércitos com um pequeno número de unidades criando defesa ribeirinha, vantagem em colinas e passagens estreitas.

## Se você não programa
Quero preparar uma estrutura de mod JSON válida para o jogo Unciv. Você pode criar um modelo de mod Unciv de amostra que inclua uma unidade de cavalaria especial e um edifício de biblioteca especial que dê um bônus à produção científica e cultural como habilidade de líder? Você pode explicar passo a passo quais arquivos JSON devo salvar em qual estrutura de pastas e como posso testar isso na interface do Mod Manager do jogo?

## Perguntas frequentes
- Quão semelhante é o Unciv com a Civilização V? A mecânica do jogo, as estatísticas das unidades, a árvore tecnológica e as condições de vitória são amplamente compatíveis com os complementos Civilization V Gods and Kings e Admirável Mundo Novo. A diferença é basicamente o uso de design visual 2D simples em vez de gráficos 3D.
- É necessária uma conexão com a Internet para jogar? Não. Unciv pode ser jogado completamente offline. Nenhuma conexão de rede é necessária para jogar contra oponentes de IA no modo single-player. Apenas downloads de mod e partidas multijogador requerem conexão.
- Como instalar mods Unciv? Acessando a aba Mods no menu principal, você pode listar centenas de mods carregados pela comunidade e baixá-los para o seu dispositivo com um único clique. Você também pode instalar diretamente adicionando um link para qualquer repositório de mod no GitHub.
- Os arquivos de gravação podem ser transferidos entre o desktop e o telefone? Sim. Você pode copiar o arquivo salvo para a área de transferência no menu de gravação do jogo, enviá-lo para o seu outro dispositivo por e-mail ou mensagem em formato de texto e continuar de onde parou com a opção de carregar a partir da área de transferência.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/unciv/
