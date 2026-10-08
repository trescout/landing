# Capacidades seguras de IA

Desenvolvido pela NVIDIA, o SkillSpector é uma ferramenta de varredura que detecta vulnerabilidades e padrões maliciosos nos pacotes de habilidades de agentes de inteligência artificial. Este software baseado em Python visa analisar os riscos de segurança encontrados durante o processo de desenvolvimento de sistemas baseados em agentes.

- ★ 19.418
- Python
- GitHub Trending · 2026-06-12

## Atualizações

- **5 de outubro de 2026:** Estrelas 18,381 → 19,418, versão mais recente v2.12.0 (23 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 16,828 → 18,381, versão mais recente v2.12.0 (23 de setembro de 2026).
- **10 de setembro de 2026:** Estrelas 16,595 → 16,828, versão mais recente v2.11.2 (9 de setembro de 2026).
- **8 de setembro de 2026:** Estrelas 16,471 → 16,595, versão mais recente v2.11.1 (7 de setembro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero fazer a triagem de segurança de uma habilidade de agente de IA usando a ferramenta SkillSpector. Como uso o comando 'skillspector scan ./my-skill/' para procurar talentos em um diretório local e quais parâmetros devo adicionar ao comando para salvar os resultados da verificação em 'report.json' no formato JSON?

## Termos relacionados do glossário

- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores de software que desenvolvem agentes de IA e desejam analisar os riscos de segurança dos pacotes de recursos que usam.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/NVIDIA/SkillSpector)
- [Ler em turco →](https://trescout.com/discover/skillspector/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-12: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/skillspector/
