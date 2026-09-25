# Fast logging library for C++ projects

spdlog is an ultra-fast, header-only or compiled C++ logging library designed for zero latency and high throughput. Utilizing modern C++ standards, it delivers thread-safe, lock-free asynchronous logging with minimal runtime overhead.

- ★ 29,437
- C++
- GitHub Trending · 2026-08-05

## Updates
- August 6, 2026: Stars 29,402 → 29,437, latest release v1.17.0 (January 4, 2026).

## What you get
- Millions of lines per second throughput: Zero-allocation design and compile-time optimizations create microsecond-level latency in caller threads.
- Asynchronous lock-free ring buffer: Offloads log writes to a dedicated worker thread pool, decoupling disk and network I/O from critical application paths.
- Versatile sink destinations: Write concurrently to colored console output, rotating files by size, daily archived logs, syslog, and Android logcat.
- Built-in {fmt} formatting power: Employs the {fmt} library (standardized in C++20) for type-safe, fast, and flexible Python-like string formatting.
- Header-only or compiled flexibility: Integrate by dropping a single directory into your project, or link as a precompiled static library for faster compilation.

## Installation

**macOS (Homebrew)**

```
brew install spdlog
```

**vcpkg package manager**

```
vcpkg install spdlog
```

**CMake FetchContent integration**

```
include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(my_project PRIVATE spdlog::spdlog)
```

Source: Homebrew formula

## Getting started and basic usage

Getting started with spdlog requires minimal boilerplate. After including the header, you can immediately log through global functions or instantiate custom logger objects:

**Basic C++ Example**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
    // Standard console logging
    spdlog::info("spdlog initialized successfully.");
    spdlog::warn("Warning: Memory consumption is rising!");
    spdlog::error("Error code: {:d}, message: {}", 404, "Page not found");

    // Rotating file logger (max 5MB, 3 files)
    auto file_logger = spdlog::rotating_logger_mt("file_logger", "logs/app.txt", 1024 * 1024 * 5, 3);
    file_logger->info("This message is thread-safe and written to an auto-rotated file.");

    return 0;
}
```

## Technical architecture and inner workings

spdlog achieves peak performance through a modular zero-overhead design:
- Logger and Sink separation: Loggers filter messages across severity levels (trace, debug, info, warn, err, critical) and forward formatted records to one or multiple sink targets.
- Thread safety (_mt vs _st): Sinks are provided in two flavors: multi-threaded with mutex synchronization (_mt) and single-threaded lock-free (_st) variants for zero mutex overhead.
- Asynchronous ring buffer: Dedicated thread pool created via spdlog::init_thread_pool buffers messages so worker threads handle I/O without blocking main logic.
- Configurable flush policy: Data is buffered in OS page cache for performance, with automatic flushing triggered on critical events via spdlog::flush_on(spdlog::level::err).

## If you do not code
🤖 If you do not code
I want to configure spdlog in a modern C++ project using CMake with an asynchronous logging setup. Could you provide an example initialization function and CMakeLists.txt that sets up colored console logging, a 10MB rotating file sink, and immediate flushing on error levels?

- **Who it is for:** C++ engineers, game engine creators, and systems developers needing zero-overhead logging.
- **License:** MIT (Permissive open source license)
- **Integration:** Header-only or precompiled library
- **Standards:** C++11, C++14, C++17, C++20

## Frequently asked questions
- How does spdlog compare to std::cout or printf? spdlog is significantly faster, thread-safe, offers structured log levels, supports non-blocking asynchronous I/O, and formats strings safely using {fmt}.
- Can spdlog log custom classes and objects? Yes. You can overload operator<< or specialize fmt::formatter for your custom classes to format them directly inside log messages.
- Is spdlog suitable for high-frequency trading and game engines? Yes. With lock-free single-threaded sinks or asynchronous ring buffers, message dispatch completes in nanoseconds without stalling game render loops or financial feeds.
- Does spdlog support structured JSON output? Yes. By attaching a custom sink or formatting pattern, spdlog can output JSON formatted log streams for Elasticsearch, Datadog, or Grafana Loki.

## Links
- [GitHub →](https://github.com/gabime/spdlog)
- [Read in Turkish →](https://trescout.com/discover/spdlog/)

## Related dictionary terms
Logging Logs Runtime Memory Management

---
Source: TreScout Discover · https://trescout.com/en/discover/spdlog/
