# Prepare PDF data for AI

OpenDataLoader PDF is an open source PDF parser that makes data available for artificial intelligence models. This Java-based project speeds up data processing processes by automating the accessibility of PDF documents.

- ★ 28,831
- Java
- GitHub Trending · 2026-06-04

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
I want to analyze the PDF files I have using the OpenDataLoader PDF tool and convert them into structured data formats (Markdown or JSON) that I can use in RAG or LLM processes. Can you help me create a script to run on my local computer using the Python SDK that will extract tables, headings, and text from my documents in the correct reading order? Also explain step by step how to enable hybrid mode for complex pages and customize the output.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/opendataloader-pdf/
