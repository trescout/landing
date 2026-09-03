# Controle de versão para agentes de inteligência artificial

Atlas é um sistema de controle de versão (source control) para agentes de inteligência artificial usados em processos de desenvolvimento de software. Ele permite monitorar e consultar as alterações feitas por múltiplos agentes de codificação a partir de um único centro.

- ★ 3.058
- Rust
- GitHub Trending · 2026-09-03

## O que você ganha
- Monitora as alterações feitas por diferentes agentes de codificação a partir de um único centro.
- Permite continuar de onde você parou nas transições de tarefas com uma memória compartilhada entre agentes.
- Associa cada alteração de código à justificativa e aos comandos do agente que realizou a alteração.

## Instalação
**Instalação das dependências necessárias**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Compilação da aplicação a partir do código-fonte**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```


## Se você não programa
Você é um assistente de desenvolvimento de software. Use o Atlas para registrar todas as alterações de código que você fizer, as decisões tomadas e as ferramentas utilizadas, juntamente com o histórico da sessão. Se precisar alternar entre diferentes agentes, como o Claude Code ou o Codex enquanto trabalha, leia os planos e notas de arquitetura da sessão anterior a partir da memória compartilhada. Mantenha o contexto chamando arquivos, pastas ou sessões anteriores na base de código com o símbolo '@' e documente o motivo de cada alteração feita, juntamente com as justificativas da sessão correspondente.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/atlas/
