# O que é In-process?

É a execução de um processo dentro da área de trabalho do próprio programa, sem a necessidade de ajuda externa.

## Definição
É um software que realiza a operação dentro de suas próprias fronteiras, sem se conectar a outro servidor ou serviço externo. Este método oferece vantagens de velocidade e segurança ao garantir que os dados não saiam da aplicação. Tudo acontece sob o mesmo teto, no mesmo espaço de memória.

## Como funciona
Enquanto o programa está em execução, ele usa as estruturas que mantém em sua própria memória, em vez de extrair os dados necessários de um banco de dados externo. Dessa forma, nenhum tráfego de rede ocorre e a transação é concluída com muito mais rapidez.

## Onde é usado
É frequentemente preferido em aplicativos de execução rápida e operações de banco de dados.

## Costuma ser confundido com
Pode ser confundido com a arquitetura cliente-servidor, onde o sistema é totalmente independente.

## Perguntas frequentes
**Devemos sempre trabalhar em processo?**
Não, se os seus dados forem muito grandes ou precisarem ser compartilhados, os sistemas externos fazem mais sentido.

**Há muita diferença na velocidade?**
Sim, como não há tempo para recuperar dados pela rede, as operações em processo são rápidas em milissegundos.


## Termos relacionados
- [In-process Vector Database](/pt/dictionary/in-process-vector-database/)
- [Runtime](/pt/dictionary/runtime/)
- [Memory Management](/pt/dictionary/memory-management/)

## Ferramentas relacionadas
- [Turso](/pt/discover/turso/)
- [Zvec](/pt/discover/zvec/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/in-process/
