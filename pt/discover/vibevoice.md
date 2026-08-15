# Analisando longas gravações de áudio com inteligência artificial

Publicado pela Microsoft, o VibeVoice foi desenvolvido como uma estrutura de IA de voz de código aberto. Com sua estrutura baseada em Python, o sistema permite aos usuários treinar seus próprios modelos de som e integrá-los em suas aplicações.

- ★ 51.860
- GitHub Trending · 2026-06-07

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
Quero analisar a gravação de áudio de 60 minutos que tenho usando o modelo VibeVoice. Preciso recuperar quem são os palestrantes, quando falaram e o conteúdo que disseram em um arquivo de texto estruturado. Quero também adicionar palavras-chave personalizadas para que o modelo reconheça os termos técnicos com mais precisão, como posso estruturar esse processo?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vibevoice/
