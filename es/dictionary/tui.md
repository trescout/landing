# ¿Qué es TUI?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

> Text User Interface

TUI (Text User Interface / Interfaz de Usuario de Texto) es una interfaz de usuario centrada en el teclado que funciona con bloques de texto y caracteres en pantallas de terminal sin necesidad de una tarjeta gráfica.

## Marco conceptual, etimología y evolución de la terminal

El término TUI es la abreviatura de la expresión en inglés Text User Interface (o, en ocasiones, Terminal User Interface). En la historia de las interfaces informáticas, es un paradigma visual híbrido que tiende un puente entre la CLI (interfaz de línea de comandos) y la GUI (interfaz gráfica de usuario):

- CLI (Interfaz de línea de comandos): Es un flujo unidimensional en el que el usuario introduce un comando de una sola línea y el sistema responde a dicho comando con una salida de texto.
- GUI (Interfaz Gráfica de Usuario): Es una interfaz visual enriquecida que utiliza píxeles, ventanas, cursores de ratón y tarjetas aceleradoras gráficas (GPU).
- TUI (Text User Interface): Es una interfaz basada en menús que, en lugar de píxeles, utiliza una cuadrícula de caracteres bidimensional compuesta por filas y columnas en la pantalla de la terminal, y que incluye ventanas, botones, barras de estado y formularios.

Las raíces de la TUI se remontan a los terminales de texto físicos de la década de 1970, como el TeleType (TTY) y el DEC VT100. En estos terminales, se desarrollaron las secuencias de escape ANSI (ANSI Escape Sequences; por ejemplo, \033[2J limpia la pantalla, \033[31m pone el texto en rojo) para imprimir texto en color en coordenadas específicas de la pantalla y mover el cursor.

***Analogía:** En lugar de la pantalla OLED táctil de alta resolución de un teléfono inteligente moderno (GUI), es como los paneles de letras mecánicos (pantallas de solapa dividida) en los aeropuertos o los marcadores de caracteres digitales. Solo puede haber una letra o símbolo en cada casilla, pero la disposición organizada de estos símbolos crea un panel de control impecable y de respuesta instantánea.*

## Arquitectura técnica: Modo raw, secuencias de escape ANSI y doble búfer

El funcionamiento en segundo plano de una aplicación TUI se basa en tres mecanismos fundamentales a nivel de sistema operativo:

1. Modo sin procesar (Raw Mode) del terminal: El entorno de terminal estándar funciona en "modo procesado" (Cooked Mode); es decir, el sistema operativo retiene y almacena los caracteres en un búfer hasta que el usuario presiona la tecla Enter. Cuando se inicia una aplicación TUI, esta cambia el terminal al "modo sin procesar" mediante la llamada termios. De este modo, cada tecla que presiona el usuario (j, k, Ctrl+C, teclas de dirección) se captura al instante sin esperar a que se pulse Enter.
2. Búfer de pantalla alternativo: El hecho de que tu historial de terminal no desaparezca al abrir htop o vim y que puedas volver a tu línea de comandos anterior al cerrar el programa, ocurre gracias al búfer alternativo (tput smcup / rmcup). La interfaz de usuario basada en texto (TUI) abre su propio lienzo virtual y regresa a la pantalla principal al salir.
3. Doble búfer y renderizado diferencial (Diff Rendering): Para evitar el parpadeo (flickering) en pantalla, los motores TUI modernos mantienen dos matrices de caracteres en memoria: la pantalla actual y la siguiente. Solo se calculan las celdas que cambian y únicamente esas diferencias (diff) se imprimen en la terminal mediante códigos ANSI; de este modo, es posible ejecutar animaciones con una fluidez de 60 FPS.

## El renacimiento moderno de la TUI y las herramientas para desarrolladores

En los últimos años, como reacción al enorme consumo de memoria de las tecnologías web (aplicaciones infladas basadas en Electron), se ha producido un tremendo renacimiento de la TUI en el ecosistema de desarrollo:

- Bajo consumo de recursos: Mientras que una interfaz gráfica consume cientos de megabytes de memoria, una aplicación TUI solo utiliza unos pocos megabytes de RAM.
- Cero latencia a través de SSH: gestionar un servidor remoto en la nube mediante transferencia gráfica (VNC / RDP) requiere un gran ancho de banda; sin embargo, la TUI fluye a la velocidad de la luz dentro de un túnel SSH, incluso en conexiones móviles de baja velocidad.
- Estado de flujo del teclado: Trabajar con las combinaciones de teclas de Vim (h, j, k, l) sin levantar la mano del ratón multiplica la concentración y la productividad de los ingenieros.

Marcos y herramientas modernos destacados:

- El mundo de Rust: las bibliotecas ratatui (anteriormente tui-rs) y crossterm se han convertido en el estándar fundamental de los proyectos TUI modernos gracias a su seguridad de memoria y su rendimiento ultra alto.
- El mundo de Go: bubbletea (un framework reactivo que adapta el patrón The Elm Architecture a la terminal), lipgloss (motor de estilos) y bubbles, desarrollados por el equipo de Charm.
- El mundo de Python: Textual y rich, escritos por Will McGugan.
- Herramientas TUI de culto: lazygit para la gestión de Git, k9s para clústeres de Kubernetes, lazydocker para Docker, btop y htop para la monitorización del sistema, y ncdu para el análisis de disco.

## Suele confundirse con

- CLI vs TUI: CLI es un modelo de preguntas y respuestas de una sola línea (git status, ls -la). TUI, por otro lado, es un panel visual bidimensional que ocupa la ventana de la terminal, con pestañas, listas y atajos de teclado (lazygit, k9s).
- TUI no es solo texto primitivo: las terminales modernas admiten Nerd Fonts (iconos), compatibilidad con TrueColor de 24 bits, caracteres de dibujo de cajas UTF-8 e incluso renderizado de imágenes reales dentro de la terminal mediante los protocolos Kitty Graphics o Sixel.

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

- [CLI](https://trescout.com/es/dictionary/cli/)
- [Terminal](https://trescout.com/es/dictionary/terminal/)
- [Terminal Control](https://trescout.com/es/dictionary/terminal-control/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Assembly](https://trescout.com/es/dictionary/assembly/)
- [Tech Stack](https://trescout.com/es/dictionary/tech-stack/)

## Herramientas relacionadas

- [PI](https://trescout.com/es/discover/pi/)
- [Witr](https://trescout.com/es/discover/witr/)
- [Hister](https://trescout.com/es/discover/hister/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/tui/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/tui/
