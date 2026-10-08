# What is Full Text Search?

*Dictionary · Data · Last updated: September 22, 2026*

Full text search is a search method that finds words in the entire content of documents.

## Definition and Word Origin

While simple search looks at the filename, full-text search scans every sentence within the document. It is the most effective way to access information in large archives. Its modern infrastructure is based on the structure called inverted index.

***Analogy:** It's like finding the sentence you're looking for by scanning all the pages of a book instead of just looking at the table of contents.*

## How to Know and Use in Daily Life?

**Search within the site:** Searching for topics on the blog.
**Email:** Finding the message from years ago.
**Code:** Searching for functions in the repository.
**Law:** Browsing the jurisprudence archive.

## Technical Depth and Architecture

The line is:

**Tokenization:** The text is divided into words, the suffixes are reduced to the root.
**Reverse index:** The document in which each word appears is written down in advance.
**Arrangement:** Algorithms like BM25 sort by title and frequency weight.

Example with Postgres:

```
SELECT baslik FROM yazilar
WHERE to_tsvector('turkish', icerik) @@ to_tsquery('turkish', 'yapay & zeka');
```

Vector search is required when semantic similarity (e.g. "car" appears when typing "automobile") is desired. Both can be used together: First, it narrows down the keyword, then it sorts the vector.

## Frequently Mixed Things

It can be confused with a metadata search. Metadata looks at file information (name, date, size), full text search looks at content. Vector search, on the other hand, looks at the meaning, not the word.

## Use in Different Disciplines

**Library:** Scanning entire text instead of receipt catalogue.
**Book:** The index section at the end.
**Archive:** Searching for topics in a collection of newspaper clippings.

## Frequently Asked Questions

**Won't it run too slowly?**

Thanks to the pre-installed index, it gives results in seconds. Scanning without an index would be slow, so an index is a must.

**Does it work on all types of files?**

Yes, in text extractable files. In scanned documents, text is first obtained with OCR.

**Do Turkish suffixes cause problems?**

In qualified analysis, the suffixes are reduced to the root. In an engine with poor language support, the accuracy drops and Turkish-supported configuration is required.

**When should you use vector search?**

When searching for synonyms and concepts. If the keyword cannot be found, vector comes into play, both are powerful together.

## Related terms

- [RAG](https://trescout.com/en/dictionary/rag/)
- [Vector Index](https://trescout.com/en/dictionary/vector-index/)
- [Document Parsing](https://trescout.com/en/dictionary/document-parsing/)

## Related tools

- [Karakeep](https://trescout.com/en/discover/karakeep/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/full-text-search/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/full-text-search/
