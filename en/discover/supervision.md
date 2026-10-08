# Tools for computer vision projects

Developed by Roboflow, Supervision offers reusable auxiliary tools and functions for computer vision projects. This Python-based library accelerates development workflows by facilitating standard operations in processes such as object detection and tracking.

- ★ 51,154
- Python
- GitHub Trending · 2026-06-09

## Updates

- **October 8, 2026:** Stars 51,146 → 51,154, latest release 0.30.9 (October 8, 2026).
- **October 7, 2026:** Stars 51,118 → 51,146, latest release 0.30.8 (October 6, 2026).
- **October 4, 2026:** Stars 51,075 → 51,118, latest release 0.30.7 (October 4, 2026).
- **September 29, 2026:** Stars 51,054 → 51,075, latest release 0.30.6 (September 29, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I installed the library with the pip install supervision command in a Python 3.9 or above environment. I want to visualize object detection results and manage my dataset in my computer vision project. How can I mark object detection results on an image using the Supervision library and how can I load and convert datasets in different formats (COCO, YOLO, etc.)? Please help me create a sample workflow using the annotator and dataset helper tools provided by the library.

## Related dictionary terms

- [Computer Vision](https://trescout.com/en/dictionary/computer-vision/)
- [Computer Vision](https://trescout.com/en/dictionary/cv/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for Python developers who want to standardize object detection and tracking processes in computer vision projects.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/roboflow/supervision)
- [Read in Turkish →](https://trescout.com/discover/supervision/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-09: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/supervision/
