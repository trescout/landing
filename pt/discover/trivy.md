# Verificador de segurança de contêineres e nuvem

Trivy é uma ferramenta abrangente de verificação de segurança que detecta vulnerabilidades, configurações incorretas e segredos em contêineres, clusters Kubernetes, repositórios de código e infraestruturas em nuvem em segundos. Ele automatiza os processos DevSecOps de ponta a ponta com suporte à lista de materiais de software (SBOM).

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## O que você ganha

- Varredura de alvo em várias camadas: inspeciona imagens de contêiner (Docker, OCI), sistemas de arquivos locais, repositórios Git remotos, discos de máquinas virtuais e clusters Kubernetes ativos com uma única ferramenta.
- Nenhuma sobrecarga adicional de infraestrutura: não há necessidade de um servidor de banco de dados externo ou de agentes pesados ​​em execução constante; Ele fornece análise em segundos como um único binário executável.
- Captura de dados confidenciais e segredos: detecta chaves de API, senhas e certificados privados incorporados acidentalmente no código-fonte ou nas camadas de imagem com seu mecanismo heurístico.
- Auditoria de infraestrutura como código (IaC): detecta configurações incorretas de segurança em arquivos Terraform, Dockerfile, Kubernetes YAML e CloudFormation antes de irem para produção.
- Conformidade com SBOM e licença de código aberto: Cumpre a segurança da cadeia de fornecimento de software com os regulamentos legais, produzindo listas de materiais de software nos padrões CycloneDX e SPDX.

## Instalação

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Execução

**Escanear imagem de contêiner**

```
trivy image imaj-adi:etiket
```

## Arquitetura técnica e princípio de funcionamento

- Banco de dados Trivy e cache local: o NVD baixa automaticamente um cache de banco de dados leve contendo boletins de segurança do GitHub Advisory Database, Red Hat, Debian, Ubuntu e Alpine. Como as varreduras são realizadas por meio desse cache local, ele funciona na velocidade da luz, mesmo em ambientes com restrições de rede.
- Análise de camada estática: analisa diretamente camadas OCI sem executar imagens de contêiner ou precisar de um daemon Docker. Esta abordagem não compromete a segurança do sistema durante o processo de digitalização.
- Mecanismo IaC e políticas Rego: controla modelos de infraestrutura com regras compatíveis com Open Policy Agent (OPA). Portas abertas inseguras ou serviços executados com privilégios de root são relatados imediatamente.
- Padronização SBOM: O gerenciador de pacotes verifica os arquivos de bloqueio (package-lock.json, poet.lock, Cargo.lock, etc.) e cria um mapa de dependência completo do seu aplicativo.

## Integração de pipeline DevSecOps e CI/CD

- Feedback em estágio inicial: os desenvolvedores veem instantaneamente vulnerabilidades em bibliotecas de código aberto executando o Trivy em seu ambiente local antes de enviar seu código para o repositório remoto.
- Relatórios SARIF automáticos: as saídas SARIF produzidas são transferidas para os painéis GitHub Code Scanning ou GitLab Security, permitindo que as equipes executem o rastreamento central de vulnerabilidades.
- Monitoramento de cluster ao vivo (Trivy Operator): ele monitora constantemente as cargas de trabalho em execução no ambiente Kubernetes e relata instantaneamente vulnerabilidades recém-descobertas de dia zero (0-day).

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero configurar um fluxo de trabalho de segurança no GitHub Actions que verifica minha imagem Docker e códigos-fonte com Trivy em cada solicitação push e pull de código (PR). Você pode criar um arquivo .github/workflows/trivy.yml completo que interrompa a construção apenas em vulnerabilidades CRÍTICAS e de ALTO nível (código de saída 1), carregue as descobertas para o painel de segurança do GitHub no formato SARIF e crie um arquivo SBOM no formato CycloneDX?

## Perguntas frequentes

- O Trivy Docker pode escanear imagens de contêiner sem um daemon? Sim. Trivy pode baixar e digitalizar imagens diretamente de repositórios de imagens remotos (Docker Hub, GitHub Container Registry, AWS ECR, etc.) ou arquivos tar locais sem a necessidade de um cliente Docker ou daemon.
- Funciona em ambientes isolados sem conexão com a internet? Sim. O banco de dados Trivy (trivy-db) pode ser baixado antecipadamente e movido para um ambiente de rede fechado. Trivy pode verificar o cache do banco de dados local sem ficar online.
- O que é SBOM e por que Trivy é preferido nesta área? SBOM (Software Bill of Materials) é uma lista de conteúdo digital que documenta todas as bibliotecas, versões e licenças de código aberto incluídas em seu software. Trivy é uma das poucas ferramentas padrão que pode produzir SBOM tanto no nível da imagem quanto no nível do código-fonte.
- Como excluir falsos positivos ou riscos aceitos? Você pode listar os códigos CVE que deseja ignorar linha por linha adicionando um arquivo .trivyignore ao diretório raiz do projeto. Dessa forma, são evitadas interrupções desnecessárias de compilação em pipelines de CI/CD.

## Termos relacionados do glossário

- [Secrets](https://trescout.com/pt/dictionary/secrets/)
- [SBOM](https://trescout.com/pt/dictionary/sbom/)
- [Root](https://trescout.com/pt/dictionary/root/)
- [Workflows](https://trescout.com/pt/dictionary/workflows/)
- [Database](https://trescout.com/pt/dictionary/database/)
- [Binary](https://trescout.com/pt/dictionary/binary/)

- **Para quem é:** Para engenheiros que desejam automatizar auditorias de segurança, verificações de chaves secretas e geração de SBOM em seus processos de desenvolvimento e implantação de software.
- **Licença:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Desenvolvedor:** Aqua Security e comunidade de código aberto
- **Formatos de saída:** Tabela, JSON, SARIF, CycloneDX, SPDX, Modelo

## Links

- [Repositório no GitHub →](https://github.com/aquasecurity/trivy)
- [Ler em turco →](https://trescout.com/discover/trivy/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-04: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/trivy/
