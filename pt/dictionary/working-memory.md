# O que é Working Memory em IA?

> Inglês: Working Memory

Working memory (memória de trabalho) em inteligência artificial é a área temporária de informações mantida ativa dentro da janela de contexto do modelo durante o raciocínio e a execução de tarefas imediatas.

## Definição e etimologia
Ela atua como a bancada de trabalho do sistema: quando a tarefa termina ou a sessão é encerrada, os dados temporários são descartados. A janela de contexto é o recipiente físico, enquanto os tokens nela carregados formam o conteúdo ativo da memória operacional.

## Contexto cotidiano e uso prático
Papéis essenciais da memória de trabalho :

## Profundidade técnica e arquitetura
Controle do orçamento de contexto :

## Costuma ser confundido com
É comum confundir com memória de longo prazo. A de longo prazo é um banco vetorial persistente que sobrevive entre conversas; a memória de trabalho é a RAM temporária que se esvazia com o fim da execução.

## Perspectivas interdisciplinares
Comparações em outros campos :

## Perguntas frequentes
**O que acontece quando a memória de trabalho da IA enche?**
O sistema precisa compactar os diálogos passados ou descartar mensagens antigas para não truncar a resposta.

**Qual a diferença entre essa memória e o treinamento do modelo?**
O treinamento gera os pesos permanentes do cérebro da IA; a memória de trabalho é apenas o texto temporário da conversa atual.

**Aumentar indefinidamente a memória de trabalho tem custo?**
Sim, o processamento da atenção cresce de forma quadrática e o modelo pode ter dificuldade para achar fatos no meio do texto.

**Qual a função do KV Cache?**
Ele armazena os cálculos de atenção dos tokens já gerados, evitando que o modelo recalcule tudo a cada nova palavra emitida.


## Termos relacionados
- [Memory](/pt/dictionary/memory/)
- [Context Window](/pt/dictionary/context-window/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/working-memory/
