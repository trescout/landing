# Interactive classroom simulation with multi-AI agents

Developed by Tsinghua University researchers, OpenMAIC brings together multiple artificial intelligence agents in the roles of teacher, student and observer in an interactive classroom environment.

- ★ 39,969
- TypeScript
- GitHub Trending · 2026-08-31

## Updates

- **October 5, 2026:** Stars 39,351 → 39,969, latest release v1.1.3 (October 5, 2026).
- **September 28, 2026:** Stars 39,156 → 39,351, latest release v1.1.2 (September 28, 2026).
- **September 27, 2026:** Stars 25,572 → 39,156, latest release v1.1.1 (September 26, 2026).

## What you get

- Role-based multi-agent architecture: Dynamic interaction of LLM agents in the roles of teacher, questioning student, debater, and summarizer.
- Visual and audio classroom interface: Immersive pedagogical experience with virtual whiteboard, real-time Q&A stream, and text-to-speech (TTS).
- Customizable course curriculum: Instantly create interactive lessons by uploading your own PDF documents or text-based lecture notes.
- One-click simulation launch: Manage complex agent orchestration via a modern web interface without needing technical coding knowledge.
- Open-weight model compatibility: The freedom to connect any AI model you want via Ollama, vLLM, or cloud LLM providers.

## Installation

**Cloning the repository and installing dependencies**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

## Running it

**Starting the development server**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```

## Technical architecture and working principle

- Chat Orchestration Engine: The central controller that manages which agent speaks when, the order of turns, and the context of the discussion.
- Memory and Context Management: Storing shared whiteboard content and student questions in short/long-term memory throughout the lesson.
- Real-Time Streaming via WebSocket: Delivering speech text, emotional expressions, and animations to the frontend interface without latency.

## Multi-agent classroom dynamics and role simulations

- Socratic Debate Environments: Agents with diverse perspectives debate a topic to trigger the user's critical thinking.
- Personalized Tutor Support: Custom AI tutors that automatically adjust the difficulty level based on the user's learning pace.
- Research on Social Interaction Between Agents: Analyzing how large language models collaborate and share information in crowded group environments.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to simulate a Socratic discussion environment by uploading my own lecture notes on the OpenMAIC platform. Could you explain step-by-step how to define the roles of the agents (teacher, curious student, critical questioner) and how to set up this class with a local Ollama model?

## Frequently asked questions

- Do I need a GPU to use OpenMAIC? If you are going to run your own local model (Ollama/vLLM), a GPU is recommended; however, it can be used directly with a standard computer via cloud APIs (OpenAI, Gemini, Groq).
- Can the user participate in the simulation via voice? Yes. Thanks to the WebRTC and voice recognition module, the user can join classroom discussions by speaking into their microphone.
- How many agents can be in a classroom at the same time? In the default configuration, an ideal interaction is achieved with between 3 and 8 agents; larger classes can be set up depending on system resources.
- In which formats can course content be uploaded? Plain text, Markdown, and PDF documents can be imported directly into the system's knowledge base.

## Related dictionary terms

- [Markdown](https://trescout.com/en/dictionary/markdown/)
- [GPU](https://trescout.com/en/dictionary/gpu/)
- [PDF](https://trescout.com/en/dictionary/pdf/)
- [LLM](https://trescout.com/en/dictionary/llm/)
- [API](https://trescout.com/en/dictionary/api/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)

- **Who it is for:** Educators, AI researchers, edtech entrepreneurs, and students.
- **License:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** TypeScript & Next.js Multi-Agent Simulator
- **Platforms:** Web browser, Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/THU-MAIC/OpenMAIC)
- [Read in Turkish →](https://trescout.com/discover/openmaic/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openmaic/
