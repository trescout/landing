# Controle computacional para agentes de inteligência artificial

CUA fornece uma infraestrutura de código aberto para agentes de inteligência artificial com capacidade de computador. Ele reúne sandbox, kit de desenvolvimento de software (SDK) e ferramentas de benchmark sob o mesmo teto com o objetivo de treinar e avaliar agentes que podem controlar sistemas operacionais de desktop.

- ★ 31.379
- HTML
- GitHub Trending · 2026-06-16

## Atualizações

- **31 de outubro de 2026:** Estrelas 31,326 → 31,379, versão mais recente cua-spaces-v0.19.2 (30 de outubro de 2026).
- **30 de outubro de 2026:** Estrelas 31,320 → 31,326, versão mais recente cua-spaces-v0.19.0 (30 de outubro de 2026).
- **30 de outubro de 2026:** Estrelas 30,972 → 31,320, versão mais recente cua-spaces-v0.18.0 (30 de outubro de 2026).
- **26 de outubro de 2026:** Estrelas 30,882 → 30,972, versão mais recente cua-spaces-v0.16.0 (25 de outubro de 2026).

## O que você ganha

- Controle aplicativos de desktop em segundo plano
- Sandboxes isolados para diferentes sistemas operacionais
- Ferramentas de benchmarking para medir o desempenho do agente

## Instalação

**Instalação do driver (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Instalação do SDK do Sandbox**

```
pip install cua
```

## Execução

**inicialização da máquina virtual macOS**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero desenvolver um agente de uso de computador usando a infraestrutura CUA. Ajude-me a configurar a estrutura básica do Python que permitirá que meu agente interaja com aplicativos de desktop em segundo plano, faça cliques do mouse e envie entradas do teclado. Crie um esboço de código de amostra que execute comandos e faça capturas de tela em um ambiente Linux usando o CUA Sandbox SDK.

Repositório: https://github.com/trycua/cua. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Benchmark](https://trescout.com/pt/dictionary/benchmark/)
- [Sandbox](https://trescout.com/pt/dictionary/sandbox/)
- [SDK](https://trescout.com/pt/dictionary/sdk/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É indicado para desenvolvedores de software e pesquisadores que desenvolvem agentes de inteligência artificial que realizam tarefas autônomas no computador.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/trycua/cua)
- [Ler em turco →](https://trescout.com/discover/cua/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cua/
