# Agentless IT Automation Platform

Ansible is an agentless tool that performs system configuration, software deployment, and IT automation through simple YAML files.

- ★ 70,299
- GitHub Trending · 2026-07-04

## What does this tool do?
Ansible is an agentless tool that performs system configuration, software deployment, and IT automation through simple, readable YAML files. It allows you to manage your infrastructure as code and standardize complex tasks.

## Who it is for
Those who want to configure multiple servers simultaneously and reliably automate management processes.

## What not to expect
Those who only want to execute simple tasks on a single local machine and do not need an automation infrastructure.

## Highlights
- Does not require agent installation on target servers.
- Keeps configurations in an easy-to-read and easy-to-write YAML format.
- Offers broad integration support with thousands of ready-to-use modules.

## First-use flow
- Install the Ansible package on your control node.
- Add the IP addresses of the servers you will manage to the configuration file (inventory).
- Set up key-based authentication to ensure SSH access to target servers.
- Run a ping test on all servers to verify the connection.

## Safe start

## First task prompt
How to install Nginx on all web servers with Ansible?

## Installation
**Using pip (PyPI)**

```
pip install ansible
```

**macOS (Homebrew)**

```
brew install ansible
```


## Running it
**Run Ansible playbook script**

```
ansible-playbook site.yml
```


## Links
- GitHub repository →
- Official Ansible README →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/ansible/
