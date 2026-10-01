# O que é ApacheBench (ab)?

> Apache HTTP Server Benchmarking Tool

É uma ferramenta de linha de comando que mede o desempenho e os limites de servidores web sob tráfego intenso de solicitações simultâneas.

## Definição
O ApacheBench (ab) é uma ferramenta de medição de desempenho leve e popular usada para testar quantas solicitações um servidor web pode atender dentro de um determinado período. Ao iniciar centenas de conexões simultâneas com um único comando a partir da linha de comando, ele relata a velocidade de resposta do sistema. Ajuda os desenvolvedores a validar as configurações do servidor e as otimizações de código.

## Como funciona
O usuário define o endereço de destino a ser testado, o número total de solicitações e a quantidade de conexões a serem abertas simultaneamente (concorrência) através do terminal. A ferramenta envia rapidamente as solicitações definidas para o servidor, coleta os tempos de resposta e apresenta métricas fundamentais, como solicitações por segundo (RPS), em formato de tabela.

## Onde é usado
É utilizado em testes de carga realizados antes de um site entrar no ar, em comparações de hardware de servidor e na medição do sucesso de otimizações de cache.

## Costuma ser confundido com
Diferente de ferramentas avançadas de teste de carga que simulam cenários complexos de usuário, ele foca apenas em aplicar carga sequencial ou simultânea a uma conexão HTTP específica.

## Perguntas frequentes
**O servidor web Apache é obrigatório para usar o ApacheBench?**
Não. Ele pode ser executado de forma independente para testar Nginx, Node.js ou qualquer outro servidor HTTP.

**Qual valor é mais observado nos resultados dos testes?**
O número de solicitações concluídas por segundo (Requests per second) e os tempos de latência das respostas em milissegundos são os indicadores mais críticos.


## Termos relacionados
- [Benchmark](/pt/dictionary/benchmark/)
- [CLI](/pt/dictionary/cli/)
- [Concurrency](/pt/dictionary/concurrency/)
- [Deployment](/pt/dictionary/deployment/)

## Ferramentas relacionadas
- [HEY](/pt/discover/hey/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/apache-bench/
