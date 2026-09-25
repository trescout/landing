# O que é Serialização (Serialization)?

> Inglês: Serialization · Etimologia: latim series (série, ordem) + facere (fazer)

**Categoria:** Dev  
**Última atualização:** 2026-09-19

Serialização (serialization) é o processo de transformar estruturas de dados dinâmicas, grafos de ponteiros e objetos alocados na memória RAM em uma sequência linear de bytes ou texto simples, adequada para tráfego em rede ou armazenamento em disco.

## O que é Serialização e por que é necessária? Modelo de Memória
Em sistemas operacionais modernos, cada processo roda em um espaço de endereçamento virtual isolado. Objetos alocados na heap se comunicam por endereços de memória locais que perdem o significado fora daquele processo. A serialização resolve isso empacotando e desconstruindo essas referências em formatos universais e portáveis.

## Formatos de Serialização: Texto vs Protocolos Binários
A escolha do formato equilibra facilidade de leitura e custo de processamento:
- **Formatos baseados em texto (JSON, YAML, XML):** Fáceis de inspecionar por humanos e integrados a qualquer linguagem, mas demandam mais processamento de CPU e ocupam mais largura de banda.- **Formatos binários (Protocol Buffers, MessagePack, Avro):** Representação condensada com tipagem rigorosa e redução drástica de payload.- **Evolução de Esquema:** Ferramentas como Protobuf oferecem compatibilidade retroativa, permitindo que sistemas convivam com versões diferentes de contratos.

## Arquitetura Zero-Copy Deserialization
Na desserialização tradicional, novos objetos precisam ser instanciados na heap consumindo ciclos de CPU. Estruturas como FlatBuffers e Cap'n Proto usam **Zero-Copy**:
- **Alinhamento Direto:** Os dados são organizados com deslocamentos internos padronizados.- **Acesso sem Cópia:** O leitor acessa os atributos diretamente da memória mapeada ou do buffer de rede sem instanciar novas estruturas na heap.

## Dimensão de Segurança: Insecure Deserialization (CWE-502)
Quando o mecanismo de serialização serializa métodos executáveis ou classes arbitrárias (comum em Python pickle ou na serialização nativa do Java), abrem-se brechas graves:
- **Execução Remota de Código (RCE):** O invasor injeta cadeias de objetos (gadget chains) que executam comandos do sistema durante a recriação do fluxo.- **Defesas:** Utilizar formatos estritos de dados (JSON, Protobuf) e validar a integridade criptográfica da mensagem via HMAC ou TLS.

## Por analogia
É como desmontar um armário em peças planas e etiquetadas para caber em uma caixa de mudança e, no destino, remontá-lo seguindo as instruções.

## Perguntas frequentes

**Qual a diferença central entre serialização e desserialização?**  
A serialização converte o grafo de objetos em fluxo linear de bytes; a desserialização reconstrói a estrutura original a partir desses bytes.

**Por que nunca devemos desserializar dados pickle não confiáveis?**  
O pickle permite a invocação de rotinas arbitrárias do Python no momento da leitura, gerando risco imediato de execução de código malicioso.

**Como FlatBuffers alcança desempenho Zero-Copy?**  
Ao organizar os campos binários com offsets pré-alinhados, dispensando a alocação de objetos intermediários na memória.

**Quando JSON é mais vantajoso que Protobuf?**  
Quando legibilidade humana imediata e depuração rápida no navegador são mais prioritárias que economia extrema de banda.

## Termos relacionados
- [API](/pt/dictionary/api/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)
- [Buffer](/pt/dictionary/buffer/)

## Ferramentas relacionadas
- [YAML Cpp](/pt/discover/yaml-cpp/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/serialization/
