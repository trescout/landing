# O que é Cloud Computing?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Cloud Computing (computação em nuvem) é a entrega de recursos de computação, como servidores, armazenamento, bancos de dados, rede e software, através da internet a partir de centros de dados remotos sob demanda, em vez de infraestruturas físicas locais.

## Definição, origem etimológica e nascimento conceitual

A computação em nuvem (Cloud Computing) é o modelo de computação moderno que permite que empresas e engenheiros aluguem poder de processamento, memória, espaço de armazenamento e clusters de GPU para inteligência artificial em segundos através da internet, em vez de construir suas próprias salas de servidores e comprar hardware físico.

Conceitualmente, suas raízes remontam a 1961, a um discurso de John McCarthy, um dos pais da inteligência artificial, no MIT. McCarthy previu que o poder computacional seria oferecido no futuro como um serviço público (utility), assim como a eletricidade e a água. A fixação da palavra "nuvem" neste setor remonta à engenharia de telecomunicações e redes: na década de 1990, arquitetos de sistemas desenhavam um "ícone de nuvem" em diagramas para representar centrais telefônicas complexas e o backbone da internet cujos detalhes eles queriam abstrair. Com o lançamento do Simple Storage Service (S3) e do Elastic Compute Cloud (EC2) da Amazon para desenvolvedores em 2006, o modelo de compra de servidores focado em despesas de capital (CapEx) deu lugar ao princípio de pagamento pelo uso (OpEx).

***Analogia:** É como conectar-se diretamente à rede elétrica nacional em vez de construir uma usina hidrelétrica ou um gerador privado no jardim da sua fábrica ou casa. Assim que você conecta o plugue na tomada, a eletricidade flui; quanto mais energia sua máquina consome, mais você paga apenas por esse consumo no final do mês; você não precisa se preocupar com falhas no gerador, combustível ou manutenção do transformador.*

## Modelos básicos de serviço e distribuição (IaaS, PaaS, SaaS, Serverless)

A arquitetura de computação em nuvem é dividida em quatro modelos principais de serviço, de acordo com os níveis de abstração:

1. IaaS (Infrastructure as a Service · Infraestrutura como Serviço): É o nível mais básico, composto por máquinas virtuais brutas, discos de armazenamento em bloco e topologias de rede virtual. AWS EC2, Google Compute Engine e Azure VM estão nesta categoria. O provedor de nuvem gerencia o hardware e a camada de virtualização; o desenvolvedor é responsável pela instalação do sistema operacional, patches de segurança e pela pilha de software.
2. PaaS (Platform as a Service · Plataforma como Serviço): São plataformas que livram o desenvolvedor das preocupações com configuração de servidor, sistema operacional e ambiente de execução (runtime). Vercel, Heroku e AWS Elastic Beanstalk podem ser citados como exemplos. O engenheiro envia apenas o código-fonte; o escalonamento, os certificados SSL e o balanceamento de carga são tratados automaticamente em segundo plano.
3. SaaS (Software as a Service · Software como Serviço): São softwares prontos para uso, acessados pelo usuário final diretamente por meio de um navegador web ou API, cuja manutenção é de total responsabilidade do fabricante. Google Workspace, Slack, Salesforce e Figma são os exemplos mais conhecidos deste modelo.
4. Serverless (FaaS · Function as a Service): É uma arquitetura orientada a eventos que abstrai completamente o conceito de servidor. O código escrito no AWS Lambda ou Cloudflare Workers é executado apenas quando um gatilho, como uma solicitação HTTP ou um evento de banco de dados, é acionado, funcionando em milissegundos e encerrando-se em seguida. Gera custo zero quando não há tráfego.

Os modelos de implementação são moldados de acordo com o local onde os dados estão alojados:

- Nuvem Pública: Estrutura na qual os recursos são compartilhados em um modelo multilocatário (multi-tenant) nos data centers globais de grandes provedores.
- Nuve Privada: Ambiente isolado utilizado por setores regulamentados, como finanças, defesa e saúde, em data centers dedicados exclusivamente a eles.
- Nuvem Híbrida (Hybrid Cloud): Uma estrutura híbrida na qual dados confidenciais de clientes são processados em servidores locais (on-premise), enquanto a camada web, que exige alto volume de processamento, opera na nuvem pública.
- Multi-Cloud: A configuração distribuída de sistemas entre AWS, Google Cloud e Azure para evitar a dependência de um único fornecedor (vendor lock-in).

## Ciência da computação e arquitetura de sistemas: Hypervisor, contêiner e CAP

O milagre técnico subjacente à computação em nuvem é a abstração de hardware via software (virtualização):

- Camada de Hypervisor: É o software central que divide os recursos de processador e RAM de um único servidor físico para compartilhá-los entre dezenas de máquinas virtuais (VMs) independentes. Os hypervisors do tipo 1 Bare-metal (KVM, VMware ESXi), que rodam diretamente sobre o hardware, são a espinha dorsal de desempenho dos provedores de nuvem.
- Contêineres e Orquestração: Para superar a sobrecarga da replicação do sistema operacional das máquinas virtuais, os contêineres Docker surgiram utilizando os recursos de cgroups (limitação de recursos) e namespaces (isolamento de processos) do kernel Linux. Já a implantação automática e a autorrecuperação (self-healing) de milhares de contêineres são garantidas pelos clusters Kubernetes.
- Teorema CAP e Resiliência Distribuída: As infraestruturas de nuvem globais operam dentro dos limites do Teorema CAP de Eric Brewer. No momento de uma partição de rede (Network Partition), o sistema deve priorizar a Consistência de Dados (Consistency) ou a Disponibilidade Ininterrupta (Availability). Arquitetos de nuvem implementam cenários de recuperação de desastres com arquiteturas geograficamente redundantes (Multi-Region / Availability Zone).
- Modelo de Responsabilidade Compartilhada: A segurança na nuvem é dividida em duas partes. O provedor é responsável pela segurança dos data centers físicos, servidores, hypervisor e cabos de rede ("Segurança DA Nuvem"). O cliente, por sua vez, é responsável pelas atualizações do sistema operacional, criptografia, funções de IAM (gerenciamento de acesso) e vulnerabilidades do código da aplicação ("Segurança NA Nuvem").

## Dimensão econômica, ecológica e geopolítica

A computação em nuvem não é apenas uma revolução técnica, mas também uma ruptura massiva na alocação global de recursos:

- Paradoxo de Jevons: O princípio estabelecido pelo economista do século XIX William Stanley Jevons para o consumo de carvão também se aplica à nuvem: à medida que o acesso ao poder computacional se torna mais barato e fácil, o consumo total não diminui, mas, pelo contrário, aumenta exponencialmente. Hoje, a capacidade de treinar modelos de inteligência artificial com centenas de bilhões de parâmetros é um resultado direto das economias de escala oferecidas pela computação em nuvem.
- Consumo de Energia e Água: Os data centers de hiperescala consomem cerca de 1-2% da eletricidade global, e milhões de metros cúbicos de água pura são utilizados para resfriar grandes clusters de GPUs. Essa situação tornou obrigatória a instalação de data centers próximos a fontes de energia renovável e climas frios.
- Soberania Digital e Regimes Jurídicos: Onde os dados estão fisicamente armazenados é uma questão geopolítica. Enquanto a lei CLOUD Act dos EUA concede às empresas americanas autoridade para intervir em servidores no exterior, a União Europeia, com o GDPR e a iniciativa GAIA-X, e a Turquia, com a legislação KVKK, incentivam que dados críticos permaneçam dentro das fronteiras nacionais.

## Costuma ser confundido com

- Armazenamento em Nuvem vs Computação em Nuvem: Google Drive, iCloud ou Dropbox são apenas serviços de armazenamento; a computação em nuvem, por outro lado, é um ecossistema gigantesco que, além do armazenamento, inclui poder de processamento dinâmico, treinamento de inteligência artificial, gerenciamento de rede e orquestração de banco de dados.
- Serverless (Sunucusuz) vs. Verdadeiramente Serverless: Na arquitetura serverless, é claro que existem servidores físicos; o termo "serverless" indica que o desenvolvedor não precisa mais se preocupar em configurar, atualizar ou monitorar um servidor, sendo que o gerenciamento do servidor é tornado invisível pelo provedor.

## Perguntas frequentes

**O que significa cloud computing e qual é a sua tradução para o português?**

Em português, significa 'computação em nuvem'. É um modelo onde o poder de processamento, servidores e recursos de armazenamento são alugados instantaneamente conforme a necessidade através da espinha dorsal da internet, em vez de computadores locais.

**Qual é a principal diferença entre os 3 principais modelos de serviço de computação em nuvem (IaaS, PaaS, SaaS)?**

IaaS é o aluguel de hardware bruto e servidores virtuais (AWS EC2), PaaS é um ambiente de execução e hospedagem direta de código (Vercel), e SaaS é um software pronto para uso oferecido ao usuário final via web (Google Docs).

**O que significa o Modelo de Responsabilidade Compartilhada (Shared Responsibility Model)?**

É a divisão de segurança onde o provedor de nuvem é responsável por proteger a infraestrutura física, o data center e o hardware; enquanto o usuário é responsável pela segurança de suas próprias aplicações, permissões de usuário (IAM) e criptografia de dados.

**Como evitar a dependência de um fornecedor de nuvem (Vendor Lock-in)?**

Utilizando padrões de código aberto (contêineres Docker, Kubernetes), motores de banco de dados independentes (PostgreSQL) e ferramentas de Infraestrutura como Código (Terraform / OpenTofu), os softwares são isolados de APIs proprietárias específicas do fornecedor.

## Termos relacionados

- [SaaS](https://trescout.com/pt/dictionary/saas/)
- [PaaS](https://trescout.com/pt/dictionary/paas/)
- [IaaS](https://trescout.com/pt/dictionary/iaas/)
- [Personal Cloud](https://trescout.com/pt/dictionary/personal-cloud/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)

## Ferramentas relacionadas

- [DevOps-Interview-Guide](https://trescout.com/pt/discover/devops-interview-guide/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/cloud-computing/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/cloud-computing/
