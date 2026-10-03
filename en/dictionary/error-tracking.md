# What is Error Tracking?

A tracking process that instantly captures, groups, and notifies developers of runtime errors occurring in applications.

## Overview
Error tracking is a monitoring approach that automatically records crashes and unexpected situations encountered by users in live software. The system documents the source of the error, operating system details, and user actions that triggered the error step by step. This enables software teams to intervene before issues are reported by users.

*Analogy: It is similar to a fire alarm in a building not only detecting smoke but also notifying the fire department of the exact room number and cause of the fire.*

## How it works
A small monitoring library embedded within the application listens to all uncaught software exceptions. When a glitch occurs, the stack trace and environmental data are packaged and sent to the analysis server. The server consolidates similar errors under a single roof and sends notifications to developers via email or instant messaging.

## Where it is used
It is actively preferred in mobile applications where user experience is critical, single-page web projects (SPAs), and microservice architectures running on the backend.

## Commonly confused with
It differs from the concept of logging, which stores all system events chronologically: error tracking focuses directly on exceptions and automatically analyzes and groups these issues.

## Frequently asked questions
**Do error tracking tools record users' sensitive data?**
Properly configured systems automatically filter and mask personal data such as passwords or credit cards before sending them to the server.

**Does the error report disappear when the application suddenly closes?**
No, the information collected at the moment of the crash is written to the device's local memory and transmitted to the center when the application is reopened.


## Related terms
- [Logging](/en/dictionary/logging/)
- [Observability](/en/dictionary/observability/)
- [Traces](/en/dictionary/traces/)
- [QA](/en/dictionary/qa/)
- [Session Replay](/en/dictionary/session-replay/)

## Related tools
- [Sentry](/en/discover/sentry/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/error-tracking/
