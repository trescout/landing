# O que é Local-first Memory?

> Arquitetura com Prioridade ao Armazenamento Local

Local-first memory (memória de prioridade local) é um modelo de arquitetura de software onde os dados e o estado principal residem diretamente no dispositivo do usuário, ficando a nuvem restrita a um papel secundário de replicação.

## Definição e etimologia
Ao contrário dos aplicativos web clássicos que travam quando a conexão cai, a arquitetura local-first assegura tempo de resposta instantâneo e total autonomia offline. A fonte de verdade é a base de dados residente no próprio aparelho.

## Contexto cotidiano e uso prático
Gestão de Conhecimento e Notas: Aplicativos como Obsidian e Logseq mantendo arquivos Markdown diretamente no disco rígido.Ferramentas de Desenho Colaborativo: Quadros interativos que operam sem internet e reconciliam edições automaticamente.Memória de Agentes de IA: Bancos vetoriais salvos localmente para garantir sigilo sobre dados de contexto pessoal.

## Profundidade técnica e arquitetura
Componentes Técnicos Principais :

## Costuma ser confundido com
Frequentemente confundida com simples cache offline. O cache é um paliativo temporário cujo dono é o servidor; na arquitetura local-first, o proprietário e mestre dos dados é o dispositivo do próprio usuário.

## Perspectivas interdisciplinares
Economia: Guardar notas em um cofre doméstico vs manter dinheiro exclusivamente em conta digital.Artes: Escrever em um diário encadernado vs redigir em um editor online na nuvem.Comércio: Manter mercadorias em estoque próprio vs depender exclusivamente de entrega sob demanda remota.

## Perguntas frequentes
**Qual o maior atrativo da arquitetura local-first?**
Velocidade imediata sem engasgos de rede, funcionamento 100% offline e privacidade rigorosa.

**Como múltiplos usuários trabalham juntos no mesmo arquivo?**
Através de CRDTs (Tipos de Dados Replicados sem Conflito), que unificam alterações com consistência matemática.

**Existe sincronização em nuvem nesse modelo?**
Sim, mas os servidores atuam meramente como correios encriptados que retransmitem atualizações entre dispositivos.

**Quais tecnologias viabilizam essa arquitetura?**
SQLite (WASM), RxDB, PGlite, ElectricSQL e bibliotecas de CRDT como Yjs e Automerge.


## Termos relacionados
- [Nuvem Pessoal](/pt/dictionary/personal-cloud/)
- [Runtime](/pt/dictionary/runtime/)
- [Privacidade Digital](/pt/dictionary/digital-privacy/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/local-first-memory/
