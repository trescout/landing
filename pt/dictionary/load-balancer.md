# O que é Load Balancer?

*Desenvolvimento · Última atualização: 20 de novembro de 2026*

É um roteador de tráfego que distribui o tráfego de rede de entrada entre vários servidores, evitando a falha do sistema e aumentando o desempenho.

## Definição

Um balanceador de carga (Load Balancer) distribui de forma equilibrada as solicitações dos usuários que chegam a um site ou serviço digital para um pool de servidores em segundo plano. Ele evita que um único servidor seja sobrecarregado e, em caso de falhas de hardware, redireciona o tráfego instantaneamente para servidores saudáveis. Assim, você garante que seu sistema forneça serviços de forma ininterrupta, rápida e confiável.

***Analogia:** É semelhante a um sistema de senhas em uma agência bancária movimentada, que direciona os clientes para os caixas que ficam livres, evitando aglomerações em frente a um único guichê.*

## Como funciona

A solicitação de rede do usuário, em vez de ir diretamente para o servidor, encontra primeiro o balanceador de carga. O sistema utiliza algoritmos como distribuição sequencial (Round Robin), menor número de conexões ou tempo de resposta do servidor para encaminhar a solicitação ao servidor mais adequado. Simultaneamente, ele verifica o estado de saúde dos servidores e remove automaticamente aqueles que apresentam falhas do fluxo de tráfego.

## Onde é usado

É utilizado em plataformas de e-commerce que atendem milhões de usuários, em arquiteturas de nuvem baseadas em microsserviços e em sistemas financeiros que não toleram interrupções.

## Costuma ser confundido com

Pode ser confundido com um API Gateway. Enquanto o API Gateway foca em funções como autenticação, transformação de solicitações e gerenciamento de API, o balanceador de carga tem como objetivo principal distribuir o tráfego de forma eficiente entre os servidores.

## Perguntas e respostas

**É obrigatório usar um balanceador de carga?**

Não é obrigatório para sites simples com baixo tráfego, mas torna-se indispensável para evitar interrupções quando sua aplicação cresce e um único servidor se torna insuficiente.

**Qual é a diferença entre um balanceador de carga de software e de hardware?**

Os modelos de hardware são dispositivos físicos dedicados instalados em data centers. Já os modelos de software, como NGINX ou HAProxy, são softwares flexíveis que rodam em ambientes de nuvem e servidores padrão.

## Termos relacionados

- [API Gateway](https://trescout.com/pt/dictionary/api-gateway/)
- [Reverse Proxy](https://trescout.com/pt/dictionary/reverse-proxy/)
- [Microservices](https://trescout.com/pt/dictionary/microservices/)
- [Cloud Computing](https://trescout.com/pt/dictionary/cloud-computing/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/load-balancer/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/load-balancer/
