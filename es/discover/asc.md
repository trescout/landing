# Analice aplicaciones de Android rápidamente

ASC es una interfaz de descompilador de Android extremadamente rápida desarrollada para investigadores de aplicaciones móviles y agentes de inteligencia artificial. Escrita en Python, esta herramienta tiene como objetivo acelerar el proceso de análisis de archivos de aplicaciones complejos.

- ★ 2.498
- Python
- GitHub Trending · 2026-09-16

## Actualizaciones

- **21 de octubre de 2026:** Estrellas 2,399 → 2,498, última versión dev-0.1.2-post3 (21 de octubre de 2026).
- **15 de octubre de 2026:** Estrellas 2,236 → 2,399, última versión dev-0.1.2-post2 (14 de octubre de 2026).
- **10 de octubre de 2026:** Estrellas 1,980 → 2,236, última versión dev-0.1.1-post4 (10 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 1,336 → 1,980, última versión dev-0.1.1-post2 (21 de septiembre de 2026).

## Qué aporta

- Escanea archivos de aplicaciones grandes en segundos
- Realiza consultas directamente sobre el código sin sobrecargar la memoria
- Genera resultados rápidos sin procesamiento previo innecesario

## Instalación

**Instalación con administrador de paquetes.**

```
pip install droidasc
```

**Instalación desde el código fuente**

```
pip install .
```

## Ejecución

**Abrir el archivo de la aplicación con una interfaz visual**

```
droidasc app.apk --gui
```

**Exportar una clase específica**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Actúa como un investigador de aplicaciones de Android. Ayúdame a encontrar una clase específica en un archivo APK, analizar el archivo AndroidManifest.xml o buscar referencias dentro del código utilizando la herramienta Droid ASC. Al generar los comandos, utiliza los comandos getclass, getmanifest y findrefs de la herramienta con los parámetros correctos y explica cómo debo interpretar los resultados.

Repositorio: https://github.com/MG1937/ASC. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Decompiler](https://trescout.com/es/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Adecuado para investigadores de seguridad de aplicaciones móviles y desarrolladores de software de Android.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/MG1937/ASC)
- [Leer en turco →](https://trescout.com/discover/asc/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-16: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/asc/
