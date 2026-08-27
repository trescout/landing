# Ferramentas para projetos de visão computacional

Desenvolvido pela Roboflow, o Supervision oferece ferramentas e funções auxiliares reutilizáveis para projetos de visão computacional. Esta biblioteca baseada em Python acelera os fluxos de trabalho de desenvolvimento, facilitando operações padrão em processos como detecção e rastreamento de objetos.

- ★ 49.757
- Python
- GitHub Trending · 2026-06-09

## O que você ganha
- Ele acelera os processos de carregamento e processamento de dados em projetos de visão computacional.
- Ele simplifica o desenvolvimento de aplicativos padronizando operações como detecção e rastreamento de objetos.
- Ele fornece visualização e gerenciamento de conjuntos de dados, funcionando de forma compatível com diferentes bibliotecas de modelos.

## Instalação
**Instalação do pacote**

```
pip install supervision
```


## Execução
**Marcando um objeto na imagem**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```


## Se você não programa
Instalei a biblioteca com o comando pip install supervision em um ambiente Python 3.9 ou superior. Quero visualizar os resultados da detecção de objetos e gerenciar meu conjunto de dados em meu projeto de visão computacional. Como posso marcar os resultados da detecção de objetos em uma imagem usando a biblioteca Supervision e como posso carregar e converter conjuntos de dados em diferentes formatos (COCO, YOLO, etc.)? Ajude-me a criar um fluxo de trabalho de amostra usando as ferramentas auxiliares de anotador e conjunto de dados fornecidas pela biblioteca.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/supervision/
