# Gerenciar contatos em simulações de física

O PPF Contact Solver, como mecanismo de física da ZOZO, foi projetado para resolver contatos entre tecido, sólido e corda em simulações baseadas em física. Aumenta a consistência física em simulações calculando a interação de diferentes geometrias. Também pode ser executado remotamente graças ao plug-in Blender.

- ★ 4.514
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## Atualizações

- **1 de outubro de 2026:** Estrelas 4,513 → 4,514, versão mais recente addon-2026-10-01-2043 (1 de outubro de 2026).
- **1 de outubro de 2026:** Estrelas 4,507 → 4,513, versão mais recente addon-2026-10-01-0946 (1 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 4,508 → 4,507, versão mais recente addon-2026-09-27-2158 (27 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 4,490 → 4,508, versão mais recente addon-2026-09-22-2204 (22 de setembro de 2026).

## Instalação

**Iniciar container GPU**

```
docker run --rm -it --name ppf-contact-solver --gpus all -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEB_PORT=8080 ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```

## O que isso faz?

- Ele realiza simulações realistas de tecidos, objetos sólidos e cordas.
- Aumenta a consistência física em simulações.
- Pode ser operado remotamente via Blender.
- É uma solução orientada para a investigação (mecanismo de física próprio da ZOZO).

## Para quem não é adequado?

Este não é um aplicativo de usuário final. É necessário conhecimento de programação e simulação física para usar; Apela mais para o campo gráfico/pesquisa.

## Como instalar, como usar?

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Execute o solucionador de contatos físicos ppf-contact-solver da ZOZO com Docker (GPU NVIDIA necessária): execute o seguinte comando docker, abra http://localhost:8080 no navegador e experimente os exemplos prontos do JupyterLab.

## Termos relacionados do glossário

- [Container](https://trescout.com/pt/dictionary/container/)
- [Localhost](https://trescout.com/pt/dictionary/localhost/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Usuários técnicos, pesquisadores que realizam simulações gráficas/físicas
- **Dificuldade:** Foco em pesquisa/técnica avançada
- **O que oferece:** Solução de contato de tecido/sólido/corda
- **Funciona:** Plug-in Python + Blender
- **Taxa:** Gratuito · código aberto (Apache-2.0)

**Licença:** Apache-2.0 · você pode usá-lo livremente, modificá-lo, fazer uso comercial (também inclui proteção de patente).

## Links

- [Repositório no GitHub →](https://github.com/st-tech/ppf-contact-solver)
- [Ler em turco →](https://trescout.com/discover/ppf-contact-solver/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-05-26: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ppf-contact-solver/
