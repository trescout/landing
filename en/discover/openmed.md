# Open Source artificial intelligence in healthcare

OpenMed is a platform that brings together open source artificial intelligence models and data sets used in healthcare. Developed for medical-oriented applications, this Python-based library aims to standardize health data processing processes.

- ★ 5,457
- Python
- GitHub Trending · 2026-06-10

## Updates

- **October 8, 2026:** Stars 5,329 → 5,457, latest release v3.0.0 (October 7, 2026).
- **September 16, 2026:** Stars 5,217 → 5,329, latest release v2.5.0 (September 15, 2026).
- **September 5, 2026:** Stars 5,076 → 5,217, latest release v2.3.0 (September 4, 2026).
- **August 21, 2026:** Stars 5,015 → 5,076, latest release v2.2.0 (August 21, 2026).

## What you get

- Extracts structured medical insights from clinical texts.
- Anonymizes personal health data on the device.
- It runs more than 1,000 medical AI models offline.

## Installation

**Basic Setup**

```
pip install "openmed[hf]"
```

**Apple Silicon (MLX) Support**

```
pip install "openmed[mlx]"
```

## Running it

**Simple Analysis with Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to analyze medical text using the OpenMed library. I have Python installed on my device. First of all, I completed the installation with the pip install "openmed[hf]" command. Now, what functions should I call in my Python code to analyze my clinical notes and detect medical terms or personal data (PII) in them? Please create me a simple sample code block on model selection and printing the outputs.

## Related dictionary terms

- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for healthcare professionals and software developers who want to perform privacy-oriented analysis on their own hardware without sending their medical data to cloud services.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/maziyarpanahi/openmed)
- [Read in Turkish →](https://trescout.com/discover/openmed/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-10: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/openmed/
