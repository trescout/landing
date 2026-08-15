# Produce sonidos naturales y suaves

MOSS-TTS (MOSI.AI y OpenMOSS); Es una familia de modelos de código abierto que proporciona reproducción de voz y sonido de alta fidelidad. Ofrece soluciones para escenarios como síntesis de voz de texto largo, soporte para múltiples hablantes y transmisión en tiempo real.

- ★ 3.939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## ¿Qué ofrece?
- Proporciona voz y síntesis de voz de alta fidelidad.
- Ofrece soporte para varios altavoces.
- Admite transmisión de audio en tiempo real.
- Se basa en la familia de modelos de código abierto.

## ¿Cómo instalar, cómo utilizar?
**Crear entorno conda**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Clonar e instalar el repositorio**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Ejecute la demostración de Gradio**

```
python clis/moss_tts_app.py
```


## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/moss-tts/
