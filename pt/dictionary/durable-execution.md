# O que é Durable Execution?

É um sistema que permite que um processo continue com segurança de onde parou, mesmo que haja um erro ou interrupção.

## Definição
Normalmente, se um programa de computador ficar sem energia ou falhar durante a execução, tudo será excluído e você terá que recomeçar. A execução durável registra cada etapa do programa, lembrando onde parou no momento da interrupção. Dessa forma, transações que levam horas podem ser concluídas com segurança.

## Como funciona
O sistema faz backup constante do estado do programa em um banco de dados. Quando ocorre um erro, o sistema reinicia o processo a partir do último ponto de backup.

## Onde é usado
É usado para transferências bancárias, longos processos de processamento de dados e fluxos de trabalho complexos de inteligência artificial.

## Costuma ser confundido com
Pode ser confundido com salvamento automático, mas preserva toda a lógica operacional do programa, não apenas o arquivo.

## Perguntas frequentes
**Todo programa deve ser durável?**
Não é necessário para transações curtas, mas é essencial para transações críticas que duram horas.

**Por que isso é tão importante?**
Em caso de erro, iniciar todo o processo do zero é perda de tempo e dinheiro.


## Termos relacionados
- [State Management](/pt/dictionary/state-management/)
- [Runtime](/pt/dictionary/runtime/)

## Ferramentas relacionadas
- [Pg Durable](/pt/discover/pg-durable/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/durable-execution/
