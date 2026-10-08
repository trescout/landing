# Sistema de Conhecimento Local para Claude Code

Sistema de conhecimento com prioridade local para Claude Code e servidores Agent Skills compatíveis. Converte materiais de referência em páginas interligadas do Obsidian que citam as fontes.

- ★ 14.822
- Python
- GitHub Trending · 2026-08-25

## Atualizações

- **11 de setembro de 2026:** Estrelas 14,727 → 14,822, versão mais recente v2.2.0 (10 de setembro de 2026).
- **8 de setembro de 2026:** Estrelas 13,706 → 14,727, versão mais recente v2.1.1 (25 de agosto de 2026).
- **27 de agosto de 2026:** Estrelas 12,404 → 13,706, versão mais recente v2.1.1 (25 de agosto de 2026).

## Instalação

**Adicionar o marketplace do Claude Code**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Instalar o plugin claude-obsidian**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Criar plano para vault separado**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```

## Execução

**Verificar instalação do plugin**

```
claude plugin list
```

**Iniciar fluxo do wiki**

```
/claude-obsidian:wiki
```

## O que esta ferramenta faz?

Organiza conteúdo de pesquisa com livros de fontes e alegações, páginas conectadas e mapas de conhecimento. Agentes paralelos geram rascunhos e um orquestrador aplica alterações aprovadas por meio de transações reversíveis.

## Para quem é?

Pessoas que querem criar uma base de conhecimento Obsidian local e referenciada para uso com Claude Code.

## O que não esperar

Registro automático de transcrições, sincronização em nuvem, garantia de veracidade ou substituição de backup e controle de versão.

## Destaques

- Operação local por padrão e abordagem de saída de rede explícita
- Páginas interligadas com citação de fontes usando livros de fontes e alegações
- Aplicação de alterações aprovadas via transações reversíveis

## Primeiro fluxo de uso

1. Clone o repositório e prepare um ambiente Python 3.11 ou superior
2. Crie um plano inicial para um vault separado e revise o plano JSON
3. Verifique o valor approved_plan_sha256 e confirme todo o procedimento
4. Abra o vault no Obsidian e execute Claude Code com o plugin local
5. Inicie o fluxo wiki usando etapas para adicionar fontes, consultar e salvar explicitamente

## Início seguro

O sistema não é uma fonte de verdade única. Use backup e controle de versão para seus dados; revise a saída de rede e o plano aplicado.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Inicie um fluxo wiki local no Obsidian associando fontes aos livros de fontes e alegações.

## Termos relacionados do glossário

- [Agent Skills](https://trescout.com/pt/dictionary/agent-skills/)
- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [Agent](https://trescout.com/pt/dictionary/agent/)

## Links

- [Repositório no GitHub →](https://github.com/AgriciDaniel/claude-obsidian)
- [Guia de instalação →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [README oficial →](https://github.com/AgriciDaniel/claude-obsidian)
- [Ler em turco →](https://trescout.com/discover/claude-obsidian/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-25: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/claude-obsidian/
