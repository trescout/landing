# Navegador sigiloso para agentes de inteligencia artificial

Camofox es un navegador sigiloso (stealth headless browser) que permite a los agentes de inteligencia artificial superar los sistemas de detección de bots y las barreras de web scraping. Funciona directamente con las herramientas de automatización de navegadores Puppeteer y Playwright, ofreciendo una solución alternativa a estas bibliotecas.

- ★ 11.460
- JavaScript
- GitHub Trending · 2026-09-08

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 11,433 → 11,460, última versión camoufox-backup-404310733 (7 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 11,411 → 11,433, última versión v1.18.1 (5 de octubre de 2026).
- **4 de octubre de 2026:** Estrellas 11,292 → 11,411, última versión camoufox-backup-402708180 (4 de octubre de 2026).
- **1 de octubre de 2026:** Estrellas 11,228 → 11,292, última versión v1.18.0 (30 de septiembre de 2026).

## Qué aporta

- Supera los sistemas de detección de bots y las barreras de web scraping a nivel de C++.
- Consume un 90% menos de datos que el HTML estándar gracias a las instantáneas de accesibilidad.
- Proporciona gestión de cookies y almacenamiento basada en el usuario gracias al aislamiento de sesiones.

## Instalación

**Operación directa**

```
npx @askjo/camofox-browser
```

**Instalación desde el código fuente**

```
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install
npm start  # downloads Camoufox on first run (~300MB)
```

## Ejecución

**Iniciando el servidor local**

```
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Eres un administrador de navegadores web. Accede a los sitios web objetivo utilizando Camofox-browser. Utiliza este navegador, oculto a nivel de C++, para evitar ser detectado como bot. Al extraer datos de páginas web, prefiere las instantáneas de accesibilidad (accessibility snapshots), que son más ligeras que el HTML sin procesar. Utiliza identificadores estables para los elementos con los que necesites interactuar y gestiona las sesiones aislándolas por usuario.

Repositorio: https://github.com/jo-inc/camofox-browser. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Stealth Headless Browser](https://trescout.com/es/dictionary/stealth-headless-browser/)
- [Headless Browser](https://trescout.com/es/dictionary/headless-browser/)
- [Web Scraping](https://trescout.com/es/dictionary/web-scraping/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Destinado a desarrolladores que crean agentes de inteligencia artificial que necesitan extraer datos de sitios web o realizar operaciones en Internet.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/jo-inc/camofox-browser)
- [Leer en turco →](https://trescout.com/discover/camofox-browser/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-08: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/camofox-browser/
