# Memory Management Stack, Heap, coletor de lixo e memória do sistema


**Categoria:** Dev  

**Última atualização:** 2026-09-19


Gerenciamento de memória (memory management) é o conjunto de regras e mecanismos de software e hardware encarregados de alocar, rastrear e liberar a memória RAM durante a execução de programas.


## 1. Anatomia da Memória: Divisão entre Stack e Heap
Todo programa em execução estrutura o espaço de memória volátil em dois blocos operacionais distintos :
- **Memória de Pilha (Stack):** Estrutura sequencial LIFO (último a entrar, primeiro a sair) operada diretamente pelo registrador de pilha da CPU. Armazena variáveis locais simples e endereços de retorno de funções. A alocação e liberação são quase instantâneas ao avançar ou retroceder o ponteiro RSP.- **Memória de Monte (Heap):** Amplo repositório dinâmico reservado para estruturas de dados complexas cujo tamanho final não pode ser determinado na compilação. Requer chamadas a alocadores do sistema operacional, sendo mais flexível, porém mais lenta que a pilha.

## 2. Três Paradigmas Modernos de Gestão de Memória
As linguagens de programação contemporâneas dividem-se em três abordagens centrais :
- **Gerenciamento Manual (C e C++):** O programador requisita blocos via <code>malloc()</code> e assume a responsabilidade de liberá-los com <code>free()</code>. Concede máxima performance, mas pode causar falhas de segurança por ponteiros nulos ou vazamentos de memória.- **Coleta Automática de Lixo (Java, Go, JavaScript e Python):** Um mecanismo integrado (Garbage Collector) varre os objetos em execução e devolve ao sistema os dados sem referências ativas, gerando pequenas pausas de processamento.- **Modelo de Posse e Empréstimo (Rust):** Elimina o Garbage Collector sem abrir mão da segurança, validando a posse das variáveis em tempo de compilação e desalocando a memória no momento exato em que a variável sai de escopo.

## 3. Nível de Sistema Operacional: Memória Virtual e OOM Killer
Na base de todo o ecossistema, o kernel coordena a memória física auxiliado pela unidade MMU (Memory Management Unit) :
- **Memória Virtual e Paginação:** Cada processo possui uma visão isolada e protegida da memória dividida em páginas padronizadas de 4 KB mapeadas para a RAM física.- **Page Faults e Swap:** Caso um bloco de dados tenha sido transferido para o disco rígido, o processador gera uma interrupção para recarregar a informação de volta para a RAM.- **OOM Killer:** Em situações de esgotamento total da memória física, o kernel do Linux aciona o OOM Killer para encerrar compulsariamente os processos mais pesados, preservando a estabilidade da máquina.

## Por analogia
A memória Stack é como uma pilha de pratos na bancada onde colocamos e tiramos louças rapidamente do topo ; a memória Heap é como um grande depósito comercial onde caixas de qualquer tamanho são guardadas mediante um catálogo de localização.

## Perguntas frequentes

**Qual a principal diferença entre Stack e Heap?**  
A Stack é ultrarrápida, automática e atrelada ao escopo das funções ; a Heap é ampla, dinâmica e requer liberação manual ou atuação de um Garbage Collector.

**O que é vazamento de memória (memory leak)?**  
É o erro que ocorre quando um programa aloca dados na Heap e perde sua referência sem liberá-los, acumulando consumo de RAM até travar o sistema.

**Como o Rust garante segurança de memória sem Garbage Collector?**  
Por meio do sistema de Ownership e Borrow Checker verificado na compilação, inserindo a rotina de limpeza de dados no código final.

**O que faz o OOM Killer no Linux?**  
Ele finaliza processos de alto consumo de memória quando a RAM se esgota para evitar que o sistema operacional congele totalmente.

## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [State Management](/pt/dictionary/state-management/)
- [Serialization](/pt/dictionary/serialization/)
- [Network Stack](/pt/dictionary/network-stack/)
- [Assembly](/pt/dictionary/assembly/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/memory-management/
