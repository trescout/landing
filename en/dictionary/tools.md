# Tools: Developer tooling, Function Calling, and MCP


**Category:** Dev  

**Last updated:** 2026-09-19


Tools in computing refer to two pivotal domains: specialized software utilities that accelerate developer productivity, and structured interfaces enabling AI models to execute code, query APIs, and interact with the physical world.


## Etymology and the Tool Metaphor in Computing
The word *tool* originates from Old English *tol* (an instrument for making or doing). In human history, toolmaking marked the boundary between biological constraints and cultural amplification. In software, Ken Thompson and Doug McIlroy shaped the Unix philosophy: write programs that do one thing well and compose them together through text streams.

## 1. Developer Tools (DevTools)
Modern software engineering advances through layers of developer tooling:
- **Compilers & Build Systems:** Compilers (GCC, Clang, rustc) and build tools (Make, Vite, Turborepack) transform human abstractions into high-speed machine instructions.
- **Debuggers & Profilers:** GDB, LLDB, and browser DevTools inspect call stacks, memory allocations, and network latency in real time.
- **Static Analysis & Linters:** Tools like ESLint, Ruff, and SonarQube enforce code standards and intercept defects before compilation.

## 2. The Turning Point in AI: Tool Use and Function Calling
Traditional large language models (LLMs) are probabilistic text predictors trapped inside static weights. Tool use bridges four critical limitations:
1. **Real-time Information:** Querying live web search APIs rather than relying on stale training cutoffs.
2. **Mathematical Precision:** Offloading arithmetic to Python runtimes rather than guessing token probabilities.
3. **External Action:** Sending emails, dispatching webhooks, or updating database rows.
4. **System Observability:** Querying file trees and git histories to inspect running services.

## 3. Model Context Protocol (MCP) as a Universal Standard
As AI agents proliferated, custom tool schemas created severe integration fragmentation. Anthropic introduced the **Model Context Protocol (MCP)** as an open standard (analogous to the Language Server Protocol for IDEs). MCP defines a uniform JSON-RPC communication bridge between AI host clients and backend tool servers.

## 4. Dual-Use Tools in Cybersecurity
In security, software tools serve offensive and defensive purposes identically:
- **Penetration Testing & Auditing:** Nmap (port scanning), Wireshark (packet analysis), and Burp Suite (web security) help engineers identify vulnerabilities before malicious adversaries exploit them.
- **Automated Exploit Defense:** Dynamic fuzzers (AFL++) continuously bombard software interfaces with randomized inputs to discover zero-day memory corruptions.

## Analogy
A large language model without tools is like a brilliant scholar locked inside a windowless library room; equipping it with tools gives it hands, a calculator, a telephone, and access to the outside world.

## Frequently asked questions

**What does tool mean in the context of modern AI?**  
In AI, a tool is an external function, API endpoint, or executable script that an LLM can invoke via structured JSON arguments to take real actions or fetch live data.

**What is the Model Context Protocol (MCP)?**  
MCP is an open standard that decouples AI models from data sources and tools, providing a plug-and-play architecture for LLM assistants.

**How does an LLM decide which tool to use?**  
The model inspects JSON descriptions and parameter schemas for available tools, selects the most relevant function, and outputs structured arguments that the host environment executes.

## Related terms
- [MCP](/en/dictionary/mcp/)
- [AI Agent](/en/dictionary/ai-agent/)
- [Plugin](/en/dictionary/plugin/)
- [SDK](/en/dictionary/sdk/)

## Related tools
- [ECC](/en/discover/ecc/)
- [System Prompts and Models of AI Tools](/en/discover/system-prompts-and-models-of-ai-tools/)
- [Claude Plugins Official](/en/discover/claude-plugins-official/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/tools/
