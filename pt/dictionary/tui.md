# O que é TUI?

> Text User Interface

TUI (Text User Interface / Interface de Usuário em Texto) é uma interface de usuário focada em teclado que opera em telas de terminal com blocos de texto e caracteres, sem a necessidade de uma placa gráfica.

## Estrutura conceitual, etimologia e a evolução do terminal
O termo TUI é uma abreviação da expressão em inglês Text User Interface (ou, por vezes, Terminal User Interface). Na história das interfaces de computador, é um paradigma visual híbrido que estabelece uma ponte entre a CLI (Interface de Linha de Comando) e a GUI (Interface Gráfica do Usuário):

## Arquitetura técnica: Modo bruto (Raw mode), sequências de escape ANSI e buffer duplo
Como uma aplicação TUI funciona em segundo plano baseia-se em três mecanismos fundamentais ao nível do sistema operacional:

## O renascimento moderno da TUI e as ferramentas de desenvolvedor
Nos últimos anos, como reação ao enorme consumo de memória das tecnologias web (aplicativos inchados baseados em Electron), houve um enorme renascimento da TUI no ecossistema de desenvolvedores:

## Costuma ser confundido com

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
- [CLI](/pt/dictionary/cli/)
- [Terminal](/pt/dictionary/terminal/)
- [Terminal Control](/pt/dictionary/terminal-control/)
- [Runtime](/pt/dictionary/runtime/)
- [Assembly](/pt/dictionary/assembly/)
- [Tech Stack](/pt/dictionary/tech-stack/)

## Ferramentas relacionadas
- [PI](/pt/discover/pi/)
- [Witr](/pt/discover/witr/)
- [Hister](/pt/discover/hister/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/tui/
