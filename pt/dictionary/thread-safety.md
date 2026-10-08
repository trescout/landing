# O que é Thread-safety?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Thread safety (Türkçe karşılığıyla iş parçacığı güvenliği), bir kodun aynı anda birden çok iş parçacığı tarafından çalıştırıldığında veriyi bozmamasıdır.

## Definição e origem da palavra

"Thread" significa encadeamento ou thread, e "safety" significa segurança. A segurança aqui não é contra hackers, mas sim para garantir que os dados permaneçam consistentes: se duas operações atualizarem a mesma conta ao mesmo tempo, o resultado pode estar incorreto. O código thread-safe regulamenta essa disputa. Aplicações bancárias, servidores web e todos os softwares multiprocessamento precisam disso.

***Analogia:** É como colocar uma tranca na porta em uma casa com um único banheiro; quando alguém está dentro, o outro tem que esperar.*

## Como conhecer e usar no dia a dia?

**Bancário:** Dois pedidos de saque da mesma conta não reduzem o saldo para negativo.
**Vendas de ingressos:** O último assento não deve ser vendido para duas pessoas ao mesmo tempo.
**Contadores:** O contador de visitantes aumenta um incremento completo a cada solicitação.

## Profundidade Técnica e Arquitetura

Ferramentas típicas são:

**Bloquear (Mutex/Bloquear):** Um thread entra na região crítica por vez, o outro espera.
**Operação atômica:** Leitura e escrita indivisíveis em uma única etapa.
**Dados imutáveis:** Os dados que não podem ser alterados não entram na corrida, são copiados.
**Mensagens:** Comunicação via fila em vez de dados compartilhados (por exemplo, canais Go).

Um pequeno exemplo de Python:

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

Nenhum outro thread pode intervir enquanto as linhas bloqueadas estão em execução. Se o bloqueio for esquecido ou recuperado na ordem errada, o programa poderá travar (impasse). É por isso que a região crítica é mantida curta.

## Coisas frequentemente misturadas

Não está relacionado à segurança cibernética. O assunto não são hackers, mas a consistência de dados: garantir que duas operações que acessam os mesmos dados ao mesmo tempo não sobrescrevam uma à outra.

## Use em diferentes disciplinas

**Tráfego:** Os semáforos que determinam a ordem de passagem em uma ponte de pista única.
**Culinária:** Cozinheiros que usam a mesma faca um de cada vez.
**Biblioteca:** A troca de um livro de exemplar único com o registro de empréstimos.

## Perguntas Frequentes

**O que acontece se não for thread-safe?**

Os dados se misturam, os cálculos dão errado ou o aplicativo trava. É difícil de depurar porque o erro não se repete a cada execução.

**Deve-se adicionar bloqueios a todo código?**

Não. Em código de thread único (single-threaded), os bloqueios trazem sobrecarga desnecessária. Apenas as seções concorrentes que acessam dados compartilhados são protegidas.

**O que é deadlock e como evitá-lo?**

É quando duas operações ficam travadas esperando pelo bloqueio uma da outra. Sempre adquirir os bloqueios na mesma ordem e manter a seção crítica curta reduz o risco.

**É detectado por testes?**

É difícil de detectar porque o erro depende de tempo (timing). Utilizam-se testes de carga e detectores de corrida (race detectors) especiais.

## Termos relacionados

- [Concurrency](https://trescout.com/pt/dictionary/concurrency/)
- [System Programming Language](https://trescout.com/pt/dictionary/system-programming-language/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/thread-safety/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/thread-safety/
