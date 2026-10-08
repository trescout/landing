# Mehrschichtiger Speicher für KI-Agenten

TencentDB Agent Memory bietet eine vollständig lokale Langzeitspeicherlösung für Agenten der künstlichen Intelligenz mit einem vierstufigen Prozess. Es führt Datenspeicherungs- und -abrufvorgänge aus, ohne dass externe Anwendungsprogrammierschnittstellen (APIs) erforderlich sind.

- ★ 27.396
- TypeScript
- GitHub Trending · 2026-07-09

## Aktualisierungen

- **28. September 2026:** Sterne 26,048 → 27,396, neueste Version v2.0.1 (25. August 2026).
- **7. September 2026:** Sterne 24,804 → 26,048, neueste Version v2.0.1 (25. August 2026).
- **27. August 2026:** Sterne 23,144 → 24,804, neueste Version v2.0.1 (25. August 2026).
- **19. August 2026:** Sterne 21,959 → 23,144, neueste Version v2.0.0 (3. August 2026).

## Was es bringt

- Reduziert den Token-Verbrauch um bis zu 61 %
- Erhöht die Erfolgsquote bei komplexen Aufgaben
- Speichert Daten in einer symbolischen und geschichteten Struktur

## Installation

**Paketinstallation**

```
mkdir -p ~/.memory-tencentdb
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest --omit=dev
cp -r node_modules/@tencentdb-agent-memory/memory-tencentdb \
      ~/.memory-tencentdb/tdai-memory-openclaw-plugin
rm -rf "$TEMP_DIR"
```

**Abhängigkeiten installieren**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npm install --omit=dev
npm install tsx
```

## Ausführung

**Starten des Servers**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
  npx tsx src/gateway/server.ts
```

**Überprüfen Sie die Verbindung**

```
curl http://127.0.0.1:8420/health
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Konfigurieren Sie den Langzeitspeicher meines KI-Agenten mit TencentDB Agent Memory. Verwenden Sie anstelle eines flachen Vektorstapels von Daten symbolische Mermaid-Diagramme für kurzfristige Aufgaben und eine geschichtete Speicherpyramide L0-L3 für langfristige Erfahrungen. Ermöglichen Sie dem Agenten, vergangene Konversationen, atomare Fakten und Benutzerpräferenzen in dieser hierarchischen Struktur zu speichern und sie bei Bedarf mit vollständiger Rückverfolgbarkeit über node_id abzurufen.

## Verwandte Begriffe aus dem Glossar

- [Long-term Memory](https://trescout.com/de/dictionary/long-term-memory/)
- [Mermaid](https://trescout.com/de/dictionary/mermaid/)
- [Memory](https://trescout.com/de/dictionary/memory/)
- [Token](https://trescout.com/de/dictionary/token/)
- [Agent](https://trescout.com/de/dictionary/agent/)
- [API](https://trescout.com/de/dictionary/api/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die nicht möchten, dass ihre KI-Agenten den Kontext vergessen, und die durch die Reduzierung der Token-Kosten konsistentere Ergebnisse erzielen möchten.

## Links

- [GitHub-Repository →](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [Auf Türkisch lesen →](https://trescout.com/discover/tencentdb-agent-memory/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-09 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/tencentdb-agent-memory/
