# What is QA?

> Quality Assurance

QA (Quality Assurance) is a systematic quality management discipline aimed at preventing defects before they emerge at every stage of the software development lifecycle, establishing engineering standards, and guaranteeing the reliability of the final product.

## Conceptual origin: From the Deming cycle and production lines to software
The concept of Quality Assurance was born in industrial manufacturing long before software, in the mid-20th century. Total Quality Management (TQM), laid down by W. Edwards Deming and Walter Shewhart, and the PDCA cycle (Plan-Do-Check-Act) argue that quality cannot be inspected into a product afterward, but must be built into it. The Jidoka principle from the Toyota Production System (instantly stopping the production line when a defective product is made) is also the ancestor of today's modern continuous integration (CI) and QA philosophy.

## Critical distinction: QA vs QC vs Testing
Although these three concepts are frequently used interchangeably, there are clear methodological boundaries between them:

## Modern QA paradigm: Shift-Left and Shift-Right
In the traditional waterfall model, developers wrote the code and then "threw it over the wall" to the QA department for testing. In the modern Agile and DevOps world, this approach has given way to two complementary directions:

## Test pyramid and automation layers
A robust QA architecture is based on Mike Cohn's Test Pyramid principle:

## QA in the Age of AI and LLMs
With the rise of probabilistic (non-deterministic) systems such as Large Language Models (LLMs), the QA discipline has entered a new phase:

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
- [Unit Testing](/en/dictionary/unit-testing/)
- [End-to-End Testing](/en/dictionary/end-to-end-testing/)
- [Testing Framework](/en/dictionary/testing-framework/)
- [Production Pipeline](/en/dictionary/production-pipeline/)
- [Benchmarks](/en/dictionary/benchmark/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [Gstack](/en/discover/gstack/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/qa/
