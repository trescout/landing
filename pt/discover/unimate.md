# Anime diferentes esqueletos de personagens com um único modelo

UniMate é uma tecnologia de animação que permite animar diferentes estruturas esqueléticas através de um único modelo. Apresentado na SIGGRAPH Asia 2026, este trabalho visa padronizar os processos de animação de personagens.

- ★ 1.166
- Python
- GitHub Trending · 2026-10-02

## O que você ganha
- Anima diferentes estruturas esqueléticas, como humanos, animais e objetos, com um único modelo de inteligência artificial.
- Oferece suporte abrangente à animação com o conjunto de dados em larga escala UniML3D.
- Acelera o fluxo de trabalho ao padronizar os processos de animação de personagens.

## Instalação
**Preparação do ambiente**

```
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools<81"
pip install -r requirements.txt --no-build-isolation
```


## Execução
**Criação de animação de exemplo**

```
python -m unimate.inference.sample \
    --exp_dir outputs/uniml3d_60frames_graph_adaln \
    --test_cases_json test_cases.json \
    --num_repetitions 3
```


## Se você não programa
Como posso animar meus modelos de personagens com diferentes estruturas esqueléticas em um formato padrão usando o projeto UniMate? Explique passo a passo o processo de criação de animação utilizando o conjunto de dados UniML3D e os pontos de verificação pré-treinados oferecidos pelo projeto.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/unimate/
