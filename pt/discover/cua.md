# Controle computacional para agentes de inteligência artificial

CUA fornece uma infraestrutura de código aberto para agentes de inteligência artificial com capacidade de computador. Ele reúne sandbox, kit de desenvolvimento de software (SDK) e ferramentas de benchmark sob o mesmo teto com o objetivo de treinar e avaliar agentes que podem controlar sistemas operacionais de desktop.

- ★ 28.129
- HTML
- GitHub Trending · 2026-06-16

## Atualizações

- **5 de outubro de 2026:** Estrelas 28,101 → 28,129, versão mais recente cua-sdk-v0.4.1 (5 de outubro de 2026).
- **5 de outubro de 2026:** Estrelas 27,988 → 28,101, versão mais recente cua-spaces-v0.7.2 (5 de outubro de 2026).
- **4 de outubro de 2026:** Estrelas 27,887 → 27,988, versão mais recente cua-sdk-v0.3.1 (4 de outubro de 2026).
- **3 de outubro de 2026:** Estrelas 27,875 → 27,887, versão mais recente cua-spacesd-v0.4.1 (3 de outubro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero desenvolver um agente de uso de computador usando a infraestrutura CUA. Ajude-me a configurar a estrutura básica do Python que permitirá que meu agente interaja com aplicativos de desktop em segundo plano, faça cliques do mouse e envie entradas do teclado. Crie um esboço de código de amostra que execute comandos e faça capturas de tela em um ambiente Linux usando o CUA Sandbox SDK.

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

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cua/
