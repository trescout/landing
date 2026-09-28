# Turn your personal computer into a local AI server

Open-source Osmantic/ODS allows you to build local large language model inference running on your personal hardware, vector search-based RAG pipelines, and autonomous agent workflows.

- ★ 6,854
- Python
- GitHub Trending · 2026-08-31

## What you get
- Complete data privacy and local execution: Secure AI operations on local GPU and CPU without sending your data to external cloud servers.
- Integrated RAG (Retrieval-Augmented Generation): Vectorize your personal notes, company documents, and code repositories to perform instant semantic search.
- Multimodal capabilities: Bringing text generation, speech recognition (Whisper), speech synthesis, and image generation together under one roof.
- OpenAI-compatible local API: Redirect your existing AI clients and tools to your local ODS server with a single URL change.
- Comprehensive agent orchestration: Smart agent chains that call local tools and autonomously solve multi-step tasks.

## Installation
**Cloning the repository and setting up the environment**

```
git clone https://github.com/Osmantic/ODS.git
cd ODS
pip install -e .
```


## Running it
**Starting the local AI server**

```
python -m ods.server --port 8000
# Web paneline http://localhost:8000 adresinden erişin
```


## Technical architecture and working principle
- Local Inference Engine (llama.cpp & vLLM): Fast loading and execution of models in GGUF and pure GPU formats with a minimum memory footprint.
- Embedded Vector Database: Chunking and indexing documents with lightweight vector storage based on ChromaDB and SQLite.
- Task Queue and Agent State Machine: Asynchronous handlers managing multi-step queries and tool-calling flows.

## Local RAG workflows and custom agent pipelines
- Working with Confidential Company Documents: Query contracts, financial statements, and internal correspondence using local RAG without moving them to the cloud.
- Local Code Analysis and Development Assistant: Index your custom software projects to provide local AI code completion on VS Code or Cursor.
- Autonomous Data Processing Agents: Define background tasks that read, summarize, and convert the formats of reports in the local file system.

## If you don't write code
Could you explain with code and terminal steps how to set up the ODS server on my personal computer to import my company's PDF documents into a local vector database, and then perform RAG Q&A queries based on these documents using a local Llama 3 model?

## Frequently asked questions
- Does it work completely offline without an internet connection? Yes. Once the necessary model weights are downloaded, ODS can operate entirely offline in air-gapped environments without requiring any network connection.
- Which model formats does it support? It supports all open models in GGUF format (Llama 3, Mistral, Qwen, DeepSeek) and raw HuggingFace weights.
- Is there a web interface? Yes. ODS comes with a built-in web panel where you can manage models, upload files, and start chat sessions.
- Does it work with just the CPU without a GPU? Yes. Thanks to the llama.cpp core, it can run with high efficiency purely on the CPU using AVX2/AVX-512 instruction sets.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ods/
