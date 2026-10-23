# Lenguaje de脚本 para sitios web

PHP se utiliza como un lenguaje de programación de propósito general (scripting language) diseñado especialmente para procesos de desarrollo web. Escrito en lenguaje C, este intérprete forma la infraestructura de muchos sitios web en todo el mundo.

- ★ 41.410
- C
- GitHub Trending · 2026-10-23

## Actualizaciones

- **23 de octubre de 2026:** Estrellas 41,391 → 41,410, última versión php-8.5.12 (21 de octubre de 2026).

## Qué aporta

- Te permite ejecutar sitios web dinámicos y aplicaciones web.
- Ofrece la oportunidad de probar la versión más reciente compilando directamente desde el código fuente.
- Te ayuda a medir la estabilidad del sistema con herramientas de prueba integradas integrales.

## Instalación

**Instalar herramientas de compilación para Ubuntu**

```
sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
```

**Instalar herramientas de compilación para Fedora**

```
sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel
```

## Ejecución

**Compilar el código fuente**

```
make -j4
```

**Ejecuta las pruebas**

```
make TEST_PHP_ARGS=-j4 test
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero compilar el intérprete de PHP desde el código fuente y probarlo. Si uso Ubuntu, ejecuta el comando sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev para instalar las herramientas de compilación necesarias a través del gestor de paquetes. Si uso Fedora, usa el comando sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel, y si uso macOS, usa el gestor de paquetes Homebrew con el comando brew install autoconf bison re2c libiconv libxml2 sqlite. Luego, ejecuta el comando make -j4 para compilar el proyecto. Una vez finalizada la compilación, aplica el comando make TEST_PHP_ARGS=-j4 test para ejecutar las pruebas concurrentemente o el comando make TESTS=tests/lang/ test para ejecutar las pruebas del lenguaje.

Repositorio: https://github.com/php/php-src. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Scripting Language](https://trescout.com/es/dictionary/scripting-language/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a desarrolladores que crean aplicaciones web y a aquellos que desean examinar el código del núcleo de PHP y compilarlo directamente desde la fuente.
- **Licencia:** BSD-3-Clause

## Enlaces

- [Repositorio en GitHub →](https://github.com/php/php-src)
- [Leer en turco →](https://trescout.com/discover/php-src/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-23: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/php-src/
