# What is Google Java Style Guide?

*Development · Last updated: September 20, 2026*

The Google Java Style Guide is a set of official coding standards established by Google to ensure code readability, consistency, and maintainability in open-source and enterprise Java projects.

## Etymology and Corporate Code Standards

The Google Java Style Guide is a set of rules developed by Google, one of the world's largest technology companies, to ensure that its tens of thousands of engineers can work seamlessly on the same codebase. Since its initial publication, it has become a de facto standard not only within Google but also in the global open-source ecosystem and the enterprise software world.

The guide outlines all the formal and structural boundaries a Java file should have, from source file structure to package declarations, indentation rules to class and variable naming conventions, and Javadoc formatting to error handling. In a software project, having everyone add spaces or open brackets according to their own personal taste leads to unnecessary debates and wasted time during code reviews. The Google Java Style Guide eliminates these subjective discussions, allowing developers to focus solely on business logic.

***Analogy:** Imagine a highway with no traffic rules, where every driver changes lanes as they please; on such a road, accidents are inevitable. A standard style guide is like the lane markings and traffic lights of that highway. When thousands of engineers work on the same codebase, no one crashes into anyone else as long as the rules are followed. A developer joining a new project feels right at home because the rhythm and structure of the code are woven with universal rules.*

## Technical Depth and Ground Rules

Source File Structure and Indentation: Files are always encoded in UTF-8. Two (2) spaces are used for indentation instead of tabs. Line length is limited to 100 characters; braces are placed at the end of the line according to the K&R style.
Import Standards: Wildcard imports (import java.util.*;) are prohibited. Each class must be imported explicitly and sorted alphabetically.
Naming Conventions: Classes are named using UpperCamelCase, methods and variables using lowerCamelCase, and constants using CONSTANT_CASE. In abbreviations, only the first letter is kept uppercase (XmlHttpRequest).
Defensive Programming and Automation: @Override is mandatory for overridden methods. Empty catch blocks are prohibited. Rules are automatically enforced in the CI/CD pipeline using google-java-format, Checkstyle, and Spotless plugins.
Javadoc and Comment Standards: Writing Javadoc descriptions for public classes is mandatory; @param, @return, and @throws tags must be filled out completely.

## Sociological Dimension: Readability and Team Productivity

Research in software engineering shows that a developer spends more than 80 percent of their time not writing new code, but reading existing code. Therefore, readability is far more valuable than ease of writing.

The Google Java Style Guide allows developers to set aside personal ego and aesthetic concerns regarding code and prioritize the team's collective productivity. For projects that accept external contributions (pull requests) in the open-source world, this guide is a universal agreement document that ensures contributors can adapt to the project effortlessly.

## Common Mistakes and Misconceptions

Trying to Format Manually: Instead of counting spaces one by one, the google-java-format plugin should be installed in the IDE and auto-save formatting should be enabled.
Disabling Checkstyle Rules: Disabling style checks in CI/CD when the process is tight increases technical debt.
Overusing Comment Lines: The code should aim to be self-explanatory; meaningless comments should not be written for obvious getter/setter methods.

## Frequently Asked Questions

**Why does the Google Java Style Guide use 2-space indentation instead of 4 spaces?**

The two-space rule prevents code from exceeding the 100-character horizontal limit, especially in nested lambda expressions, anonymous classes, and builder patterns, and uses screen space more efficiently.

**How are Google Java style rules automatically applied in projects?**

The 'google-java-format' tool provided by Google is integrated into IDEs (IntelliJ, Eclipse, VS Code) or automatically formatted during code saving and CI build stages using Spotless/Maven/Gradle plugins.

**What is the difference between the Google Java Style Guide and the Oracle (Sun) coding conventions?**

While Sun conventions use 4-space indentation and an 80-character limit, the Google style focuses on 2-space indentation, a 100-character limit, strict import rules, and modern tool automation.

**Are Checkstyle and the Google Java Style Guide the same thing?**

No; the Google Java Style Guide is a documentation of rules, whereas Checkstyle is a static analysis tool that structures these rules in XML format and audits the codebase for rule violations.

## Related terms

- [Sun Code Conventions](https://trescout.com/en/dictionary/sun-code-conventions/)
- [Code Snippets](https://trescout.com/en/dictionary/code-snippets/)
- [Refactoring](https://trescout.com/en/dictionary/refactoring/)
- [QA](https://trescout.com/en/dictionary/qa/)
- [Production Pipeline](https://trescout.com/en/dictionary/production-pipeline/)
- [TDD](https://trescout.com/en/dictionary/tdd/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/google-java-style-guide/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/google-java-style-guide/
