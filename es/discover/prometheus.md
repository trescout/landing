# Herramienta de supervisión de sistemas y servicios prometheus

Prometheus es una herramienta de supervisión que ofrece operaciones de monitoreo de sistemas y servicios, así como la gestión de bases de datos de series temporales (time series database). El sistema, que recopila métricas de los objetivos a intervalos determinados, evalúa las reglas, muestra los resultados y puede generar alertas en las condiciones definidas.

- ★ 67.226
- Go
- GitHub Trending · 2026-11-07

## Actualizaciones

- **7 de noviembre de 2026:** Estrellas 67,225 → 67,226, última versión v3.16.0 (5 de noviembre de 2026).

## Qué aporta

- recopila métricas de los objetivos a intervalos determinados
- evalúa las reglas y muestra los resultados
- puede generar alertas en las condiciones definidas

## Instalación

**ejecución con docker**

```
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

## Ejecución

**compilación y ejecución desde el código fuente**

```
make build
./prometheus --config.file=your_config.yml
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero iniciar la aplicación Prometheus, una herramienta de supervisión de sistemas y servicios, utilizando Docker. Para este propósito, ejecuta el comando docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus.

Repositorio: https://github.com/prometheus/prometheus. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Time Series Database](https://trescout.com/es/dictionary/time-series-database/)
- [Database](https://trescout.com/es/dictionary/database/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** desarrolladores y administradores de sistemas que desean monitorear el estado de los sistemas y servicios
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/prometheus/prometheus)
- [Leer en turco →](https://trescout.com/discover/prometheus/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-07: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/prometheus/
