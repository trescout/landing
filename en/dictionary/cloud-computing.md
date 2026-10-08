# What is Cloud Computing?

*Dictionary · Dev · Last updated: September 19, 2026*

Cloud Computing is the provision of computing resources such as servers, storage, databases, networks and software on-demand from remote data centers over the Internet instead of physical local infrastructures.

## Definition, etymology and conceptual genesis

Cloud computing allows companies and engineers to build their own server rooms instead of purchasing physical hardware; It is a modern computing model that allows users to rent computing power, memory, storage and artificial intelligence GPU clusters over the internet in seconds.

Its conceptual roots date back to 1961, when John McCarthy, one of the fathers of artificial intelligence, gave a speech at MIT. McCarthy predicted that computing power would be offered as a public service in the future, just like electricity and water. The use of the word "cloud" in this sector dates back to telecommunications and network engineering: In the 1990s, system architects would place complex telephone exchanges and internet backbones, the details of which they wanted to abstract, by drawing a "cloud icon" on diagrams. With Amazon opening its Simple Storage Service (S3) and Elastic Compute Cloud (EC2) services to developers in 2006, the capital investment (CapEx)-oriented server purchasing model was replaced by the pay-as-you-use (OpEx) principle.

***Analogy:** It is like connecting directly to the national power grid instead of installing a special hydroelectric power plant or generator in the garden of your own factory or home. As soon as you plug it into the socket, electricity flows; however much power your machine consumes, you only pay for that consumption at the end of the month; You won't have to deal with generator malfunction, fuel or transformer maintenance.*

## Basic service and distribution models (IaaS, PaaS, SaaS, Serverless)

Cloud computing architecture is divided into four main service models based on their level of abstraction:

1. IaaS (Infrastructure as a Service): It consists of low-level raw virtual machines, block storage disks, and virtual network topologies. AWS EC2, Google Compute Engine, and Azure VMs fall into this category. The cloud provider manages the hardware and virtualization layer, while the developer is responsible for operating system installation, security patches, and the software stack.
2. PaaS (Platform as a Service): These are platforms that relieve developers from the hassles of server configuration, operating systems, and runtime environments. Examples include Vercel, Heroku, and AWS Elastic Beanstalk. The engineer simply submits the source code; scaling, SSL certificates, and load balancing are handled automatically in the background.
3. SaaS (Software as a Service): Turnkey software that end users access directly via a web browser or API, with maintenance fully managed by the provider. Google Workspace, Slack, Salesforce, and Figma are among the best-known examples of this model.
4. Serverless (FaaS · Function as a Service): An event-driven architecture that completely abstracts the concept of servers. Code written on AWS Lambda or Cloudflare Workers spins up only when a triggering HTTP request or database event arrives, executes in milliseconds, and shuts down. It produces zero cost when there is no traffic.

Distribution models depend on where the data is hosted:

- Public Cloud: An architecture where resources are shared in a multi-tenant model across the global data centers of major providers.
- Private Cloud: An isolated environment operated by regulated sectors such as finance, defense, and healthcare in data centers exclusively allocated to them.
- Hybrid Cloud: A hybrid architecture where sensitive customer data runs on private on-premise servers, while the high-transaction-volume web tier runs in the public cloud.
- Multi-Cloud: The distributed setup of systems across AWS, Google Cloud, and Azure to avoid dependency on a single company (vendor lock-in).

## Computer science and system architecture: Hypervisor, container and CAP

The technical miracle underlying cloud computing is the software abstraction of hardware (virtualization):

- Hypervisor Layer: It is the core software that divides the processor and RAM resources of a single physical server and distributes them among dozens of independent virtual machines (VMs). Type 1 bare-metal (KVM, VMware ESXi) hypervisors running directly on the hardware form the performance backbone of cloud providers.
- Containers and Orchestration: Docker containers were born by utilizing the Linux kernel's cgroups (resource limitation) and namespaces (process isolation) capabilities to overcome the operating system duplication overhead of virtual machines. The automated deployment and self-healing of thousands of containers are achieved through Kubernetes clusters.
- CAP Theorem and Distributed Resilience: Global cloud infrastructures operate within the boundaries of Eric Brewer's CAP Theorem. During a network partition, a system must prioritize either Data Consistency or Continuous Availability. Cloud architects implement disaster recovery scenarios using geographically redundant (Multi-Region / Availability Zone) architectures.
- Shared Responsibility Model: Security in the cloud is split in two. The provider is responsible for the security of physical datacenters, servers, the hypervisor, and network cables ("Security OF the Cloud"). The customer, on the other hand, is responsible for operating system updates, encryption, IAM (identity and access management) roles, and application code vulnerabilities ("Security IN the Cloud").

## Economic, ecological and geopolitical dimension

Cloud computing is not only a technical revolution, but also a massive disruption in global resource allocation:

- Jevons Paradox: The principle established for coal consumption by 19th-century economist William Stanley Jevons also holds true in the cloud: as access to computing power becomes cheaper and easier, total consumption does not decrease, but rather increases exponentially. The ability to train artificial intelligence models with hundreds of billions of parameters today is a direct result of the economies of scale offered by cloud computing.
- Energy and Water Consumption: Hyperscale data centers account for approximately 1-2% of global electricity consumption, and millions of cubic meters of pure water are used to cool massive GPU clusters. This reality has made it mandatory to build data centers near renewable energy sources and cold climates.
- Digital Sovereignty and Legal Regimes: Where data physically resides is a geopolitical issue. While the US CLOUD Act grants authorities the power to access American companies' servers abroad, the European Union·through GDPR and the GAIA-X initiative·and Turkey·via KVKK regulations·encourage critical data to remain within national borders.

## Commonly confused with

- Cloud Storage vs Cloud Computing: Google Drive, iCloud, or Dropbox are merely storage services; cloud computing, on the other hand, is a massive ecosystem that includes dynamic processing power, artificial intelligence training, network management, and database orchestration alongside storage.
- Serverless vs Truly Serverless: Physical servers of course do exist in serverless architecture; the term "serverless" means that the developer no longer has to deal with configuring, updating, or monitoring a server, and server management is made invisible by the provider.

## Frequently asked questions

**What does cloud computing mean and what is its Turkish equivalent?**

It means 'cloud computing' in Turkish. It is a model where computing power, servers, and storage resources are rented on-demand via the internet backbone rather than local computers.

**What is the main difference between the 3 main cloud computing service models (IaaS, PaaS, SaaS)?**

IaaS is raw hardware and virtual server rental (AWS EC2), PaaS is a direct code execution and hosting environment (Vercel), and SaaS is turnkey software delivered to the end user over the web (Google Docs).

**What does the Shared Responsibility Model mean?**

It is a security division where the cloud provider is responsible for protecting the physical infrastructure, data center, and hardware, while the user is responsible for their own application security, user permissions (IAM), and data encryption.

**How can vendor lock-in be prevented?**

By using open-source standards (Docker containers, Kubernetes), independent database engines (PostgreSQL), and Infrastructure as Code (Terraform / OpenTofu) tools, software is isolated from provider-specific proprietary APIs.

## Related terms

- [SaaS](https://trescout.com/en/dictionary/saas/)
- [PaaS](https://trescout.com/en/dictionary/paas/)
- [IaaS](https://trescout.com/en/dictionary/iaas/)
- [Personal Cloud](https://trescout.com/en/dictionary/personal-cloud/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Memory Management](https://trescout.com/en/dictionary/memory-management/)

## Related tools

- [DevOps-Interview-Guide](https://trescout.com/en/discover/devops-interview-guide/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/cloud-computing/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/cloud-computing/
