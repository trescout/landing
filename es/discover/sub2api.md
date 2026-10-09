# Gestione las suscripciones de IA desde un único centro

Sub2API es un servicio intermediario de código abierto que proporciona acceso de punto único y costos compartidos a las suscripciones de Claude, OpenAI, Gemini y Grok.

- ★ 43.558
- Go
- GitHub Trending · 2026-08-23

## Actualizaciones

- **9 de octubre de 2026:** Estrellas 43,391 → 43,558, última versión v0.2.15 (9 de octubre de 2026).
- **7 de octubre de 2026:** Estrellas 43,206 → 43,391, última versión v0.2.14 (7 de octubre de 2026).
- **2 de octubre de 2026:** Estrellas 43,199 → 43,206, última versión v0.2.13 (2 de octubre de 2026).
- **2 de octubre de 2026:** Estrellas 43,119 → 43,199, última versión v0.2.12 (2 de octubre de 2026).

## Qué aporta

- Combina diferentes suscripciones de IA en una sola interfaz
- Le ayuda a asignar los costos de suscripción de manera eficiente
- Ofrece la oportunidad de trabajar integrado con herramientas existentes.

## Instalación

**instalación automática**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Instalación con Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```

## Ejecución

**Iniciar el servicio**

```
docker compose up -d
```

**Ver contraseña de administrador**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Cómo puedo configurar diferentes servicios de IA como Claude, OpenAI, Gemini y Grok a través de una única puerta de enlace API utilizando la plataforma Sub2API? Explique los pasos básicos que debo seguir para asignar eficientemente mis cuotas de suscripción e integrarlas con mis herramientas de software existentes. Además, resuma las cuestiones legales y técnicas a las que debo prestar atención para cumplir con los términos de servicio de proveedores como Anthropic al utilizar esta plataforma.

## Términos relacionados del glosario

- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para desarrolladores que desean gestionar múltiples suscripciones de IA en una única plataforma y optimizar sus costos.
- **Licencia:** LGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/Wei-Shaw/sub2api)
- [Leer en turco →](https://trescout.com/discover/sub2api/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-23: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sub2api/
