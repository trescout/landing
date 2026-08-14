# O que é Stacked Pull Requests?

É um método de introdução sequencial de grandes alterações de software no sistema, em partes pequenas e gerenciáveis, interconectadas.

## Definição
Ao desenvolver software, em vez de enviar uma grande mudança de uma só vez, você divide essa mudança em partes lógicas e as envia uma após a outra. Cada peça se baseia na anterior. Dessa forma, as pessoas que revisam seu código podem aprovar etapas pequenas e focadas com mais rapidez, em vez de tentar entender uma estrutura complexa de uma só vez.

## Como funciona
Divida suas alterações em blocos lógicos. Envie o primeiro bloco e comece a construir o próximo antes de ser aprovado. Esse processo garante que o código permaneça mais limpo e que os erros sejam detectados mais cedo.

## Onde é usado
Ele é usado em processos internos de revisão de código da equipe em plataformas como GitHub ou GitLab, especialmente ao desenvolver recursos grandes.

## Costuma ser confundido com
Pode ser confundido com uma única grande 'solicitação pull'; no entanto, este método oferece uma abordagem fragmentada e sequencial.

## Perguntas frequentes
**Por que não enviamos tudo de uma vez?**
Grandes mudanças são mais propensas a erros e dificultam a revisão do código por outras pessoas.

**Se tudo estiver conectado, o que acontece se uma parte quebrar?**
Por ser sequencial, você precisa gerenciar suas alterações com cuidado para evitar quebrar a cadeia.


## Termos relacionados
- [Code Review](/pt/dictionary/code-review/)
- [Git Push](/pt/dictionary/git-push/)
- [Checkout](/pt/dictionary/checkout/)

## Ferramentas relacionadas
- [Gh Stack](/pt/discover/gh-stack/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/stacked-pull-requests/
