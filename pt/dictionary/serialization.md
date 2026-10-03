# O que é Serialization?

A serialização é o processo de converter objetos, estruturas de dados e grafos de ponteiros alocados dinamicamente na memória de trabalho (RAM) de uma linguagem de programação em um fluxo de bytes (byte stream) linear e simples ou em um formato de texto que pode ser transmitido pela rede ou armazenado em disco.

## O que é Serialização e por que é obrigatória? Modelo de Memória
Nos sistemas operacionais modernos, cada processo é executado em seu próprio espaço de endereço virtual isolado. Um objeto em tempo de execução; Ele contém variáveis ​​locais na pilha, blocos de memória alocados dinamicamente no heap, ponteiros de função (vtable) e endereços de referência (0x7ffee4b2...).

## Formatos de Serialização: Baseado em Texto vs. Binário
Escolher o formato de serialização correto na arquitetura de software exige um equilíbrio entre legibilidade humana, custo de processamento (parsing) de CPU, largura de banda de rede e segurança de tipos.

## Arquitetura de Desserialização Zero-Copy
Em bibliotecas de serialização clássicas (analisadores JSON ou Protobuf padrão), o processo de desserialização é executado com as seguintes etapas:

## Dimensão de segurança: desserialização insegura (CWE-502)
Vulnerabilidades de segurança catastróficas surgem quando a serialização tenta serializar classes de objetos e comportamentos de tempo de execução, em vez de apenas mover dados puros. A desserialização insegura (serialização reversa insegura), que está na lista dos 10 principais do OWASP, permite que um invasor execute código arbitrário (execução remota de código - RCE) no sistema.

## Perguntas frequentes
**Qual é a principal diferença entre serialização e desserialização?**
Serialização é o processo de conversão de objetos ativos na memória em um fluxo de bytes/texto que pode ser armazenado ou transmitido. A desserialização é o processo de ler e analisar essa sequência de bytes e convertê-la em um objeto que funciona na memória do sistema de destino.

**Quando Protobuf ou FlatBuffers devem ser usados ​​em vez de JSON em projetos web?**
Para clientes da Web públicos e APIs públicas, o JSON é ideal devido à compatibilidade do navegador e à facilidade de depuração. No entanto, para microsserviços internos, back-ends de aplicativos móveis ou fluxos de dados em tempo real, Protobuf ou FlatBuffers devem ser preferidos para limitar a largura de banda da rede e reduzir o custo de decomposição da CPU.

**Como funciona o ataque de desserialização insegura e como evitá-lo?**
O invasor injeta funções maliciosas ou estruturas de classe nos dados serializados para serem executados durante a desserialização. Quando o servidor analisa esses dados, comandos do sistema podem ser acionados. Para evitar isso, os formatos que transportam lógica de classe devem ser abandonados e apenas os formatos de esquema que transportam dados puros (Protobuf, JSON Schema) devem ser usados.

**O que significa desserialização de cópia zero?**
É uma técnica de leitura de dados diretamente com deslocamentos de ponteiro na memória buffer, em vez de copiar o fluxo de bytes de entrada alocando novas áreas de memória. Ele alivia o processador e o coletor de lixo redefinindo a alocação de memória.

**O que é evolução do esquema? Como garantir compatibilidade com versões anteriores e futuras?**
Os modelos de dados mudam à medida que o software é atualizado. Sistemas como Protobuf e Avro fornecem IDs numéricos exclusivos aos campos, permitindo que clientes antigos ignorem novos campos (compatibilidade com versões anteriores) e novos clientes leiam dados antigos com valores padrão (compatibilidade com versões anteriores).


## Termos relacionados
- [API](/pt/dictionary/api/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)
- [Memory Management](/pt/dictionary/memory-management/)
- [Network Stack](/pt/dictionary/network-stack/)

## Ferramentas relacionadas
- [YAML Cpp](/pt/discover/yaml-cpp/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/serialization/
