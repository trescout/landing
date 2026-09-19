# Sistema de almacenamiento de objetos de alto rendimiento

RustFS fue desarrollado como un sistema de almacenamiento de objetos de alto rendimiento compatible con S3. Ofrece soporte para interoperabilidad y migración de datos con otras plataformas compatibles con S3 como MinIO y Ceph.

- ★ 33.264
- Rust
- GitHub Trending · 2026-09-19

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
Quiero configurar un entorno de almacenamiento de objetos de alto rendimiento utilizando RustFS. ¿Cómo puedo gestionar mis datos aprovechando la compatibilidad con S3 del sistema y qué debo tener en cuenta al escalar en una arquitectura distribuida? Guíame paso a paso sobre la instalación y los ajustes de configuración básicos de este sistema con licencia Apache 2.0.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rustfs/
