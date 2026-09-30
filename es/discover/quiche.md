# Soporte para QUIC y HTTP/3 con Rust

Desarrollado por Cloudflare, quiche ofrece una implementación escrita en Rust del protocolo de transporte QUIC y del estándar de red HTTP/3. Diseñada para acelerar el tráfico de internet, esta biblioteca proporciona una infraestructura de bajo nivel para los desarrolladores que buscan optimizar el rendimiento de la red.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Qué aporta
- Implementar el protocolo de transporte QUIC
- Trabajar en el estándar de red HTTP/3
- Procesar paquetes de red de bajo nivel

## Instalación
**Clona el proyecto**

```
git clone https://github.com/cloudflare/quiche
```


## Ejecución
**Ejecuta el cliente**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Ejecuta el servidor**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```


## Si no programa
Quiero procesar paquetes QUIC y gestionar los estados de las conexiones de red utilizando esta biblioteca escrita en el lenguaje de programación Rust. Después de clonar el proyecto, ¿qué pasos debo seguir para ejecutar el cliente y el servidor?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/quiche/
