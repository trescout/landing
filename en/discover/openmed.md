# Open Source artificial intelligence in healthcare

OpenMed is a platform that brings together open source artificial intelligence models and data sets used in healthcare. Developed for medical-oriented applications, this Python-based library aims to standardize health data processing processes.

- ★ 5,076
- Python
- GitHub Trending · 2026-06-10

## What you get
- Extracts structured medical insights from clinical texts.
- Anonymizes personal health data on the device.
- It runs more than 1,000 medical AI models offline.

## Installation
**Basic Setup**

```
pip install "openmed[hf]"
```

**Apple Silicon (MLX) Support**

```
pip install "openmed[mlx]"
```


## Running it
**Simple Analysis with Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```


## If you don't write code
I want to analyze medical text using the OpenMed library. I have Python installed on my device. First of all, I completed the installation with the pip install "openmed[hf]" command. Now, what functions should I call in my Python code to analyze my clinical notes and detect medical terms or personal data (PII) in them? Please create me a simple sample code block on model selection and printing the outputs.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/openmed/
