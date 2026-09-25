# What is QA (Quality Assurance)?

**Category:** Development
**Last updated:** 2026-09-19

QA (Quality Assurance) is a systematic software engineering discipline dedicated to preventing defects across every phase of the software development lifecycle (SDLC), establishing architectural standards, and guaranteeing product reliability.

## Conceptual Origins: From Deming Cycles and Manufacturing to Software
Quality Assurance originated in mid-20th-century manufacturing long before software existed. Total Quality Management (TQM) and the PDCA cycle (Plan-Do-Check-Act) pioneered by W. Edwards Deming and Walter Shewhart posited that quality cannot be inspected into a finished product; it must be built directly into the manufacturing process. Similarly, the Toyota Production System's Jidoka principle (halting the assembly line the moment an anomaly is detected) represents the historical precursor to modern Continuous Integration (CI) and QA philosophy.In software, Barry Boehm's foundational study on Software Engineering Economics demonstrated that fixing a defect discovered during design costs 1x, whereas remediating the exact same bug after production release escalates up to 100x. QA exists to mitigate this catastrophic financial and reputational liability.

## Critical Distinction: QA vs QC vs Testing
While these three terms are colloquially interchanged, rigorous methodological boundaries separate them:Testing: The execution of test suites to uncover concrete bugs in a specific software build (product-focused and reactive).Quality Control (QC): The validation gate verifying whether a built artifact adheres to predefined functional specifications and acceptance criteria before shipment (product-focused and reactive).Quality Assurance (QA): The overarching umbrella discipline that designs development methodologies, test infrastructure, coding standards, and automated CI/CD pipelines to prevent defects from manifesting initially (process-focused and proactive).

## Modern QA Paradigms: Shift-Left and Shift-Right
In legacy waterfall workflows, developers authored code and 'threw it over the wall' to a downstream QA department. Modern Agile and DevOps teams replace this bottleneck with two complementary practices:1. Shift-Left: Moving validation to the earliest possible point of development. While coding, engineers execute static analysis (ESLint, SonarQube), static type checking (TypeScript), unit testing (Jest, pytest), and TDD. The QA engineer acts not as a manual tester, but as an enablement architect designing frameworks and pipelines.2. Shift-Right: Guarding software health post-deployment in production. Synthetic monitoring, canary deployments, error telemetry (Sentry), chaos engineering, and real-user monitoring continuously audit live operational resilience.

## The Test Pyramid and Automation Layers
A robust QA architecture reflects Mike Cohn's Test Pyramid principle:Unit Tests: Form the foundation; isolated, executing in milliseconds with negligible operational maintenance.Integration and Contract Tests: Validate communication boundaries across databases, distributed caches, and microservice API contracts (e.g., Pact).End-to-End (E2E) Tests: Drive headless browsers via Playwright or Cypress to simulate real user journeys; high fidelity, but higher maintenance overhead.Non-Functional Verification: Load testing (k6, Locust), automated security scanning (SAST/DAST), and accessibility (WCAG/a11y) audits.

## Analogy
Debugging is akin to surgical intervention, while testing resembles running clinical lab diagnostics. Quality Assurance represents preventive public health policy: it institutes sanitation standards, nutritional protocols, and immunization programs to systematically eradicate disease vectors before infection can occur.

## QA in the Era of AI and Large Language Models
As probabilistic, non-deterministic architectures like LLMs proliferate, QA expands into new evaluation frontiers:LLM Evals: Automated frameworks (DeepEval, Ragas) quantifying hallucination frequency, factual accuracy, toxicity, and semantic relevance.Semantic Regression Testing: Benchmarking suites ensuring prompt modifications or model fine-tunes preserve baseline answer fidelity.AI-Assisted Test Generation: Autonomous synthesis of edge-case test payloads and visual UI regression verification using computer vision.

## Frequently asked questions

### What does QA stand for in software engineering?
QA stands for Quality Assurance. It is the proactive engineering discipline tasked with designing development processes and automation to prevent software bugs and ensure system reliability.

### How does QA differ from QC and software testing?
Testing and QC are reactive measures that detect defects in existing builds. QA is proactive, building the frameworks, linting rules, and CI pipelines that prevent bugs from being authored in the first place.

### What are Shift-Left and Shift-Right testing?
Shift-Left integrates quality checks early at the code-writing stage (unit tests, static analysis), while Shift-Right continuously monitors production health and user telemetry post-launch.

### How is QA executed in LLM and AI applications?
Beyond traditional software tests, teams implement evaluation frameworks (evals) that programmatically benchmark hallucination rates, semantic drift, and retrieval accuracy (RAG).

## Related terms
- [Unit Testing](/en/dictionary/unit-testing/)
- [End-to-End Testing](/en/dictionary/end-to-end-testing/)
- [Testing Framework](/en/dictionary/testing-framework/)
- [Production Pipeline](/en/dictionary/production-pipeline/)
- [Benchmarks](/en/dictionary/benchmark/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [Gstack](/en/discover/gstack/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/qa/
