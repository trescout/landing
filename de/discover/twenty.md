# Modernes und Open-Source-CRM

Twenty ist eine Open-Source-Salesforce-Alternative, die es technischen Teams ermöglicht, ein modernes CRM aufzubauen, das an ihre Geschäftsprozesse angepasst werden kann. Sie können dieses System, das auf künstliche Intelligenz-gestützte Workflows setzt, auf Ihrem eigenen Server hosten.

- ★ 55.660
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Was es bringt
- Eine kostenlose und Open-Source-Alternative zu Salesforce.
- Volle Kontrolle über Ihre Daten mit der Self-Host-Option.
- Moderne Workflows auf Basis von KI.
- Flexible Bausteine, die an Ihre Geschäftsanforderungen angepasst werden können.

## Installation
**Umgebungsvorlage herunterladen**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Compose-Datei herunterladen**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Verschlüsselungsschlüssel generieren**

```
openssl rand -base64 32
```

**Dienste starten**

```
docker compose up -d
```


## Ausführung
**Lokale Oberfläche öffnen**

```
http://localhost:3000
```


## Wie installiere ich?
Die Installation erfolgt üblicherweise mit Docker auf dem eigenen Server; Installationsschritte finden Sie in der Dokumentation. Für die Verwaltung sind einige technische Kenntnisse erforderlich.

## Wie installiere ich, wie verwende ich?
Ich möchte ein Open-Source-CRM namens Twenty installieren. Erstellen Sie im Terminal eine neue App mit dem Befehl „npx create-twenty-app my-app“ und veröffentlichen Sie sie dann mit „npx twenty app:publish --private“ in meinem Arbeitsbereich. Sagen Sie mir auch, wie man es mit Docker Compose zum Selbsthosten ausführt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/twenty/
