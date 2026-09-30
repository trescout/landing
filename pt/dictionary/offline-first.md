# O que é Offline-first?

É uma abordagem de design de software que continua a executar todas as funções básicas do aplicativo sem interrupção, mesmo se a conexão com a Internet for perdida.

## Definição
Nesta abordagem, o aplicativo primeiro armazena dados no próprio dispositivo do usuário e executa operações localmente. Assim que uma conexão com a Internet é estabelecida, os dados no dispositivo são sincronizados silenciosamente com o servidor em nuvem em segundo plano. Como TreScout, recomendamos esta arquitetura para manter a experiência do usuário no mais alto nível e não ser afetado por interrupções de conexão.

## Como funciona
Quando o aplicativo é aberto, ele lê os dados do banco de dados local no dispositivo, em vez de extraí-los de um servidor remoto. Todos os novos registros e alterações feitas pelo usuário são primeiro gravados neste banco de dados local. Um mecanismo especial de sincronização executado em segundo plano verifica constantemente a conexão à Internet e sincroniza os dados bilateralmente com o servidor.

## Onde é usado
É frequentemente usado em aplicativos de anotações usados ​​durante viagens de metrô, em sistemas de rastreamento de trabalho onde os trabalhadores de campo inserem dados em locais sem conexão com a Internet e em aplicativos de mapas.

## Costuma ser confundido com
É confundido com o modo de operação offline: enquanto o modo offline visa apenas evitar erros quando não há internet, a abordagem offline primeiro baseia o principal princípio de funcionamento do aplicativo inteiramente em dados locais.

## Perguntas frequentes
**O que acontece se as alterações feitas off-line entrarem em conflito com os dados de outros usuários quando estiverem on-line?**
Algoritmos de resolução de conflitos no software entram em ação e mesclam os dados com segurança, preservando ou avisando ao usuário a última alteração feita.

**Os aplicativos offline ocupam muito espaço no dispositivo?**
Não, uma vez que apenas dados baseados em texto e pequenos arquivos que o usuário usa ativamente são armazenados no dispositivo, ele não ocupa espaço de armazenamento desnecessariamente.


## Termos relacionados
- [Local-first](/pt/dictionary/local-first/)
- [Offline](/pt/dictionary/offline/)
- [Database](/pt/dictionary/database/)
- [State Management](/pt/dictionary/state-management/)

## Ferramentas relacionadas
- [LAP](/pt/discover/lap/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/offline-first/
