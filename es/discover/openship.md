# Implementación de aplicaciones en su propio servidor

OpenShip ofrece una plataforma de distribución de aplicaciones que los usuarios pueden alojar en sus propios servidores. Esta herramienta, desarrollada con el lenguaje TypeScript, facilita procesos de autohospedaje como alternativa a los servicios de infraestructura basados ​​en la nube.

- ★ 14.928
- TypeScript
- GitHub Trending · 2026-07-21

## Actualizaciones

- **25 de octubre de 2026:** Estrellas 14,787 → 14,928, última versión v0.9.5 (24 de octubre de 2026).
- **17 de octubre de 2026:** Estrellas 14,772 → 14,787, última versión v0.9.3 (17 de octubre de 2026).
- **16 de octubre de 2026:** Estrellas 14,714 → 14,772, última versión v0.9.2 (16 de octubre de 2026).
- **13 de octubre de 2026:** Estrellas 14,701 → 14,714, última versión v0.9.1 (13 de octubre de 2026).

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

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero publicar un proyecto usando Openship. Mientras está en el directorio del proyecto, ¿es suficiente conectar el directorio al proyecto con el comando openship init y luego ejecutar el comando openship desplegar? ¿Puedes explicar paso a paso cómo se gestiona automáticamente la base de datos y la configuración SSL en este proceso?

Repositorio: https://github.com/oblien/openship. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

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

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-21: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openship/
