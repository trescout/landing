# TreScout Model Context Protocol (MCP) Server

Official Model Context Protocol (MCP) server for **[TreScout](https://trescout.com)**. Connect your Claude Desktop, Cursor, Antigravity, or custom AI Agents directly to 470+ curated open-source projects, 530+ software & AI dictionary definitions, and daily technology intelligence reports.

---

## 🚀 Capabilities & Tools

| Tool | Description |
| :--- | :--- |
| `search_tools` | Search 470+ open-source tools & AI repositories by query, tag, language, or popularity. |
| `get_tool_detail` | Get complete metadata, installation commands, and analysis for a given tool slug. |
| `lookup_term` | Query TreScout technical dictionary for AI, cloud, and engineering concepts with multilingual explanations. |
| `get_daily_report` | Fetch structured overview, editorial insights, and highlights from any daily TreScout report. |
| `list_recent_reports` | List recent tech reports published on TreScout. |

---

## 📦 Setup & Configuration

### 1. Claude Desktop
Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "trescout": {
      "command": "node",
      "args": [
        "/absolute/path/to/trescout-landing/packages/mcp/index.js"
      ]
    }
  }
}
```

### 2. Cursor
Go to **Settings → Features → MCP Servers → Add New MCP Server**:
* **Name:** `trescout`
* **Type:** `command`
* **Command:** `node /absolute/path/to/trescout-landing/packages/mcp/index.js`

---

## 💡 Example Prompts

Once configured, you can prompt your AI:
* *"TreScout'a sor: Bugün GitHub'da öne çıkan en popüler Rust ve AI projeleri hangileri?"*
* *"What is 'prompt-as-code' according to TreScout dictionary?"*
* *"Find open-source CLI tools for web scraping on TreScout."*
* *"Summarize today's TreScout daily tech report."*

---

## 🔒 Privacy & Local-First
* **Zero Telemetry / Zero PII:** Runs completely locally reading from static catalogs and reports.
* **Fast:** Zero external API latency.
