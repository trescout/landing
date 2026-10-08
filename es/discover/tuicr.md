# Revisando código con Vim en la terminal

Desarrollado con el lenguaje Rust, tuicr es una herramienta de revisión de código basada en una interfaz de usuario de terminal que admite atajos de teclado de Vim. Permite a los desarrolladores gestionar su proceso de revisión de código directamente desde la terminal.

- ★ 3.221
- Rust
- GitHub Trending · 2026-07-31

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 3,132 → 3,221, última versión v0.27.0 (23 de septiembre de 2026).
- **16 de septiembre de 2026:** Estrellas 3,009 → 3,132, última versión v0.26.0 (15 de septiembre de 2026).
- **3 de septiembre de 2026:** Estrellas 2,908 → 3,009, última versión v0.25.0 (2 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 2,817 → 2,908, última versión v0.24.0 (25 de agosto de 2026).

## Qué aporta

- Revisión rápida de código en terminal con atajos de Vim
- Publicar comentarios directamente en GitHub y GitLab
- Soporte de salida estructurada para herramientas de IA

## Instalación

**Instalación estándar**

```
curl -fsSL tuicr.dev/install.sh | sh
# or
brew install agavra/tap/tuicr
```

**Gestores de paquetes alternativos**

```
# Cargo
cargo install tuicr

# Mise
mise use github:agavra/tuicr

# Nix
nix run github:agavra/tuicr
```

## Ejecución

**Revisar los cambios locales**

```
tuicr -w
```

**Revisar un PR específico**

```
tuicr pr 125
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Revise esta revisión de código y prepare una lista estructurada de cualquier error o sugerencia de mejora que encuentre, con cada comentario identificado por ruta de archivo y número de línea. Mientras realiza la revisión, proporcione sugerencias concretas que aumenten la legibilidad y el rendimiento del código, según los datos en formato Markdown que copié de tuicr.

## Términos relacionados del glosario

- [Code Review](https://trescout.com/es/dictionary/code-review/)
- [User Interface](https://trescout.com/es/dictionary/user-interface/)
- [Markdown](https://trescout.com/es/dictionary/markdown/)
- [Terminal](https://trescout.com/es/dictionary/terminal/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que quieren gestionar sus procesos de revisión de código con atajos de Vim sin salir del terminal.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/agavra/tuicr)
- [Leer en turco →](https://trescout.com/discover/tuicr/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-31: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/tuicr/
