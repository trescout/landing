# Capacidades seguras de IA

Desenvolvido pela NVIDIA, o SkillSpector é uma ferramenta de varredura que detecta vulnerabilidades e padrões maliciosos nos pacotes de habilidades de agentes de inteligência artificial. Este software baseado em Python visa analisar os riscos de segurança encontrados durante o processo de desenvolvimento de sistemas baseados em agentes.

- ★ 15.024
- Python
- GitHub Trending · 2026-06-12

## O que você ganha
- A IA detecta vulnerabilidades e padrões maliciosos nas capacidades dos agentes.
- Oferece verificação de segurança em dois estágios com análise estática e avaliação de IA opcional.
- Permite verificar a segurança dos agentes com pontuação de risco e relatórios detalhados.

## Instalação
**Clonando o repositório e criando um ambiente virtual**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Conclua a configuração**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```


## Execução
**Digitalizar o diretório local**

```
skillspector scan ./my-skill/
```

**Digitalize o repositório Git**

```
skillspector scan https://github.com/user/my-skill
```


## Se você não programa
Quero fazer a triagem de segurança de uma habilidade de agente de IA usando a ferramenta SkillSpector. Como uso o comando 'skillspector scan ./my-skill/' para procurar talentos em um diretório local e quais parâmetros devo adicionar ao comando para salvar os resultados da verificação em 'report.json' no formato JSON?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/skillspector/
