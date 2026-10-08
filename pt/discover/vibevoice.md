# Analisando longas gravações de áudio com inteligência artificial

Publicado pela Microsoft, o VibeVoice foi desenvolvido como uma estrutura de IA de voz de código aberto. Com sua estrutura baseada em Python, o sistema permite aos usuários treinar seus próprios modelos de som e integrá-los em suas aplicações.

- ★ 54.502
- GitHub Trending · 2026-06-07

**Nota da TreScout:** O repositório mudou após a publicação: A parte que converte som em texto permanece, a parte que converte texto em som foi retirada. Sua característica distintiva é que ele pode processar registros longos de uma só vez. É um projeto que muda rapidamente. Dê uma olhada no estado atual do armazém antes de adicioná-lo ao seu negócio.

## Atualizações

- **27 de setembro de 2026:** Estrelas 51,860 → 54,502.
- **2 de agosto de 2026:** Estrelas 48,569 → 51,860.

## O que você ganha

- Converte até 60 minutos de gravação de áudio em texto por vez.
- Ele fornece ID do palestrante, carimbo de data/hora e detalhes do conteúdo de forma estruturada.
- Fornece suporte a palavras-chave definidas pelo usuário para termos e nomes personalizados.

## Instalação

**Instalar do GitHub**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```

## Execução

**Demonstração de Gradio**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Transcrição do arquivo**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero analisar a gravação de áudio de 60 minutos que tenho usando o modelo VibeVoice. Preciso recuperar quem são os palestrantes, quando falaram e o conteúdo que disseram em um arquivo de texto estruturado. Quero também adicionar palavras-chave personalizadas para que o modelo reconheça os termos técnicos com mais precisão, como posso estruturar esse processo?

## Termos relacionados do glossário

- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para usuários que desejam converter de forma rápida e estruturada gravações de áudio de longo prazo, resumos de reuniões ou conteúdo de podcast em texto.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/microsoft/VibeVoice)
- [Ler em turco →](https://trescout.com/discover/vibevoice/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-07: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vibevoice/
