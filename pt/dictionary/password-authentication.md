# O que é Password Authentication?

*Desenvolvimento · Última atualização: 6 de novembro de 2026*

É o processo de usar uma senha para verificar a identidade do usuário ao fazer login no sistema.

## Definição

A autenticação por senha é um método de verificar a senha secreta definida por um usuário para determinar se ele tem o direito de acessar um sistema digital. O sistema solicita que o usuário prove ser quem afirma ser. A senha inserida é comparada com sua contraparte criptografada armazenada com segurança no banco de dados.

***Analogia:** É semelhante a inserir e girar a chave correta na fechadura da porta para entrar em casa. Se a chave estiver correta, a porta se abre; se estiver errada, você fica do lado de fora.*

## Como funciona

O nome de usuário e a senha são digitados na tela correspondente e enviados. O software no lado do servidor não armazena a senha diretamente como texto simples; em vez disso, ele a processa por meio de funções de hash matemáticas seguras. Se o hash da senha recebida for igual ao hash no banco de dados, a permissão de acesso é concedida.

## Onde é usado

É usado como uma camada básica de segurança em logins de usuários em sites, telas de início de sessão de computadores, painéis de gerenciamento de servidores em nuvem e acessos a redes corporativas.

## Costuma ser confundido com

Pode ser confundido com autorização. A autenticação por senha prova quem você é, enquanto a autorização determina o que você pode acessar ao entrar no sistema.

## Perguntas e respostas

**Como as senhas são armazenadas no banco de dados?**

Por razões de segurança, elas nunca são armazenadas como texto simples. Elas são criptografadas de forma irreversível usando algoritmos de hash especiais e técnicas de salting.

**É seguro o suficiente por si só?**

Atualmente, como é fácil de ser roubada ou adivinhada, geralmente é complementada com medidas adicionais, como a autenticação em duas etapas.

## Termos relacionados

- [SSO](https://trescout.com/pt/dictionary/sso/)
- [OIDC](https://trescout.com/pt/dictionary/oidc/)
- [RBAC](https://trescout.com/pt/dictionary/rbac/)
- [Security Scanner](https://trescout.com/pt/dictionary/security-scanner/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/password-authentication/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/password-authentication/
