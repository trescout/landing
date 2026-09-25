# Scanner de segurança para contêineres e nuvem

O Trivy é uma ferramenta abrangente e extremamente rápida para detectar vulnerabilidades (CVEs), erros de configuração e segredos vazados em contêineres, clusters Kubernetes e repositórios. Com suporte nativo a SBOM, automatiza a segurança DevSecOps de ponta a ponta.

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## O que você ganha
- Verificação para múltiplos alvos: Inspecione imagens Docker/OCI, sistemas de arquivos, repositórios Git remotos e clusters Kubernetes com uma única ferramenta.
- Zero sobrecarga de infraestrutura: Não requer servidores de banco de dados externos nem daemons em segundo plano; roda como um binário independente.
- Detecção de segredos e chaves sensíveis: Identifica chaves de API, senhas e certificados privados commitados indevidamente no código ou nas camadas da imagem.
- Auditoria de infraestrutura como código (IaC): Valida arquivos Terraform, Dockerfile e manifestos Kubernetes YAML antes da implantação em produção.
- Conformidade com SBOM e licenças: Gera listas de materiais de software (SBOM) nos padrões CycloneDX e SPDX para atender normas de segurança da cadeia de suprimentos.

## Instalação

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Uso básico

**Verificar imagem de contêiner**

```
trivy image nome-imagem:tag
```

**Verificar código local e segredos**

```
trivy fs --scanners vuln,secret,misconfig .
```

**Gerar SBOM em formato CycloneDX**

```
trivy image --format cyclonedx --output sbom.json nome-imagem:tag
```

## Arquitetura técnica e funcionamento interno

Desenvolvido pela Aqua Security e comunidade open-source, o Trivy adota uma engenharia focada em velocidade e rigor:
- Banco de vulnerabilidades local (Trivy DB): Sincroniza uma base leve com dados do NVD, GitHub Advisory, Red Hat e Debian para realizar verificações ultrarrápidas offline.
- Análise estática de camadas: Decompõe camadas de imagem OCI sem executar o contêiner e sem depender do daemon do Docker, eliminando riscos de segurança.
- Motor IaC baseado em Rego: Avalia modelos de infraestrutura com políticas OPA (Open Policy Agent) para identificar portas abertas e permissões de root.
- Mapeamento profundo de dependências: Analisa arquivos de trava (package-lock.json, poetry.lock, Cargo.lock) para descobrir falhas transitivas.

## Integração DevSecOps e esteiras de CI/CD

O Trivy funciona como um portão de qualidade (quality gate) para barrar códigos vulneráveis antes da entrega em produção:

**Falhar build em vulnerabilidades críticas ou altas**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH nome-imagem:tag
```
- Feedback ágil à esquerda (Shift-left): Desenvolvedores identificam vulnerabilidades de pacotes open-source localmente antes do push.
- Relatórios automatizados em SARIF: Exporte para as abas de segurança do GitHub ou GitLab para triagem centralizada de riscos.
- Monitoramento de clusters (Trivy Operator): Rastreia continuamente cargas no Kubernetes para sinalizar vulnerabilidades de dia zero.

## Se você não programa
🤖 Se você não programa
Quero configurar um workflow do GitHub Actions que verifique minha imagem Docker e código com o Trivy a cada push e PR. Você pode criar um arquivo .github/workflows/trivy.yml completo que falhe o build (exit-code 1) apenas em vulnerabilidades CRITICAL e HIGH, envie os resultados em SARIF para a aba de segurança do GitHub e gere um artefato SBOM em formato CycloneDX?

- **Para quem:** Engenheiros DevOps, equipes de segurança e desenvolvedores que buscam automatizar auditorias de vulnerabilidades e gerar SBOM.
- **Licença:** Apache-2.0 (Código aberto permissivo)
- **Desenvolvedor:** Aqua Security e comunidade open-source
- **Formatos de saída:** Tabela, JSON, SARIF, CycloneDX, SPDX, Template

## Perguntas frequentes
- O Trivy pode verificar imagens sem o daemon do Docker? Sim. O Trivy pode baixar e inspecionar imagens diretamente de registros remotos (Docker Hub, GitHub Container Registry) ou ler arquivos tar locais sem o Docker rodando.
- Funciona em ambientes isolados (air-gapped)? Sim. O banco de dados do Trivy pode ser baixado previamente e transferido para redes isoladas para varreduras sem internet.
- O que é SBOM e por que usar o Trivy? SBOM é a lista digital de componentes que documenta bibliotecas e licenças do software. O Trivy gera SBOMs padronizados tanto para o código quanto para contêineres.
- Quão rápida é uma verificação típica? Como a consulta é feita contra o cache local pré-indexado sem depender da rede durante o scan, a análise completa ocorre em poucos segundos.

## Links
- [GitHub →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

## Termos relacionados do glossário
Container CI-CD Vulnerability Scanning Cloud Native

---
Source: TreScout Discover · https://trescout.com/pt/discover/trivy/
