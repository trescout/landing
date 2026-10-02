# O que é Memory Management?

Gerenciamento de Memória (Memory Management) é o processo de alocação, proteção e devolução ao sistema da memória de acesso aleatório (RAM) física e virtual do computador entre os softwares em execução, quando o uso termina.

## 1. Anatomia da memória: A distinção entre Stack (Pilha) e Heap (Monte)
Quando um programa é executado, o sistema operacional aloca um espaço de memória virtual (Virtual Address Space) específico para esse processo. Os dois componentes mais críticos desse espaço são a Stack e a Heap:

## 2. Três paradigmas fundamentais de gerenciamento de memória

## 3. Memória em nível de sistema operacional: Memória virtual e OOM Killer
Os sistemas operacionais modernos usam memória virtual e arquitetura de paginação para evitar que programas leiam a memória uns dos outros. A Unidade de Gerenciamento de Memória (MMU) na CPU converte endereços virtuais em endereços físicos em hardware com a ajuda do cache TLB. Quando a RAM física e a troca estão completamente esgotadas, o mecanismo OOM Killer (Out of Memory Killer) do kernel Linux encerra o processo mais agressivo com SIGKILL para salvar o sistema.

## Perguntas frequentes
**O que significa Memory management e qual é a sua tradução para o português?**
Memory Management significa "gerenciamento de memória" em português. É o conjunto de processos de alocação, monitoramento e liberação de recursos de RAM durante a execução de um programa de computador.

**Qual é a diferença fundamental entre Stack e Heap?**
A Stack gerencia variáveis locais conhecidas em tempo de compilação de forma extremamente rápida com a lógica LIFO; o Heap é o pool de memória flexível, com gerenciamento mais complexo, reservado para objetos que crescem dinamicamente em tempo de execução.

**Como funciona o Garbage Collection (Coletor de Lixo)?**
Em linguagens onde o programador não faz a exclusão manual (Java, Go, JS, etc.), o motor que roda em segundo plano detecta objetos órfãos que não podem ser alcançados a partir de variáveis raiz e limpa a RAM.

**Como evitar o vazamento de memória (Memory Leak)?**
Em linguagens manuais, escrevendo um free para cada malloc ou estabelecendo padrões RAII; em linguagens com coletor de lixo, limpando referências de arrays globais e ouvintes de eventos (event listeners) que não foram fechados.


## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [State Management](/pt/dictionary/state-management/)
- [Serialization](/pt/dictionary/serialization/)
- [Network Stack](/pt/dictionary/network-stack/)
- [Assembly](/pt/dictionary/assembly/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/memory-management/
