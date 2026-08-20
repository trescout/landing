# Puerta de enlace de código abierto para WhatsApp

OpenWA ofrece una solución de puerta de enlace API gratuita y de código abierto para el protocolo de mensajería de WhatsApp. Esta herramienta, desarrollada con lenguaje TypeScript, permite a los usuarios gestionar las integraciones de WhatsApp en sus propios servidores (autohospedados).

- ★ 12.991
- TypeScript
- GitHub Trending · 2026-06-17

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
Quiero automatizar mis procesos de mensajería vía WhatsApp usando la herramienta OpenWA. Guíeme a través de los pasos de configuración básicos necesarios para crear una nueva sesión, enviar mensajes y escuchar los mensajes entrantes a través de un webhook utilizando puntos finales de API REST. Dígame a qué debo prestar atención, especialmente con respecto a la administración de sesiones múltiples y la seguridad de las claves API.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openwa/
