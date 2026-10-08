# Assembly: Definição, registradores e arquitetura de sistemas

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Assembly refere-se a dois conceitos essenciais na ciência da computação: a linguagem simbólica de mais baixo nível para controle direto da CPU e os pacotes de implantação modulares (.NET assemblies).

## 1. Linguagem de Baixo Nível (Assembly Language)

Processadores entendem apenas códigos binários de máquina (opcodes). A linguagem assembly converte esses números em mnemônicos legíveis por humanos:

- `MOV`: transfere dados entre registradores ou posições de memória.
- `ADD` / `SUB`: realiza operações aritméticas diretas.
- `PUSH` / `POP`: manipula elementos no topo da pilha de chamadas (stack).
- `JMP` / `JE` / `JNE`: desvia o fluxo de execução baseado em condições.

O código é convertido diretamente para binário por assemblers (como NASM e GAS), sem camadas intermediárias de máquinas virtuais.

## 2. Registradores de CPU e Arquitetura x86-64

Em processadores x86-64 modernos de 64 bits, destacam-se registradores de propósito geral e específico:

- **Registradores Gerais:** `RAX` (acumulador e retorno de função), `RBX` (base), `RCX` (contador de laço), `RDX` (dados e aritmética), `RDI` e `RSI` (índices de origem e destino).
- **Registradores Especiais:** `RSP` (Stack Pointer), `RBP` (Base Pointer de quadro), `RIP` (Instruction Pointer) e `RFLAGS` (sinalizadores de status como zero e carry).

## 3. CISC vs RISC: Diferenças entre x86-64 e ARM64

A arquitetura x86-64 segue a filosofia **CISC** (conjunto complexo de instruções), com comandos de tamanho variável que operam na memória. O padrão ARM64 (Apple Silicon e dispositivos móveis) adota **RISC** (conjunto reduzido de instruções) com tamanho fixo de 32 bits e arquitetura Load-Store, proporcionando alta eficiência energética.

## 4. Chamadas de Sistema (Syscalls) e Exemplo Linux x86-64

```
section .text
global _start

_start:
    ; 1. Escrever na saída padrão (sys_write = syscall 1)
    mov rax, 1          ; número syscall: 1 (sys_write)
    mov rdi, 1          ; descritor: 1 (stdout)
    mov rsi, msg        ; endereço do buffer de texto
    mov rdx, 13         ; comprimento
    syscall             ; chamada ao kernel

    ; 2. Encerrar programa (sys_exit = syscall 60)
    mov rax, 60         ; número syscall: 60 (sys_exit)
    xor rdi, rdi        ; código de saída 0
    syscall

section .data
    msg db "Olá, mundo!", 10
```

## 5. .NET Assembly e WebAssembly (WASM)

- **.NET Assembly:** No ecossistema .NET, a compilação gera pacotes estruturados em bytecode CIL e metadados na forma de arquivos `.dll` ou `.exe`.
- **WebAssembly (WASM):** Formato binário compacto executado no navegador em ambiente isolado (sandbox) com velocidade próxima à nativa.

*A linguagem Assembly é como montar as engrenagens e molas de um relógio de pulso mecânico com uma pinça sob um microscópio: entrega máxima precisão, mas exige controle minucioso de cada detalhe.*

## Perguntas frequentes

**O que significa Assembly e para que serve?**

É a linguagem simbólica de menor nível, mapeando comandos um para um com as instruções do processador, vital para drivers, kernels e cibersegurança.

**Qual a diferença entre um assembler e um compilador?**

Compiladores traduzem abstrações de alto nível em código executável, enquanto o assembler faz a tradução literal de mnemônicos para códigos de máquina binários.

**Onde o Assembly ainda é aplicado atualmente?**

Em rotinas de bootloaders, sistemas embarcados críticos, engenharia reversa de softwares maliciosos e motores gráficos de alta taxa de quadros.

## Termos relacionados

- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Compilation](https://trescout.com/pt/dictionary/compilation/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)
- [Emulator](https://trescout.com/pt/dictionary/emulator/)

## Ferramentas relacionadas

- [Apollo-11](https://trescout.com/pt/discover/apollo-11/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/assembly/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/assembly/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/assembly/
