# Implementación de aplicaciones en su propio servidor

OpenShip ofrece una plataforma de distribución de aplicaciones que los usuarios pueden alojar en sus propios servidores. Esta herramienta, desarrollada con el lenguaje TypeScript, facilita procesos de autohospedaje como alternativa a los servicios de infraestructura basados ​​en la nube.

- ★ 14.584
- TypeScript
- GitHub Trending · 2026-07-21

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 14,558 → 14,584, última versión v0.8.2 (6 de octubre de 2026).
- **6 de octubre de 2026:** Estrellas 13,545 → 14,558, última versión v0.8.0 (27 de septiembre de 2026).
- **29 de septiembre de 2026:** Estrellas 12,541 → 13,545, última versión v0.8.0 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 12,135 → 12,541, última versión v0.8.0 (27 de septiembre de 2026).

## Qué aporta

- Procesos CI/CD automatizados
- Transición rápida del código al contenedor
- Gestión de bases de datos y SSL

## Instalación

**Instalación rápida a través de CLI**

```
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

**Instalación con Docker**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Ejecución

**Iniciar la implementación del proyecto**

```
cd your-project
openship init         # link this directory to a project
openship deploy
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero publicar un proyecto usando Openship. Mientras está en el directorio del proyecto, ¿es suficiente conectar el directorio al proyecto con el comando openship init y luego ejecutar el comando openship desplegar? ¿Puedes explicar paso a paso cómo se gestiona automáticamente la base de datos y la configuración SSL en este proceso?

## Términos relacionados del glosario

- [Deployment Platform](https://trescout.com/es/dictionary/deployment-platform/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [CI/CD](https://trescout.com/es/dictionary/ci-cd/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores de software que desean alojar aplicaciones en sus propios servidores y desean implementarlas rápidamente sin tener que lidiar con archivos de configuración complejos.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/oblien/openship)
- [Leer en turco →](https://trescout.com/discover/openship/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-21: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openship/
