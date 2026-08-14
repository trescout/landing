# O que é Secrets?

Estas são as senhas, chaves de API e códigos de acesso que os aplicativos de software precisam para operar com segurança.

## Definição
Segredos são informações secretas que um programa usa para se autenticar ao se conectar a outro sistema. Muitas vezes, podem ser senhas de banco de dados, chaves privadas ou tokens de acesso a serviços. Como a incorporação dessas informações no código representa um risco à segurança, elas geralmente são armazenadas em sistemas especiais de cofre.

## Como funciona
Em vez de gravar essas informações confidenciais em arquivos de código, os desenvolvedores as definem com segurança para o aplicativo usando variáveis ​​de ambiente ou ferramentas de gerenciamento confidenciais.

## Onde é usado
É usado em serviços em nuvem, conexões de banco de dados e processos de autenticação de aplicativos.

## Costuma ser confundido com
Pode ser confundida com senhas normais de usuários, mas são identidades digitais projetadas para máquinas, não para pessoas.

## Perguntas frequentes
**Por que os segredos não são mantidos dentro do código?**
Quando você compartilha seu código ou o carrega acidentalmente na Internet, qualquer pessoa pode obter essas chaves e se infiltrar em seus sistemas.

**O que devo fazer se os segredos forem roubados?**
Você deve cancelar imediatamente essa chave, criar uma nova e verificar se há alguma infiltração em seu sistema.


## Termos relacionados
- [API](/pt/dictionary/api/)
- [Self-hosting](/pt/dictionary/self-hosting/)
- [Observability](/pt/dictionary/observability/)

## Ferramentas relacionadas
- [Trivy](/pt/discover/trivy/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/secrets/
