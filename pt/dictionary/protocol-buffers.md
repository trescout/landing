# O que é Protocol Buffers?

> Protobuf

É um método que permite que diferentes softwares empacotem e transportem dados muito rapidamente e em tamanhos pequenos enquanto se comunicam entre si.

## Definição
O software geralmente usa arquivos de texto ao enviar dados entre si, mas às vezes esses arquivos podem ser muito grandes. Os buffers de protocolo convertem dados em formato binário, permitindo que ocupem muito menos espaço e sejam transmitidos com muito mais rapidez. Foi desenvolvido pelo Google e hoje é considerado o padrão em comunicação entre sistemas.

## Como funciona
Primeiro você define a estrutura dos dados em um arquivo de modelo. Em seguida, seu software empacota os dados usando esse modelo e os envia para a outra parte. O lado receptor restaura os dados usando o mesmo modelo.

## Onde é usado
É utilizado em arquiteturas de microsserviços, comunicação de aplicações móveis com servidores e sistemas que requerem alto desempenho.

## Costuma ser confundido com
Pode ser confundido com formatos de dados baseados em texto, como JSON ou XML, mas é muito mais rápido e menor.

## Perguntas frequentes
**As pessoas sabem ler?**
Não, os dados não podem ser lidos diretamente por humanos, pois estão em formato binário; eles são projetados para que apenas os computadores possam entendê-los.


## Termos relacionados
- [API](/pt/dictionary/api/)
- [Networking Stack](/pt/dictionary/networking-stack/)
- [Serialization](/pt/dictionary/serialization/)

## Ferramentas relacionadas
- [Protobuf](/pt/discover/protobuf/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/protocol-buffers/
