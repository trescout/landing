# O que é Compositor?

*Desenvolvimento · Última atualização: 3 de novembro de 2026*

É a camada de software que gerencia onde as janelas aparecerão na tela e a interação visual entre elas.

## Definição

No sistema operacional, é responsável por desenhar as janelas, efeitos de transparência, sombras e cálculos de visibilidade quando as janelas se sobrepõem. As estruturas modernas que substituem os gerenciadores de janelas tradicionais aumentam a qualidade visual e garantem que as janelas se movam de forma fluida usando o poder da placa de imagem. O software combina as imagens vindas das janelas e envia a versão final em pixels para o monitor.

***Analogia:** É como o diretor de palco de um teatro, que define qual cenário fica na frente, qual ator fica atrás e em quem a luz deve incidir.*

## Como funciona

Ele coleta os dados gráficos dos aplicativos, processa a posição das janelas e os efeitos visuais, fazendo com que a placa de vídeo renderize a imagem final.

## Onde é usado

Ele está presente em servidores gráficos Linux, no protocolo Wayland e na arquitetura gráfica central dos sistemas operacionais de desktop modernos.

## Costuma ser confundido com

Ele é frequentemente confundido com o driver da placa de vídeo diretamente, mas enquanto o driver gerencia o hardware, o compositor organiza as camadas visuais.

## Perguntas e respostas

**Ele sobrecarrega a placa de vídeo?**

Em hardwares modernos, ele é bastante leve e alivia o processador, transferindo a carga para a placa de vídeo.

**Por que isso é importante?**

Ele evita tremores ao mover as janelas e garante que os efeitos visuais modernos funcionem perfeitamente.

## Termos relacionados

- [Dynamic Tiling](https://trescout.com/pt/dictionary/dynamic-tiling/)
- [TUI](https://trescout.com/pt/dictionary/tui/)
- [User Interface](https://trescout.com/pt/dictionary/user-interface/)

## Ferramentas relacionadas

- [Hyprland](https://trescout.com/pt/discover/hyprland/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/compositor/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/compositor/
