# O que é DTLS?

*Desenvolvimento · Última atualização: 7 de novembro de 2026*

> Datagram Transport Layer Security

É um protocolo de comunicação seguro adaptado para situações que exigem velocidade e continuidade na transmissão de dados.

## Definição

O DTLS é uma reformulação do protocolo TLS, que normalmente opera com base em TCP, para redes como UDP, que são contínuas, mas apresentam risco de perda de pacotes. Em situações onde o fluxo de dados em tempo real é vital, ele minimiza a latência sem abrir mão da segurança.

***Analogia:** É como enviar documentos valiosos por um mensageiro de moto rápido em vez de correio normal; a ordem dos pacotes pode às vezes ser alterada, mas ganha-se velocidade.*

## Como funciona

Ele adota as regras de criptografia e segurança da lógica do TLS, mas as flexibiliza para lidar com situações em que pacotes podem ser perdidos ou ter sua ordem alterada.

## Onde é usado

É utilizado em aplicativos de chamadas de voz e vídeo, jogos online e protocolos de transmissão ao vivo.

## Costuma ser confundido com

É confundido com o TLS padrão; a diferença fundamental é que um é seguro, mas lento, enquanto o outro é adequado para fluxos instantâneos.

## Perguntas e respostas

**Por que o TLS padrão não é utilizado?**

O TLS padrão não tolera a perda de pacotes e causa travamentos em transmissões ao vivo.

**Em que tipo de rede ele funciona?**

Geralmente funciona sobre protocolos de rede baseados em UDP.

## Termos relacionados

- [TLS](https://trescout.com/pt/dictionary/tls/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Streaming Applications](https://trescout.com/pt/dictionary/streaming-applications/)

## Ferramentas relacionadas

- [Openssl](https://trescout.com/pt/discover/openssl/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/dtls/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/dtls/
