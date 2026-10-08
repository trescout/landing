# What is Compiler?

*Dictionary · Dev · Last updated: September 22, 2026*

Compiler is a program that translates the code you write into machine language that the computer can run.

## Definition and Word Origin

"Compile" means to compile, collect. Computers only understand strings of 0 and 1. Programmers write in readable language. The compiler translates between these two worlds: It scans the code, turns it into an executable file if there are no errors.

***Analogy:** It's like turning a recipe written in English into written instructions for a chef who doesn't speak any English, in a language he can understand.*

## How to Know and Use in Daily Life?

**Installing the application:** The compiled version of the program you downloaded will run.
**Error messages:** The compiler warns you when you forget a semicolon.
**Game engines:** Separate build output for each platform.

## Technical Depth and Architecture

Compilation goes through four stages:

**Scanning and analysis:** The code is broken into pieces, the sentence structure is extracted.
**Meaning check:** Undefined variables and type mismatches are looked for.
**Optimization:** Equivalent but faster code is generated.
**Code generation:** Machine code specific to the processor is written.

Compilation in C is as follows:

```
gcc merhaba.c -o merhaba
./merhaba
```

The first line translates, the second line executes. The interpreter runs line by line and does not produce a separate output file.

## Use in Different Disciplines

**Translation:** Difference between simultaneous translation (interpreter) and written translation (compiler).
**Printing press:** Conversion of the draft into a printing plate.
**Kitchen:** Turning the recipe into a pre-prepared meal.

## Frequently Asked Questions

**Is each language's compiler different?**

Yes. Every language requires a compiler or interpreter that suits its own rules. Some languages ​​use both together.

**What is the difference with Interpreter?**

The compiler translates the code beforehand and produces a file, then the program runs faster. The interpreter translates and executes line by line, it is flexible but generally slow.

**What is JIT?**

Just-in-time compilation translates frequently used sections into machine code while running. It's a middle ground, using Java and JavaScript.

**Who compiled the first compiler?**

It's a chicken-and-egg question. The first compilers were written by hand in machine code, the later ones were compiled with the previous compiler (bootstrapping).

## Related terms

- [Rust](https://trescout.com/en/dictionary/rust/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Compile-time](https://trescout.com/en/dictionary/compile-time/)

## Related tools

- [Llvm Project](https://trescout.com/en/discover/llvm-project/)
- [SWC](https://trescout.com/en/discover/swc/)
- [FMT](https://trescout.com/en/discover/fmt/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/compiler/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/compiler/
