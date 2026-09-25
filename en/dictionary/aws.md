# What is AWS?

> Amazon Web Services

**Category:** Dev  
**Last updated:** 2026-09-22

AWS (Amazon Web Services) is a comprehensive cloud computing platform offering on-demand compute power, database storage, content delivery, and scalable infrastructure via the internet.

## Definition and Etymology
Instead of investing capital into physical on-premise data centers, organizations lease elastic computing resources from Amazon. Capacity scales elastically with incoming user traffic and contracts when demand subsides. Operating on a pay-as-you-go utility model, AWS underpins the backend architecture of modern enterprise software and consumer services.

## Everyday Context and Practical Usage
- **Web & Mobile Applications:** Auto-scaling application servers dynamically handling traffic spikes.
- **Disaster Recovery & Archival:** Highly durable, globally distributed object storage for backups.
- **Streaming Media:** Edge caching networks distributing high-definition video with minimal latency.
- **Early-Stage Startups:** Launching global enterprise-grade products without physical server room capital.

## Technical Depth and Architecture
Foundational Infrastructure Services:- **EC2 (Elastic Compute Cloud):** Resizable virtual machine instances running Linux and Windows.
- **S3 (Simple Storage Service):** Industry-standard object storage boasting 99.999999999% durability.
- **RDS (Relational Database Service):** Managed databases supporting PostgreSQL, MySQL, and Aurora.
- **Lambda:** Event-driven serverless compute executing microservices in response to real-time events.

Core operational concepts include geographic Regions and multi-datacenter Availability Zones (AZs) for high availability, alongside the Shared Responsibility Model: Amazon secures the cloud infrastructure, while customers secure the operating systems, data, and access policies deployed within.<div class="disc-cmd"><div class="disc-cmd-head"><span>List running EC2 instances via AWS CLI</span></div><pre><code>aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"</code></pre></div>

## Commonly Confused With
Commonly confused with basic web hosting. Basic web hosts simply serve static HTML and PHP scripts; AWS is a comprehensive catalog of over 200 managed primitives spanning networking, artificial intelligence, quantum computing, and enterprise security.

## Cross-Disciplinary Perspectives
- **Electrical Grid:** Drawing electricity from wall outlets instead of building a private power station.
- **Storage Lockers:** Renting modular storage space only when household inventory expands.
- **Ridesharing:** Accessing transportation instantly per mile without purchasing vehicle fleets.

## Analogy
Rather than building and maintaining your own private power plant, AWS is like plugging into the municipal electrical grid: you consume energy on demand and pay strictly for what you use.

## Frequently Asked Questions

**Why choose AWS over on-premise hardware?**  
AWS removes upfront capital expenses, offers instant global scaling across dozens of countries, and provides managed automated maintenance for databases and servers.

**Can I use AWS for free?**  
Yes. AWS provides a Free Tier offering limited monthly allowances for EC2, S3, and Lambda; review current quota thresholds to prevent unintended billable usage.

**Where is customer data physically located?**  
Data resides strictly within the geographic Region selected during provisioning, enabling adherence to data residency regulations such as GDPR.

**How do teams avoid unexpected cloud bills?**  
Through automated AWS Budget alerts, CloudWatch metric monitors, automated tagging conventions, and regular deletion of unattached storage volumes.

## Related terms
- [Cloud Computing](/en/dictionary/cloud-computing/)
- [IaaS](/en/dictionary/iaas/)
- [PaaS](/en/dictionary/paas/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/aws/
