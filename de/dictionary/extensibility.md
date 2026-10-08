# Was ist Extensibility?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Unter Erweiterbarkeit versteht man die Fähigkeit einer Software, mit Plug-Ins und Modulen neue Fähigkeiten zu erlangen, ohne ihren Hauptcode anzutasten.

## Definition und Wortherkunft

Der Begriff „Extensibility“ leitet sich vom englischen Wurzelwort „extend“ ab. Es hängt eng mit dem Open-Closed-Prinzip in der Softwareentwicklung zusammen: Ein Modul sollte offen für Erweiterungen, aber geschlossen für Änderungen sein. Wenn also eine neue Funktion benötigt wird, fügen Sie dem System einfach einen neuen Teil hinzu, anstatt den vorhandenen Code zu zerstören.

***Analogie:** Es ist wie ein Schweizer Taschenmesser; Der Körper bleibt derselbe, Sie können einen neuen Schraubenzieher- oder Taschenlampeneinsatz hinzufügen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

Als Endbenutzer stoßen Sie täglich auf Erweiterbarkeit:

**Browser-Add-ons:** Installieren Sie einen Werbeblocker oder Passwort-Manager in Ihrem Browser.
**Editor-Plugins:** Sie müssen das Python- oder Prettier-Plugin in VS Code hinzufügen.
**Inhaltssysteme:** Installieren Sie ein Kontaktformular oder ein Caching-Plugin auf Ihrer WordPress-Site.
**Design-Tools:** Sie installieren ein fertiges Komponentenpaket aus der Figma-Community.

## Technische Tiefe und Architektur

Der Kern eines erweiterbaren Systems ist klein, seine Umgebung wächst durch Erweiterungen. Typische Teile dieser Architektur sind:

**Plugin-Schnittstelle (Plugin-API):** Es ist die kontrollierte Tür, die der Kernel für Erweiterungen öffnet. Das Plugin berührt das System nur über diese Schnittstelle.
**Hook- und Event-System (Hooks & Events):** Der Kernel sendet zu bestimmten Zeitpunkten Ereignisse. Plugins abonnieren diese Ereignisse.
**Manifestdatei (Manifest):** Jedes Plugin enthält eine kleine Datei, die seinen Namen, seine Version und die angeforderten Berechtigungen angibt. Das System installiert das Plugin nicht, das den Regeln nicht entspricht.
**Sandbox und Berechtigungen:** Der Zugriff auf Plugins ist begrenzt. Auf diese Weise kann ein fehlerhaftes Plugin nicht das gesamte System zum Absturz bringen.
**Versionskompatibilität:** Die Schnittstelle muss beim Aktualisieren des Kernels abwärtskompatibel bleiben. Andernfalls gehen die Plugins kaputt.

Hier ist ein kleines Beispiel, eine typische Plugin-Deklaration:

```
{
  "name": "ornek-eklenti",
  "version": "1.0.0"
}
```

## Einsatz in verschiedenen Disziplinen

**Architektur:** Vorgefertigte Strukturen, bei denen neue Module hinzugefügt werden können, ohne die tragenden Wände zu berühren.
**Produktion:** Küchenmaschinen, bei denen verschiedene Aufsätze am selben Gehäuse befestigt werden können.
**Spiel:** Mod-Communitys, die neue Karten und Missionen hinzufügen, ohne das Hauptspiel zu ändern.

## Häufig gestellte Fragen

**Ist jede Software erweiterbar?**

Nein. Wenn die Software nicht von Anfang an mit dieser Flexibilität ausgestattet ist, ist das spätere Hinzufügen von Plug-in-Unterstützung oft teuer und riskant.

**Was ist der Unterschied zwischen einem Plugin und einem Fork?**

Sie kopieren nicht den Hauptcode im Plugin, sondern stellen von außen eine Verbindung zum System her. Beim Forken kopieren Sie den gesamten Code und wechseln zu einem separaten Pfad.

**Sind Plugins sicher?**

Es variiert je nach Quelle. Wählen Sie aktuelle und weit verbreitete Plugins aus offiziellen Stores. Seien Sie vorsichtig bei Plugins, die unnötige Berechtigungen anfordern.

**Reduziert Erweiterbarkeit die Leistung?**

Jedes Plugin verursacht eine gewisse Belastung. Wenn Sie wenige und gut gepflegte Plug-Ins verwenden, ist der Effekt oft nicht spürbar.

## Verwandte Begriffe

- [Plugin](https://trescout.com/de/dictionary/plugin/)
- [API](https://trescout.com/de/dictionary/api/)
- [Framework](https://trescout.com/de/dictionary/framework/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/extensibility/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/extensibility/
