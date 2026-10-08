# Modelo de linguagem de 64M de parâmetros treinado do zero em duas horas

O MiniMind oferece as etapas de tokenização, pré-treinamento, ajuste fino supervisionado (SFT), LoRA e DPO com código PyTorch simples para desenvolvedores que desejam entender os princípios de funcionamento dos grandes modelos de linguagem (LLM).

- ★ 62.670
- Python
- GitHub Trending · 2026-08-31

## Atualizações

- **27 de setembro de 2026:** Estrelas 55,708 → 62,670, versão mais recente v2 (21 de outubro de 2025).

## O que você ganha

- Treinamento em 2 horas em hardware de consumo: Arquitetura compacta que pode ser treinada do zero em aproximadamente 2 horas em uma única placa de vídeo NVIDIA RTX 3090/4090.
- Ciclo de vida completo de treinamento de LLM: tokenização BPE, pré-treinamento, ajuste fino supervisionado (SFT), adaptação LoRA e pipeline de alinhamento DPO.
- Base de código minimalista e legível: blocos Transformer transparentes escritos em PyTorch puro, sem abstrações complexas de terceiros.
- Suporte a MoE (Mixture of Experts): Possibilidade de experimentar e executar a arquitetura 8x MoE do zero, além de modelos densos.
- Um excelente recurso educacional e pedagógico: o guia ideal para pesquisadores que desejam compreender experimentalmente o funcionamento interno dos grandes modelos de linguagem.

## Instalação

**Clonando o repositório e instalando dependências**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

## Execução

**Iniciando o pré-treinamento e testando a saída do modelo**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```

## Arquitetura técnica e princípio de funcionamento

- Ativações RoPE e SwiGLU: Padrões de arquitetura modernos com embeddings posicionais rotacionais (Rotary Position Embeddings) e funções de ativação SwiGLU.
- Fluxo de Gradiente Estável com RMSNorm: Uso da normalização de camada RMSNorm, que é mais rápida e estável do que a LayerNorm tradicional.
- Integração do Flash Attention: Otimização do Flash Attention v2 para calcular rapidamente grandes matrizes de atenção na memória da GPU.

## Fases de treinamento: Pré-treinamento, SFT e DPO

- Etapa 1 - Pré-treinamento (1-pretrain.py): Aprende gramática e conhecimentos gerais de mundo com a lógica de predição do próximo token em textos brutos.
- Etapa 2 - Ajuste Fino Supervisionado (2-sft.py): Transforma o modelo em um assistente que obedece a comandos do usuário usando conjuntos de dados de perguntas e respostas e instruções.
- Etapa 3 - Alinhamento DPO (4-dpo.py): Otimiza o modelo diretamente de acordo com as preferências do usuário por meio de pares de respostas boas e ruins.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero treinar um modelo de linguagem de 64M de parâmetros do zero com PyTorch usando o repositório MiniMind. Você poderia explicar passo a passo como preparar o tokenizer para meu próprio conjunto de dados de texto em turco, como executar o script 1-pretrain.py e, em seguida, como fazer o ajuste fino com LoRA?

## Perguntas frequentes

- Quanto VRAM é necessário para treinar o MiniMind? O modelo de 64M de parâmetros pode ser treinado confortavelmente com uma VRAM entre 6GB e 12GB, dependendo da configuração do tamanho do lote (batch size); até mesmo uma RTX 3060 ou RTX 4060 é suficiente.
- Funciona no Apple Silicon (série M do Mac)? Sim. O treinamento e a inferência também podem ser realizados em computadores Mac com a aceleração PyTorch MPS (Metal Performance Shaders).
- As saídas do modelo são suficientes para uma conversa casual? O 64M é um modelo pequeno; ele foi otimizado para demonstrar a estrutura da linguagem, responder a perguntas básicas e realizar a conclusão de texto, em vez de raciocínio lógico complexo.
- Quais conjuntos de dados vêm prontos? O repositório oferece comandos de download automático para conjuntos de dados abertos filtrados para pré-treinamento e SFT em chinês e inglês.

## Termos relacionados do glossário

- [Tokenizer](https://trescout.com/pt/dictionary/tokenizer/)
- [LoRA](https://trescout.com/pt/dictionary/lora/)
- [VRAM](https://trescout.com/pt/dictionary/vram/)
- [Attention](https://trescout.com/pt/dictionary/attention/)
- [Transformer](https://trescout.com/pt/dictionary/transformer/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)

- **Para quem é:** Pesquisadores de inteligência artificial, engenheiros de aprendizado de máquina, cientistas de dados e estudantes.
- **Licença:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Framework LLM Minimalista Baseado em PyTorch
- **Plataformas:** Linux, macOS (Apple Silicon MPS), Windows

## Links

- [Repositório no GitHub →](https://github.com/jingyaogong/minimind)
- [Ler em turco →](https://trescout.com/discover/minimind/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-31: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/minimind/
