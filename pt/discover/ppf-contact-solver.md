# Gerenciar contatos em simulações de física

O PPF Contact Solver, como mecanismo de física da ZOZO, foi projetado para resolver contatos entre tecido, sólido e corda em simulações baseadas em física. Aumenta a consistência física em simulações calculando a interação de diferentes geometrias. Também pode ser executado remotamente graças ao plug-in Blender.

- ★ 4.404
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## O que isso faz?
- Ele realiza simulações realistas de tecidos, objetos sólidos e cordas.
- Aumenta a consistência física em simulações.
- Pode ser operado remotamente via Blender.
- É uma solução orientada para a investigação (mecanismo de física próprio da ZOZO).

## Para quem não é adequado?
Este não é um aplicativo de usuário final. É necessário conhecimento de programação e simulação física para usar; Apela mais para o campo gráfico/pesquisa.

## Como instalar, como usar?
**Inicie com Docker (requer GPU NVIDIA)**

```
docker run --rm -it --name ppf-contact-solver --gpus all \
  -p 8080:8080 -p 9090:9090 -e WEB_PORT=8080 \
  ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```


## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ppf-contact-solver/
