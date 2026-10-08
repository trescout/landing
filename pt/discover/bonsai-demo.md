# Modelos de IA no dispositivo local

O projeto de demonstração Bonsai fornece um conjunto de ferramentas projetado para simplificar os processos de implantação de modelos de aprendizado de máquina. O software ajuda os desenvolvedores a otimizar seus processos de aplicativos, transformando arquiteturas de modelos complexos em fluxos de trabalho gerenciáveis.

- ★ 2.706
- Shell
- GitHub Trending · 2026-07-17

## Atualizações

- **19 de setembro de 2026:** Estrelas 1,587 → 2,706.

## O que você ganha

- Executa modelos de alto desempenho localmente com baixo uso de memória.
- Ele oferece recursos avançados, como processamento visual e carona.
- Fornece ampla compatibilidade com diferentes arquiteturas de hardware.

## Instalação

**Instalação do macOS e Linux**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Execução

**Iniciando o servidor local**

```
./scripts/start_llama_server.sh    # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero executar modelos de IA em meu dispositivo local usando o projeto bonsai-demo. Depois de clonar o repositório git necessário para instalação, preciso definir as informações do meu token HuggingFace e baixar as dependências e modelos com o comando ./setup.sh. Então, usando o comando ./scripts/start_llama_server.sh, posso levantar o servidor local e interagir com a IA através da porta 8080 através do meu navegador.

## Termos relacionados do glossário

- [Machine Learning](https://trescout.com/pt/dictionary/machine-learning/)
- [Shell](https://trescout.com/pt/dictionary/shell/)
- [Token](https://trescout.com/pt/dictionary/token/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores que desejam executar modelos de IA de alto rendimento em seu hardware nativo.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/PrismML-Eng/Bonsai-demo)
- [Ler em turco →](https://trescout.com/discover/bonsai-demo/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-17: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/bonsai-demo/
