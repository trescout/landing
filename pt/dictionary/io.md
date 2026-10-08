# O que é I/O?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> Input/Output

I/O (Input/Output, entrada/saída) é a troca de dados do sistema com o mundo exterior.

## Definição e origem da palavra

Digitação no teclado, arquivo baixado, resultado exibido na tela: Tudo isso é operação de E/S. O sistema conversa com o mundo exterior através deste canal. É como os sentidos e as mãos do computador.

***Analogia:** É como um ser humano receber informações do mundo exterior e reagir a ele; os olhos são a entrada, a fala é a saída.*

## Como conhecer e usar no dia a dia?

**Teclado:** Entrada de texto.
**Rede:** Download de arquivo.
**Tela:** Exibição de resultado.

## Profundidade Técnica e Arquitetura

Conceitos:

**Blocking (Bloqueante):** Aguardar até que a operação seja concluída.
**Non-blocking (Não bloqueante):** Continuar sem esperar, avisar quando o resultado chegar.
**Buffer:** Armazém temporário que equilibra a diferença de velocidade.
**Gargalo:** O elo mais lento desacelera toda a linha, geralmente sendo o disco ou a rede.

Exemplo de leitura de arquivo:

```
const veri = await fs.readFile("not.txt", "utf8");
```

Esta linha não espera o arquivo chegar, as outras tarefas continuam. A execução prossegue assim que o resultado estiver pronto.

## Use em diferentes disciplinas

**Humano:** Entrada por olhos e ouvidos, saída por fala.
**Restaurante:** Entrada de pedido, saída de atendimento.
**Fábrica:** Entrada de matéria-prima, saída de produto.

## Perguntas Frequentes

**Por que a E/S é um gargalo?**

O processador é rápido, o disco e a rede são lentos. Quando os dados não chegam a tempo, o sistema espera e o gargalo surge aqui.

**O que é bloqueio (blocking)?**

É uma chamada que aguarda até que o resultado chegue. Ela trava a interface e desperdiça trabalho no servidor.

**Como acelerar?**

Com cache, leitura em lote e chamadas assíncronas. Primeiro mede-se, depois conserta-se o elo mais fraco.

**O que o Async tem a ver com isso?**

É um mecanismo para realizar outro trabalho durante a espera. Permite lidar com muitas tarefas usando uma única thread.

## Termos relacionados

- [API](https://trescout.com/pt/dictionary/api/)
- [Data Pipeline](https://trescout.com/pt/dictionary/data-pipeline/)
- [Streaming Applications](https://trescout.com/pt/dictionary/streaming-applications/)

## Ferramentas relacionadas

- [Asio](https://trescout.com/pt/discover/asio/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/io/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/io/
