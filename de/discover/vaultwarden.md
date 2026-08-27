# Passwortverwaltung auf Ihrem eigenen Server

Eine Zusammenfassung für diesen Artikel konnte heute nicht erstellt werden. Einzelheiten finden Sie im Quelllink.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## Was es bringt
- Vollständig kompatibel mit offiziellen Bitwarden-Clients
- Kann mit geringem Ressourcenverbrauch auf Ihrem eigenen Server gehostet werden
- Bietet Zwei-Faktor-Authentifizierung und Notfallzugriff

## Installation
**Laden Sie den Container herunter und führen Sie ihn aus**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```


## Wenn Sie nicht programmieren
Helfen Sie mir bei der Installation von Vaultwarden, einem Tool, das die Passwortverwaltung auf meinem eigenen Server ermöglicht. Dieses Tool ist eine Serversoftware, die mit Bitwarden-Clients kompatibel ist. Da ich die Installation mit Docker durchführen werde, erklären Sie mir Schritt für Schritt, wie Sie die Image-Befehle zum Abrufen und Ausführen konfigurieren, ein Volume bereitstellen, um meine Daten beizubehalten, und wie Sie HTTPS-Anforderungen berücksichtigen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vaultwarden/
