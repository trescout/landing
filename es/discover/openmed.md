# Inteligencia artificial de código abierto en la atención sanitaria

OpenMed es una plataforma que reúne modelos de inteligencia artificial de código abierto y conjuntos de datos utilizados en la atención sanitaria. Desarrollada para aplicaciones orientadas a la medicina, esta biblioteca basada en Python tiene como objetivo estandarizar los procesos de procesamiento de datos de salud.

- ★ 5.217
- Python
- GitHub Trending · 2026-06-10

## Qué aporta
- Extrae conocimientos médicos estructurados de textos clínicos.
- Anonimiza los datos de salud personales en el dispositivo.
- Ejecuta más de 1000 modelos médicos de IA sin conexión.

## Instalación
**Configuración básica**

```
pip install "openmed[hf]"
```

**Compatibilidad con Apple Silicon (MLX)**

```
pip install "openmed[mlx]"
```


## Ejecución
**Análisis simple con Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```


## Si no programa
Quiero analizar textos médicos usando la biblioteca OpenMed. Tengo Python instalado en mi dispositivo. En primer lugar, completé la instalación con el comando pip install "openmed[hf]". Ahora bien, ¿qué funciones debo llamar en mi código Python para analizar mis notas clínicas y detectar términos médicos o datos personales (PII) en ellas? Créame un bloque de código de muestra simple sobre la selección del modelo y la impresión de los resultados.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openmed/
