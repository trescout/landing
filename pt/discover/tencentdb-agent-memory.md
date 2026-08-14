# Memória em camadas para agentes de IA

TencentDB Agent Memory oferece uma solução de memória de longo prazo totalmente local para agentes de inteligência artificial com um processo de quatro estágios. Ele executa operações de armazenamento e recuperação de dados sem a necessidade de interfaces de programação de aplicativos (APIs) externas.

- ★ 20.021
- TypeScript
- GitHub Trending · 2026-07-09

## Atualizar
- 12 de agosto de 2026: Star 18.953 → 20.021, versão mais recente v2.0.0 (3 de agosto de 2026).
- 10 de agosto de 2026: Star 17.887 → 18.953, versão mais recente v2.0.0 (3 de agosto de 2026).
- 8 de agosto de 2026: Star 16.699 → 17.887, versão mais recente v2.0.0 (3 de agosto de 2026).
- 7 de agosto de 2026: Star 15.363 → 16.699, versão mais recente v2.0.0 (3 de agosto de 2026).

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
Configure a memória de longo prazo do meu agente de IA usando TencentDB Agent Memory. Em vez de uma pilha vetorial plana de dados, use gráficos simbólicos Mermaid para tarefas de curto prazo e uma pirâmide de memória em camadas L0-L3 para experiências de longo prazo. Permita que o agente armazene conversas passadas, fatos atômicos e preferências do usuário nesta estrutura hierárquica e recupere-os sempre que necessário com rastreabilidade total via node_id.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/tencentdb-agent-memory/
