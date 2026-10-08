# Prepare datos PDF para IA

OpenDataLoader PDF es un analizador de PDF de código abierto que pone datos a disposición de modelos de inteligencia artificial. Este proyecto basado en Java acelera los procesos de procesamiento de datos al automatizar la accesibilidad de los documentos PDF.

- ★ 29.447
- Java
- GitHub Trending · 2026-06-04

## Actualizaciones

- **1 de octubre de 2026:** Estrellas 29,384 → 29,447, última versión v2.5.12 (1 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 29,312 → 29,384, última versión v2.5.11 (22 de septiembre de 2026).
- **18 de septiembre de 2026:** Estrellas 29,278 → 29,312, última versión v2.5.10 (18 de septiembre de 2026).
- **16 de septiembre de 2026:** Estrellas 29,080 → 29,278, última versión v2.5.9 (16 de septiembre de 2026).

## Qué aporta

- Convierte archivos PDF a formato Markdown, JSON o HTML para modelos de IA.
- Proporciona extracción de datos de alta precisión para documentos escaneados y tablas complejas.
- Etiqueta automáticamente archivos PDF de acuerdo con los estándares de accesibilidad.

## Instalación

**Instalación con Python**

```
pip install -U opendataloader-pdf
```

**Instalación con modo híbrido**

```
pip install -U "opendataloader-pdf[hybrid]"
```

## Ejecución

**Proceso de conversión de PDF**

```
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero analizar los archivos PDF que tengo usando la herramienta OpenDataLoader PDF y convertirlos a formatos de datos estructurados (Markdown o JSON) que pueda usar en procesos RAG o LLM. ¿Pueden ayudarme a crear un script para ejecutar en mi computadora local usando el SDK de Python que extraiga tablas, encabezados y texto de mis documentos en el orden de lectura correcto? También explique paso a paso cómo habilitar el modo híbrido para páginas complejas y personalizar la salida.

## Términos relacionados del glosario

- [PDF Parser](https://trescout.com/es/dictionary/pdf-parser/)
- [Parser](https://trescout.com/es/dictionary/parser/)
- [Markdown](https://trescout.com/es/dictionary/markdown/)
- [SDK](https://trescout.com/es/dictionary/sdk/)
- [RAG](https://trescout.com/es/dictionary/rag/)
- [PDF](https://trescout.com/es/dictionary/pdf/)

- **Para quién es:** Para desarrolladores que desean convertir documentos PDF en datos estructurados para modelos de IA y para usuarios que necesitan automatizar la accesibilidad de PDF.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/opendataloader-project/opendataloader-pdf)
- [Leer en turco →](https://trescout.com/discover/opendataloader-pdf/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-04: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/opendataloader-pdf/
