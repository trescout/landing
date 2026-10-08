# Haga una copia de seguridad de sus datos de forma segura cifrándolos

Desarrollado con el lenguaje Go, Restic ofrece un programa de copia de seguridad de código abierto que realiza copias de seguridad de los datos de forma rápida y eficiente cifrándolos. Esta herramienta, que admite diferentes sistemas de almacenamiento, ahorra espacio de almacenamiento con el método de copia de seguridad incremental.

- ★ 35.302
- GitHub Trending · 2026-06-12

**Nota de TreScout:** Almacena tus copias de seguridad cifrándolas y no ocupa espacio porque no escribe el mismo archivo dos veces. No tiene una interfaz en la que se puede hacer clic, se ejecuta desde la línea de comandos y usted establece la tarea de limpiar las copias de seguridad antiguas; de lo contrario, el almacenamiento aumentará con el tiempo. Intente restaurar un archivo el mismo día que lo instaló: de lo contrario, no podrá saber si la copia de seguridad realmente funcionó.

## Actualizaciones

- **2 de agosto de 2026:** Estrellas 34,273 → 35,302, última versión v0.19.1 (5 de julio de 2026).

## Qué aporta

- Proporciona alta seguridad al cifrar los datos.
- Ahorra espacio de almacenamiento con copia de seguridad incremental
- Compatible con diferentes sistemas de almacenamiento local y en la nube

## Instalación

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Ejecución

**Crear repositorio de respaldo**

```
restic init --repo /path/to/repo
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero hacer una copia de seguridad de mis datos de forma segura usando Restic. ¿Cómo puedo exportar una carpeta local o un directorio específico a un almacenamiento de respaldo cifrado? ¿Puede explicar paso a paso cómo crear el repositorio de respaldo e iniciar el proceso de respaldo inicial para que mis datos estén cifrados?

## Términos relacionados del glosario

- [Backup Program](https://trescout.com/es/dictionary/backup-program/)
- [Incremental Backup](https://trescout.com/es/dictionary/incremental-backup/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para todos los usuarios que quieran realizar una copia de seguridad de sus datos de forma rápida y eficaz cifrándolos.
- **Licencia:** BSD-2-Clause

## Enlaces

- [Repositorio en GitHub →](https://github.com/restic/restic)
- [Leer en turco →](https://trescout.com/discover/restic/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/restic/
