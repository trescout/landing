# Plataforma de atención al cliente de código abierto

Chatwoot es una plataforma de código abierto que ofrece chat en vivo, soporte por correo electrónico y gestión de escritorio omnicanal. Desarrollada como una alternativa a software comerciales como Intercom y Zendesk, esta herramienta permite gestionar las interacciones con los clientes desde un único centro.

- ★ 36.927
- GitHub Trending · 2026-06-12

**Nota de TreScout:** Recopila mensajes de clientes en una sola pantalla: chat del sitio, correo electrónico, WhatsApp. Los servicios ya preparados que hacen el mismo trabajo cobran una tarifa mensual por persona, pero como se ejecuta en su propio servidor, no existe tal tarifa, a cambio, el servidor y el mantenimiento se convierten en su trabajo. Su instalación no es monolítica, requiere varias utilidades y tiene dificultades con los paquetes de servidor más baratos.

## Actualizaciones

- **18 de septiembre de 2026:** Estrellas 36,253 → 36,927, última versión v4.18.0 (18 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 36,001 → 36,253, última versión v4.17.1 (27 de agosto de 2026).
- **20 de agosto de 2026:** Estrellas 35,290 → 36,001, última versión v4.17.0 (20 de agosto de 2026).
- **1 de agosto de 2026:** Estrellas 30,493 → 35,290, última versión v4.16.2 (27 de julio de 2026).

## Qué aporta

- Combina todos los canales de clientes en una única bandeja de entrada.
- Responde automáticamente preguntas rutinarias con un asistente respaldado por inteligencia artificial.
- Le brinda control total sobre los datos de sus clientes al alojarlos en su propio servidor.

## Instalación

**Descargar archivo de entorno**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Descargar archivo Docker Compose**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Preparar base de datos**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Ejecución

**Iniciar servicios**

```
docker compose up -d
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Responda preguntas haciéndose pasar por un representante de atención al cliente. Como asistente del Capitán AI en Chatwoot, resuelve automáticamente las preguntas más frecuentes y dirige los problemas complejos a los compañeros de equipo relevantes. Mejore la experiencia de atención al cliente brindando siempre información cortés, rápida y precisa.

## Términos relacionados del glosario

- [Omni-channel Desk](https://trescout.com/es/dictionary/omni-channel-desk/)
- [Omni-channel](https://trescout.com/es/dictionary/omni-channel/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para empresas que desean gestionar las interacciones con los clientes desde un único centro y automatizar los procesos de soporte.

## Enlaces

- [Repositorio en GitHub →](https://github.com/chatwoot/chatwoot)
- [Leer en turco →](https://trescout.com/discover/chatwoot/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/chatwoot/
