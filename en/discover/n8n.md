# Visual Workflows and AI Automation

n8n combines a visual canvas, custom code, AI agents and workflows in a fair-code automation platform. It supports self-hosted or cloud deployment and can include different model providers in your workflows.

- ★ 203,105
- GitHub Trending · 2026-08-23

## Installation
**Create the data volume**

```
docker volume create n8n_data
```


## Running it
**Start the n8n Docker container**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```


## What does this tool do?
With n8n, you can build workflows on a visual canvas and extend them with JavaScript, Python and npm packages. Official sources list model flexibility across OpenAI, Anthropic, Google and open-source models, along with human approvals, observability, role-based access and audit trails. The platform can be deployed self-hosted or in the cloud.

## Who it is for
Teams that want to combine visual workflow design with custom code and AI agents.

## What not to expect
People who only want closed-source licensed products or do not want to extend workflows with code or configuration.

## Highlights
- Combines a visual canvas, custom code and AI agents in workflows.
- Can be extended with JavaScript, Python and npm packages.
- Offers self-hosted and cloud deployment options.
- Lists human approvals, observability, role-based access and audit trails.

## First-use flow
- Follow the official quick start with Docker to run n8n.
- Open the editor on port 5678 in your browser.
- Create your first workflow on the visual canvas.
- Add custom code or a supported model provider according to your needs.

## Safe start

## First task prompt
Help me design a workflow on the visual canvas that accepts an input, processes it with an AI model and passes the result to the next step.

## Related dictionary terms

## Links
- GitHub repository →
- Official n8n GitHub repository →
- Official n8n documentation →
- n8n documentation repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/n8n/
