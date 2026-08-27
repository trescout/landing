# Verwalten Sie Kontakte in Physiksimulationen

PPF Contact Solver ist als Physik-Engine von ZOZO darauf ausgelegt, Kontakte zwischen Stoff, Festkörper und Seil in physikbasierten Simulationen zu lösen. Es erhöht die physikalische Konsistenz in Simulationen, indem es das Zusammenspiel verschiedener Geometrien berechnet. Dank des Blender-Plug-Ins kann es auch aus der Ferne ausgeführt werden.

- ★ 4.427
- Python
- Apache-2.0
- GitHub Trending · 26 May 2026

## Installation
**GPU-Container starten**

```
docker run --rm -it --name ppf-contact-solver --gpus all -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEB_PORT=8080 ghcr.io/st-tech/ppf-contact-solver-compiled:latest
```


## Was macht es?
- Es führt realistische Stoff-, Festkörper- und Seilsimulationen durch.
- Erhöht die physikalische Konsistenz in Simulationen.
- Es kann über Blender ferngesteuert werden.
- Es handelt sich um eine forschungsbasierte Lösung (ZOZOs eigene Physik-Engine).

## Für wen ist es nicht geeignet?
Dies ist keine Endbenutzeranwendung. Für die Nutzung sind Kenntnisse in Programmierung und physikalischer Simulation erforderlich. Es spricht eher den Grafik-/Forschungsbereich an.

## Wie installiere ich, wie verwende ich?
Führen Sie den physikalischen Kontaktlöser ppf-contact-solver von ZOZO mit Docker aus (NVIDIA-GPU erforderlich): Führen Sie den folgenden Docker-Befehl aus, öffnen Sie dann http://localhost:8080 im Browser und probieren Sie die vorgefertigten JupyterLab-Beispiele aus.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ppf-contact-solver/
