# O que é Virtual Machines?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Uma máquina virtual é um computador independente que partilha o hardware.

## Definição e origem da palavra

"Virtual" significa virtual. Executa vários sistemas operacionais em uma única máquina. Cada um opera isoladamente com seus próprios recursos e não causa danos ao sistema principal.

***Analogia:** É semelhante a alugar quartos com portas separadas na mesma casa.*

## Como conhecer e usar no dia a dia?

**Apresentador:** Hospedagem multilocatário.
**Teste:** Experimentação de sistemas diferentes.
**Desenvolvimento:** Ambiente de teste limpo.

## Profundidade Técnica e Arquitetura

Camadas:

**Hipervisor:** O software que divide o hardware.
**Convidado:** O sistema que roda em cima.
**Snapshot:** Instantâneo, bilhete de regresso.

Máquina rápida:

```
multipass launch --name test --cpus 2 --memory 4G
```

A diferença do contentor: A máquina transporta o sistema, o contentor transporta a aplicação. O isolamento é forte na máquina.

## Coisas frequentemente misturadas

Pensa-se que é um contentor. A máquina é um sistema completo, o contentor é um núcleo partilhado. Um é um apartamento, o outro é partilhar quarto.

## Use em diferentes disciplinas

**Quartos:** Divisões com portas independentes.
**Apartamento:** Edifício comum, espaço privado.
**Mala:** Transporte com compartimentos.

## Perguntas Frequentes

**Desacelera?**

Há uma taxa de partilha. Não é perceptível com o dimensionamento correto.

**O vírus passa?**

Geralmente não. O isolamento é forte, a pasta partilhada é monitorizada.

**Quanto recurso é fornecido?**

Determinado pelo trabalho. Ajustado gradualmente com monitorização.

**Qual é a diferença do contentor?**

A máquina transporta o sistema, o contentor a aplicação. O isolamento e a velocidade são trocados.

## Termos relacionados

- [Containers](https://trescout.com/pt/dictionary/containers/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Self-hosting](https://trescout.com/pt/dictionary/self-hosting/)

## Ferramentas relacionadas

- [Container](https://trescout.com/pt/discover/container/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/virtual-machines/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/virtual-machines/
