# Sistema de almacenamiento de objetos de alto rendimiento

RustFS fue desarrollado como un sistema de almacenamiento de objetos de alto rendimiento compatible con S3. Ofrece soporte para interoperabilidad y migración de datos con otras plataformas compatibles con S3 como MinIO y Ceph.

- ★ 34.330
- Rust
- GitHub Trending · 2026-09-19

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 33,264 → 34,330, última versión 1.0.1 (3 de octubre de 2026).
- **19 de septiembre de 2026:** Estrellas 33,264 → 33,264, última versión 1.0.0 (16 de septiembre de 2026).

## Qué aporta

- Proporciona alta velocidad y seguridad de memoria con el lenguaje Rust
- Funciona sin problemas con herramientas existentes gracias a su estructura compatible con S3
- Ofrece uso comercial sin restricciones con la licencia Apache 2.0

## Instalación

**Iniciar con el script de instalación**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Ejecutar la versión más reciente con Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```

## Ejecución

**Iniciar el sistema usando Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero configurar un entorno de almacenamiento de objetos de alto rendimiento utilizando RustFS. ¿Cómo puedo gestionar mis datos aprovechando la compatibilidad con S3 del sistema y qué debo tener en cuenta al escalar en una arquitectura distribuida? Guíame paso a paso sobre la instalación y los ajustes de configuración básicos de este sistema con licencia Apache 2.0.

## Términos relacionados del glosario

- [Object Storage System](https://trescout.com/es/dictionary/object-storage-system/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a administradores de sistemas y desarrolladores que buscan una solución de almacenamiento rápida, segura y compatible con S3 para cargas de trabajo de big data, proyectos de inteligencia artificial y lagos de datos.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/rustfs/rustfs)
- [Leer en turco →](https://trescout.com/discover/rustfs/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-19: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rustfs/
