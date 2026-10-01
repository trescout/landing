# What is Deployment?

Deployment (software deployment / going live) is the process of compiling and installing a software component, which has been developed and tested in a local environment, onto target servers or cloud infrastructure, and making it available to end users.

## Conceptual framework, etymology, and historical transformation
Etimologically, the term deployment is rooted in military terminology, referring to the dispatching and readiness of troops, ammunition, or naval fleets into strategic combat positions ("to deploy"). In software engineering, it began in the 1970s and 80s with loading punched cards or magnetic tapes onto mainframes, evolved into manually executed FTP/SSH file transfers in the 1990s, and has today transformed into fully declarative and automated cloud pipelines (GitOps).

## Zero-Downtime deployment strategies
The core deployment patterns developed to ensure users experience no service interruptions while applications are being updated are:

## CI/CD pipeline, GitOps, and database migrations
A successful deployment architecture is built upon three critical engineering foundations:

## Error management, observability, and rollback architecture
For production environment errors that are missed even in the most advanced test environments, there are two primary lifelines:

## Commonly confused with

## Frequently asked questions
**What does deployment mean and what is its Turkish equivalent?**
It is a word of English origin meaning 'distribution' or 'going live'. It is the process of compiling a software package and making it operational on target servers or in a cloud environment.

**What is the difference between Deployment and Release?**
Deployment is the technical installation and execution of code on a server. Release, on the other hand, is the official opening of the feature to the end user's access via Feature Flags or marketing steps.

**What is the main difference between Blue-Green and Canary deployment?**
In a Blue-Green deployment, there are two identical environments, and traffic is switched 100% to the new environment instantly via a load balancer. In a Canary deployment, the new version is gradually introduced to a small slice of users, such as 1-5% first, and the ratio is increased while observing metrics.

**How are database schema changes managed in a Zero-Downtime deployment?**
They are managed using the Expand-Contract pattern. First, backwards-compatible new fields are added; after all the servers in the system switch to the new code and data flow is established, the old fields are cleaned up.


## Related terms
- [Runtime](/en/dictionary/runtime/)
- [Compile-time](/en/dictionary/compile-time/)
- [Cloud Computing](/en/dictionary/cloud-computing/)
- [Production Pipeline](/en/dictionary/production-pipeline/)
- [Tech Stack](/en/dictionary/tech-stack/)
- [Git Push](/en/dictionary/git-push/)

## Related tools
- [Rocket.Chat](/en/discover/rocket-chat/)
- [Chatwoot](/en/discover/chatwoot/)
- [Argo Cd](/en/discover/argo-cd/)
- [Openship](/en/discover/openship/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/deployment/
