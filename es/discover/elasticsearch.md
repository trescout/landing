# Motor de búsqueda distribuido y potente

Elasticsearch es un motor de búsqueda y análisis distribuido de alto rendimiento basado en una API RESTful.

- ★ 77.846
- GitHub Trending · 2026-07-04

## ¿Qué hace esta herramienta?
Elasticsearch es un motor de búsqueda y análisis distribuido de alto rendimiento basado en una API RESTful. Proporciona una infraestructura para búsquedas en tiempo real, análisis de registros y visualización de datos sobre grandes volúmenes de datos textuales, numéricos y geográficos.

## ¿Para quién es?
Para aquellos que desean realizar búsquedas complejas y análisis de registros en millones de filas de datos en milisegundos.

## Qué no esperar
Usuarios de bases de datos tradicionales que necesitan modelos de datos relacionales y operaciones SQL `JOIN` complejas.

## Aspectos destacados
- Ofrece búsqueda de texto completo de alta velocidad en grandes volúmenes de datos.
- Gracias a su arquitectura distribuida, se puede escalar horizontalmente con facilidad.
- Alberga un rico ecosistema para la gestión de registros y la monitorización de sistemas.

## Primer flujo de uso
- Instale Elasticsearch siguiendo las instrucciones de Docker o del gestor de paquetes en la documentación oficial.
- Configure los ajustes de seguridad predeterminados (contraseñas y certificados).
- Verifique el estado del clúster enviando una solicitud al punto final principal con un cliente REST.

## Inicio seguro

## Primer prompt
¿Cómo se crea un nuevo índice en Elasticsearch?

## Instalación
**Extraiga la imagen de Docker**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (Homebrew)**

```
brew install elastic/tap/elasticsearch-full
```


## Ejecución
**Inicie con Docker en modo de nodo único**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```


## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- README oficial de Elasticsearch →
- Sitio oficial de Elasticsearch →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/elasticsearch/
