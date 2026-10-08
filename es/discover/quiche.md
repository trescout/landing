# Soporte para QUIC y HTTP/3 con Rust

Desarrollado por Cloudflare, quiche ofrece una implementación escrita en Rust del protocolo de transporte QUIC y del estándar de red HTTP/3. Diseñada para acelerar el tráfico de internet, esta biblioteca proporciona una infraestructura de bajo nivel para los desarrolladores que buscan optimizar el rendimiento de la red.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 12,452 → 12,638, última versión 0.30.0 (17 de septiembre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero procesar paquetes QUIC y gestionar los estados de las conexiones de red utilizando esta biblioteca escrita en el lenguaje de programación Rust. Después de clonar el proyecto, ¿qué pasos debo seguir para ejecutar el cliente y el servidor?

## Términos relacionados del glosario

- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Desarrolladores que desean optimizar el rendimiento de la red y ofrecer compatibilidad con HTTP/3.
- **Licencia:** BSD-2-Clause

## Enlaces

- [Repositorio en GitHub →](https://github.com/cloudflare/quiche)
- [Leer en turco →](https://trescout.com/discover/quiche/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-20: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/quiche/
