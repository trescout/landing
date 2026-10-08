# Herramientas para proyectos de visión por computadora.

Desarrollado por Roboflow, Supervision ofrece herramientas y funciones auxiliares reutilizables para proyectos de visión por computadora. Esta biblioteca basada en Python acelera los flujos de trabajo de desarrollo al facilitar operaciones estándar en procesos como la detección y el seguimiento de objetos.

- ★ 51.154
- Python
- GitHub Trending · 2026-06-09

## Actualizaciones

- **8 de octubre de 2026:** Estrellas 51,146 → 51,154, última versión 0.30.9 (8 de octubre de 2026).
- **7 de octubre de 2026:** Estrellas 51,118 → 51,146, última versión 0.30.8 (6 de octubre de 2026).
- **4 de octubre de 2026:** Estrellas 51,075 → 51,118, última versión 0.30.7 (4 de octubre de 2026).
- **29 de septiembre de 2026:** Estrellas 51,054 → 51,075, última versión 0.30.6 (29 de septiembre de 2026).

## Qué aporta

- Acelera los procesos de carga y procesamiento de datos en proyectos de visión por computadora.
- Simplifica el desarrollo de aplicaciones al estandarizar operaciones como la detección y el seguimiento de objetos.
- Proporciona visualización y gestión de conjuntos de datos al trabajar de forma compatible con diferentes bibliotecas de modelos.

## Instalación

**Instalación del paquete**

```
pip install supervision
```

## Ejecución

**Marcar un objeto en la imagen**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Instalé la biblioteca con el comando de supervisión pip install en un entorno Python 3.9 o superior. Quiero visualizar los resultados de la detección de objetos y administrar mi conjunto de datos en mi proyecto de visión por computadora. ¿Cómo puedo marcar los resultados de la detección de objetos en una imagen usando la biblioteca de Supervisión y cómo puedo cargar y convertir conjuntos de datos en diferentes formatos (COCO, YOLO, etc.)? Ayúdenme a crear un flujo de trabajo de muestra utilizando el anotador y las herramientas auxiliares de conjunto de datos proporcionadas por la biblioteca.

## Términos relacionados del glosario

- [Computer Vision](https://trescout.com/es/dictionary/computer-vision/)
- [Computer Vision](https://trescout.com/es/dictionary/cv/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores de Python que desean estandarizar los procesos de seguimiento y detección de objetos en proyectos de visión por computadora.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/roboflow/supervision)
- [Leer en turco →](https://trescout.com/discover/supervision/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-09: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/supervision/
