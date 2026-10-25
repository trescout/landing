# Tools for computer vision projects

Developed by Roboflow, Supervision offers reusable auxiliary tools and functions for computer vision projects. This Python-based library accelerates development workflows by facilitating standard operations in processes such as object detection and tracking.

- ★ 51,348
- Python
- GitHub Trending · 2026-06-09

## Updates

- **October 25, 2026:** Stars 51,253 → 51,348, latest release 0.31.2 (October 24, 2026).
- **October 21, 2026:** Stars 51,223 → 51,253, latest release 0.31.1 (October 20, 2026).
- **October 17, 2026:** Stars 51,154 → 51,223, latest release 0.31.0 (October 16, 2026).
- **October 8, 2026:** Stars 51,146 → 51,154, latest release 0.30.9 (October 8, 2026).

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

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I installed the library with the pip install supervision command in a Python 3.9 or above environment. I want to visualize object detection results and manage my dataset in my computer vision project. How can I mark object detection results on an image using the Supervision library and how can I load and convert datasets in different formats (COCO, YOLO, etc.)? Please help me create a sample workflow using the annotator and dataset helper tools provided by the library.

Repository: https://github.com/roboflow/supervision. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Computer Vision](https://trescout.com/en/dictionary/computer-vision/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for Python developers who want to standardize object detection and tracking processes in computer vision projects.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/roboflow/supervision)
- [Read in Turkish →](https://trescout.com/discover/supervision/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-09: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/supervision/
