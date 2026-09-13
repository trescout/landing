# O que é Worktree?

É uma estrutura que permite trabalhar em diferentes versões do projeto simultaneamente, sem alterar a pasta do projeto original.

## Definição
O Worktree permite que você abra diferentes ramificações (branches) do projeto em pastas separadas sem interromper seu espaço de trabalho principal durante o desenvolvimento de software. Por exemplo, enquanto desenvolve um recurso no projeto principal, você pode corrigir um erro antigo em outra pasta ao mesmo tempo. Isso elimina a perda de tempo e a confusão causadas pela troca constante de ramificações.

## Como funciona
Você adiciona um novo worktree através de sistemas de controle de versão como o Git. O sistema vincula uma cópia do projeto a um diretório diferente para você, e você continua trabalhando lá sem tocar no diretório principal.

## Onde é usado
É utilizado em projetos de software complexos, em situações onde correções de erros urgentes precisam ser feitas durante o desenvolvimento de recursos de longa duração.

## Costuma ser confundido com
Não é o mesmo que apenas copiar pastas; os worktrees estão vinculados ao mesmo repositório Git e funcionam de forma sincronizada entre si.

## Perguntas frequentes
**Por que não copiamos pastas separadas?**
Copiar desperdiça espaço em disco e torna o gerenciamento do histórico do Git difícil; o worktree é muito mais eficiente.

**Funciona em todos os projetos Git?**
Sim, este recurso é suportado em todas as versões modernas do Git.


## Termos relacionados
- [Source Control](/pt/dictionary/source-control/)
- [Git Push](/pt/dictionary/git-push/)
- [Repository Checkout](/pt/dictionary/repository-checkout/)

## Ferramentas relacionadas
- [Worktrunk](/pt/discover/worktrunk/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/worktree/
