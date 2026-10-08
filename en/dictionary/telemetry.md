# What is Telemetry?

*Dictionary · Dev · Last updated: September 22, 2026*

Telemetry is the automatic collection and transmission of status information from software and devices to a central location.

## Definition and Word Origin

The word comes from the Greek roots tele (far) and metron (measure). Applications send reports on how the software is performing to the developer: which features are used the most, where the application crashes. For the user, it is generally a data stream flowing silently in the background.

***Analogy:** It is like the sensors inside a car constantly reporting the engine temperature and fuel status to the driver's dashboard.*

## How to Know and Use in Daily Life?

**Debugging:** Automatic collection of crash reports.
**Product decision:** Simplifying an underused button.
**Performance:** Monitoring startup time version by version.

## Technical Depth and Architecture

The three pillars of observability:

**Log:** Event lines ("payment started", "payment finished").
**Metric:** Numerical metrics (request count, average latency).
**Trace:** Recording the request's journey between services.

Open standards such as OpenTelemetry are used for collection. Two rules are observed: in high-traffic scenarios, sending samples of requests rather than every single one (sampling), and ensuring personal data (email, location) is not logged. You can view which data is being sent and disable it in the application's settings section.

## Frequently Mixed Things

It can be confused with logging. A log is a single event line. A metric is a numerical summary. A trace is the journey of a request. Telemetry is the name of the process of collecting and transmitting these three.

## Use in Different Disciplines

**Hospital:** A patient monitor transmitting the pulse to the nurse's screen.
**Aviation:** Storing flight data in the black box.
**Energy:** Meters reporting consumption to the center.

## Frequently Asked Questions

**Does it affect my privacy?**

Data is generally collected anonymously and in aggregate. You can see which data is being sent in the settings section of the application and turn it off.

**What is the difference from observability?**

Telemetry collects and transmits data. Observability is the ability to understand the inner workings of a system using the collected data. One is a tool, the other is a goal.

**Can it be turned off?**

In most applications, yes, it can be turned off in the settings. On corporate devices, it may remain on due to policy.

**Is there a cost?**

Yes. There is a cost for data transfer and storage. Therefore, sampling is performed during high traffic, where only a portion of events is sent rather than every single one.

## Related terms

- [Logs](https://trescout.com/en/dictionary/logs/)
- [Observability](https://trescout.com/en/dictionary/observability/)
- [Traces](https://trescout.com/en/dictionary/traces/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/telemetry/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/telemetry/
