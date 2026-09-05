# Implementación de aplicaciones en su propio servidor

OpenShip ofrece una plataforma de distribución de aplicaciones que los usuarios pueden alojar en sus propios servidores. Esta herramienta, desarrollada con el lenguaje TypeScript, facilita procesos de autohospedaje como alternativa a los servicios de infraestructura basados ​​en la nube.

- ★ 12.101
- TypeScript
- GitHub Trending · 2026-07-21

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
Quiero publicar un proyecto usando Openship. Mientras está en el directorio del proyecto, ¿es suficiente conectar el directorio al proyecto con el comando openship init y luego ejecutar el comando openship desplegar? ¿Puedes explicar paso a paso cómo se gestiona automáticamente la base de datos y la configuración SSL en este proceso?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openship/
