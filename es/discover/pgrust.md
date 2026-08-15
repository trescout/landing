# PostgreSQL reescrito con Rust

El proyecto pgrust, en el que se reescribió el sistema de gestión de bases de datos PostgreSQL con el lenguaje de programación Rust, completa con éxito todas las pruebas de regresión. Este estudio tiene como objetivo modernizar la arquitectura de la base de datos con un lenguaje centrado en la seguridad de la memoria.

- ★ 3.957
- Rust
- GitHub Trending · 2026-07-12

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
¿Cuál es el objetivo principal del proyecto Pgrust, cómo se garantiza la compatibilidad del disco con PostgreSQL existente y cómo se utiliza la programación respaldada por inteligencia artificial en el desarrollo del proyecto? Cuéntenos sobre la compatibilidad de la versión actual de Pgrust con Postgres 18.3 y su éxito en las pruebas de regresión.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/pgrust/
