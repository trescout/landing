# Gestión de datos persistentes en sistemas distribuidos.

Desarrollado por Deno, Celld ofrece una infraestructura de objetos duraderos autohospedados para sistemas distribuidos. Esta tecnología, escrita en lenguaje Rust, permite distribuir la gestión del estado entre diferentes nodos de forma escalable.

- ★ 4.405
- Rust
- GitHub Trending · 2026-08-08

## Qué aporta
- Proporciona gestión de estado escalable en su propia infraestructura.
- Almacena cada objeto como una base de datos SQLite independiente.
- Establece la coordinación entre nodos con almacenamiento compatible con S3.

## Instalación
**Descarga la herramienta a tu computadora**

```
curl -fsSL https://celld.dev/install.sh | sh
```


## Ejecución
**Nodo de recursos restringidos**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```


## Si no programa
Quiero construir un sistema distribuido usando Celld. Después de crear un espacio de almacenamiento compatible con S3, explique paso a paso cómo los nodos utilizarán este espacio y cómo distribuir los paquetes de Wrangler. Resuma los detalles técnicos en un lenguaje sencillo, especialmente sobre cómo los nodos se descubren entre sí y garantizan la coherencia de los datos en S3.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/celld/
