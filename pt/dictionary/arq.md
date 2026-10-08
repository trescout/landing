# O que é ARQ?

*Glossário · Dev · Última atualização: 12 de junho de 2026*

> Automatic Repeat Request

É um mecanismo de controle de erros que garante que as informações sejam reenviadas automaticamente quando ocorre um erro durante a transmissão de dados.

## Definição

Ao enviar dados pela Internet, às vezes os pacotes podem ser perdidos ou corrompidos. ARQ verifica se o destinatário recebeu os dados e, se detectar algum erro, informa ao remetente 'Não recebi, envie novamente'. Desta forma, garante-se que os dados são recebidos de forma completa e sem erros.

***Analogia:** Enquanto fala ao telefone, a outra parte diz: 'Não entendi, você pode falar de novo?' É como dizer e você repetir essa frase.*

## Como funciona

O remetente envia o pacote de dados e aguarda uma confirmação. Se a confirmação não for recebida dentro de um determinado período de tempo, o pacote será considerado danificado ou perdido e será enviado novamente.

## Onde é usado

É usado nos protocolos básicos e nos protocolos de rede da Internet, como o protocolo TCP.

## Perguntas frequentes

**Por que isso é tão importante?**

As conexões com a Internet nem sempre são perfeitas; ARQ garante a confiabilidade dos dados.

**Isso causará atraso?**

Sim, o reenvio de pacotes com defeito pode retardar um pouco o processo.

## Termos relacionados

- [API](https://trescout.com/pt/dictionary/api/)
- [DNS Tunneling](https://trescout.com/pt/dictionary/dns-tunneling/)
- [Computer Science](https://trescout.com/pt/dictionary/computer-science/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/arq/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/arq/
