# Gestión de datos persistentes en sistemas distribuidos.

Desarrollado por Deno, Celld ofrece una infraestructura de objetos duraderos autohospedados para sistemas distribuidos. Esta tecnología, escrita en lenguaje Rust, permite distribuir la gestión del estado entre diferentes nodos de forma escalable.

- ★ 6.043
- Rust
- GitHub Trending · 2026-08-08

## Actualizaciones

- **22 de octubre de 2026:** Estrellas 5,067 → 6,043, última versión v0.6.3 (21 de octubre de 2026).
- **8 de octubre de 2026:** Estrellas 4,937 → 5,067, última versión v0.6.2 (7 de octubre de 2026).
- **2 de octubre de 2026:** Estrellas 4,817 → 4,937, última versión v0.6.1 (1 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 4,630 → 4,817, última versión v0.6.0 (26 de septiembre de 2026).

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

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero construir un sistema distribuido usando Celld. Después de crear un espacio de almacenamiento compatible con S3, explique paso a paso cómo los nodos utilizarán este espacio y cómo distribuir los paquetes de Wrangler. Resuma los detalles técnicos en un lenguaje sencillo, especialmente sobre cómo los nodos se descubren entre sí y garantizan la coherencia de los datos en S3.

Repositorio: https://github.com/denoland/celld. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [State Management](https://trescout.com/es/dictionary/state-management/)
- [Durable Objects](https://trescout.com/es/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores que trabajan en sistemas distribuidos y desean establecer una gestión de estado escalable en sus propios servidores.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/denoland/celld)
- [Leer en turco →](https://trescout.com/discover/celld/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-08: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/celld/
