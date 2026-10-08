# What is QA?

*Dictionary · Dev · Last updated: September 19, 2026*

> Quality Assurance

QA (Quality Assurance) is a systematic quality management discipline aimed at preventing defects before they emerge at every stage of the software development lifecycle, establishing engineering standards, and guaranteeing the reliability of the final product.

## Conceptual origin: From the Deming cycle and production lines to software

The concept of Quality Assurance was born in industrial manufacturing long before software, in the mid-20th century. Total Quality Management (TQM), laid down by W. Edwards Deming and Walter Shewhart, and the PDCA cycle (Plan-Do-Check-Act) argue that quality cannot be inspected into a product afterward, but must be built into it. The Jidoka principle from the Toyota Production System (instantly stopping the production line when a defective product is made) is also the ancestor of today's modern continuous integration (CI) and QA philosophy.

In the software world, Barry Boehm's famous "Software Engineering Economics" research proved that while the cost of fixing a bug caught during the design phase is 1 unit, the cost of fixing it after release to production can soar up to 100 times. QA exists to prevent this massive cost and loss of reputation.

***Analogy:** Debugging is like operating on the surgical table, while software testing is like taking laboratory blood work. QA, on the other hand, is public health and preventive medicine protocol: By establishing healthy nutrition guides, vaccination schedules, and hygiene rules, it aims to eliminate the risk of getting sick in the first place.*

## Critical distinction: QA vs QC vs Testing

Although these three concepts are frequently used interchangeably, there are clear methodological boundaries between them:

**Testing:** The execution of scenarios to find concrete bugs in a specific version of the software (product-oriented and reactive).

**Quality Control (QC):** The inspection gate that verifies whether the product complies with specified technical specifications and acceptance criteria before release (product-oriented and reactive).

**Quality Assurance (QA):** It is the overarching discipline (process-oriented and proactive) that designs development methodologies, test infrastructure, architectural standards, and CI/CD processes to prevent defects from ever occurring.

## Modern QA paradigm: Shift-Left and Shift-Right

In the traditional waterfall model, developers wrote the code and then "threw it over the wall" to the QA department for testing. In the modern Agile and DevOps world, this approach has given way to two complementary directions:

**1. Shift-Left:** It moves quality control to the very beginning of development. While writing code, the developer applies static analysis (ESLint, SonarQube), type checking (TypeScript), unit tests (Jest, pytest), and TDD (Test-Driven Development). Here, the QA engineer is not someone who runs tests, but a platform architect who builds the test infrastructure and frameworks.

**2. Shift-Right:** It is the maintenance of quality after the code goes live. Real user experience is monitored through synthetic monitoring, canary deployments, error tracking (Sentry), chaos engineering (Chaos Engineering), and live traffic analytics.

## Test pyramid and automation layers

A robust QA architecture is based on Mike Cohn's Test Pyramid principle:

**Unit Tests:** They form the base; they test independent functions in isolation, run in milliseconds, and have the lowest cost.

**Integration & Contract Tests:** Verifies databases, caches, and inter-microservice API contracts (e.g., Pact).

**End-to-End Tests (E2E Tests):** Simulates a real user's steps in the browser using tools like Cypress or Playwright; it has a broad scope but is more costly to maintain.

**Non-Functional Tests:** Includes load and stress tests (k6, Locust), vulnerability scans (SAST/DAST), and accessibility (WCAG / a11y) audits.

## QA in the Age of AI and LLMs

With the rise of probabilistic (non-deterministic) systems such as Large Language Models (LLMs), the QA discipline has entered a new phase:

**LLM Evaluations (Evals):** Automated checks that score model responses for hallucination, accuracy, toxicity, and relevance (DeepEval, Ragas).

**Semantic Regression Tests:** Benchmarks that measure whether a change made to prompt templates has degraded previous response quality.

**AI-Powered Test Generation:** Automatic detection of test scenarios and visual UI regression differences using AI models.

## Frequently asked questions

**What does QA mean and what is its expansion?**

It is the abbreviation for Quality Assurance; it means Quality Assurance in Turkish. It is the engineering discipline that ensures software processes run flawlessly from start to finish.

**What is the difference between QA, QC (Quality Control), and Testing?**

Testing and QC are reactive steps focused on finding bugs in existing code. QA, on the other hand, is a proactive process that designs development processes, standards, and tools to prevent bugs from occurring in the first place.

**What do Shift-Left and Shift-Right testing approaches mean?**

Shift-Left refers to pulling test processes to the very beginning of development (at the moment of coding); Shift-Right refers to real-time monitoring of system health and user behaviors in the production environment.

**How is QA performed in artificial intelligence and LLM-based applications?**

In addition to traditional tests, specialized evaluation (evals) frameworks are used to measure hallucination rates, semantic similarity, prompt regression, and RAG accuracy metrics.

## Related terms

- [Unit Testing](https://trescout.com/en/dictionary/unit-testing/)
- [End-to-End Testing](https://trescout.com/en/dictionary/end-to-end-testing/)
- [Testing Framework](https://trescout.com/en/dictionary/testing-framework/)
- [Production Pipeline](https://trescout.com/en/dictionary/production-pipeline/)
- [Benchmarks](https://trescout.com/en/dictionary/benchmark/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)

## Related tools

- [Gstack](https://trescout.com/en/discover/gstack/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/qa/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/qa/
