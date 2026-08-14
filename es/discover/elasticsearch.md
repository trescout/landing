# Busque big data rápidamente

Desarrollado con Java, Elasticsearch es un motor de búsqueda distribuido y de código abierto que permite búsquedas y análisis rápidos en grandes conjuntos de datos. Gracias a su arquitectura RESTful, admite la indexación y consulta de datos en tiempo real.

- ★ 77.837
- Java
- GitHub Trending · 2026-07-04

## Actualizar
- 12 de agosto de 2026: Star 77,787 → 77,837, última versión v9.5.1 (11 de agosto de 2026).
- 6 de agosto de 2026: Star 77,640 → 77,787, última versión v9.5.0 (4 de agosto de 2026).
- 2 de agosto de 2026: Star 77,374 → 77,640, última versión v9.4.4 (21 de julio de 2026).

## Qué aporta
- Búsqueda y análisis rápidos de grandes conjuntos de datos.
- Integración con búsqueda de vectores y aplicaciones de IA.
- Indexación y consulta de datos en tiempo real

## Instalación
**Extraiga la imagen de Docker**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (hecho en casa)**

```
brew install elastic/tap/elasticsearch-full
```


## Ejecución
**Inicie con Docker en modo de nodo único**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Cómo empezar
- Fuente oficial →
La forma más sencilla de comenzar con Elasticsearch es crear una implementación administrada a través de Elastic Cloud. Alternativamente, si desea administrar su propia instalación, puede visitar la página de descarga en el sitio web oficial o revisar los scripts de inicio basados ​​en Docker disponibles para entornos de desarrollo locales.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/elasticsearch/
