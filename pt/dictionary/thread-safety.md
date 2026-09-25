# O que é Thread Safety?

> Inglês: Thread Safety · Etimologia: inglês arcaico thraed (fio, meada) + latim salvus (ileso/seguro)

**Categoria:** Dev  
**Última atualização:** 2026-09-22

Thread safety (segurança de thread) é a propriedade de um algoritmo ou estrutura de dados de funcionar corretamente quando acessado por múltiplas threads simultaneamente, evitando corrupção de memória.

## Definição e etimologia
O conceito combina thread (linha de execução independente) e segurança de coerência de dados. Não se trata de segurança contra invasores externos, mas de preservar a consistência das informações: se dois processos alteram o mesmo saldo ao mesmo tempo sem coordenação, o valor final resultará incorreto.

## Contexto cotidiano e uso prático
Cenários práticos que exigem thread safety :
- **Transações Bancárias:** Garantir que saques concorrentes não permitam retirar mais dinheiro do que o disponível.- **Venda de Ingressos:** Assegurar que um assento numerado seja reservado para apenas um comprador.- **Servidores de Aplicação:** Responder a milhares de requisições simultâneas sem corromper estruturas em cache.

## Profundidade técnica e arquitetura
Estratégias de engenharia para atingir thread safety :
- **Exclusão Mútua (Mutex e Locks):** Bloqueios temporários que garantem acesso exclusivo à seção crítica.- **Operações Atômicas:** Instruções de hardware (como CAS) que executam leitura e escrita em passo único e indivisível.- **Imutabilidade:** Dados constantes que podem ser lidos por quantas threads forem necessárias sem travas.- **Sistemas de Tipos Modernos (Rust):** Regras de ownership verificadas em tempo de compilação que eliminam data races.

## Costuma ser confundido com
É comum confundir com segurança cibernética. O objetivo aqui não é barrar vírus ou hackers, mas evitar anomalias e comportamentos imprevisíveis na concorrência de memória.

## Perspectivas interdisciplinares
Exemplos cotidianos :
- **Trânsito:** Uma ponte de pista única controlada por semáforos alternados.- **Cozinha Profissional:** Cozinheiros que compartilham uma única faca afiada, usando-a um por vez.- **Fila Bancária:** Atendimento individual por caixa, evitando que dois clientes sejam atendidos juntos no mesmo guichê.

## Por analogia
É como colocar um trinco na porta de um banheiro compartilhado: enquanto alguém estiver usando, os demais esperam do lado de fora.

## Perguntas frequentes

**O que acontece quando o código não é thread-safe?**  
Ocorrem condições de corrida que alteram silenciosamente variáveis na memória, gerando falhas difíceis de reproduzir.

**O uso de travas (locks) resolve tudo?**  
Travas mal projetadas podem causar deadlocks, onde duas threads ficam bloqueadas aguardando a liberação mútua de recursos.

**Como linguagens modernas lidam com isso?**  
Linguagens como Rust utilizam o sistema de posse e empréstimo de memória para barrar erros de concorrência antes mesmo da execução.

**Dados imutáveis são sempre seguros entre threads?**  
Sim, pois se a estrutura nunca é alterada após sua criação, leituras concorrentes ocorrem sem qualquer interferência mútua.

## Termos relacionados
- [Concurrency](/pt/dictionary/concurrency/)
- [System Programming Language](/pt/dictionary/system-programming-language/)
- [Mutex](/pt/dictionary/mutex/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/thread-safety/
