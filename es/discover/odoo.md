# Planificación de recursos empresariales de código abierto

Odoo es una plataforma de planificación de recursos empresariales de código abierto que permite a las empresas gestionar todos sus procesos operativos bajo un mismo techo. Desarrollado con lenguaje Python, este sistema ofrece una amplia gama de aplicaciones comerciales modulares, desde ventas hasta contabilidad.

- ★ 54.692
- GitHub Trending · 2026-06-04

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 52,082 → 54,692.

## Qué aporta

- Gestiona procesos de negocio como ventas, contabilidad y almacén desde un único centro.
- Ofrece aplicaciones empresariales modulares que son compatibles entre sí.
- Proporciona una infraestructura de código abierto que se puede personalizar según las necesidades.

## Instalación

**Iniciar base de datos PostgreSQL**

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

**Iniciar Odoo conectado a la base de datos**

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```

## Ejecución

**Acceder a la interfaz local**

```
http://localhost:8069
```

## Cómo empezar

- Fuente oficial →

## Términos relacionados del glosario

- [Enterprise Resource Planning](https://trescout.com/es/dictionary/enterprise-resource-planning/)

- **Para quién es:** Es adecuado para empresas que desean gestionar todos sus procesos operativos en una única plataforma.

## Enlaces

- [Repositorio en GitHub →](https://www.odoo.com)
- [Leer en turco →](https://trescout.com/discover/odoo/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-04: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/odoo/
