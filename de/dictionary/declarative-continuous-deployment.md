# Was ist Declarative Continuous Deployment?

Es ist die Methode, die den Endzustand des Systems definiert und sicherstellt, dass Updates automatisch dieses Ziel erreichen.

## Definition
Es interessiert Sie nicht, wie das System aktualisiert wird, sondern wie das Ergebnis aussehen soll. Sie sagen einfach „Lassen Sie das System in diesem Zustand sein“ und die Tools werden alle notwendigen Schritte unternehmen, um diesen Zustand zu erfassen. Dies verhindert fehlerhafte manuelle Updates.

## So funktioniert es
Sie bereiten eine Konfigurationsdatei vor. Das automatische System liest diese Datei, vergleicht sie mit der aktuellen Situation und nimmt die notwendigen Anpassungen vor, um die Lücke zu schließen.

## Wo es eingesetzt wird
Es wird in cloudbasierten Anwendungen und bei der Verwaltung umfangreicher Server verwendet.

## Häufig verwechselt mit
Es kann mit imperativen (befehlsorientierten) Methoden verwechselt werden; Bei dieser Methode erzählen Sie jeden Schritt einzeln.

## Häufige Fragen
**Warum sollten wir diese Methode wählen?**
Es minimiert menschliche Fehler und stellt sicher, dass das System immer im gewünschten Zustand bleibt.

**Was passiert, wenn ich einen Fehler mache?**
Das System erkennt, dass Sie den falschen Zustand definiert haben und kehrt in der Regel in den alten, funktionierenden Zustand zurück.


## Verwandte Begriffe
- [Cloud Native](/de/dictionary/cloud-native/)
- [Deployment](/de/dictionary/deployment/)

## Verwandte Werkzeuge
- [Argo Cd](/de/discover/argo-cd/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/declarative-continuous-deployment/
