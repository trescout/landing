# Recopile datos de redes sociales automáticamente

MediaCrawler recopila automáticamente publicaciones y comentarios de usuarios en plataformas de redes sociales populares chinas a través del web scraping. Esta herramienta basada en Python ofrece una infraestructura integral de rastreo de datos para procesos de análisis de contenido y recopilación de datos.

- ★ 62.789
- Python
- GitHub Trending · 2026-06-26

## Qué aporta
- Extrayendo publicaciones y comentarios de plataformas populares
- Inicio de sesión sencillo con automatización del navegador
- Admite grabación en múltiples formatos de datos

## Instalación
**Instalando dependencias**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Instalación del controlador del escáner**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```


## Ejecución
**Iniciar extracción de datos**

```
# 在 config/base_config.py 查看配置项目功能，写的有中文注释

# 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
uv run main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例，执行下面的命令查看
uv run main.py --help
```


## Si no programa
Quiero extraer datos de una plataforma de redes sociales específica utilizando la herramienta MediaCrawler. Permítame verificar la configuración en el archivo config/base_config.py y explicarle paso a paso cómo debo configurar el comando uv run main.py para recopilar información de publicaciones y comentarios mediante una búsqueda de palabras clave para la plataforma xhs.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/mediacrawler/
