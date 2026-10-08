# Estrutura TypeScript para agentes de IA

Desenvolvido pela equipe Astro, Flue se destaca como uma estrutura de agente sandbox baseada em TypeScript. Essa estrutura permite que desenvolvedores criem agentes de inteligência artificial em ambientes seguros e isolados.

- ★ 8.393
- TypeScript
- GitHub Trending · 2026-06-06

## Atualizações

- **29 de setembro de 2026:** Estrelas 8,374 → 8,393, versão mais recente @flue/cli@2.2.2 (28 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 8,295 → 8,374, versão mais recente @flue/cli@2.1.1 (23 de setembro de 2026).
- **19 de setembro de 2026:** Estrelas 8,255 → 8,295, versão mais recente @flue/cli@2.1.0 (18 de setembro de 2026).
- **17 de setembro de 2026:** Estrelas 8,244 → 8,255, versão mais recente @flue/cli@2.0.8 (16 de setembro de 2026).

## O que você ganha

- Criação de agentes programáveis ​​e headless baseados em TypeScript.
- Ambiente de trabalho rápido e escalável com sandbox virtual.
- Implantação versátil em processos Node.js, Cloudflare e CI/CD.

## Instalação

**Servidor de desenvolvimento Node.js.**

```
flue dev --target node
```

**compilação**

```
flue build --target node          # Node.js server (single bundled .mjs)
flue build --target cloudflare    # Cloudflare Workers + Durable Objects
```

## Execução

**Executando o fluxo de trabalho Hello World**

```
flue run hello --target node \
  --payload '{"text": "Hello world", "language": "French"}'
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero desenvolver um agente de inteligência artificial usando o framework Flue. Como posso definir um fluxo de trabalho usando TypeScript em meu projeto? Especificamente, como posso configurar o modelo com a função createAgent e interagir com meu agente com session.prompt? Usando um exemplo simples de 'hello-world', você pode explicar passo a passo como posso iniciar um agente em tempo de execução e obter resultados?

## Termos relacionados do glossário

- [Sandbox Agent Framework](https://trescout.com/pt/dictionary/sandbox-agent-framework/)
- [Prompt](https://trescout.com/pt/dictionary/prompt/)
- [CI/CD](https://trescout.com/pt/dictionary/ci-cd/)
- [Sandbox](https://trescout.com/pt/dictionary/sandbox/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Framework](https://trescout.com/pt/dictionary/framework/)

- **Para quem é:** É adequado para desenvolvedores de software que desejam desenvolver seus próprios agentes autônomos de inteligência artificial com TypeScript e executá-los em diferentes plataformas.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/withastro/flue)
- [Ler em turco →](https://trescout.com/discover/flue/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-06: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/flue/
