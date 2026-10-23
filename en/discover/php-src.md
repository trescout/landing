# Scripting language for websites

PHP is used as a general-purpose scripting language specifically designed for web development processes. Written in C, this interpreter powers the infrastructure of many websites around the world.

- ★ 41,410
- C
- GitHub Trending · 2026-10-23

## Updates

- **October 23, 2026:** Stars 41,391 → 41,410, latest release php-8.5.12 (October 21, 2026).

## What you get

- Allows you to run dynamic websites and web applications.
- Offers the opportunity to test the latest version by compiling directly from the source code.
- Helps you measure system stability with comprehensive built-in testing tools.

## Installation

**Install build tools for Ubuntu**

```
sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
```

**Install build tools for Fedora**

```
sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel
```

## Running it

**Compile the source code**

```
make -j4
```

**Run the tests**

```
make TEST_PHP_ARGS=-j4 test
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to compile the PHP interpreter from source code and test it. If I am using Ubuntu, run the command sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev to install the necessary build tools via the package management tool. If I am using Fedora, use the command sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel, and if I am using macOS, use the command brew install autoconf bison re2c libiconv libxml2 sqlite with the Homebrew package manager. Then, execute the command make -j4 to compile the project. After the compilation is complete, apply the command make TEST_PHP_ARGS=-j4 test to run the tests concurrently, or the command make TESTS=tests/lang/ test to run the language tests.

Repository: https://github.com/php/php-src. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Scripting Language](https://trescout.com/en/dictionary/scripting-language/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for web application developers and developers who want to examine the PHP core code and compile it directly from source.
- **License:** BSD-3-Clause

## Links

- [GitHub repository →](https://github.com/php/php-src)
- [Read in Turkish →](https://trescout.com/discover/php-src/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-10-23: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/php-src/
