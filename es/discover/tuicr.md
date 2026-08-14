# Revisando código con Vim en la terminal

Desarrollado con el lenguaje Rust, tuicr es una herramienta de revisión de código basada en una interfaz de usuario de terminal que admite atajos de teclado de Vim. Permite a los desarrolladores gestionar su proceso de revisión de código directamente desde la terminal.

- ★ 2.439
- Rust
- GitHub Trending · 2026-07-31

## Actualizar
- 6 de agosto de 2026: Star 2291 → 2439, última versión v0.21.0 (5 de agosto de 2026).
- 2 de agosto de 2026: Star 1940 → 2291, última versión v0.20.0 (2 de agosto de 2026).

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
Revise esta revisión de código y prepare una lista estructurada de cualquier error o sugerencia de mejora que encuentre, con cada comentario identificado por ruta de archivo y número de línea. Mientras realiza la revisión, proporcione sugerencias concretas que aumenten la legibilidad y el rendimiento del código, según los datos en formato Markdown que copié de tuicr.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/tuicr/
