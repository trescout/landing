# Túnel TCP para tráfico de red

OpenFlux, desarrollado en el lenguaje Go, es una herramienta de túnel TCP diseñada para la investigación de la pila de red (network stack). Gracias a su soporte para transportes conectables (pluggable transports), ofrece capacidades flexibles de análisis y gestión sobre el tráfico de red.

- ★ 2.019
- Go
- GitHub Trending · 2026-09-12

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 1,910 → 2,019, última versión v0.4.1 (7 de octubre de 2026).
- **1 de octubre de 2026:** Estrellas 1,896 → 1,910, última versión v0.3.0 (30 de septiembre de 2026).
- **29 de septiembre de 2026:** Estrellas 1,884 → 1,896, última versión v0.2.0 (28 de septiembre de 2026).
- **28 de septiembre de 2026:** Estrellas 1,870 → 1,884, última versión node-v1.0.1 (27 de septiembre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear un túnel TCP utilizando la herramienta OpenFlux. Explica paso a paso los pasos de compilación necesarios para ejecutar el cliente en mi computadora de escritorio y cómo configurar posteriormente los ajustes del proxy SOCKS5 en el navegador. Además, detalla técnicamente por qué es necesario bloquear los paquetes RST con iptables al configurar un nodo de salida (exit node) en un servidor Linux y cuál es el impacto de esta operación en la seguridad de la red.

## Términos relacionados del glosario

- [Pluggable Transports](https://trescout.com/es/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Proxy](https://trescout.com/es/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para usuarios que investigan la pila de red y desean tunelizar el tráfico TCP a través de diferentes protocolos de transporte.
- **Licencia:** GPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/p1neappleXpress/OpenFlux)
- [Leer en turco →](https://trescout.com/discover/openflux/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openflux/
