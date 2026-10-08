# O que é End-to-End Encryption?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> E2EE

A criptografia de ponta a ponta é um sistema de segurança que só pode ser lido pelas extremidades.

## Definição e origem da palavra

Os dados são bloqueados no dispositivo e desbloqueados no destino. O transportador e o servidor não conseguem ver o conteúdo. É o escudo fundamental da privacidade. WhatsApp e Signal são exemplos conhecidos.

***Analogia:** É semelhante a trocar cartas com uma caixa cuja chave apenas vocês dois possuem.*

## Como conhecer e usar no dia a dia?

**Mensagem:** Conversas privadas.
**Arquivo:** Transferência segura.
**Backup:** Cópia criptografada.

## Profundidade Técnica e Arquitetura

Layout:

**Par de chaves:** Chave pública e privada.
**Verificação:** Identidade da outra parte.
**Sigilo de transmissão:** A chave de sessão é atualizada.

Regra: O backup é mantido criptografado, a chave é armazenada separadamente. Em caso de perda do dispositivo, um código de recuperação é necessário.

## Coisas frequentemente misturadas

Pensa-se que é TLS. O TLS protege no caminho, o servidor vê. Na criptografia de ponta a ponta, nem o servidor consegue ver. Um é uma armadura de correio, o outro é um envelope selado.

## Use em diferentes disciplinas

**Caixa trancada:** O transportador não consegue ver o conteúdo.
**Selo:** Envelope que revela se foi aberto.
**Circuito fechado:** Linha fechada para o exterior.

## Perguntas Frequentes

**Se for roubado, pode ser lido?**

Não. A chave está nas pontas, o que foi roubado é um amontoado sem sentido.

**Está disponível em todos os aplicativos?**

Não. É verificado nas configurações, não se fazem suposições.

**Como funciona o backup?**

É necessário um backup criptografado e um código de recuperação. Não há restauração sem o código.

**É adequado para empresas?**

É equilibrado com a necessidade de registro e auditoria. A política é definida.

## Termos relacionados

- [Security Scanner](https://trescout.com/pt/dictionary/security-scanner/)
- [Linux Server Security](https://trescout.com/pt/dictionary/linux-server-security/)
- [SSO](https://trescout.com/pt/dictionary/sso/)

## Ferramentas relacionadas

- [Croc](https://trescout.com/pt/discover/croc/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/end-to-end-encryption/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/end-to-end-encryption/
