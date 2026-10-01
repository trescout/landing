# O que é I/O?

> Input/Output

I/O (Input/Output, entrada/saída) é a troca de dados do sistema com o mundo exterior.

## Definição e origem da palavra
Digitação no teclado, arquivo baixado, resultado exibido na tela: Tudo isso é operação de E/S. O sistema conversa com o mundo exterior através deste canal. É como os sentidos e as mãos do computador.

## Como conhecer e usar no dia a dia?
Teclado: Entrada de texto.Rede: Download de arquivo.Tela: Exibição de resultado.

## Profundidade Técnica e Arquitetura
Conceitos:

## Use em diferentes disciplinas
Humano: Entrada por olhos e ouvidos, saída por fala.Restaurante: Entrada de pedido, saída de atendimento.Fábrica: Entrada de matéria-prima, saída de produto.

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
- [API](/pt/dictionary/api/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)
- [Streaming Applications](/pt/dictionary/streaming-applications/)

## Ferramentas relacionadas
- [Asio](/pt/discover/asio/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/io/
