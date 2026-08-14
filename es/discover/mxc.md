# Aislamiento del sistema en capas basado en políticas con Rust

Desarrollado por Microsoft, MXC es una solución de contención y aislamiento en capas basada en políticas escrita en lenguaje Rust. Está diseñado para limitar de forma segura los recursos del sistema y aumentar la seguridad de las aplicaciones.

- ★ 641
- Rust
- GitHub Trending · 2026-06-07

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
Quiero ejecutar un fragmento de código que no es de confianza en un contenedor aislado utilizando la herramienta MXC desarrollada por Microsoft. Según la documentación en el repositorio GitHub del proyecto, necesito preparar un archivo de configuración basado en JSON y usar el binario apropiado para mi plataforma. ¿Pueden crearme un archivo de configuración JSON de muestra que me permita ejecutar un script de Python con un sistema de archivos y acceso a la red restringidos, y explicarme paso a paso cómo ejecutar esta configuración con wxc-exec.exe?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/mxc/
