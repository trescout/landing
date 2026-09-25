# Container and cloud security scanner

Trivy is a comprehensive and lightning-fast security scanner that detects vulnerabilities (CVEs), misconfigurations, and leaked secrets across containers, Kubernetes clusters, repositories, and cloud environments. With native Software Bill of Materials (SBOM) generation, it automates DevSecOps compliance from code to production.

- ★ 35,511
- Go
- GitHub Trending · 2026-06-04

## What you get
- Multi-target scanning: Inspect container images (Docker, OCI), local filesystems, remote Git repositories, VM images, and live Kubernetes clusters with a single tool.
- Zero operational overhead: Requires no external database servers or persistent heavyweight background daemons; runs as a self-contained standalone binary.
- Secret and sensitive data detection: Identifies hardcoded API keys, passwords, and private tokens accidentally committed into source code or image layers.
- Infrastructure as Code (IaC) linting: Validates Terraform, Dockerfile, Kubernetes YAML, and CloudFormation templates against security policies before deployment.
- Native SBOM and license compliance: Generates CycloneDX and SPDX standard Software Bill of Materials to satisfy regulatory supply-chain compliance.

## Installation

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Basic usage

**Scan container image**

```
trivy image image-name:tag
```

**Scan local filesystem for vulnerabilities and secrets**

```
trivy fs --scanners vuln,secret,misconfig .
```

**Generate SBOM in CycloneDX format**

```
trivy image --format cyclonedx --output sbom.json image-name:tag
```

## Technical architecture and inner workings

Developed by Aqua Security and the open-source community, Trivy delivers production-grade DevSecOps guardrails:
- Trivy DB and cached vulnerability feeds: Automatically synchronizes a compact, local vulnerability database aggregated from NVD, GitHub Advisory Database, Red Hat, Debian, Ubuntu, and Alpine feeds for offline execution.
- Static layer parsing: Examines OCI image tar archives and filesystem layers directly without running containers or requiring Docker daemon privileges.
- IaC policy engine with Rego: Enforces Open Policy Agent (OPA) compliant rules to catch unencrypted buckets, open ports, and root privilege escalations.
- Deep dependency graph analysis: Parses lockfiles (package-lock.json, poetry.lock, Cargo.lock, go.sum) to detect direct and transitive supply-chain flaws.

## DevSecOps and CI/CD pipeline integration

Trivy serves as an automated quality gate in software delivery pipelines. Set specific severity thresholds to halt builds when severe risks are introduced:

**Fail CI build on Critical or High vulnerabilities**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH image-name:tag
```
- Shift-left feedback: Developers identify flaws in third-party libraries locally before pushing commits to remote repositories.
- Automated SARIF reports: Ingest SARIF outputs into GitHub Code Scanning or GitLab Security dashboards for centralized vulnerability triage.
- Live cluster monitoring (Trivy Operator): Continuously scans running Kubernetes workloads to surface newly disclosed zero-day vulnerabilities.

## If you do not code
🤖 If you do not code
I want to create a GitHub Actions workflow that scans my Docker image and source code with Trivy on every push and pull request. Can you provide a complete .github/workflows/trivy.yml file that fails the build (exit-code 1) only on CRITICAL and HIGH severity issues, uploads findings as SARIF to the GitHub Security tab, and generates a CycloneDX SBOM artifact?

- **Who it is for:** DevOps engineers, security teams, and software developers automating vulnerability scanning and SBOM generation.
- **License:** Apache-2.0 (Open source license)
- **Maintainer:** Aqua Security and Open Source Community
- **Output Formats:** Table, JSON, SARIF, CycloneDX, SPDX, Template

## Frequently asked questions
- Can Trivy scan images without the Docker daemon? Yes. Trivy can pull and inspect images directly from remote registries (Docker Hub, GitHub Container Registry, AWS ECR) or read archived tar files without Docker running.
- Does Trivy work in air-gapped environments? Yes. The vulnerability database can be pre-downloaded and transferred to isolated internal environments for completely offline scanning.
- What is an SBOM and why use Trivy for it? A Software Bill of Materials (SBOM) lists all open-source packages, versions, and licenses within an application. Trivy produces industry-standard CycloneDX and SPDX files for both codebases and built containers.
- How fast is a typical Trivy scan? Because Trivy evaluates vulnerabilities against its local pre-indexed database without network calls during execution, scans usually complete in a few seconds.

## Links
- [GitHub →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

## Related dictionary terms
Container CI-CD Vulnerability Scanning Cloud Native

---
Source: TreScout Discover · https://trescout.com/en/discover/trivy/
