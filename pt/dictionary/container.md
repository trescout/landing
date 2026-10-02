# O que é Container?

O container é o empacotamento do código de uma aplicação junto com suas dependências em um único pacote, garantindo que ela seja executada da mesma forma em qualquer ambiente.

## Definição e origem da palavra
Os containers colocam o código, as bibliotecas e as configurações da aplicação em um único pacote. Da mesma forma que funciona no seu computador, funciona no servidor. A ideia é antiga (chroot, LXC), popularizou-se após 2013 com o Docker e hoje é definida pelo padrão OCI.

## Como conhecer e usar no dia a dia?
Distribuição: O mesmo pacote do desenvolvedor para a produção.Microsserviço: Cada serviço tem sua própria caixa.CI: Cada teste é executado em uma caixa limpa.

## Profundidade Técnica e Arquitetura
Conceitos:

## Coisas frequentemente misturadas
Confundido com uma máquina virtual. A máquina possui um sistema operacional completo, enquanto o contêiner carrega apenas a aplicação. O isolamento é forte na máquina e suficiente no contêiner; a escolha é feita de acordo com a carga.

## Use em diferentes disciplinas
Transporte: Compatibilidade de navios, trens e caminhões com contêineres de tamanho padrão.Culinária: Uma marmita com os ingredientes já preparados dentro.Acampamento: Um kit de acampamento transportado com sua organização dentro da bolsa.

## Perguntas Frequentes
**Por que o contêiner é tão popular?**
Por garantir o mesmo funcionamento e uma instalação rápida em qualquer ambiente. Tornou-se um padrão juntamente com os microsserviços e a orquestração em nuvem.

**Qual é a diferença entre um contêiner e uma máquina virtual?**
A máquina possui seu próprio sistema operacional, enquanto o contêiner compartilha o núcleo principal. O contêiner é leve e rápido, e a máquina é forte em isolamento.

**O contêiner é seguro?**
Como o núcleo é compartilhado, ele não é tão isolado quanto uma máquina. Você precisa baixar as imagens de uma fonte confiável e mantê-las atualizadas.

**Quando a máquina virtual é preferida?**
Quando são necessários diferentes sistemas operacionais ou um isolamento forte. Para a maioria das outras cargas de trabalho, o contêiner é suficiente.


## Termos relacionados
- [Containers](/pt/dictionary/containers/)
- [Virtual Machines](/pt/dictionary/virtual-machines/)
- [Deployment](/pt/dictionary/deployment/)

## Ferramentas relacionadas
- [N8n](/pt/discover/n8n/)
- [Stirling-PDF](/pt/discover/stirling-pdf/)
- [Core](/pt/discover/core/)
- [Container](/pt/discover/container/)
- [Mattermost](/pt/discover/mattermost/)
- [Keycloak](/pt/discover/keycloak/)
- [Trivy](/pt/discover/trivy/)
- [PPF Contact Solver](/pt/discover/ppf-contact-solver/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/container/
