# Aislamiento del sistema en capas basado en políticas con Rust

Desarrollado por Microsoft, MXC es una solución de contención y aislamiento en capas basada en políticas escrita en lenguaje Rust. Está diseñado para limitar de forma segura los recursos del sistema y aumentar la seguridad de las aplicaciones.

- ★ 2.882
- Rust
- GitHub Trending · 2026-06-07

## Actualizaciones

- **17 de octubre de 2026:** Estrellas 2,506 → 2,882, última versión v1.0.1 (17 de octubre de 2026).
- **10 de octubre de 2026:** Estrellas 1,398 → 2,506, última versión v1.0.0 (7 de octubre de 2026).
- **7 de octubre de 2026:** Estrellas 641 → 1,398, última versión v1.0.0 (7 de octubre de 2026).

## Qué aporta

- Ejecuta código que no es de confianza de forma segura en entornos aislados.
- Controla el acceso a archivos, redes e interfaces con políticas basadas en JSON.
- Ofrece múltiples backends de aislamiento en Windows, Linux y macOS.

## Instalación

**Compilando en Linux**

```
./build.sh
```

**Construir en macOS**

```
./build-mac.sh
```

## Ejecución

**Ejecutando con binario nativo**

```
wxc-exec.exe config.json
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar un fragmento de código que no es de confianza en un contenedor aislado utilizando la herramienta MXC desarrollada por Microsoft. Según la documentación en el repositorio GitHub del proyecto, necesito preparar un archivo de configuración basado en JSON y usar el binario apropiado para mi plataforma. ¿Pueden crearme un archivo de configuración JSON de muestra que me permita ejecutar un script de Python con un sistema de archivos y acceso a la red restringidos, y explicarme paso a paso cómo ejecutar esta configuración con wxc-exec.exe?

Repositorio: https://github.com/microsoft/mxc. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para desarrolladores que desean ejecutar código, complementos o herramientas que no son de confianza en un entorno aislado y al mismo tiempo preservar los recursos del sistema.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/microsoft/mxc)
- [Leer en turco →](https://trescout.com/discover/mxc/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-07: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/mxc/
