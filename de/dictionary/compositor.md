# Was ist Compositor?

*Entwicklung · Zuletzt aktualisiert: 3. November 2026*

Es handelt sich um die Software-Schicht, die steuert, wo Fenster auf dem Bildschirm angezeigt werden und wie sie visuell miteinander interagieren.

## Definition

Er ist im Betriebssystem verantwortlich für das Zeichnen von Fenstern, Transparenzeffekte, Schatten und Sichtbarkeitsberechnungen, wenn sich Fenster überlappen. Moderne Strukturen, die herkömmliche Fenster Manager ersetzen, erhöhen sowohl die visuelle Qualität als auch sorgen sie dafür, dass sich Fenster flüssig bewegen, indem sie die Leistung der Grafikkarte nutzen. Die Software führt die von den Fenstern kommenden Bilder zusammen und sendet das finale Pixel-Ergebnis an den Monitor.

***Analogie:** Er ist wie der Bühnenregisseur, der auf einer Theaterbühne festlegt, welche Kulisse vorne und welcher Schauspieler hinten steht sowie wen das Licht anstrahlt.*

## So funktioniert es

Er sammelt die Grafikdaten von Anwendungen, verarbeitet die Position der Fenster sowie visuelle Effekte und lässt die Grafikkarte das finale Bild zeichnen.

## Wo es eingesetzt wird

Er ist in Linux-Grafikservern, dem Wayland-Protokoll und der grafischen Kernarchitektur moderner Desktop-Betriebssysteme enthalten.

## Häufig verwechselt mit

Er wird oft direkt mit dem Grafikkartentreiber verwechselt, aber während der Treiber die Hardware verwaltet, organisiert der Compositor die visuellen Ebenen.

## Fragen und Antworten

**Belastet er die Grafikkarte?**

Auf moderner Hardware ist er äußerst leichtgewichtig und entlastet den Prozessor, indem er die Last auf die Grafikkarte verlagert.

**Warum ist es wichtig?**

Er verhindert das Flackern beim Verschieben von Fenstern und sorgt dafür, dass moderne visuelle Effekte reibungslos funktionieren.

## Verwandte Begriffe

- [Dynamic Tiling](https://trescout.com/de/dictionary/dynamic-tiling/)
- [TUI](https://trescout.com/de/dictionary/tui/)
- [User Interface](https://trescout.com/de/dictionary/user-interface/)

## Verwandte Werkzeuge

- [Hyprland](https://trescout.com/de/discover/hyprland/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/compositor/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/compositor/
