# Cliente de base de datos ligero

Desarrollado con el lenguaje Rust, dbx ofrece un cliente de base de datos ligero de 25 MB que admite más de 100 tipos de bases de datos. La aplicación de escritorio incluye soporte para interfaz de línea de comandos (CLI) y Docker, además de características como un asistente de inteligencia artificial integrado y el Protocolo de Conexión de Modelos (MCP).

- ★ 22.868
- Rust
- GitHub Trending · 2026-09-29

## Qué aporta
- Admite más de cien tipos de bases de datos.
- Funciona con escritorio, Docker y línea de comandos.
- Incluye asistente de inteligencia artificial y Protocolo de Conexión de Modelos.

## Instalación
**Instalación de la aplicación de escritorio**

```
brew install --cask dbx
```

**Instalación de la herramienta de línea de comandos**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```


## Ejecución
**Ejecutando con Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```


## Si no programa
Sigue los pasos necesarios para instalar y ejecutar la aplicación dbx. Utiliza el comando brew install --cask dbx para la aplicación de escritorio y, para la herramienta de línea de comandos, emplea npm install -g @dbx-app/cli
# o mediante Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json. Si deseas ejecutarlo con Docker, utiliza el comando # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/dbx/
