# O que é Assembly?

Assembly refere-se a dois conceitos básicos em ciência da computação: primeiro, a linguagem de programação simbólica de nível mais baixo (linguagem Assembly) que governa diretamente o processador de hardware (CPU); A segunda é transformar módulos de software compilados (montagem .NET) em um único pacote distribuível.

## 1. Linguagem de programação de baixo nível (linguagem Assembly)
O processador do computador entende apenas os sinais binários 0 e 1 (código de máquina/opcodes). A linguagem assembly consiste em abreviações simbólicas legíveis por humanos (mnemônicos) correspondentes a estes códigos de máquina brutos:

## 2. Registros do processador e arquitetura x86-64
Os registros mais críticos em um processador x86-64 moderno de 64 bits são:

## 3. CISC vs RISC: diferença entre x86-64 e ARM64
A arquitetura x86-64 trabalha com a filosofia CISC (Complex Instruction Set); Possui tamanhos de instruções variáveis ​​e instruções ricas que podem operar diretamente na memória. ARM64 (Apple Silicon, Mobile) é baseado em RISC (Conjunto de Instruções Reduzido); Ele oferece grande superioridade em eficiência energética com seu comprimento de comando fixo de 32 bits e arquitetura Load-Store.

## 4. Exemplo de chamadas de sistema (Syscall) e Linux x86-64

## 5. Montagem .NET e WebAssembly (WASM)

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
- [Memory Management](/pt/dictionary/memory-management/)
- [Runtime](/pt/dictionary/runtime/)
- [Compilation](/pt/dictionary/compilation/)
- [Apple Silicon](/pt/dictionary/apple-silicon/)
- [Emulator](/pt/dictionary/emulator/)

## Ferramentas relacionadas
- [Ghidra](/pt/discover/ghidra/)
- [Apollo-11](/pt/discover/apollo-11/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/assembly/
