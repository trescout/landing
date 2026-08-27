# O que é Append-only?

É um método de gravação no qual os dados só podem ser anexados, não podendo ser alterados ou excluídos.

## Definição
Ao adicionar informações a um banco de dados ou arquivo, o princípio é adicionar cada nova informação ao final da lista, em vez de substituir os dados antigos. Este método é fundamental para preservar o histórico e a segurança dos dados. Como nenhum dado é excluído, é possível rastrear todos os movimentos no sistema.

## Como funciona
O sistema aceita apenas um comando 'adicionar' em vez de um comando que atualiza os dados. Desta forma, o histórico dos dados é sempre preservado.

## Onde é usado
É usado em tecnologias blockchain, sistemas de manutenção de registros e bancos de dados auditáveis.

## Costuma ser confundido com
Pode ser confundido com bancos de dados tradicionais; os tradicionais podem atualizar os dados, este método nunca permite.

## Perguntas frequentes
**O que acontece se eu cometer um erro?**
Em vez de excluir os dados errados, você adiciona um novo registro que corrige o erro.

**Por que é tão seguro?**
Como os dados não podem ser alterados, é quase impossível manipular o passado.


## Termos relacionados
- [Database](/pt/dictionary/database/)
- [Logs](/pt/dictionary/logs/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/append-only/
