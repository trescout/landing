# Navegador sigiloso para agentes de inteligencia artificial

Camofox es un navegador sigiloso (stealth headless browser) que permite a los agentes de inteligencia artificial superar los sistemas de detección de bots y las barreras de web scraping. Funciona directamente con las herramientas de automatización de navegadores Puppeteer y Playwright, ofreciendo una solución alternativa a estas bibliotecas.

- ★ 10.066
- JavaScript
- GitHub Trending · 2026-09-08

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
Eres un administrador de navegadores web. Accede a los sitios web objetivo utilizando Camofox-browser. Utiliza este navegador, oculto a nivel de C++, para evitar ser detectado como bot. Al extraer datos de páginas web, prefiere las instantáneas de accesibilidad (accessibility snapshots), que son más ligeras que el HTML sin procesar. Utiliza identificadores estables para los elementos con los que necesites interactuar y gestiona las sesiones aislándolas por usuario.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/camofox-browser/
