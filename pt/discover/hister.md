# Motor de Busca Privado para Páginas e Arquivos Pessoais

Motor de busca privado com licença AGPLv3 para páginas visitadas e arquivos guardados pelo usuário. Oferece indexação full-text, filtros de consulta avançados e busca semântica opcional.

- ★ 5.740
- Go
- GitHub Trending · 2026-08-25

## Atualizações

- **27 de setembro de 2026:** Estrelas 4,602 → 5,740, versão mais recente v0.20.0 (24 de setembro de 2026).
- **18 de setembro de 2026:** Estrelas 3,574 → 4,602, versão mais recente v0.19.0 (3 de setembro de 2026).
- **4 de setembro de 2026:** Estrelas 3,100 → 3,574, versão mais recente v0.19.0 (3 de setembro de 2026).
- **27 de agosto de 2026:** Estrelas 2,620 → 3,100, versão mais recente v0.18.0 (23 de agosto de 2026).

## Instalação

**Tornar o binário executável**

```
chmod +x hister
```

## Execução

**Iniciar o servidor hister**

```
./hister listen
```

**Acessar interface local**

```
http://127.0.0.1:4433
```

## O que esta ferramenta faz?

O Hister pode rodar localmente ou na infraestrutura que você controla; não exige serviço em nuvem ou telemetria obrigatória. Indexa páginas via extensões Chrome e Firefox, oferece opções de rastreamento de sites e importação do histórico do navegador. Se a busca semântica estiver ativada, o texto do documento é enviado ao endpoint de embeddings selecionado.

## Para quem é?

Quem quer consultar páginas web e arquivos pessoais em uma infraestrutura de busca sob seu controle.

## O que não esperar

Cenários que exigem serviço em nuvem obrigatório ou telemetria, ou fluxos de indexação do navegador que não permitem enviar conteúdo ao servidor Hister configurado.

## Destaques

- Opera localmente ou em infraestrutura controlada, sem telemetria ou serviço em nuvem obrigatório
- Consultas com full-text, filtros por campo, frases, curingas, negações e prioridades
- Busca opcional semântica com clientes web, terminal, TUI, CLI e MCP

## Primeiro fluxo de uso

1. Baixe o binário apropriado para sua plataforma e torne-o executável no Linux ou macOS
2. Inicie o servidor Hister em modo de escuta local
3. Abra a interface web local
4. Instale a extensão do Chrome ou Firefox e selecione as páginas a serem indexadas

## Início seguro

A extensão do navegador envia o conteúdo indexado ao servidor Hister configurado, exceto pelo download de favicons. A busca semântica opcional envia o texto do documento ao endpoint de embeddings selecionado.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Abra a interface local, indexe as páginas selecionadas com a extensão do navegador e verifique as pesquisas usando filtros de consulta.

## Termos relacionados do glossário

- [TUI](https://trescout.com/pt/dictionary/tui/)
- [Binary](https://trescout.com/pt/dictionary/binary/)
- [MCP](https://trescout.com/pt/dictionary/mcp/)
- [Terminal](https://trescout.com/pt/dictionary/terminal/)
- [CLI](https://trescout.com/pt/dictionary/cli/)

## Links

- [Repositório no GitHub →](https://github.com/asciimoo/hister)
- [Início rápido →](https://hister.org/docs/quickstart)
- [README de privacidade e uso →](https://github.com/asciimoo/hister)
- [Fluxo de uso →](https://hister.org/posts/how-i-use-hister)
- [Ler em turco →](https://trescout.com/discover/hister/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-25: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/hister/
