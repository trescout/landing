# Fast logging for C++ projects

spdlog is an ultra-fast logging library developed for the C++ programming language, which can be used header-only or as a compiled library. It offers lag-free and high-performance output management in software projects using modern C++ standards.

- ★ 29,437
- C++
- GitHub Trending · 2026-08-05

## What you get
- Millions of lines per second logging performance: Creates microsecond-level latency in the main application thread with a zero memory allocation approach and compile-time optimizations.
- Asynchronous and lock-free ring queue: Completely isolates file or network I/O bottlenecks from the calling pipeline by offloading log writes to the background pool.
- Rich target variety: Colorful console output, files rotating by size, archives with daily dates, simultaneous writing to syslog and Android logcat targets.
- Integrated fmt formatting power: Provides safe, fast and flexible Python-style text formatting using the {fmt} library, which is the basis of the C++20 formatting standard.
- Flexibility of header-only or compiled use: You can include it in your project by copying a single directory or link it as a static library to reduce compilation times.

## Installation
**macOS (Homebrew)**

```
brew install spdlog
```


## How to get started and basic usage
Getting started with the spdlog library is extremely effortless. Once you include the header file in your project, you can call global logging functions directly or create customized logger objects:

## Technical architecture and working principle
- Logger and Sink distinction: The Logger object filters the incoming log (trace, debug, info, warn, err, critical). Accepted messages are transferred to one or more Sink objects. For example, a single logger can write to the file in JSON format while simultaneously printing color to the console.
- Thread-safe (_mt vs _st): spdlog provides all sink classes in two forms: multi-thread-safe mutex-locking (_mt) and single-thread-specific lock-free (_st) versions. In single-threaded mode, the mutex cost is completely zero.
- Asynchronous ring queue (Ring Buffer): The memory block allocated with spdlog::init_thread_pool is consumed by the thread running in the background. The main application leaves the log in the queue and continues on its way immediately.
- Intelligent buffer flushing (Flush): Data is kept in the operating system buffer for performance; However, the spdlog::flush_on(spdlog::level::err) mechanism can be triggered to prevent data loss in critical error moments.

## If you don't write code
I want to configure the spdlog library with asynchronous architecture using CMake in a modern C++ project. Can you prepare the CMakeLists.txt file with a sample C++ initialization function that rotates the file when the log reaches 10MB in size, also gives color output to the console, and flushes it to disk immediately upon error level?

## Frequently asked questions
- Should spdlog be used header-only or compiled? In small and medium-sized projects, using header-only by adding only the include directory provides great practicality. However, in large C++ projects consisting of hundreds of source files, it is recommended to compile and link the library with the SPDLOG_COMPILED flag to optimize compilation time.
- Does logging affect the running speed of the main application? Running at the microsecond level even in synchronous mode, spdlog reduces the I/O load on the main thread to almost zero when using asynchronous logger architecture. The message is copied to the queue and disk writing occurs in the background.
- How does the rotating file mechanism work? When the specified maximum file size (for example 10MB) is reached, the active file is archived (application.1.txt, application.2.txt) and a new file is opened from scratch. When the specified maximum number of files is exceeded, the oldest log file is automatically cleared.
- Will there be a conflict with the external fmt library? No. spdlog uses the internally packaged version of fmt by default. If you wish, you can directly integrate the existing independent fmt library in your system with spdlog by defining the SPDLOG_FMT_EXTERNAL macro.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/spdlog/
