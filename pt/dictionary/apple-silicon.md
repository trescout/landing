# O que é Apple Silicon?

Apple Silicon é a família de processadores SoC (System on a Chip) de alto desempenho baseada em ARM, projetada internamente pela Apple para dispositivos Mac e iPad, que reúne CPU, GPU, Neural Engine e memória unificada (Unified Memory) em uma única placa de silício.

## Gênese conceitual, histórico e a grande migração de x86 para ARM
"Silicon" (silício) é o elemento químico fundamental utilizado na fabricação de microchips semicondutores. Já o Apple Silicon representa o design de microprocessadores proprietários da Apple, pondo fim à sua dependência de fabricantes de chips terceirizados (Intel, Motorola, IBM) e integrando verticalmente seu próprio hardware e software.

## Sistema em Chip (SoC) e Arquitetura de Memória Unificada (UMA)
Num computador desktop ou portátil tradicional, o hardware é fragmentado: existe um soquete de CPU separado na placa-mãe, uma enorme placa gráfica dedicada (GPU) inserida numa ranhura PCIe, módulos de RAM separados e pontes na placa-mãe. Para exibir no ecrã uma imagem processada pela CPU, os dados têm de ser copiados através do barramento da placa-mãe da RAM para a própria VRAM da GPU. Isto cria latência e um elevado consumo de energia.

## Anatomia do núcleo, aceleradores e Rosetta 2
O equilíbrio de desempenho puro e eficiência do Apple Silicon baseia-se em três componentes de engenharia fundamentais:

## Perguntas frequentes
**O que significa Apple Silicon e quais processadores ele engloba?**
É a família de processadores System on a Chip (SoC) baseada em ARM projetada pela própria Apple. Ela engloba os chips da série A em iPhones e iPads, bem como os processadores da série M (M1, M2, M3, M4 e suas variantes) que alimentam os computadores Mac.

**Por que a Arquitetura de Memória Unificada (UMA) é diferente da RAM e VRAM tradicionais?**
Nos sistemas tradicionais, a CPU tem sua própria RAM de sistema e a placa gráfica tem sua própria VRAM, e os dados são copiados entre as duas. Na UMA, a memória está diretamente no pacote do processador; a CPU, a GPU e o motor de inteligência artificial acessam o mesmo pool de memória sem atraso de cópia e a custo zero.

**Aplicativos antigos da Intel funcionam em um Mac com processador Apple Silicon?**
Sim, graças ao mecanismo de tradução Rosetta 2 integrado ao sistema operacional macOS, a grande maioria dos aplicativos escritos para Intel (x86_64) é executada em alta velocidade sem que o usuário perceba.

**Por que o Apple Silicon é tão popular no desenvolvimento de inteligência artificial local (LLM)?**
Porque, graças à Arquitetura de Memória Unificada, pools de memória gigantescos, como 64 GB, 96 GB ou 128 GB, podem ser usados diretamente pela GPU como VRAM. Isso permite que grandes modelos de linguagem com mais de 70 bilhões de parâmetros sejam executados localmente sem GPUs de servidor caras.


## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [Computer Science](/pt/dictionary/computer-science/)
- [Assembly](/pt/dictionary/assembly/)
- [Memory Management](/pt/dictionary/memory-management/)
- [Emulator](/pt/dictionary/emulator/)
- [Cloud Computing](/pt/dictionary/cloud-computing/)

## Ferramentas relacionadas
- [Minimind](/pt/discover/minimind/)
- [Container](/pt/discover/container/)
- [Airllm](/pt/discover/airllm/)
- [Omlx](/pt/discover/omlx/)
- [Palmier Pro](/pt/discover/palmier-pro/)
- [Openmed](/pt/discover/openmed/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/apple-silicon/
