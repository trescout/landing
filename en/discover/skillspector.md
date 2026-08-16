# Secure AI capabilities

Developed by NVIDIA, SkillSpector is a scanning tool that detects vulnerabilities and malicious patterns in the skill packages of artificial intelligence agents. This Python-based software aims to analyze security risks encountered during the development process of agent-based systems.

- ★ 14,655
- Python
- GitHub Trending · 2026-06-12

## What you get
- AI detects vulnerabilities and malicious patterns in agent capabilities.
- It offers two-stage security scanning with static analysis and optional AI assessment.
- It allows verifying the security of agents with risk scoring and detailed reporting.

## Installation
**Cloning the repository and creating a virtual environment**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Complete the setup**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```


## Running it
**Scan local directory**

```
skillspector scan ./my-skill/
```

**Scan the Git repository**

```
skillspector scan https://github.com/user/my-skill
```


## If you don't write code
I want to security screen an AI agent skill using the SkillSpector tool. How do I use the 'skillspector scan ./my-skill/' command to scan for talent in a local directory and what parameters should I add to the command to save the scan results in 'report.json' in JSON format?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/skillspector/
