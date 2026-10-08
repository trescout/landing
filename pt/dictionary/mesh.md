# O que é Mesh?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Mesh (em português, rede em malha) é uma estrutura de rede em que dispositivos ou serviços se conectam e transferem dados entre si sem depender de um servidor central.

## Definição e origem da palavra

Mesh em inglês significa malha ou rede. Assim como os nós de uma rede de pesca são conectados entre si, cada nó em uma rede mesh está conectado aos seus vizinhos. Em redes sem fio, o Wi-Fi mesh, e em arquiteturas de microsserviços, o service mesh (ex. Istio, Linkerd) são dois usos comuns desse conceito.

***Analogia:** É como todos os músicos tocarem em harmonia, ouvindo uns aos outros, sem um maestro.*

## Como conhecer e usar no dia a dia?

**Mesh Wi-Fi em casa:** Enquanto um único modem fica fraco em um cômodo, 2 a 3 unidades mesh colocadas pela casa fornecem cobertura contínua sob um único nome de rede. Sua conexão não cai ao passar de um cômodo para outro.
**Casa inteligente:** A lâmpada, o termostato e os sensores são conectados entre si; se um deles for desativado, o sinal continua seu caminho através do dispositivo vizinho.
**Redes de emergência:** Em áreas onde a infraestrutura foi danificada, os telefones se conectam uns aos outros para transmitir mensagens.

## Profundidade Técnica e Arquitetura

Existem três mecanismos que sustentam a estrutura de malha (mesh):

**Descoberta de nós (Discovery):** Cada nó descobre os nós ao seu redor e mantém sua lista de conexões atualizada.
**Roteamento:** Os dados são transferidos de nó para nó, da origem ao destino. Alguns protocolos transmitem a mensagem para todos, enquanto outros calculam o caminho mais curto.
**Auto-recuperação:** Se um nó ficar inativo, o tráfego é automaticamente redirecionado para outro caminho. Não há um único ponto de falha.

Essa resiliência tem um preço: cada salto (hop) adiciona latência e, como os nós transportam o tráfego uns dos outros, a largura de banda total é compartilhada. É por isso que as redes mesh são preferidas onde a cobertura e a resiliência são mais importantes do que a velocidade.

O service mesh em microsserviços é um pouco diferente: um pequeno proxy chamado sidecar é colocado ao lado dos serviços. O tráfego flui através desses proxies, de modo que políticas de observabilidade, segurança e novas tentativas são aplicadas a cada serviço sem a necessidade de escrever código separado.

## Use em diferentes disciplinas

**Urbanismo:** Ruas em grade. Se uma rua for fechada, o tráfego flui pelas ruas vizinhas.
**Têxtil:** Trama do tecido. Mesmo se um único fio se romper, o tecido mantém sua integridade estrutural.
**Biologia:** Redes neurais. O sinal pode contornar a região danificada.

## Perguntas Frequentes

**Para que serve o Mesh Wi-Fi?**

Ele fornece um sinal forte em todos os cômodos da casa sob um único nome de rede. A diferença em relação aos repetidores de alcance é que ele tenta não perder a conexão ao alternar entre os cômodos.

**Service mesh e rede mesh são a mesma coisa?**

Não. Uma rede mesh é a forma como os dispositivos se conectam. Um service mesh, por outro lado, é a camada de software que gerencia o tráfego entre microsserviços. Ambos se alimentam da ideia de conectividade descentralizada.

**Mesh é sempre melhor?**

Não. Em casas pequenas ou ambientes com poucos dispositivos, um único modem potente pode ser mais simples e rápido. O Mesh faz sentido para problemas de cobertura ou estruturas com vários nós.

**É difícil de instalar?**

Os kits mesh residenciais geralmente são configurados em minutos com um aplicativo móvel. Já a instalação de rede mesh corporativa ou de serviço exige planejamento.

## Termos relacionados

- [Service Mesh](https://trescout.com/pt/dictionary/service-mesh/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Distributed](https://trescout.com/pt/dictionary/distributed/)

## Ferramentas relacionadas

- [Bitchat](https://trescout.com/pt/discover/bitchat/)
- [Meshery](https://trescout.com/pt/discover/meshery/)
- [Meshoptimizer](https://trescout.com/pt/discover/meshoptimizer/)
- [Modly](https://trescout.com/pt/discover/modly/)
- [Tailcat](https://trescout.com/pt/discover/tailcat/)
- [Bitchat Android](https://trescout.com/pt/discover/bitchat-android/)
- [Spirula Studio](https://trescout.com/pt/discover/spirula-studio/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/mesh/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/mesh/
