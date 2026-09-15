# Composición editable con inteligencia artificial en la producción musical

YuE es un sistema de generación musical equipado con capacidades como planificación simbólica y generación de covers de disparo cero (zero-shot). Este modelo de IA, que automatiza los procesos de edición musical, le permite gestionar composiciones complejas mediante flujos de trabajo agénticos.

- ★ 8.744
- Python
- GitHub Trending · 2026-09-13

## Qué aporta
- Generación de planes de melodía y acordes a partir de letras y entradas de estilo
- Capacidad de editar notas musicales antes de convertirlas en archivos de audio
- Reinterpretación y edición de canciones existentes en diferentes estilos

## Instalación
**Descarga e instalación del proyecto**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```


## Ejecución
**Creación de canciones con notas editadas**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```


## Si no programa
Quiero crear una canción usando YuE2. Por favor, prepárame un plan de melodía y acordes editable basado en la letra y el estilo musical que deseo. Luego, utiliza este plan para producir una grabación completa de la canción que incluya voces y acompañamiento instrumental. Si tengo un archivo de notación, permíteme usarlo para realizar ediciones.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/yue/
