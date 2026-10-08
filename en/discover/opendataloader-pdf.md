# Prepare PDF data for AI

OpenDataLoader PDF is an open source PDF parser that makes data available for artificial intelligence models. This Java-based project speeds up data processing processes by automating the accessibility of PDF documents.

- ★ 29,447
- Java
- GitHub Trending · 2026-06-04

## Updates

- **October 1, 2026:** Stars 29,384 → 29,447, latest release v2.5.12 (October 1, 2026).
- **September 27, 2026:** Stars 29,312 → 29,384, latest release v2.5.11 (September 22, 2026).
- **September 18, 2026:** Stars 29,278 → 29,312, latest release v2.5.10 (September 18, 2026).
- **September 16, 2026:** Stars 29,080 → 29,278, latest release v2.5.9 (September 16, 2026).

## What you get

- Converts PDF files to Markdown, JSON or HTML format for AI models.
- Provides high-accuracy data extraction for scanned documents and complex tables.
- Automatically tags PDF files in accordance with accessibility standards.

## Installation

**Installation with Python**

```
pip install -U opendataloader-pdf
```

**Installation with hybrid mode**

```
pip install -U "opendataloader-pdf[hybrid]"
```

## Running it

**PDF conversion process**

```
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to analyze the PDF files I have using the OpenDataLoader PDF tool and convert them into structured data formats (Markdown or JSON) that I can use in RAG or LLM processes. Can you help me create a script to run on my local computer using the Python SDK that will extract tables, headings, and text from my documents in the correct reading order? Also explain step by step how to enable hybrid mode for complex pages and customize the output.

## Related dictionary terms

- [PDF Parser](https://trescout.com/en/dictionary/pdf-parser/)
- [Parser](https://trescout.com/en/dictionary/parser/)
- [Markdown](https://trescout.com/en/dictionary/markdown/)
- [SDK](https://trescout.com/en/dictionary/sdk/)
- [RAG](https://trescout.com/en/dictionary/rag/)
- [PDF](https://trescout.com/en/dictionary/pdf/)

- **Who it is for:** For developers who want to convert PDF documents into structured data for AI models and for users who need to automate PDF accessibility.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/opendataloader-project/opendataloader-pdf)
- [Read in Turkish →](https://trescout.com/discover/opendataloader-pdf/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-04: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/opendataloader-pdf/
