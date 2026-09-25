# O que é Working Memory em IA?

> Inglês: Working Memory · Etimologia: inglês arcaico weorc (trabalho) + latim memoria (lembrança)

**Categoria:** AI  
**Última atualização:** 2026-09-22

Working memory (memória de trabalho) em inteligência artificial é a área temporária de informações mantida ativa dentro da janela de contexto do modelo durante o raciocínio e a execução de tarefas imediatas.

## Definição e etimologia
Ela atua como a bancada de trabalho do sistema: quando a tarefa termina ou a sessão é encerrada, os dados temporários são descartados. A janela de contexto é o recipiente físico, enquanto os tokens nela carregados formam o conteúdo ativo da memória operacional.

## Contexto cotidiano e uso prático
Papéis essenciais da memória de trabalho :
- **Retenção no Diálogo:** Lembrar do que o usuário disse nas mensagens anteriores durante a conversa.- **Raciocínio Passo a Passo:** Guardar deduções lógicas intermediárias em prompts de Chain-of-Thought.- **Uso de Ferramentas:** Processar resultados brutos retornados por APIs antes de redigir a resposta final.

## Profundidade técnica e arquitetura
Controle do orçamento de contexto :
- **Limites de Tokens:** Em uma janela de 128 mil tokens, se o histórico consome 100 mil, restam apenas 28 mil para o raciocínio e saída.- **KV Cache:** Mecanismo que guarda as matrizes de atenção das palavras anteriores na GPU para acelerar a geração.- **Descarte e Sumarização:** Quando o espaço se esgota, o sistema resume mensagens antigas para abrir espaço.

## Costuma ser confundido com
É comum confundir com memória de longo prazo. A de longo prazo é um banco vetorial persistente que sobrevive entre conversas; a memória de trabalho é a RAM temporária que se esvazia com o fim da execução.

## Perspectivas interdisciplinares
Comparações em outros campos :
- **Matemática:** O papel de rascunho usado para fazer contas durante uma prova e jogado fora depois.- **Marcenaria:** A bancada onde ficam as ferramentas durante a montagem de um móvel.- **Computação:** A memória cache do processador frente ao disco rígido secundário.

## Por analogia
É como um pedaço de rascunho que usamos para fazer contas rápidas enquanto resolvemos um problema complexo; encontrada a resposta final, o rascunho perde a utilidade.

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
- [Attention Mechanism](/pt/dictionary/attention-mechanism/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/working-memory/
