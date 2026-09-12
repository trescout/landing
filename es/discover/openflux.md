# Túnel TCP para tráfico de red

OpenFlux, desarrollado en el lenguaje Go, es una herramienta de túnel TCP diseñada para la investigación de la pila de red (network stack). Gracias a su soporte para transportes conectables (pluggable transports), ofrece capacidades flexibles de análisis y gestión sobre el tráfico de red.

- ★ 1.241
- Go
- GitHub Trending · 2026-09-12

## Qué aporta
- Gestión de red flexible con transportes conectables
- Enrutamiento de tráfico de red local con soporte de proxy SOCKS5
- Transmisión de datos a través de Yandex Docs y WebRTC

## Instalación
**Compilación del cliente de escritorio y del nodo de salida**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Compilación del cliente Android**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```


## Ejecución
**Iniciar el cliente de escritorio**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```


## Si no programa
Quiero crear un túnel TCP utilizando la herramienta OpenFlux. Explica paso a paso los pasos de compilación necesarios para ejecutar el cliente en mi computadora de escritorio y cómo configurar posteriormente los ajustes del proxy SOCKS5 en el navegador. Además, detalla técnicamente por qué es necesario bloquear los paquetes RST con iptables al configurar un nodo de salida (exit node) en un servidor Linux y cuál es el impacto de esta operación en la seguridad de la red.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openflux/
