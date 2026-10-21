# O que é Intermediate CA?

*Desenvolvimento · Última atualização: 21 de outubro de 2026*

> Intermediate Certificate Authority

Autoridade intermediária localizada entre o certificado raiz, que verifica a identidade de sites seguros, e o usuário final.

## Definição

Uma autoridade de certificação intermediária (intermediate CA) é uma instituição de segurança intermediária autorizada pela autoridade de certificação raiz, constituindo a base de conexões HTTPS seguras na internet. Como o uso direto do certificado raiz em servidores expostos à internet cria um risco de segurança, essa tarefa é delegada aos certificados intermediários. Assim, certificados de segurança digital podem ser distribuídos com segurança para sites da Web, enquanto a cadeia de confiança principal é protegida.

***Analogia:** É semelhante ao fato de o governo, em vez de emitir identidades diretamente de sua sede, conceder uma autoridade de certificação a um cartório local e conduzir os processos de aprovação por meio dele.*

## Como funciona

Quando seu navegador acessa um site, o servidor apresenta uma cadeia de certificados. Essa cadeia começa no certificado do usuário final, passa pelo certificado intermediário e chega ao certificado raiz principal pré-instalado no seu dispositivo, estabelecendo assim um vínculo de confiança.

## Onde é usado

Atua ativamente no gerenciamento de certificados SSL/TLS, em configurações de servidores web e em infraestruturas de segurança corporativa.

## Costuma ser confundido com

Não é diretamente o certificado raiz em si, mas sim a etapa intermediária que atua como uma ponte que transporta a confiança entre a raiz e o ponto final.

## Perguntas frequentes

**Por que um certificado raiz direto não é usado no lugar do certificado intermediário?**

Se a chave privada do certificado raiz for comprometida, toda a segurança da internet poderá entrar em colapso; portanto, o risco é limitado com o uso de certificados intermediários.

**Como os navegadores verificam o certificado intermediário?**

O servidor transmite os certificados intermediários ausentes para o navegador, e o navegador conclui a verificação usando a cadeia de confiança integrada.

## Termos relacionados

- [End-to-End Encryption](https://trescout.com/pt/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/pt/dictionary/identity-provider/)
- [OIDC](https://trescout.com/pt/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/pt/dictionary/vulnerability-scanning/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/intermediate-ca/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/intermediate-ca/
