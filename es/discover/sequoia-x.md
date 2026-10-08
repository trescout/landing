# Selección automática de acciones para la bolsa de valores de China

Sequoia-X es un software basado en Python que realiza la selección automática de acciones según fórmulas de análisis técnico utilizando datos de la bolsa de valores de China. Realiza operaciones de escaneo después del cierre del mercado al final del día y envía los resultados a través de Feishu, una aplicación de mensajería corporativa.

- ★ 7.594
- Python
- GitHub Trending · 2026-09-03

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 6,376 → 7,594.

## Qué aporta

- Almacena los datos de las acciones en una base de datos local
- Aplica automáticamente múltiples estrategias de análisis técnico
- Envía los resultados del final del día a través de la aplicación de mensajería Feishu

## Instalación

**Instalación de las bibliotecas necesarias**

```
pip install .
```

## Ejecución

**Carga inicial de datos históricos**

```
python main.py --backfill
```

**Iniciar el escaneo diario**

```
python main.py
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero utilizar la herramienta Sequoia-X para escanear acciones en la bolsa de valores de China mediante métodos de análisis técnico. Después de realizar las instalaciones necesarias en mi entorno de Python, utilizaré primero el modo 'backfill' para cargar los datos históricos y, posteriormente, el modo de ejecución diaria para realizar el escaneo automático y recibir notificaciones después del cierre del mercado. En este proceso, deseo asegurar que los datos se almacenen en una base de datos SQLite local y que los resultados se envíen a través de Feishu.

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está destinado a inversores que operan en la bolsa de valores de China y desean automatizar sus estrategias de análisis técnico.

## Enlaces

- [Repositorio en GitHub →](https://github.com/sngyai/Sequoia-X)
- [Leer en turco →](https://trescout.com/discover/sequoia-x/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-03: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sequoia-x/
