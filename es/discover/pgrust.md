# PostgreSQL reescrito con Rust

El proyecto pgrust, en el que se reescribió el sistema de gestión de bases de datos PostgreSQL con el lenguaje de programación Rust, completa con éxito todas las pruebas de regresión. Este estudio tiene como objetivo modernizar la arquitectura de la base de datos con un lenguaje centrado en la seguridad de la memoria.

- ★ 5.030
- Rust
- GitHub Trending · 2026-07-12

## Actualizaciones

- **16 de septiembre de 2026:** Estrellas 4,964 → 5,030, última versión v0.3 (15 de septiembre de 2026).
- **10 de septiembre de 2026:** Estrellas 3,957 → 4,964, última versión v0.2-release (30 de julio de 2026).
- **2 de agosto de 2026:** Estrellas 2,171 → 3,957, última versión v0.2-release (30 de julio de 2026).

## Qué aporta

- Compatibilidad de disco con Postgres 18.3
- Más de 46 mil éxitos en pruebas de regresión
- Arquitectura moderna centrada en la seguridad de la memoria.

## Instalación

**Prueba rápida con Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Cuál es el objetivo principal del proyecto Pgrust, cómo se garantiza la compatibilidad del disco con PostgreSQL existente y cómo se utiliza la programación respaldada por inteligencia artificial en el desarrollo del proyecto? Cuéntenos sobre la compatibilidad de la versión actual de Pgrust con Postgres 18.3 y su éxito en las pruebas de regresión.

## Términos relacionados del glosario

- [Memory](https://trescout.com/es/dictionary/memory/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores e investigadores de bases de datos que desean modernizar la arquitectura PostgreSQL con el lenguaje Rust.
- **Licencia:** AGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/malisper/pgrust)
- [Leer en turco →](https://trescout.com/discover/pgrust/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/pgrust/
