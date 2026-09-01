# Plataforma Aberta de Desenvolvimento para Pesquisa de Modelos de Base

Programa de pesquisa, plataforma de software e comunidade para investigar e desenvolver modelos de base. Documenta o escopo desde o processamento de dados até pré-treinamento, fine-tuning e avaliação.

- ★ 3.089
- Python
- GitHub Trending · 2026-08-25

## Instalação
**Clonar repositório oficial**

```
git clone https://github.com/marin-community/marin.git
```

**Criar ambiente Python**

```
uv venv --python 3.12
```

**Instalar dependências**

```
uv sync --all-packages
```


## Execução
**Executar smoke test na CPU**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```


## O que esta ferramenta faz?
Executa experimentos como passos dependentes em ordem topológica. O experimento inicial oficial demonstra tokenização do TinyStories e o treinamento de um pequeno modelo de linguagem; a abordagem de desenvolvimento aberto documenta código, dados, decisões e experimentos malsucedidos.

## Para quem é?
Equipes que pesquisam curadoria, transformação, filtragem de dados, tokenização, treinamento de modelos e avaliação.

## O que não esperar
Trabalhos de desenvolvimento de aplicações simples que não fazem parte de pesquisa de modelos de base ou para quem não quer configurar o ambiente Python e de desenvolvimento necessário.

## Destaques
- Cobertura de pesquisa do processamento de dados ao pré-treinamento, fine-tuning e avaliação
- Fluxo de trabalho de experimentos que executa passos dependentes em ordem topológica
- Documentação aberta que inclui experimentos fracassados e decisões de desenvolvimento

## Primeiro fluxo de uso
- Clone o repositório oficial e crie um ambiente virtual Python 3.12 ou superior
- Sincronize dependências com uv
- Configure a variável de ambiente MARIN_PREFIX
- Execute o teste rápido (smoke test) offline do TinyStories na CPU

## Início seguro

## Primeiro prompt
Execute como verificação inicial o fluxo TinyStories offline treinando um pequeno modelo na CPU.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Documentação de instalação →
- Primeiro experimento →
- README oficial →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/marin/
