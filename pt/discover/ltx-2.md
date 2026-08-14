# Produção de vídeos com inteligência artificial no sistema local

Desenvolvido pela Lightricks, o LTX-2 oferece um pacote de treinamento de inferência Python e adaptação de baixa classificação (LoRA) para modelos de inteligência artificial que produzem áudio e vídeo. Este conjunto de ferramentas permite aos usuários treinar modelos LTX-2 com seus próprios dados e executar saídas de modelo em sistemas locais.

- ★ 8.587
- GitHub Trending · 2026-06-19

## Atualizar
- 12 de agosto de 2026: Star 8.554 → 8.587, versão mais recente v1.2.0 (11 de agosto de 2026).
- 10 de agosto de 2026: Estrela 7.550 → 8.554.

## O que você ganha
- Fornece sincronização de áudio e vídeo
- Você pode treinar LoRA com seus próprios dados
- Produção de vídeo de alta qualidade em sistema local

## Instalação
**Clone o repositório do GitHub e entre no diretório**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Baixe os pesos do modelo (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```


## Execução
**execute pipeline de inferência com uv**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```


## Se você não programa
Crie um vídeo usando o modelo LTX-2 que descreva detalhadamente a cena que desejo e inclua sincronização de áudio e vídeo. Faça com que o modelo produza resultados especificando detalhes da cena, aparência do personagem, ângulo da câmera e texto de fala.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ltx-2/
