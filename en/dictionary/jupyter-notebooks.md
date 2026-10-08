# What is Jupyter Notebooks?

*Dictionary · Data · Last updated: September 19, 2026*

Jupyter Notebook is an open-source computing environment that combines live code execution in languages ​​such as Python, R, and Julia, rich text, mathematical formulas, and data visualizations into a single interactive web document.

## Birth, philosophy and literary programming

Jupyter Notebooks are the de facto workplace for modern data science, machine learning, and academic research. Project Jupyter, an independent framework, was born in 2014 as an evolution of the IPython (Interactive Python) project started by Fernando Perez in 2001.

The origin of the name is a two-meaning reference:

1. A combination of the letters Julia, Python and R, three pioneering open source languages ​​of scientific computing.
2. Respect for the notebooks kept by astronomer Galileo Galilei while exploring the moons of Jupiter in 1610.

Philosophically, it is based on the principle of "Literate Programming" put forward by computer scientist Donald Knuth: Programs should be written not only for machines to run, but primarily for people to read and follow the train of thought. Jupyter; It combines your hypotheses, code, visual graphs, and conclusions into a single living document.

***Analogy:** A traditional Python script is like a closed factory; You give the raw material and only get the final product without seeing what's inside. Jupyter Notebook, on the other hand, is like a transparent kitchen and a recipe book with step-by-step photos: You add each ingredient one by one, taste it instantly, take a photo and attach your notes right next to it.*

## System architecture: Client, server and kernel

The Jupyter infrastructure operates on a loosely coupled three-layer architecture:

1. Client (Web Interface): JavaScript/HTML5 frontend (JupyterLab or classic interface) that runs in your browser, allowing you to edit and run cells and view output.
2. Jupyter Server (Tornado-based Web Server): The backend running on your local machine or a remote server, managing the file system, coordinating sessions, and providing WebSocket connections.
3. Kernel: It is the isolated language that actually runs the code. For example, ipykernel is used for Python, IRkernel for R, and IJulia for Julia. Communication between the server and the kernel occurs in JSON format over industry standard ZeroMQ messaging sockets.

**Internal Structure of .ipynb File:** Even though Jupyter documents have the extension .ipynb, they are actually hierarchical JSON files. The type of each cell (code, markdown), execution order (execution_count), source code and produced outputs (outputs · text, HTML, PNG graphics in Base64 format) are stored in this JSON object.

## The power of data science and the pitfalls of software engineering

- Exploratory Data Analysis (EDA): Once a massive data set is loaded into memory, data scientists can clean data in different cells, train models, and visualize with Matplotlib/Seaborn/Plotly without repeating the hours-long memory loading phase.
- Hidden State Risk: Executing cells in a random order rather than top-down order (out-of-order execution) may leave variable states invisible in memory. This may cause different results or errors when someone else runs the same notebook ("reproducibility crisis").
- Version Control (Git) Challenges: Since .ipynb files contain rich output and Base64 graphics, it is difficult to examine line differences and resolve merge conflicts on Git. To overcome this problem, tools such as jupytext (tool that syncs notebook with clean Markdown or Python script) and nbdime are used.

## Frequently asked questions

**What does Jupyter Notebook mean and where does its meaning come from?**

Jupyter name; Julia is derived from the first letters of the Python and R programming languages ​​and a reference to astronomer Galileo's Jupiter observation notes. It is an interactive notebook with live code and rich text.

**What is the difference between Jupyter Notebook and a standard Python file (.py)?**

.py files are pure text codes that are compiled and run in a single piece from start to finish. .ipynb, on the other hand, is a JSON structure that can run the code in segmented cells and stores outputs, tables and graphs directly under the code.

**What is the relationship between Google Colab and Jupyter Notebook?**

Google Colab is a proprietary cloud variant of the Jupyter Notebook infrastructure that runs on the Google cloud, offers free GPU and TPU hardware acceleration, and requires no installation.

**How to ensure clean code and version control in Jupyter Notebook?**

The best approach is to clear the cell outputs (Clear All Outputs) before sending the codes to the repository, re-run the cells sequentially from top to bottom, and make the file format versionable with tools such as jupytext.

## Related terms

- [Data Pipeline](https://trescout.com/en/dictionary/data-pipeline/)
- [Markdown](https://trescout.com/en/dictionary/markdown/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Apple Silicon](https://trescout.com/en/dictionary/apple-silicon/)
- [Tech Stack](https://trescout.com/en/dictionary/tech-stack/)

## Related tools

- [Generative AI for Beginners](https://trescout.com/en/discover/generative-ai-for-beginners/)
- [AI-For-Beginners](https://trescout.com/en/discover/ai-for-beginners/)
- [Dive Into Llms](https://trescout.com/en/discover/dive-into-llms/)
- [Claude Cookbooks](https://trescout.com/en/discover/claude-cookbooks/)
- [Airllm](https://trescout.com/en/discover/airllm/)
- [Machine Learning for Trading](https://trescout.com/en/discover/machine-learning-for-trading/)
- [Cosmos](https://trescout.com/en/discover/cosmos/)
- [Train LLM from Scratch](https://trescout.com/en/discover/train-llm-from-scratch/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/jupyter-notebooks/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/jupyter-notebooks/
