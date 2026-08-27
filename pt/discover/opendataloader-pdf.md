# Prepare dados PDF para IA

OpenDataLoader PDF é um analisador de PDF de código aberto que disponibiliza dados para modelos de inteligência artificial. Este projeto baseado em Java acelera os processos de processamento de dados, automatizando a acessibilidade de documentos PDF.

- ★ 28.831
- Java
- GitHub Trending · 2026-06-04

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
Quero analisar os arquivos PDF que possuo usando a ferramenta OpenDataLoader PDF e convertê-los em formatos de dados estruturados (Markdown ou JSON) que posso usar em processos RAG ou LLM. Você pode me ajudar a criar um script para ser executado em meu computador local usando o Python SDK que extrairá tabelas, títulos e texto de meus documentos na ordem de leitura correta? Explique também passo a passo como habilitar o modo híbrido para páginas complexas e personalizar a saída.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/opendataloader-pdf/
