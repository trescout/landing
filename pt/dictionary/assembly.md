# Assembly: Definição, registradores e arquitetura de sistemas

Assembly refere-se a dois conceitos essenciais na ciência da computação: a linguagem simbólica de mais baixo nível para controle direto da CPU e os pacotes de implantação modulares (.NET assemblies).

## 1. Linguagem de Baixo Nível (Assembly Language)
Processadores entendem apenas códigos binários de máquina (opcodes). A linguagem assembly converte esses números em mnemônicos legíveis por humanos:

## 2. Registradores de CPU e Arquitetura x86-64
Em processadores x86-64 modernos de 64 bits, destacam-se registradores de propósito geral e específico:

## 3. CISC vs RISC: Diferenças entre x86-64 e ARM64
A arquitetura x86-64 segue a filosofia CISC (conjunto complexo de instruções), com comandos de tamanho variável que operam na memória. O padrão ARM64 (Apple Silicon e dispositivos móveis) adota RISC (conjunto reduzido de instruções) com tamanho fixo de 32 bits e arquitetura Load-Store, proporcionando alta eficiência energética.

## 4. Chamadas de Sistema (Syscalls) e Exemplo Linux x86-64

## 5. .NET Assembly e WebAssembly (WASM)

## Perguntas frequentes
**O que significa Assembly e para que serve?**
É a linguagem simbólica de menor nível, mapeando comandos um para um com as instruções do processador, vital para drivers, kernels e cibersegurança.

**Qual a diferença entre um assembler e um compilador?**
Compiladores traduzem abstrações de alto nível em código executável, enquanto o assembler faz a tradução literal de mnemônicos para códigos de máquina binários.

**Onde o Assembly ainda é aplicado atualmente?**
Em rotinas de bootloaders, sistemas embarcados críticos, engenharia reversa de softwares maliciosos e motores gráficos de alta taxa de quadros.


## Termos relacionados
- [Memory Management](/pt/dictionary/memory-management/)
- [Runtime](/pt/dictionary/runtime/)
- [Compilation](/pt/dictionary/compilation/)
- [Apple Silicon](/pt/dictionary/apple-silicon/)
- [Emulator](/pt/dictionary/emulator/)

## Ferramentas relacionadas
- [Apollo-11](/pt/discover/apollo-11/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/assembly/
