# What is Telemetry?

Telemetry is the automatic collection and transmission of status information from software and devices to a central location.

## Definition and Word Origin
The word comes from the Greek roots tele (far) and metron (measure). Applications send reports on how the software is performing to the developer: which features are used the most, where the application crashes. For the user, it is generally a data stream flowing silently in the background.

## How to Know and Use in Daily Life?
Debugging: Automatic collection of crash reports.Product decision: Simplifying an underused button.Performance: Monitoring startup time version by version.

## Technical Depth and Architecture
The three pillars of observability:

## Frequently Mixed Things
It can be confused with logging. A log is a single event line. A metric is a numerical summary. A trace is the journey of a request. Telemetry is the name of the process of collecting and transmitting these three.

## Use in Different Disciplines
Hospital: A patient monitor transmitting the pulse to the nurse's screen.Aviation: Storing flight data in the black box.Energy: Meters reporting consumption to the center.

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
- [Logs](/en/dictionary/logs/)
- [Observability](/en/dictionary/observability/)
- [Traces](/en/dictionary/traces/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/telemetry/
