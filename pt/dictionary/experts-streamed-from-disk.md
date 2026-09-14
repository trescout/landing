# O que é Experts Streamed from Disk?

É um método em que partes de modelos gigantes de inteligência artificial são carregadas instantaneamente do disco quando não cabem na memória.

## Definição
Os modelos de inteligência artificial são, por vezes, tão grandes que não cabem na capacidade de RAM do computador. Nesta técnica, apenas as partes do modelo (especialistas) necessárias naquele momento são lidas rapidamente do disco e trazidas para a memória. Assim, modelos muito grandes tornam-se capazes de funcionar mesmo em hardware limitado.

## Como funciona
O sistema divide os pesos do modelo em pequenas partes e armazena-as no disco. Quando um utilizador faz uma pergunta, as partes relevantes do modelo são transferidas muito rapidamente do disco para a memória, o processamento é realizado e, em seguida, a memória é libertada.

## Onde é usado
É utilizado especialmente por programadores que desejam executar modelos de linguagem muito grandes em computadores domésticos e em servidores com restrições de hardware.

## Costuma ser confundido com
Pode ser confundido com o carregamento de todo o modelo na memória; aqui, o carregamento ocorre apenas no momento da necessidade.

## Perguntas frequentes
**Este método reduz a velocidade?**
Sim, como a operação de leitura do disco é mais lenta do que a da RAM, pode haver um certo atraso no tempo de resposta do modelo.

**Qualquer modelo pode funcionar desta forma?**
O modelo precisa de ter sido concebido com esta arquitetura; ou seja, é obrigatório que tenha uma estrutura fragmentada (Mixture of Experts).


## Termos relacionados
- [Mixture of Experts](/pt/dictionary/mixture-of-experts/)
- [RAM](/pt/dictionary/ram/)
- [Inference Engine](/pt/dictionary/inference-engine/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/experts-streamed-from-disk/
