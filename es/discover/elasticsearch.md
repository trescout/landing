# Busque big data rápidamente

Desarrollado con Java, Elasticsearch es un motor de búsqueda distribuido y de código abierto que permite búsquedas y análisis rápidos en grandes conjuntos de datos. Gracias a su arquitectura RESTful, admite la indexación y consulta de datos en tiempo real.

- ★ 77.846
- Java
- GitHub Trending · 2026-07-04

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

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/elasticsearch/
