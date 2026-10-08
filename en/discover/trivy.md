# Container and cloud security scanner

Trivy is a comprehensive security scanning tool that detects vulnerabilities, misconfigurations, and secrets in containers, Kubernetes clusters, code repositories, and cloud infrastructures in seconds. It automates DevSecOps processes end-to-end with software bill of materials (SBOM) support.

- ★ 35,511
- Go
- GitHub Trending · 2026-06-04

## What you get

- Multi-layered target scanning: Inspects container images (Docker, OCI), local file systems, remote Git repositories, virtual machine disks and live Kubernetes clusters with a single tool.
- Zero additional infrastructure overhead: No need for an external database server or heavy agents running constantly; It delivers analysis in seconds as a single executable binary.
- Capturing sensitive data and secrets: It detects API keys, passwords and private certificates accidentally embedded in the source code or image layers with its heuristic engine.
- Infrastructure as code (IaC) audit: Catches security misconfigurations in Terraform, Dockerfile, Kubernetes YAML, and CloudFormation files before they go to production.
- SBOM and open source license compliance: Complies software supply chain security with legal regulations by producing software bill of materials in CycloneDX and SPDX standards.

## Installation

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Running it

**Scan container image**

```
trivy image imaj-adi:etiket
```

## Technical architecture and working principle

- Trivy DB and local cache: NVD automatically downloads a lightweight database cache containing GitHub Advisory Database, Red Hat, Debian, Ubuntu, and Alpine security bulletins. Since scans are performed through this local cache, it runs at lightning speed even in environments with network restrictions.
- Static layer analysis: Directly parses OCI layers without running container images or needing a Docker daemon. This approach does not compromise system security during the scanning process.
- IaC engine and Rego policies: Controls infrastructure templates with Open Policy Agent (OPA) compliant rules. Insecure open ports or services running with root privilege are reported immediately.
- SBOM standardization: The package manager scans the lock files (package-lock.json, poetry.lock, Cargo.lock, etc.) and creates a complete dependency map of your application.

## DevSecOps and CI/CD pipeline integration

- Early stage feedback: Developers instantly see vulnerabilities in open source libraries by running Trivy in their local environment before pushing their code to the remote repository.
- Automatic SARIF reporting: The produced SARIF outputs are transferred to GitHub Code Scanning or GitLab Security dashboards, allowing teams to perform central vulnerability tracking.
- Live cluster monitoring (Trivy Operator): It constantly monitors workloads running in the Kubernetes environment and instantly reports newly discovered zero-day (0-day) vulnerabilities.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up a security workflow on GitHub Actions that scans my Docker image and source codes with Trivy at every code push and pull request (PR). Can you make a complete .github/workflows/trivy.yml file that stops the build only on CRITICAL and HIGH level vulnerabilities (exit-code 1), uploads the findings to the GitHub Security dashboard in SARIF format, and creates a SBOM file in CycloneDX format?

## Frequently asked questions

- Can Trivy Docker scan container images without a daemon? Yes. Trivy can download and scan images directly from remote image repositories (Docker Hub, GitHub Container Registry, AWS ECR, etc.) or local tar archives without the need for a Docker client or daemon.
- Does it work in air-gapped environments without internet connection? Yes. The Trivy database (trivy-db) can be downloaded in advance and moved to a closed network environment. Trivy can scan through the local database cache without going online.
- What is SBOM and why is Trivy preferred in this field? SBOM (Software Bill of Materials) is a digital content list that documents all open source libraries, versions and licenses included in your software. Trivy is one of the few standard tools that can produce SBOM at both the image level and the source code level.
- How to exclude false positives or accepted risks? You can list the CVE codes you want to ignore line by line by adding a .trivyignore file to the project root directory. In this way, unnecessary compilation interruptions in CI/CD pipelines are prevented.

## Related dictionary terms

- [Secrets](https://trescout.com/en/dictionary/secrets/)
- [SBOM](https://trescout.com/en/dictionary/sbom/)
- [Root](https://trescout.com/en/dictionary/root/)
- [Workflows](https://trescout.com/en/dictionary/workflows/)
- [Database](https://trescout.com/en/dictionary/database/)
- [Binary](https://trescout.com/en/dictionary/binary/)

- **Who it is for:** For engineers who want to automate security audits, secret key checks, and SBOM generation in their software development and deployment processes.
- **License:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Developer:** Aqua Security and Open Source Community
- **Output Formats:** Table, JSON, SARIF, CycloneDX, SPDX, Template

## Links

- [GitHub repository →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-04: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/trivy/
