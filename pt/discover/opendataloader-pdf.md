# Prepare dados PDF para IA

OpenDataLoader PDF é um analisador de PDF de código aberto que disponibiliza dados para modelos de inteligência artificial. Este projeto baseado em Java acelera os processos de processamento de dados, automatizando a acessibilidade de documentos PDF.

- ★ 29.447
- Java
- GitHub Trending · 2026-06-04

## Atualizações

- **1 de outubro de 2026:** Estrelas 29,384 → 29,447, versão mais recente v2.5.12 (1 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 29,312 → 29,384, versão mais recente v2.5.11 (22 de setembro de 2026).
- **18 de setembro de 2026:** Estrelas 29,278 → 29,312, versão mais recente v2.5.10 (18 de setembro de 2026).
- **16 de setembro de 2026:** Estrelas 29,080 → 29,278, versão mais recente v2.5.9 (16 de setembro de 2026).

## O que você ganha

- Converte arquivos PDF em formato Markdown, JSON ou HTML para modelos de IA.
- Fornece extração de dados de alta precisão para documentos digitalizados e tabelas complexas.
- Marca automaticamente arquivos PDF de acordo com os padrões de acessibilidade.

## Instalação

**Instalação com Python**

```
pip install -U opendataloader-pdf
```

**Instalação com modo híbrido**

```
pip install -U "opendataloader-pdf[hybrid]"
```

## Execução

**Processo de conversão de PDF**

```
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero analisar os arquivos PDF que possuo usando a ferramenta OpenDataLoader PDF e convertê-los em formatos de dados estruturados (Markdown ou JSON) que posso usar em processos RAG ou LLM. Você pode me ajudar a criar um script para ser executado em meu computador local usando o Python SDK que extrairá tabelas, títulos e texto de meus documentos na ordem de leitura correta? Explique também passo a passo como habilitar o modo híbrido para páginas complexas e personalizar a saída.

## Termos relacionados do glossário

- [PDF Parser](https://trescout.com/pt/dictionary/pdf-parser/)
- [Parser](https://trescout.com/pt/dictionary/parser/)
- [Markdown](https://trescout.com/pt/dictionary/markdown/)
- [SDK](https://trescout.com/pt/dictionary/sdk/)
- [RAG](https://trescout.com/pt/dictionary/rag/)
- [PDF](https://trescout.com/pt/dictionary/pdf/)

- **Para quem é:** Para desenvolvedores que desejam converter documentos PDF em dados estruturados para modelos de IA e para usuários que precisam automatizar a acessibilidade ao PDF.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/opendataloader-project/opendataloader-pdf)
- [Ler em turco →](https://trescout.com/discover/opendataloader-pdf/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-04: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/opendataloader-pdf/
