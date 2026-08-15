# Estrutura TypeScript para agentes de IA

Desenvolvido pela equipe Astro, Flue se destaca como uma estrutura de agente sandbox baseada em TypeScript. Essa estrutura permite que desenvolvedores criem agentes de inteligência artificial em ambientes seguros e isolados.

- ★ 7.625
- TypeScript
- GitHub Trending · 2026-06-06

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
Quero desenvolver um agente de inteligência artificial usando o framework Flue. Como posso definir um fluxo de trabalho usando TypeScript em meu projeto? Especificamente, como posso configurar o modelo com a função createAgent e interagir com meu agente com session.prompt? Usando um exemplo simples de 'hello-world', você pode explicar passo a passo como posso iniciar um agente em tempo de execução e obter resultados?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/flue/
