# Memória em camadas para agentes de IA

TencentDB Agent Memory oferece uma solução de memória de longo prazo totalmente local para agentes de inteligência artificial com um processo de quatro estágios. Ele executa operações de armazenamento e recuperação de dados sem a necessidade de interfaces de programação de aplicativos (APIs) externas.

- ★ 27.855
- TypeScript
- GitHub Trending · 2026-07-09

## Atualizações

- **9 de outubro de 2026:** Estrelas 27,396 → 27,855, versão mais recente v2.0.2 (9 de outubro de 2026).
- **28 de setembro de 2026:** Estrelas 26,048 → 27,396, versão mais recente v2.0.1 (25 de agosto de 2026).
- **7 de setembro de 2026:** Estrelas 24,804 → 26,048, versão mais recente v2.0.1 (25 de agosto de 2026).
- **27 de agosto de 2026:** Estrelas 23,144 → 24,804, versão mais recente v2.0.1 (25 de agosto de 2026).

## O que você ganha

- Reduz o uso de tokens em até 61%
- Aumenta a taxa de sucesso em tarefas complexas
- Armazena dados em uma estrutura simbólica e em camadas

## Instalação

**Instalação do pacote**

```
mkdir -p ~/.memory-tencentdb
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest --omit=dev
cp -r node_modules/@tencentdb-agent-memory/memory-tencentdb \
      ~/.memory-tencentdb/tdai-memory-openclaw-plugin
rm -rf "$TEMP_DIR"
```

**Instalando dependências**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npm install --omit=dev
npm install tsx
```

## Execução

**Iniciando o servidor**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
  npx tsx src/gateway/server.ts
```

**Verifique a conexão**

```
curl http://127.0.0.1:8420/health
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Configure a memória de longo prazo do meu agente de IA usando TencentDB Agent Memory. Em vez de uma pilha vetorial plana de dados, use gráficos simbólicos Mermaid para tarefas de curto prazo e uma pirâmide de memória em camadas L0-L3 para experiências de longo prazo. Permita que o agente armazene conversas passadas, fatos atômicos e preferências do usuário nesta estrutura hierárquica e recupere-os sempre que necessário com rastreabilidade total via node_id.

## Termos relacionados do glossário

- [Long-term Memory](https://trescout.com/pt/dictionary/long-term-memory/)
- [Mermaid](https://trescout.com/pt/dictionary/mermaid/)
- [Memory](https://trescout.com/pt/dictionary/memory/)
- [Token](https://trescout.com/pt/dictionary/token/)
- [Agent](https://trescout.com/pt/dictionary/agent/)
- [API](https://trescout.com/pt/dictionary/api/)

- **Para quem é:** É para desenvolvedores que não desejam que seus agentes de IA esqueçam o contexto e buscam obter resultados mais consistentes reduzindo custos de tokens.

## Links

- [Repositório no GitHub →](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [Ler em turco →](https://trescout.com/discover/tencentdb-agent-memory/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-09: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/tencentdb-agent-memory/
