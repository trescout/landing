# ¿Qué es Full Text Search?

*Glosario · Data · Última actualización: 22 de septiembre de 2026*

La búsqueda de texto completo (tam metin arama en su equivalente turco) es un método de búsqueda que encuentra palabras que aparecen en todo el contenido de los documentos.

## Definición y origen de la palabra

Mientras que la búsqueda simple revisa el nombre del archivo, la búsqueda de texto completo escanea cada oración dentro del documento. Es la forma más eficaz de acceder a la información en archivos grandes. Su infraestructura moderna se basa en una estructura llamada índice invertido (inverted index).

***Analogía:** Es como buscar la frase que buscas escaneando todas las páginas en lugar de mirar solo la tabla de contenido de un libro.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Búsqueda en el sitio:** Buscar un tema en el blog.
**Correo electrónico:** Encontrar un mensaje de hace años.
**Código:** Buscar una función en el repositorio.
**Derecho:** Escanear el archivo de jurisprudencia.

## Profundidad técnica y arquitectura

La ruta es la siguiente:

**Tokenización:** El texto se divide en palabras, los sufijos se reducen a la raíz.
**Índice invertido:** Se registra de antemano en qué documento aparece cada palabra.
**Ordenación:** Los algoritmos como BM25 ordenan según el peso del título y la frecuencia.

Ejemplo con Postgres:

```
SELECT baslik FROM yazilar
WHERE to_tsvector('turkish', icerik) @@ to_tsquery('turkish', 'yapay & zeka');
```

Cuando se requiere similitud semántica (p. ej., que aparezca "coche" al escribir "automóvil"), se necesita búsqueda vectorial. También se usan ambos juntos: primero la palabra clave reduce los resultados y luego el vector los ordena.

## Cosas frecuentemente mezcladas

Se puede confundir con la búsqueda de metadatos. Los metadatos miran la información del archivo (nombre, fecha, tamaño), la búsqueda de texto completo mira el contenido. Por su parte, la búsqueda vectorial no mira la palabra, sino el significado.

## Uso en diferentes disciplinas

**Biblioteca:** Búsqueda de texto completo en lugar de catálogo de fichas.
**Libro:** La sección de índice al final.
**Archivo:** Buscar un tema en una colección de recortes de periódicos.

## Preguntas frecuentes

**¿No irá demasiado lento?**

Da resultados en segundos gracias al índice preestablecido. El escaneo sin índice es lento, por lo que el índice es esencial.

**¿Funciona en todo tipo de archivos?**

Sí, en archivos de los que se puede extraer texto. En documentos escaneados, el texto se obtiene primero mediante OCR.

**¿Los sufijos turcos causan problemas?**

En el análisis cualitativo, los sufijos se reducen a la raíz. En un motor con poco soporte de idiomas, la precisión disminuye, se requiere una configuración compatible con turco.

**¿Cuándo se necesita la búsqueda vectorial?**

Cuando se buscan sinónimos y conceptos. Si no se encuentra la palabra clave, entra en juego el vector, ambos juntos son poderosos.

## Términos relacionados

- [RAG](https://trescout.com/es/dictionary/rag/)
- [Vector Index](https://trescout.com/es/dictionary/vector-index/)
- [Document Parsing](https://trescout.com/es/dictionary/document-parsing/)

## Herramientas relacionadas

- [Karakeep](https://trescout.com/es/discover/karakeep/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/full-text-search/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/full-text-search/
