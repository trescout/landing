# Puerta de enlace de código abierto para WhatsApp

OpenWA ofrece una solución de puerta de enlace API gratuita y de código abierto para el protocolo de mensajería de WhatsApp. Esta herramienta, desarrollada con lenguaje TypeScript, permite a los usuarios gestionar las integraciones de WhatsApp en sus propios servidores (autohospedados).

- ★ 14.976
- TypeScript
- GitHub Trending · 2026-06-17

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 14,622 → 14,976, última versión v0.24.0 (3 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 14,197 → 14,622, última versión v0.23.7 (25 de septiembre de 2026).
- **16 de septiembre de 2026:** Estrellas 13,775 → 14,197, última versión v0.23.5 (15 de septiembre de 2026).
- **5 de septiembre de 2026:** Estrellas 13,239 → 13,775, última versión v0.23.4 (5 de septiembre de 2026).

## Qué aporta

- Control total sobre la infraestructura de mensajería de WhatsApp
- Gestión de sesiones y webhooks con interfaz moderna
- Instalación rápida y sencilla con soporte Docker

## Instalación

**Instalación rápida con Docker**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Entorno de desarrollo local**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

## Ejecución

**Lanzamiento en un entorno de producción**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero automatizar mis procesos de mensajería vía WhatsApp usando la herramienta OpenWA. Guíeme a través de los pasos de configuración básicos necesarios para crear una nueva sesión, enviar mensajes y escuchar los mensajes entrantes a través de un webhook utilizando puntos finales de API REST. Dígame a qué debo prestar atención, especialmente con respecto a la administración de sesiones múltiples y la seguridad de las claves API.

## Términos relacionados del glosario

- [API Gateway](https://trescout.com/es/dictionary/api-gateway/)
- [Gateway](https://trescout.com/es/dictionary/gateway/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que desean desarrollar sus propias integraciones de WhatsApp y pretenden tener control total sobre la infraestructura de mensajería.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/rmyndharis/OpenWA)
- [Leer en turco →](https://trescout.com/discover/openwa/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-17: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openwa/
