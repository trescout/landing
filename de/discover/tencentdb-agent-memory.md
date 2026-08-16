# Mehrschichtiger Speicher für KI-Agenten

TencentDB Agent Memory bietet eine vollständig lokale Langzeitspeicherlösung für Agenten der künstlichen Intelligenz mit einem vierstufigen Prozess. Es führt Datenspeicherungs- und -abrufvorgänge aus, ohne dass externe Anwendungsprogrammierschnittstellen (APIs) erforderlich sind.

- ★ 21.959
- TypeScript
- GitHub Trending · 2026-07-09

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
Konfigurieren Sie den Langzeitspeicher meines KI-Agenten mit TencentDB Agent Memory. Verwenden Sie anstelle eines flachen Vektorstapels von Daten symbolische Mermaid-Diagramme für kurzfristige Aufgaben und eine geschichtete Speicherpyramide L0-L3 für langfristige Erfahrungen. Ermöglichen Sie dem Agenten, vergangene Konversationen, atomare Fakten und Benutzerpräferenzen in dieser hierarchischen Struktur zu speichern und sie bei Bedarf mit vollständiger Rückverfolgbarkeit über node_id abzurufen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/tencentdb-agent-memory/
