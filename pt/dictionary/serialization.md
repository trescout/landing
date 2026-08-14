# O que é Serialization?

É o processo de conversão de estruturas de dados complexas em um texto simples ou matriz de bytes que pode ser armazenado ou transmitido.

## Definição
Você precisa traduzir objetos armazenados de forma complexa na memória do computador (por exemplo, um perfil de usuário) em uma linha reta para enviá-los pela Internet ou salvá-los em um arquivo. Este processo é chamado de serialização. Quando a outra parte recebe esses dados, ela realiza a 'desserialização' e os restaura à sua antiga estrutura complexa.

## Como funciona
Os dados geralmente são convertidos para JSON, XML ou formatos binários mais rápidos. Desta forma, a estrutura original dos dados é preservada e torna-se portável entre diferentes sistemas.

## Onde é usado
Ele é usado em comunicações de API, registros de banco de dados e criação de arquivos salvos em jogos.

## Perguntas frequentes
**Por que precisamos de serialização?**
Os dados na memória do computador são significativos apenas para o programa atual. Para enviar dados para outro computador ou disco, precisamos convertê-los para um formato universal.


## Termos relacionados
- [API](/pt/dictionary/api/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)

## Ferramentas relacionadas
- [YAML Cpp](/pt/discover/yaml-cpp/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/serialization/
