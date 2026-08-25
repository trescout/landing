# Planificación de recursos empresariales de código abierto

Odoo es una plataforma de planificación de recursos empresariales de código abierto que permite a las empresas gestionar todos sus procesos operativos bajo un mismo techo. Desarrollado con lenguaje Python, este sistema ofrece una amplia gama de aplicaciones comerciales modulares, desde ventas hasta contabilidad.

- ★ 52.082
- GitHub Trending · 2026-06-04

## Qué aporta
- Gestiona procesos de negocio como ventas, contabilidad y almacén desde un único centro.
- Ofrece aplicaciones empresariales modulares que son compatibles entre sí.
- Proporciona una infraestructura de código abierto que se puede personalizar según las necesidades.

## Instalación
****

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

****

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```


## Ejecución
****

```
http://localhost:8069
```


## Cómo empezar
- Fuente oficial →

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/odoo/
