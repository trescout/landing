# Herramientas para proyectos de visión por computadora.

Desarrollado por Roboflow, Supervision ofrece herramientas y funciones auxiliares reutilizables para proyectos de visión por computadora. Esta biblioteca basada en Python acelera los flujos de trabajo de desarrollo al facilitar operaciones estándar en procesos como la detección y el seguimiento de objetos.

- ★ 49.757
- Python
- GitHub Trending · 2026-06-09

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
Instalé la biblioteca con el comando de supervisión pip install en un entorno Python 3.9 o superior. Quiero visualizar los resultados de la detección de objetos y administrar mi conjunto de datos en mi proyecto de visión por computadora. ¿Cómo puedo marcar los resultados de la detección de objetos en una imagen usando la biblioteca de Supervisión y cómo puedo cargar y convertir conjuntos de datos en diferentes formatos (COCO, YOLO, etc.)? Ayúdenme a crear un flujo de trabajo de muestra utilizando el anotador y las herramientas auxiliares de conjunto de datos proporcionadas por la biblioteca.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/supervision/
