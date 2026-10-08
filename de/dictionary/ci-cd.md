# Was ist CI/CD?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> Continuous Integration / Continuous Deployment

CI/CD (Continuous Integration / Continuous Deployment) ist das automatische Testen und Freigeben des Codes.

## Definition und Wortherkunft

Dabei handelt es sich um eine automatische Linie, die dafür sorgt, dass der geschriebene Code fehlerfrei beim Benutzer ankommt. CI stellt den Code ständig zusammen, testet ihn und überträgt ihn auf eine Live-CD. Die Ära der manuellen Veröffentlichungen geht zu Ende.

***Analogie:** Es ist wie ein Klebeband, das dafür sorgt, dass das Essen in der Restaurantküche zubereitet, den Geschmackstest bestanden und dem Kunden serviert wird.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Team:** Test nach jedem Commit.
**Mobile:** Automatische Freigabe zur Aufbewahrung.
**Web:** Bei Kombination freigeben.

## Technische Tiefe und Architektur

Linienstufen:

**Fussel:** Stilkontrolle.
**Test:** Einheit und Ende an Ende.
**Kompilierung:** Paketproduktion.
**Veröffentlichung:** Allmähliche Öffnung.

Beispielschritt:

```
steps:
  - run: npm ci
  - run: npm test
```

In kritischen Publikationen wird ein manuelles Genehmigungstor platziert. Unterschied zur Lieferung: Lieferung wird vorbereitet, Bereitstellung wird gedruckt. Der Erste wartet, der Zweite geht.

## Häufig gemischte Dinge

Es wird davon ausgegangen, dass es sich um einen manuellen Test handelt. Allerdings läuft der Ablauf völlig automatisch ab: Der Code kommt, der Test läuft, das Ergebnis kommt raus. Man wartet einfach an der Tür.

## Einsatz in verschiedenen Disziplinen

**Küchenband:** Zubereitung, Verkostung und Service.
**Fließband:** Teil, Inspektion und Verpackung.
**Gepäckband:** Registrieren, Durchsuchen und Hochladen.

## Häufig gestellte Fragen

**Warum ist es so wichtig?**

Es übersetzt den fehlerhaften Code live und erhöht die Geschwindigkeit. Häufiges Senden ist sicher.

**Sollte es immer automatisch sein?**

Im Allgemeinen ja, die manuelle Tür wird in der kritischen Version hinzugefügt.

**Was ist der Unterschied zur Lieferung?**

Die Lieferung bereitet sich vor und wartet, der Einsatz erfolgt und geht. Der erste ist zugelassen, der zweite ist vollautomatisch.

**Was passiert, wenn es kaputt geht?**

Die Leitung stoppt und die Übertragung wird unterbrochen. Deshalb sind ein Backup-Plan und eine schnelle Wiederherstellung unerlässlich.

## Verwandte Begriffe

- [Continuous Integration](https://trescout.com/de/dictionary/continuous-integration/)
- [Continuous Deployment](https://trescout.com/de/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [QA](https://trescout.com/de/dictionary/qa/)

## Verwandte Werkzeuge

- [Free for Dev](https://trescout.com/de/discover/free-for-dev/)
- [Strix](https://trescout.com/de/discover/strix/)
- [Googletest](https://trescout.com/de/discover/googletest/)
- [Trivy](https://trescout.com/de/discover/trivy/)
- [Openship](https://trescout.com/de/discover/openship/)
- [Ipatool](https://trescout.com/de/discover/ipatool/)
- [Checkstyle](https://trescout.com/de/discover/checkstyle/)
- [Flue](https://trescout.com/de/discover/flue/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/ci-cd/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/ci-cd/
