# Security testing for AI models

YuJunZhiXue/dsh-purge is a JavaScript tool aimed at bypassing security restrictions (jailbreaking) using customizable prompts for different AI models. The project allows users to define their own prompts for various models and focuses on local models by default.

- ★ 10,352
- JavaScript
- GitHub Trending · 2026-10-19

## Updates

- **October 27, 2026:** Stars 9,063 → 10,352, latest release v1.1.79 (October 26, 2026).
- **October 26, 2026:** Stars 7,485 → 9,063, latest release v1.1.78 (October 24, 2026).
- **October 24, 2026:** Stars 7,355 → 7,485, latest release v1.1.78 (October 24, 2026).
- **October 24, 2026:** Stars 6,673 → 7,355, latest release v1.1.77 (October 23, 2026).

## What you get

- You can test security and auditing rules on the AI runtime environment DeepSeek Harness in a local environment.
- You can directly inspect model responses and system filters by defining custom prompts for different models.
- You can manage system patches applied via the developer interface and revert to the previous state at any time.

## Installation

**Cloning the repository to the plugin directory**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**Switching to the relevant profile directory and dependenci**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Running it

**Verify code syntax**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to install and verify the dsh-purge plugin to perform a security evaluation on the AI runtime environment DeepSeek Harness. First, run the command git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" to download the repository using the version control software Git. Then, complete the step cd "$DSH_HOME/profiles/web" # 或 profiles/desktop\npnpm install to install the profile dependencies using the package manager pnpm. As the final step, run the command node --check lib/index.js\nnode --check lib/core.js\nnode --check lib/rewind.js\nnode --check lib/skills.js\nnode --check client.js to check the files using the JavaScript runtime Node.js.

Repository: https://github.com/YuJunZhiXue/dsh-purge. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Jailbreak](https://trescout.com/en/dictionary/jailbreak/)
- [Harness](https://trescout.com/en/dictionary/harness/)
- [Clone](https://trescout.com/en/dictionary/clone/)
- [AI Skills](https://trescout.com/en/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for researchers who want to inspect the safety boundaries and system filters of AI models in their own local environment.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/YuJunZhiXue/dsh-purge)
- [Read in Turkish →](https://trescout.com/discover/dsh-purge/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-19: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/dsh-purge/
