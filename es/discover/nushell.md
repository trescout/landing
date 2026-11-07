# Interfaz de línea de comandos que ofrece objetos estructurados

Desarrollado en Rust, nushell ofrece una nueva interfaz de línea de comandos (shell) que procesa los datos como objetos estructurados. Aunque este proyecto ha alcanzado el nivel de producto mínimo viable (minimum-viable-product) y puede mostrar inestabilidad en algunos comandos, se prefiere para el uso diario.

- ★ 41.012
- Rust
- GitHub Trending · 2026-11-07

## Actualizaciones

- **7 de noviembre de 2026:** Estrellas 41,011 → 41,012, última versión 0.116.1 (4 de octubre de 2026).

## Qué aporta

- Procesa los datos como objetos estructurados.
- Permite el flujo de canalización (pipeline) entre comandos.
- Carga el contenido de los archivos como datos estructurados.

## Instalación

**Instalación**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Ejecución

**Listar carpetas**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar y usar la nueva interfaz de línea de comandos llamada Nushell. Una vez completada la instalación, ayúdame a ejecutar el comando ls | where type == "dir" | table.

Repositorio: https://github.com/nushell/nushell. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Shell](https://trescout.com/es/dictionary/shell/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores que desean gestionar datos como objetos estructurados en la línea de comandos.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/nushell/nushell)
- [Leer en turco →](https://trescout.com/discover/nushell/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-07: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/nushell/
