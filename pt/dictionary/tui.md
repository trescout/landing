# O que é TUI?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

> Text User Interface

TUI (Text User Interface / Interface de Usuário em Texto) é uma interface de usuário focada em teclado que opera em telas de terminal com blocos de texto e caracteres, sem a necessidade de uma placa gráfica.

## Estrutura conceitual, etimologia e a evolução do terminal

O termo TUI é uma abreviação da expressão em inglês Text User Interface (ou, por vezes, Terminal User Interface). Na história das interfaces de computador, é um paradigma visual híbrido que estabelece uma ponte entre a CLI (Interface de Linha de Comando) e a GUI (Interface Gráfica do Usuário):

- CLI (Interface de Linha de Comando): É um fluxo unidimensional onde o usuário insere um comando em uma única linha e o sistema responde a esse comando com uma saída de texto.
- GUI (Interface Gráfica do Usuário): É uma interface visual rica que utiliza pixels, janelas, cursores de mouse e placas aceleradoras gráficas (GPU).
- TUI (Text User Interface): É uma interface com menus que utiliza uma grade de caracteres bidimensional composta por linhas e colunas na tela do terminal, em vez de pixels, e que contém janelas, botões, barras de status e formulários.

As raízes da TUI remontam aos terminais de texto físicos da década de 1970, como o TeleType (TTY) e o DEC VT100. Nesses terminais, foram desenvolvidas as Sequências de Escape ANSI (ANSI Escape Sequences · por exemplo, \033[2J limpa a tela, \033[31m torna o texto vermelho) para imprimir texto colorido em coordenadas específicas da tela e mover o cursor.

***Analogia:** Em vez da tela OLED de alta resolução sensível ao toque de um smartphone moderno (GUI), é como os painéis de letras mecânicos (split-flap display) em aeroportos ou placares de caracteres digitais. Cada caixa pode conter apenas uma única letra ou símbolo, mas a disposição organizada desses símbolos cria um painel de controle perfeito e de resposta imediata.*

## Arquitetura técnica: Modo bruto (Raw mode), sequências de escape ANSI e buffer duplo

Como uma aplicação TUI funciona em segundo plano baseia-se em três mecanismos fundamentais ao nível do sistema operacional:

1. Modo Raw do Terminal: O ambiente de terminal padrão opera em "Cooked Mode"; ou seja, o sistema operacional retém e armazena os caracteres em buffer até que o usuário pressione a tecla Enter. Quando uma aplicação TUI é iniciada, ela coloca o terminal em "Raw Mode" por meio da chamada termios. Assim, cada tecla pressionada pelo usuário (j, k, Ctrl+C, teclas de direção) é capturada instantaneamente, sem a necessidade de pressionar Enter.
2. Buffer de Tela Alternativo (Alternate Screen Buffer): O fato de o seu histórico do terminal não desaparecer ao abrir o htop ou o vim e de você poder retornar à sua linha de comando anterior ao fechar o programa acontece graças ao buffer alternativo (tput smcup / rmcup). A TUI abre sua própria tela virtual e retorna à tela principal ao ser encerrada.
3. Double Buffering e Renderização de Diferenças (Diff Rendering): Para evitar cintilação (flickering) na tela, os motores TUI modernos mantêm duas matrizes de caracteres na memória: a tela atual e a próxima tela. Apenas as células alteradas são calculadas e somente essas diferenças (diff) são enviadas ao terminal com códigos ANSI; assim, animações podem ser executadas com a fluidez de 60 FPS.

## O renascimento moderno da TUI e as ferramentas de desenvolvedor

Nos últimos anos, como reação ao enorme consumo de memória das tecnologias web (aplicativos inchados baseados em Electron), houve um enorme renascimento da TUI no ecossistema de desenvolvedores:

- Baixo consumo de recursos: Enquanto uma interface gráfica consome centenas de megabytes de memória, uma aplicação TUI utiliza apenas alguns megabytes de RAM.
- Latência zero via SSH: Gerenciar um servidor remoto na nuvem via interface gráfica (VNC/RDP) exige alta largura de banda; já a TUI flui na velocidade da luz dentro de um túnel SSH, mesmo em conexões móveis de baixa velocidade.
- Estado de Fluxo do Teclado: Trabalhar com os atalhos do Vim (h, j, k, l) sem tirar a mão do mouse multiplica o foco e a produtividade dos engenheiros.

Frameworks e Ferramentas Modernas em Destaque:

- Mundo Rust: as bibliotecas ratatui (antiga tui-rs) e crossterm tornaram-se o padrão fundamental para projetos TUI modernos, graças à sua segurança de memória e desempenho ultra-alto.
- Mundo Go: A equipe Charm desenvolveu o bubbletea (framework reativo que adapta o padrão The Elm Architecture para o terminal), o lipgloss (mecanismo de estilo) e o bubbles.
- Mundo Python: Textual e rich, escritos por Will McGugan.
- Ferramentas TUI de culto: lazygit para gerenciamento de Git, k9s para clusters Kubernetes, lazydocker para Docker, btop e htop para monitoramento de sistema, ncdu para análise de disco.

## Costuma ser confundido com

- CLI vs TUI: CLI, tek satırlık soru-cevap modelidir (git status, ls -la). TUI ise terminal penceresini kaplayan, sekmeleri, listeleri ve klavye kısayolları olan iki boyutlu görsel bir paneldir (lazygit, k9s).
- TUI não se resume apenas a texto primitivo: os terminais modernos suportam Nerd Fonts (ícones), suporte a TrueColor de 24 bits, caracteres de desenho de caixa UTF-8 e até mesmo renderização gráfica real dentro do terminal com os protocolos Kitty Graphics / Sixel.

## Perguntas frequentes

**O que significa TUI e qual é a sua sigla?**

TUI é a abreviação de Text User Interface (Interface de Usuário de Texto) ou Terminal User Interface (Interface de Usuário de Terminal). Define interfaces visuais e interativas que operam na grade de caracteres do terminal sem um gerenciador de janelas gráfico.

**Quais são as principais diferenças entre CLI, GUI e TUI?**

A CLI funciona com comandos de texto de uma única linha; a GUI é gerenciada com pixels, janelas e mouse; enquanto a TUI é um formato híbrido que funciona dentro do terminal com menus, painéis e caixas focados no teclado.

**Como as interfaces de usuário de terminal desenham a tela?**

Através de sequências de escape ANSI e códigos de controle de terminal, o cursor é movido para a linha e coluna desejadas na tela, códigos de cores são atribuídos e caracteres de caixa Unicode são desenhados.

**Quais são as bibliotecas mais populares para o desenvolvimento de TUI moderna?**

No ecossistema Rust, ratatui; na linguagem Go, bubbletea e lipgloss; e no lado do Python, as bibliotecas Textual e rich são o padrão da indústria.

## Termos relacionados

- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Terminal](https://trescout.com/pt/dictionary/terminal/)
- [Terminal Control](https://trescout.com/pt/dictionary/terminal-control/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Assembly](https://trescout.com/pt/dictionary/assembly/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)

## Ferramentas relacionadas

- [PI](https://trescout.com/pt/discover/pi/)
- [Witr](https://trescout.com/pt/discover/witr/)
- [Hister](https://trescout.com/pt/discover/hister/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/tui/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/tui/
