# Administrar contactos en simulaciones de física

PPF Contact Solver, como motor de física de ZOZO, está diseñado para resolver contactos entre tela, sólido y cuerda en simulaciones basadas en física. Aumenta la consistencia física en las simulaciones calculando la interacción de diferentes geometrías. También se puede ejecutar de forma remota gracias al complemento Blender.

- ★ 4.404
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## ¿Qué hace?
- Realiza simulaciones realistas de telas, objetos sólidos y cuerdas.
- Aumenta la consistencia física en las simulaciones.
- Se puede operar de forma remota a través de Blender.
- Es una solución basada en la investigación (el propio motor de física de ZOZO).

## ¿Para quién no es adecuado?
Esta no es una aplicación de usuario final. Se requieren conocimientos de programación y simulación física para su uso; Atrae más al campo de los gráficos/investigación.

## ¿Cómo instalar, cómo utilizar?
**Inicie con Docker (se requiere GPU NVIDIA)**

```
docker run --rm -it --name ppf-contact-solver --gpus all \
  -p 8080:8080 -p 9090:9090 -e WEB_PORT=8080 \
  ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```


## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ppf-contact-solver/
