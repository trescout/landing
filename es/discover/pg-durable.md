# Gestión sólida de procesos en PostgreSQL

Desarrollada por Microsoft, pg_durable es una biblioteca diseñada para gestionar procesos de ejecución duraderos en PostgreSQL. Escrita en Rust, la herramienta permite ejecutar flujos de trabajo complejos dentro de la base de datos de manera persistente y tolerante a fallas.

- ★ 2.831
- Rust
- GitHub Trending · 2026-06-08

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 2,811 → 2,831, última versión v0.2.9 (7 de octubre de 2026).
- **12 de septiembre de 2026:** Estrellas 2,800 → 2,811, última versión v0.2.8 (11 de septiembre de 2026).
- **2 de septiembre de 2026:** Estrellas 2,781 → 2,800, última versión v0.2.7 (1 de septiembre de 2026).
- **24 de agosto de 2026:** Estrellas 2,716 → 2,781, última versión v0.2.6 (24 de agosto de 2026).

## Qué aporta

- Gestiona los flujos de trabajo dentro de la base de datos de forma persistente y tolerante a fallos.
- En caso de caída o interrupción, continúa operaciones desde el último punto de control.
- Se ejecuta directamente en PostgreSQL sin requerir infraestructura adicional.

## Instalación

**Activando el complemento**

```
CREATE EXTENSION pg_durable;
```

## Ejecución

**Iniciar un flujo de trabajo**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear un flujo de trabajo usando el complemento pg_durable en PostgreSQL. ¿Cómo debo configurar la función df.start() para gestionar un proceso persistente y tolerante a fallos dentro de la base de datos? ¿Cómo puedo crear una estructura que procese datos y pueda continuar desde donde lo dejó en caso de error, usando los operadores ~> y |=> que conectan los pasos de SQL? Explique este proceso dando ejemplos con comandos SQL.

## Términos relacionados del glosario

- [Durable Execution](https://trescout.com/es/dictionary/durable-execution/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores backend, administradores de bases de datos e ingenieros de datos que desean administrar procesos de procesamiento de datos directamente en PostgreSQL de una manera persistente y tolerante a fallas.

## Enlaces

- [Repositorio en GitHub →](https://github.com/microsoft/pg_durable)
- [Leer en turco →](https://trescout.com/discover/pg-durable/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-08: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/pg-durable/
