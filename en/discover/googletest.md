# Industry-standard unit tests in C++ projects

GoogleTest and GoogleMock are industry-standard open-source testing frameworks that enable you to run unit tests, mock objects, and parameterized tests in modern C++ projects.

- ★ 39,588
- C++
- GitHub Trending · 2026-08-27

## Updates

- **September 27, 2026:** Stars 38,987 → 39,588, latest release v1.18.0 (August 10, 2026).

## What you get

- Rich verification macros: Clear error diagnosis with ASSERT_* (critical failure, terminates the test) and EXPECT_* (records the error, continues the test flow) macros.
- Advanced Mock infrastructure (GoogleMock): Easily mock interfaces using MOCK_METHOD to isolate dependencies and define call expectations.
- Parametric test capability: The ability to automatically repeat the same test logic over dozens of different inputs and data sets using a single template.
- Cross-platform and thread safety: Verifying crash scenarios in Linux, macOS, and Windows environments using a thread-safe architecture and death tests.
- CI/CD and reporting integration: Seamless integration with GitHub Actions, Jenkins, and GitLab CI pipelines via JUnit-compatible XML and JSON output formats.

## Installation

**Adding to the project with CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```

## Running it

**Compiling the test and executing with CTest**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```

## Technical architecture and working principle

- Test Fixture and Lifecycle Management: Memory resources are securely managed before and after each test using SetUp and TearDown procedures.
- Process Isolation for Death Tests: Captures unexpected program crashes or asserts in isolated child processes using a fork mechanism.
- Type-Parameterized Test Templates: Provides a Type-Parameterized test infrastructure to test templated classes (C++ templates) with different data types at once.

## Test scenarios and GoogleMock integration

- Abstraction of Database and Network Calls: Simulate expected API responses and latencies without establishing real network connections by using MOCK_METHOD.
- Call Count and Parameter Validation: Verify how many times, with which arguments, and in what order a function is called using the EXPECT_CALL macro.
- Reviewing Exception Throwing Scenarios: Ensure resilience by testing code blocks that throw exceptions with EXPECT_THROW macros.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to write unit tests for a data parser class using GoogleTest and GoogleMock in a modern C++ project. Could you explain with code examples how to configure my CMakeLists.txt file, provide an example TEST_F test fixture, and show how to create a mock object with MOCK_METHOD and verify call expectations?

## Frequently asked questions

- What is the most modern way to include GoogleTest in a project? In modern CMake projects, the FetchContent mechanism is the most recommended approach. It downloads the source code and links it to the target build process without needing an external package manager.
- What is the main difference between EXPECT_* and ASSERT_*? EXPECT_* macros log the error when they fail, but allow the rest of the function to run. ASSERT_* immediately exits the current test function upon an error.
- Is GoogleMock a separate library? GoogleMock was originally a separate project, but it has long been merged under the same roof as the GoogleTest repository; the two are installed and used together.
- Does it offer thread safety? Yes. GoogleTest runs thread-safely on systems supporting pthreads and on Windows; it correctly synchronizes simultaneous notifications coming from multiple threads.

## Related dictionary terms

- [Fork](https://trescout.com/en/dictionary/fork/)
- [Parser](https://trescout.com/en/dictionary/parser/)
- [CI/CD](https://trescout.com/en/dictionary/ci-cd/)
- [API](https://trescout.com/en/dictionary/api/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** C++ software engineers, embedded systems developers, and system architects.
- **License:** BSD 3-Clause (Esnek açık kaynak lisansı)
- **Framework:** C++ Test and Mock Library
- **Platforms:** Linux, macOS, Windows, Android, iOS

## Links

- [GitHub repository →](https://github.com/google/googletest)
- [Read in Turkish →](https://trescout.com/discover/googletest/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-27: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/googletest/
