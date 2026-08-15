# Tools for computer vision projects

Developed by Roboflow, Supervision offers reusable auxiliary tools and functions for computer vision projects. This Python-based library accelerates development workflows by facilitating standard operations in processes such as object detection and tracking.

- ★ 49,033
- Python
- GitHub Trending · 2026-06-09

## What you get
- It accelerates data loading and processing processes in computer vision projects.
- It simplifies application development by standardizing operations such as object detection and tracking.
- It provides visualization and data set management by working compatible with different model libraries.

## Installation
**Package Installation**

```
pip install supervision
```


## Running it
**Marking an Object on the Image**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```


## If you don't write code
I installed the library with the pip install supervision command in a Python 3.9 or above environment. I want to visualize object detection results and manage my dataset in my computer vision project. How can I mark object detection results on an image using the Supervision library and how can I load and convert datasets in different formats (COCO, YOLO, etc.)? Please help me create a sample workflow using the annotator and dataset helper tools provided by the library.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/supervision/
