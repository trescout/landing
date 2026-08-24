# Gestión sólida de procesos en PostgreSQL

Desarrollada por Microsoft, pg_durable es una biblioteca diseñada para gestionar procesos de ejecución duraderos en PostgreSQL. Escrita en Rust, la herramienta permite ejecutar flujos de trabajo complejos dentro de la base de datos de manera persistente y tolerante a fallas.

- ★ 2.781
- Rust
- GitHub Trending · 2026-06-08

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
Quiero crear un flujo de trabajo usando el complemento pg_durable en PostgreSQL. ¿Cómo debo configurar la función df.start() para gestionar un proceso persistente y tolerante a fallos dentro de la base de datos? ¿Cómo puedo crear una estructura que procese datos y pueda continuar desde donde lo dejó en caso de error, usando los operadores ~> y |=> que conectan los pasos de SQL? Explique este proceso dando ejemplos con comandos SQL.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/pg-durable/
