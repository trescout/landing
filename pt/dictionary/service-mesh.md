# O que é Service Mesh?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Service mesh é a camada de infraestrutura invisível que gerencia o tráfego de microsserviços.

## Definição e origem da palavra

Em um sistema com centenas de partes, é difícil para elas se encontrarem e comunicarem com segurança. O service mesh gerencia a comunicação, organiza o tráfego e garante a segurança. Ele aplica políticas de rede sem tocar no código.

***Analogia:** É como a torre que gerencia o tráfego de voos em um grande aeroporto; garante que os serviços se movam com segurança sem colidir uns com os outros.*

## Como conhecer e usar no dia a dia?

**Nuvem:** Grandes aplicações baseadas em microsserviços.
**Banco:** Tráfego de serviços com segurança rigorosa.
**E-commerce:** Linha de pedidos sob carga de campanhas.

## Profundidade Técnica e Arquitetura

Peças:

**Sidecar:** O pequeno proxy ao lado de cada serviço, por onde o tráfego flui.
**Control plane:** O cérebro que distribui as regras.
**Data plane:** Os proxies que fazem o trabalho.
**mTLS:** Identidade criptografada entre serviços.
**Resiliência:** Nova tentativa e disjuntor.

Regra de nova tentativa:

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio e Linkerd são implementações conhecidas. Em um sistema pequeno, o custo supera o benefício.

## Use em diferentes disciplinas

**Aeroporto:** A torre que evita colisões de aviões.
**Tráfego:** A rede de sinalização que regula o fluxo.
**Correio:** O centro de distribuição que separa a remessa.

## Perguntas Frequentes

**É necessário para todos os projetos?**

Não. Em um sistema com poucos serviços, isso traz carga. Ganha sentido quando a complexidade aumenta.

**Quanto custa?**

Adiciona memória e latência por proxy. É pago em troca do ganho de observabilidade.

**O Kubernetes é obrigatório?**

Não, mas geralmente são usados juntos. Existem versões que também executam em máquinas virtuais.

**Substitui o API gateway?**

Não. O gateway é a porta de entrada externa, o mesh é o tráfego interno. Os dois trabalham juntos.

## Termos relacionados

- [Cloud Native](https://trescout.com/pt/dictionary/cloud-native/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Proxy](https://trescout.com/pt/dictionary/proxy/)

## Ferramentas relacionadas

- [Meshery](https://trescout.com/pt/discover/meshery/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/service-mesh/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/service-mesh/
