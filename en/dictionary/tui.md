# What is TUI?

> Text User Interface

TUI (Text User Interface), is a keyboard-driven user interface that operates on terminal screens using text and character blocks without the need for a graphics card.

## Conceptual framework, etymology, and the evolution of the terminal
The term TUI is an abbreviation of the English expression Text User Interface (or Terminal User Interface from time to time). In the history of computer interfaces, it is a hybrid visual paradigm bridging CLI (Command Line Interface) and GUI (Graphical User Interface):

## Technical architecture: Raw mode, ANSI escape sequences, and double buffering
How a TUI application works in the background relies on three fundamental mechanisms at the operating system level:

## The modern TUI renaissance and developer tools
In recent years, as a reaction to the massive memory consumption of web technologies (Electron-based bloated apps), a tremendous TUI renaissance has occurred in the developer ecosystem:

## Commonly confused with

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
- [CLI](/en/dictionary/cli/)
- [Terminal](/en/dictionary/terminal/)
- [Terminal Control](/en/dictionary/terminal-control/)
- [Runtime](/en/dictionary/runtime/)
- [Assembly](/en/dictionary/assembly/)
- [Tech Stack](/en/dictionary/tech-stack/)

## Related tools
- [PI](/en/discover/pi/)
- [Witr](/en/discover/witr/)
- [Hister](/en/discover/hister/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/tui/
