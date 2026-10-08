# What is TUI?

*Dictionary · Dev · Last updated: September 19, 2026*

> Text User Interface

TUI (Text User Interface), is a keyboard-driven user interface that operates on terminal screens using text and character blocks without the need for a graphics card.

## Conceptual framework, etymology, and the evolution of the terminal

The term TUI is an abbreviation of the English expression Text User Interface (or Terminal User Interface from time to time). In the history of computer interfaces, it is a hybrid visual paradigm bridging CLI (Command Line Interface) and GUI (Graphical User Interface):

- CLI (Command-Line Interface): A one-dimensional flow where the user enters a single-line command and the system responds to this command with text output.
- GUI (Graphical User Interface): A rich visual interface that uses pixels, windows, mouse cursors, and graphics accelerator cards (GPUs).
- TUI (Text User Interface): A menu-driven interface that uses a two-dimensional character grid consisting of rows and columns on the terminal screen instead of pixels, featuring windows, buttons, status bars, and forms.

The roots of TUI trace back to physical text terminals of the 1970s such as the TeleType (TTY) and DEC VT100. On these terminals, ANSI Escape Sequences (such as \033[2J to clear the screen and \033[31m to make text red) were developed to print colored text at specific screen coordinates and move the cursor.

***Analogy:** Instead of the touch-sensitive, high-resolution OLED screen (GUI) of a modern smartphone, it is like the mechanical split-flap displays at airports or digital character scoreboards. Only a single letter or symbol can fit in each box, but through the organized arrangement of these symbols, a flawless and instantly responsive control panel emerges.*

## Technical architecture: Raw mode, ANSI escape sequences, and double buffering

How a TUI application works in the background relies on three fundamental mechanisms at the operating system level:

1. Raw Mode of the Terminal: The standard terminal environment operates in "Cooked Mode"; meaning the operating system holds and buffers characters until the user presses the Enter key. When a TUI application starts, it puts the terminal into "Raw Mode" via a termios call. Thus, every key pressed by the user (j, k, Ctrl+C, arrow keys) is captured instantly without waiting for Enter.
2. Alternate Screen Buffer: The fact that your terminal history isn't lost when you open htop or vim, and that you can return to your previous command line when the program closes, is made possible by the alternate buffer (tput smcup / rmcup). The TUI opens its own virtual canvas and returns to the main screen upon exit.
3. Double Buffering and Diff Rendering: To prevent screen flickering, modern TUI engines maintain two character matrices in memory: the current screen and the next screen. Only the changing cells are calculated, and just these diffs are printed to the terminal using ANSI codes; thus, animations can run at a fluidity of 60 FPS.

## The modern TUI renaissance and developer tools

In recent years, as a reaction to the massive memory consumption of web technologies (Electron-based bloated apps), a tremendous TUI renaissance has occurred in the developer ecosystem:

- Low Resource Consumption: While a graphical interface consumes hundreds of megabytes of memory, a TUI application uses only a few megabytes of RAM.
- Zero-Lag Over SSH: Managing a remote server in the cloud via graphical streaming (VNC / RDP) requires high bandwidth; whereas TUI flies at lightning speed inside an SSH tunnel, even on low-speed mobile connections.
- Keyboard Flow State: Working without lifting your hand from the mouse, using Vim keybindings (h, j, k, l), multiplies engineers' focus and productivity.

Prominent Modern Frameworks and Tools:

- Rust World: The ratatui (formerly tui-rs) and crossterm libraries have become the core standard for modern TUI projects with their memory safety and ultra-high performance.
- Go World: bubbletea (a reactive framework adapting The Elm Architecture pattern for the terminal), lipgloss (a styling engine) and bubbles, all developed by the Charm team.
- Python World: Textual and rich, written by Will McGugan.
- Cult TUI Tools: lazygit for Git management, k9s for Kubernetes clusters, lazydocker for Docker, btop and htop for system monitoring, ncdu for disk analysis.

## Commonly confused with

- CLI vs TUI: The CLI is a single-line question-and-answer model (git status, ls -la). The TUI, on the other hand, is a two-dimensional visual panel that fills the terminal window, featuring tabs, lists, and keyboard shortcuts (lazygit, k9s).
- TUIs Are More Than Just Primitive Text: Modern terminals support Nerd Fonts (icons), 24-bit TrueColor support, UTF-8 box-drawing characters, and even true visual rendering within the terminal using Kitty Graphics / Sixel protocols.

## Frequently asked questions

**What does TUI mean and what does it stand for?**

TUI stands for Text User Interface or Terminal User Interface. It describes visual and interactive interfaces that run on the terminal character grid without a graphical window manager.

**What are the main differences between CLI, GUI, and TUI?**

CLI works with single-line text commands; GUI is managed with pixels, windows, and a mouse; whereas TUI is a hybrid format that works inside the terminal with keyboard-oriented menus, panels, and boxes.

**How do terminal user interfaces draw the screen?**

Through ANSI escape sequences and terminal control codes, the cursor is moved to the desired row and column on the screen, color codes are assigned, and Unicode box-drawing characters are rendered.

**What are the most popular libraries for developing modern TUIs?**

Ratatui in the Rust ecosystem, bubbletea and lipgloss in Go, and Textual and rich libraries on the Python side are industry standards.

## Related terms

- [CLI](https://trescout.com/en/dictionary/cli/)
- [Terminal](https://trescout.com/en/dictionary/terminal/)
- [Terminal Control](https://trescout.com/en/dictionary/terminal-control/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Assembly](https://trescout.com/en/dictionary/assembly/)
- [Tech Stack](https://trescout.com/en/dictionary/tech-stack/)

## Related tools

- [PI](https://trescout.com/en/discover/pi/)
- [Witr](https://trescout.com/en/discover/witr/)
- [Hister](https://trescout.com/en/discover/hister/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/tui/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/tui/
