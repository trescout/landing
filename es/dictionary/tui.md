# ¿Qué es TUI?

> Text User Interface

TUI (Text User Interface / Interfaz de Usuario de Texto) es una interfaz de usuario centrada en el teclado que funciona con bloques de texto y caracteres en pantallas de terminal sin necesidad de una tarjeta gráfica.

## Marco conceptual, etimología y evolución de la terminal
El término TUI es la abreviatura de la expresión en inglés Text User Interface (o, en ocasiones, Terminal User Interface). En la historia de las interfaces informáticas, es un paradigma visual híbrido que tiende un puente entre la CLI (interfaz de línea de comandos) y la GUI (interfaz gráfica de usuario):

## Arquitectura técnica: Modo raw, secuencias de escape ANSI y doble búfer
El funcionamiento en segundo plano de una aplicación TUI se basa en tres mecanismos fundamentales a nivel de sistema operativo:

## El renacimiento moderno de la TUI y las herramientas para desarrolladores
En los últimos años, como reacción al enorme consumo de memoria de las tecnologías web (aplicaciones infladas basadas en Electron), se ha producido un tremendo renacimiento de la TUI en el ecosistema de desarrollo:

## Suele confundirse con

## Preguntas frecuentes
**¿Qué significa TUI y cuál es su abreviatura?**
TUI es la abreviatura de Text User Interface (Interfaz de Usuario de Texto) o Terminal User Interface (Interfaz de Usuario de Terminal). Define interfaces visuales e interactivas que funcionan sobre la cuadrícula de caracteres del terminal sin un gestor de ventanas gráfico.

**¿Cuáles son las diferencias fundamentales entre CLI, GUI y TUI?**
La CLI funciona con comandos de texto de una sola línea; la GUI se gestiona mediante píxeles, ventanas y ratón; mientras que la TUI es un formato híbrido que funciona dentro de la terminal con menús, paneles y cuadros orientados al teclado.

**¿Cómo dibujan la pantalla las interfaces de usuario de terminal?**
A través de secuencias de escape ANSI y códigos de control de terminal, el cursor se mueve a la fila y columna deseada de la pantalla, se asignan códigos de color y se dibujan caracteres de cuadro Unicode.

**¿Cuáles son las bibliotecas más populares para desarrollar TUI modernas?**
En el ecosistema de Rust, ratatui; en el lenguaje Go, bubbletea y lipgloss; y en el lado de Python, las bibliotecas Textual y rich son el estándar de la industria.


## Términos relacionados
- [CLI](/es/dictionary/cli/)
- [Terminal](/es/dictionary/terminal/)
- [Terminal Control](/es/dictionary/terminal-control/)
- [Runtime](/es/dictionary/runtime/)
- [Assembly](/es/dictionary/assembly/)
- [Tech Stack](/es/dictionary/tech-stack/)

## Herramientas relacionadas
- [PI](/es/discover/pi/)
- [Witr](/es/discover/witr/)
- [Hister](/es/discover/hister/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/tui/
