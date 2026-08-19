# Controle computacional para agentes de inteligência artificial

CUA fornece uma infraestrutura de código aberto para agentes de inteligência artificial com capacidade de computador. Ele reúne sandbox, kit de desenvolvimento de software (SDK) e ferramentas de benchmark sob o mesmo teto com o objetivo de treinar e avaliar agentes que podem controlar sistemas operacionais de desktop.

- ★ 21.461
- HTML
- GitHub Trending · 2026-06-16

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
Quero desenvolver um agente de uso de computador usando a infraestrutura CUA. Ajude-me a configurar a estrutura básica do Python que permitirá que meu agente interaja com aplicativos de desktop em segundo plano, faça cliques do mouse e envie entradas do teclado. Crie um esboço de código de amostra que execute comandos e faça capturas de tela em um ambiente Linux usando o CUA Sandbox SDK.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cua/
