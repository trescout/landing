# What is LSP?

> Language Server Protocol

LSP (Language Server Protocol) is a JSON-RPC-based open protocol that provides standard communication between modern code editors and analysis engines of programming languages.

## 1. Definition and the mathematical problem it solves: M × N complexity
Language Server Protocol (LSP) is a universal protocol developed in 2016 under the leadership of Microsoft (VS Code team), Red Hat and Codenvy, and has become the cornerstone of developer tools today.

## 2. How does LSP work? Protocol architecture and JSON-RPC 2.0
LSP is a JSON-RPC 2.0 messaging protocol between the editor (Client) and the language analysis engine (Server) that usually works over local standard input/output (stdin/stdout) or local sockets (IPC).

## Frequently asked questions
**What does LSP mean and what does it stand for?**
It stands for Language Server Protocol. It is an open protocol that standardizes communication between code editors and the syntax, type checking, and autocompletion engines of programming languages.

**Why does LSP solve the M × N problem?**
In the old model, M × N plug-ins had to be written specifically for each editor for M languages ​​and N editors. With LSP, each language writes a single server and each editor writes a single client, achieving the M + N integration formula.

**How does LSP prevent the editor from slowing down?**
The language's heavy syntax tree (AST) analysis and type parsing are executed in background processes (via JSON-RPC) isolated from the main editor process; so the interface never crashes.

**What is the difference between DAP and LSP?**
While LSP analyzes code writing, code completion and syntax errors; DAP (Debug Adapter Protocol) allows the code to be debugged step by step by setting breakpoints at run time.


## Related terms
- [Agentic Coding Tool](/en/dictionary/agentic-coding-tool/)
- [CLI](/en/dictionary/cli/)
- [Keybindings](/en/dictionary/keybindings/)
- [Code Snippets](/en/dictionary/code-snippets/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [Oh My Pi](/en/discover/oh-my-pi/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/lsp/
