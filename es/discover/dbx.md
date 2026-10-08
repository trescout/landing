# Cliente de base de datos ligero

Desarrollado con el lenguaje Rust, dbx ofrece un cliente de base de datos ligero de 25 MB que admite más de 100 tipos de bases de datos. La aplicación de escritorio incluye soporte para interfaz de línea de comandos (CLI) y Docker, además de características como un asistente de inteligencia artificial integrado y el Protocolo de Conexión de Modelos (MCP).

- ★ 24.988
- Rust
- GitHub Trending · 2026-09-29

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 24,669 → 24,988, última versión v0.6.35 (6 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 24,470 → 24,669, última versión v0.6.34 (4 de octubre de 2026).
- **4 de octubre de 2026:** Estrellas 24,157 → 24,470, última versión v0.6.33 (4 de octubre de 2026).
- **3 de octubre de 2026:** Estrellas 23,846 → 24,157, última versión v0.6.32 (3 de octubre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

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

- [Database Client](https://trescout.com/es/dictionary/database-client/)
- [Local](https://trescout.com/es/dictionary/local/)
- [Database](https://trescout.com/es/dictionary/database/)
- [MCP](https://trescout.com/es/dictionary/mcp/)
- [Agent](https://trescout.com/es/dictionary/agent/)
- [CLI](https://trescout.com/es/dictionary/cli/)

- **Para quién es:** Para desarrolladores que desean gestionar diferentes tipos de bases de datos con una interfaz ligera y soporte de inteligencia artificial.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/t8y2/dbx)
- [Leer en turco →](https://trescout.com/discover/dbx/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-29: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/dbx/
