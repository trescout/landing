# Ferramentas para projetos de visão computacional

Desenvolvido pela Roboflow, o Supervision oferece ferramentas e funções auxiliares reutilizáveis para projetos de visão computacional. Esta biblioteca baseada em Python acelera os fluxos de trabalho de desenvolvimento, facilitando operações padrão em processos como detecção e rastreamento de objetos.

- ★ 51.154
- Python
- GitHub Trending · 2026-06-09

## Atualizações

- **8 de outubro de 2026:** Estrelas 51,146 → 51,154, versão mais recente 0.30.9 (8 de outubro de 2026).
- **7 de outubro de 2026:** Estrelas 51,118 → 51,146, versão mais recente 0.30.8 (6 de outubro de 2026).
- **4 de outubro de 2026:** Estrelas 51,075 → 51,118, versão mais recente 0.30.7 (4 de outubro de 2026).
- **29 de setembro de 2026:** Estrelas 51,054 → 51,075, versão mais recente 0.30.6 (29 de setembro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Instalei a biblioteca com o comando pip install supervision em um ambiente Python 3.9 ou superior. Quero visualizar os resultados da detecção de objetos e gerenciar meu conjunto de dados em meu projeto de visão computacional. Como posso marcar os resultados da detecção de objetos em uma imagem usando a biblioteca Supervision e como posso carregar e converter conjuntos de dados em diferentes formatos (COCO, YOLO, etc.)? Ajude-me a criar um fluxo de trabalho de amostra usando as ferramentas auxiliares de anotador e conjunto de dados fornecidas pela biblioteca.

## Termos relacionados do glossário

- [Computer Vision](https://trescout.com/pt/dictionary/computer-vision/)
- [Computer Vision](https://trescout.com/pt/dictionary/cv/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores Python que desejam padronizar processos de detecção e rastreamento de objetos em projetos de visão computacional.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/roboflow/supervision)
- [Ler em turco →](https://trescout.com/discover/supervision/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-09: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/supervision/
