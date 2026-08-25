# Sistema de Conhecimento Local para Claude Code

Sistema de conhecimento com prioridade local para Claude Code e servidores Agent Skills compatíveis. Converte materiais de referência em páginas interligadas do Obsidian que citam as fontes.

- ★ 12.404
- Python
- GitHub Trending · 2026-08-25

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
- Clone o repositório e prepare um ambiente Python 3.11 ou superior
- Crie um plano inicial para um vault separado e revise o plano JSON
- Verifique o valor approved_plan_sha256 e confirme todo o procedimento
- Abra o vault no Obsidian e execute Claude Code com o plugin local
- Inicie o fluxo wiki usando etapas para adicionar fontes, consultar e salvar explicitamente

## Início seguro

## Primeiro prompt
Inicie um fluxo wiki local no Obsidian associando fontes aos livros de fontes e alegações.

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


## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Guia de instalação →
- README oficial →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/claude-obsidian/
