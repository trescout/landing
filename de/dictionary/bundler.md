# Was ist Bundler?

Ein Bundler (Modul-Bündler) ist ein Entwicklungstool, das im modernen Web- und Softwareentwicklungs-Ökosystem Quellcodes (JavaScript, TypeScript, CSS, HTML, Grafik- und Schriftart-Assets), die in Hunderte unabhängige Teile unterteilt sind, sowie externe Bibliotheksabhängigkeiten analysiert und diese Assets in optimierte Dateipakete (Bundles) umwandelt, die von Browsern am schnellsten und effizientesten ausgeführt werden können.

## Was bedeutet Bundler und warum ist er entstanden?
In den Anfangsjahren des Webs bestanden Websites aus wenigen <script>-Tags, die nacheinander in HTML eingebunden wurden. Doch als Webanwendungen so komplex wie Desktop-Software wurden und zu riesigen Codebasen aus Tausenden von Modulen heranwuchsen, traten ernsthafte strukturelle Hindernisse auf:

## Wie funktioniert ein Bundler? Eine tiefgehende Architektur
Die Funktionsweise eines modernen Bundlers besteht im Grunde aus drei Phasen:

## Kritische Optimierungstechniken

## Vergleich des Bundler-Ökosystems
Die herausragenden Werkzeuge im Web-Ökosystem, die auf unterschiedliche Bedürfnisse reagieren, sind:

## Häufige Fragen
**Was ist ein Bundler und warum ist er in der modernen Webentwicklung unverzichtbar?**
Ein Bundler ist ein Werkzeug, das Hunderte von modularen Quelldateien, Bildern und Stildateien, die vom Entwickler geschrieben wurden, in Pakete umwandelt, die der Browser einzeln und optimiert verarbeiten kann. Er gilt in modernen Projekten als unverzichtbar für die Optimierung der Dateigröße, die Reduzierung von Netzwerkanfragen und die Browserkompatibilität.

**Was ist der Hauptunterschied zwischen Webpack und Vite?**
Webpack kompiliert das gesamte Projekt auch in der Entwicklungsumgebung und erstellt ein einziges Paket im Speicher; je größer das Projekt, desto länger die Startzeit. Vite hingegen nutzt in der Entwicklungsumgebung die native ES-Modul-Unterstützung (Native ESM) des Browsers und kompiliert Dateien nur dann, wenn der Browser sie anfordert, wodurch es unabhängig von der Projektgröße sofort startet.

**Was ist Tree-Shaking und warum funktioniert es nur mit ES-Modulen?**
Tree-Shaking ist das Entfernen von Funktionen und Codeblöcken, die im Projekt nie verwendet werden, aus dem endgültigen Paket. Dieser Vorgang kann nur sicher im ESM-Format durchgeführt werden, das über eine statische Syntax wie import und export verfügt; eine vollständige Analyse von dynamisch aufrufbarem CommonJS-Code (require()) ist in der Kompilierungsphase nicht möglich.

**Was ist der Unterschied zwischen einem Transpiler (Babel, SWC) und einem Bundler?**
Ein Transpiler wandelt nur die Syntax des Codes um (z. B. modernen TypeScript- oder ES6+-Code in ES5). Ein Bundler hingegen führt diese umgewandelten, unabhängigen Dateien zusammen, indem er ihre Abhängigkeitsbeziehungen auflöst und sie unter einem Dach bündelt.

**Was bewirkt Code-Splitting?**
Es ermöglicht, dass der Anwendungscode in fragmentierte Dateien statt in eine einzige große Datei aufgeteilt wird. Der Benutzer lädt nur den Code der Seite herunter, die er gerade betrachtet, was die anfängliche Ladezeit erheblich verkürzt und die Benutzererfahrung verbessert.


## Verwandte Begriffe
- [Bundling](/de/dictionary/bundling/)
- [Compilation](/de/dictionary/compilation/)
- [Frontend Stack](/de/dictionary/frontend-stack/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Webpack](/de/discover/webpack/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/bundler/
