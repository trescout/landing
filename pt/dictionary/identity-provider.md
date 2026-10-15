# O que é Identity Provider?

*Desenvolvimento · Última atualização: 22 de setembro de 2026*

Identity provider (provedor de identidade), é o serviço central que valida os logins.

## Definição e origem da palavra

Em vez de uma senha separada para cada aplicativo, o login é feito a partir de um único centro. O aplicativo pergunta ao serviço quem você é e recebe a confirmação. Sua senha não é distribuída para os aplicativos, ela permanece no centro.

***Analogia:** É semelhante a mostrar o passaporte na recepção do hotel para receber um cartão-chave; a porta do quarto confia na aprovação da recepção.*

## Como conhecer e usar no dia a dia?

**Empresa:** Todos os sistemas com um único login.
**Web:** Login com conta social.
**Institucional:** Ciclo de vida do funcionário.

## Profundidade Técnica e Arquitetura

Fluxo:

```
giriş → doğrulama → jeton → uygulama
```

Peças:

**Token de identidade:** O documento de quem você é.
**Token de acesso:** A permissão do que você pode fazer.
**MFA:** Segundo fator de prova além da senha.
**Sessão:** Single Sign-On (SSO).

Regra: O tempo do token é mantido curto, a renovação ocorre em segundo plano.

## Coisas frequentemente misturadas

É confundido com um gerenciador de senhas. Ele armazena a senha, este confirma a identidade. Um é um cofre, o outro é um tabelião.

## Use em diferentes disciplinas

**Recepção:** Passaporte versus cartão-chave.
**Tabelião:** Autenticação de identidade.
**Controle de passaporte:** Passagem com carimbo.

## Perguntas Frequentes

**É seguro?**

Sim. Como a senha não é distribuída para cada aplicativo, a superfície de ataque diminui.

**O que acontece se o sistema travar?**

Os aplicativos conectados são afetados. A redundância e um plano de acesso de emergência são essenciais.

**Qual é a diferença do SSO?**

SSO é uma experiência de login único, é a infraestrutura do provedor. Um é o rosto, o outro é a espinha dorsal.

**Posso configurar eu mesmo?**

Sim, existem opções de código aberto. A disciplina de patches e backups é de sua responsabilidade.

## Termos relacionados

- [SSO](https://trescout.com/pt/dictionary/sso/)
- [OIDC](https://trescout.com/pt/dictionary/oidc/)
- [RBAC](https://trescout.com/pt/dictionary/rbac/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/identity-provider/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/identity-provider/
