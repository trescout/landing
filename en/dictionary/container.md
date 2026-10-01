# What is Container?

A container packages an application with its code and dependencies into a single unit, ensuring it runs identically in any environment.

## Definition and Word Origin
Containers bundle the application's code, libraries, and settings into a single package. It runs on the server just like it does on your computer. The idea is old (chroot, LXC), became widespread with Docker after 2013, and is defined today by the OCI standard.

## How to Know and Use in Daily Life?
Distribution: The same package from developer to production.Microservice: Each service in its own box.CI: Running each test in a clean box.

## Technical Depth and Architecture
Concepts:

## Frequently Mixed Things
Mistaken for a virtual machine. A machine carries a full operating system, while a container carries only the application. Isolation is strong in a machine and sufficient in a container; the choice depends on the workload.

## Use in Different Disciplines
Shipping: Compatibility with ships, trains, and trucks using standard-sized containers.Kitchen: A ready-to-eat meal box with its ingredients inside.Camping: A camp set carried with its organization in a bag.

## Frequently Asked Questions
**Why is the container so popular?**
Because it ensures the same operation and fast setup in any environment. It has become a standard along with microservices and cloud orchestration.

**What is the difference between a container and a virtual machine?**
A machine carries its own operating system, while a container shares the host kernel. Containers are lightweight and fast, whereas machines are strong in isolation.

**Are containers secure?**
Since the kernel is shared, they are not as isolated as a machine. You need to pull images from trusted sources and keep them up to date.

**When are virtual machines preferred?**
When a different operating system or strong isolation is required. For most other workloads, a container is sufficient.


## Related terms
- [Containers](/en/dictionary/containers/)
- [Virtual Machines](/en/dictionary/virtual-machines/)
- [Deployment](/en/dictionary/deployment/)

## Related tools
- [N8n](/en/discover/n8n/)
- [Stirling-PDF](/en/discover/stirling-pdf/)
- [Core](/en/discover/core/)
- [Container](/en/discover/container/)
- [Mattermost](/en/discover/mattermost/)
- [Keycloak](/en/discover/keycloak/)
- [Trivy](/en/discover/trivy/)
- [PPF Contact Solver](/en/discover/ppf-contact-solver/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/container/
