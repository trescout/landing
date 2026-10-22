# O que é Assembly?

*Desenvolvimento · Última atualização: 19 de setembro de 2026*

Assembly refere-se a dois conceitos básicos em ciência da computação: primeiro, a linguagem de programação simbólica de nível mais baixo (linguagem Assembly) que governa diretamente o processador de hardware (CPU); A segunda é transformar módulos de software compilados (montagem .NET) em um único pacote distribuível.

## 1. Linguagem de programação de baixo nível (linguagem Assembly)

O processador do computador entende apenas os sinais binários 0 e 1 (código de máquina/opcodes). A linguagem assembly consiste em abreviações simbólicas legíveis por humanos (mnemônicos) correspondentes a estes códigos de máquina brutos:

- MOV: Copia dados de um registro para outro ou endereço de memória.
- ADD/SUB: Executa operações matemáticas de adição e subtração.
- PUSH/POP: Adiciona ou extrai dados para a pilha de chamadas.
- JMP/JE/JNE: Ramifica o fluxo do programa para outro endereço de memória de acordo com o resultado da comparação.

Os códigos assembly escritos são traduzidos diretamente em código de máquina por meio de conversores chamados Assemblers (nasm, gas); Não há nenhuma camada de máquina virtual intermediária.

***Analogia:** A linguagem assembly é como colocar as engrenagens, molas e eixos de um relógio, um por um, com uma pinça sob um microscópio; Ele fornece a mais alta precisão e desempenho, mas requer muito cuidado. A montagem do software significa colocar esse delicado mecanismo dentro da caixa e encaixotá-lo como um relógio de pulso funcional.*

## 2. Registros do processador e arquitetura x86-64

Os registros mais críticos em um processador x86-64 moderno de 64 bits são:

- Registros de uso geral: RAX (acumulador e retorno de função), RBX (ponteiro de dados base), RCX (contador de loop), RDX (dados de entrada/saída), RDI e RSI (ponteiros de destino e origem).
- Registros de Propósitos Especiais: RSP (Stack Pointer - topo da pilha), RBP (Base Pointer - base do quadro de função), RIP (Instruction Pointer - endereço da próxima instrução a ser executada) e RFLAGS (Zero, Carry flags).

## 3. CISC vs RISC: diferença entre x86-64 e ARM64

A arquitetura x86-64 trabalha com a filosofia CISC (Complex Instruction Set); Possui tamanhos de instruções variáveis ​​e instruções ricas que podem operar diretamente na memória. ARM64 (Apple Silicon, Mobile) é baseado em RISC (Conjunto de Instruções Reduzido); Ele oferece grande superioridade em eficiência energética com seu comprimento de comando fixo de 32 bits e arquitetura Load-Store.

## 4. Exemplo de chamadas de sistema (Syscall) e Linux x86-64

```
section .text
global _start

_start:
    ; 1. Ekrana "Merhaba" yazdır (sys_write = syscall 1)
    mov rax, 1          ; syscall numarası: 1 (sys_write)
    mov rdi, 1          ; dosya tanıtıcı: 1 (stdout)
    mov rsi, mesaj      ; metnin bellek adresi
    mov rdx, 8          ; metin uzunluğu
    syscall             ; çekirdeğe geçiş yap

    ; 2. Programı güvenle sonlandır (sys_exit = syscall 60)
    mov rax, 60         ; syscall numarası: 60 (sys_exit)
    xor rdi, rdi        ; çıkış kodu 0
    syscall

section .data
    mesaj db "Merhaba", 10
```

## 5. Montagem .NET e WebAssembly (WASM)

- Assembly .NET: Quando o código C# é compilado, um pacote de assembly lógico (Assembly) é criado no formato .dll ou .exe contendo bytecodes e metadados CIL/MSIL.
- WebAssembly (WASM): um bytecode de máquina virtual de pilha portátil que permite que códigos C, C++ e Rust sejam executados no navegador com desempenho quase nativo.

## Perguntas frequentes

**O que significa montagem e o que ela faz?**

Assembly é a linguagem de programação simbólica de nível mais baixo que corresponde 1 a 1 ao conjunto de instruções de hardware do processador do computador. É usado para controlar diretamente os registros e a memória da CPU.

**Qual é a diferença entre Assembler e Compilador?**

O compilador (C, C++, Rust) analisa, otimiza e traduz lógica humana complexa e loops em código de máquina. O Assembler, por outro lado, converte instruções assembly, que já são versões simbólicas do código de máquina, diretamente em código de bytes binários.

**Onde a linguagem assembly ainda é usada hoje?**

É usado ativamente em kernels de sistemas operacionais (bootloader), drivers de dispositivos de hardware, engenharia reversa, análise de malware, detecção de vulnerabilidades cibernéticas e sistemas embarcados (IoT/microcontrolador).

**Qual é a diferença entre CISC e RISC?**

CISC (x86-64) possui um rico conjunto de instruções que pode executar vários subprocessos e acessos à memória em uma única instrução; RISC (ARM), por outro lado, é uma arquitetura simplificada e com baixo consumo de energia que executa cada comando em um único ciclo de clock.

## Termos relacionados

- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Compilation](https://trescout.com/pt/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/pt/dictionary/emulator/)

## Ferramentas relacionadas

- [Ghidra](https://trescout.com/pt/discover/ghidra/)
- [Apollo-11](https://trescout.com/pt/discover/apollo-11/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/assembly/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/assembly/
