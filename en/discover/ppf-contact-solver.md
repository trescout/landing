# Manage Contacts in Physics Simulations

PPF Contact Solver, as ZOZO's physics engine, is designed to solve contacts between fabric, solid and rope in physics-based simulations. It increases physical consistency in simulations by calculating the interaction of different geometries. It can also be run remotely thanks to the Blender plug-in.

- ★ 4,404
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## What does it do?
- It performs realistic fabric, solid object and rope simulations.
- Increases physical consistency in simulations.
- It can be operated remotely via Blender.
- It is a research-driven solution (ZOZO's own physics engine).

## Who is it not suitable for?
This is not an end-user application. Knowledge of programming and physics simulation is required to use; It appeals more to the graphics/research field.

## How to install, how to use?
**Launch with Docker (NVIDIA GPU required)**

```
docker run --rm -it --name ppf-contact-solver --gpus all \
  -p 8080:8080 -p 9090:9090 -e WEB_PORT=8080 \
  ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```


## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ppf-contact-solver/
