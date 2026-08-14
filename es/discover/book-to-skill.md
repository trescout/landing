# Convierta los libros técnicos en talento de IA

El proyecto book-to-skill convierte formatos de documentos portátiles (PDF) de libros técnicos en paquetes de habilidades (habilidades) utilizables para Claude Code. Esta herramienta permite referenciar directamente los recursos técnicos y aplicarlos en los procesos de trabajo.

- ★ 20.129
- Python
- GitHub Trending · 2026-07-29

## Actualizar
- 11 de agosto de 2026: Star 19 562 → 20 129, última versión v1.4.0 (10 de agosto de 2026).
- 10 de agosto de 2026: Star 18,272 → 19,562, última versión v1.3.0 (30 de julio de 2026).
- 7 de agosto de 2026: Star 17,132 → 18,272, última versión v1.3.0 (30 de julio de 2026).
- 6 de agosto de 2026: Star 15,238 → 17,132, última versión v1.3.0 (30 de julio de 2026).

## Qué aporta
- Transfiere libros y documentos directamente a la memoria de trabajo de su agente de IA.
- Evita el consumo innecesario de tokens al dividir archivos grandes en secciones.
- Convierte muchos formatos, como PDF, EPUB y Markdown, en un conjunto estructurado de capacidades.

## Instalación
**Configurar y comprobar la herramienta**

```
pip install "book-to-skill[pdf,epub,docx]"   # engine + optional extractors
book-to-skill ~/path/to/book.pdf --mode text  # or: python -m book_to_skill ...
book-to-skill --check                          # report which extractors are installed
```


## Ejecución
**Convertir un documento en un paquete de capacidades**

```
/book-to-skill <path-to-document-folder-or-glob>... [skill-name-slug]
```


## Si no programa
Utilizo este recurso técnico como un paquete de habilidades. Cíñete únicamente a las secciones convertidas y a los archivos estructurados al analizar el contenido. Cuando haga una pregunta, responda con referencia a la sección correspondiente y utilice únicamente la información técnica del documento, evitando alucinaciones.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/book-to-skill/
