# Produza sons naturais e suaves

MOSS-TTS (MOSI.AI e OpenMOSS); É uma família de modelos de código aberto que oferece reprodução de voz e som de alta fidelidade. Ele oferece soluções para cenários como síntese de fala de texto longo, suporte para vários alto-falantes e streaming em tempo real.

- ★ 3.939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## O que isso oferece?
- Ele fornece fala de alta fidelidade e síntese de voz.
- Oferece suporte para vários alto-falantes.
- Suporta streaming de áudio em tempo real.
- É baseado na família de modelos de código aberto.

## Como instalar, como usar?
**Criar ambiente conda**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Clone e instale o repositório**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Execute a demonstração do Gradio**

```
python clis/moss_tts_app.py
```


## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/moss-tts/
