# Analice aplicaciones de Android rápidamente

ASC es una interfaz de descompilador de Android extremadamente rápida desarrollada para investigadores de aplicaciones móviles y agentes de inteligencia artificial. Escrita en Python, esta herramienta tiene como objetivo acelerar el proceso de análisis de archivos de aplicaciones complejos.

- ★ 1.336
- Python
- GitHub Trending · 2026-09-16

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
Actúa como un investigador de aplicaciones de Android. Ayúdame a encontrar una clase específica en un archivo APK, analizar el archivo AndroidManifest.xml o buscar referencias dentro del código utilizando la herramienta Droid ASC. Al generar los comandos, utiliza los comandos getclass, getmanifest y findrefs de la herramienta con los parámetros correctos y explica cómo debo interpretar los resultados.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/asc/
