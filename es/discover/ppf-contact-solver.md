# Administrar contactos en simulaciones de física

PPF Contact Solver, como motor de física de ZOZO, está diseñado para resolver contactos entre tela, sólido y cuerda en simulaciones basadas en física. Aumenta la consistencia física en las simulaciones calculando la interacción de diferentes geometrías. También se puede ejecutar de forma remota gracias al complemento Blender.

- ★ 4.514
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## Actualizaciones

- **1 de octubre de 2026:** Estrellas 4,513 → 4,514, última versión addon-2026-10-01-2043 (1 de octubre de 2026).
- **1 de octubre de 2026:** Estrellas 4,507 → 4,513, última versión addon-2026-10-01-0946 (1 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 4,508 → 4,507, última versión addon-2026-09-27-2158 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 4,490 → 4,508, última versión addon-2026-09-22-2204 (22 de septiembre de 2026).

## Instalación

**Iniciar contenedor GPU**

```
docker run --rm -it --name ppf-contact-solver --gpus all -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEB_PORT=8080 ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```

## ¿Qué hace?

- Realiza simulaciones realistas de telas, objetos sólidos y cuerdas.
- Aumenta la consistencia física en las simulaciones.
- Se puede operar de forma remota a través de Blender.
- Es una solución basada en la investigación (el propio motor de física de ZOZO).

## ¿Para quién no es adecuado?

Esta no es una aplicación de usuario final. Se requieren conocimientos de programación y simulación física para su uso; Atrae más al campo de los gráficos/investigación.

## ¿Cómo instalar, cómo utilizar?

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Ejecute el solucionador de contactos físicos ppf-contact-solver de ZOZO con Docker (se requiere GPU NVIDIA): ejecute el siguiente comando de Docker, luego abra http://localhost:8080 en el navegador y pruebe los ejemplos de JupyterLab ya preparados.

## Términos relacionados del glosario

- [Container](https://trescout.com/es/dictionary/container/)
- [Localhost](https://trescout.com/es/dictionary/localhost/)
- [GPU](https://trescout.com/es/dictionary/gpu/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Usuarios técnicos, investigadores que realizan simulaciones gráficas/físicas.
- **dificultad:** Técnico avanzado/centrado en la investigación.
- **Que ofertas:** Solución de contacto de tela/sólido/cuerda
- **Funciona:** Complemento Python + Blender
- **Tarifa:** Gratis · código abierto (Apache-2.0)

**Licencia:** Apache-2.0 · puedes usarlo libremente, modificarlo, hacer uso comercial (también incluye protección por patente).

## Enlaces

- [Repositorio en GitHub →](https://github.com/st-tech/ppf-contact-solver)
- [Leer en turco →](https://trescout.com/discover/ppf-contact-solver/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-05-26: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ppf-contact-solver/
