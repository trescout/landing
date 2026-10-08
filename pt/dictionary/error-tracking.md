# O que é Error Tracking?

*Glossário · Dev · Última atualização: 3 de outubro de 2026*

O processo de monitoramento que captura, agrupa e notifica os desenvolvedores em tempo real sobre erros de tempo de execução que ocorrem em aplicativos.

## Definição

O rastreamento de erros é uma abordagem de monitoramento que registra automaticamente falhas e situações inesperadas encontradas pelos usuários em softwares em ambiente de produção. O sistema documenta passo a passo a origem do erro, os detalhes do sistema operacional e as ações do usuário que acionaram o erro. Dessa forma, as equipes de software têm a chance de intervir nos problemas antes que eles sejam relatados pelos usuários.

***Analogia:** É semelhante a um alarme de incêndio em um edifício que não apenas detecta fumaça, mas também informa ao corpo de bombeiros o número exato do quarto do incêndio e a causa da origem.*

## Como funciona

Uma pequena biblioteca de monitoramento incorporada ao aplicativo escuta todas as exceções de software não capturadas. Quando ocorre uma falha, o rastreamento de pilha (stack trace) e os dados ambientais são empacotados e enviados para o servidor de análise. O servidor reúne erros semelhantes sob o mesmo teto e envia notificações aos desenvolvedores por e-mail ou mensagem instantânea.

## Onde é usado

É ativamente preferido em aplicativos móveis onde a experiência do usuário é crítica, em projetos web de página única (SPA) e em arquiteturas de microsserviços executadas no back-end.

## Costuma ser confundido com

É diferente do conceito de registro (logging), que armazena todos os eventos do sistema cronologicamente: o rastreamento de erros concentra-se diretamente nas exceções e analisa e agrupa esses problemas automaticamente.

## Perguntas frequentes

**As ferramentas de rastreamento de erros registram os dados confidenciais dos usuários?**

Sistemas configurados corretamente filtram e ocultam automaticamente dados pessoais, como senhas ou cartões de crédito, antes de enviá-los ao servidor.

**O relatório de erros desaparece quando o aplicativo fecha repentinamente?**

Não, as informações coletadas no momento da falha são gravadas na memória local do dispositivo e transmitidas ao centro quando o aplicativo é reaberto.

## Termos relacionados

- [Logging](https://trescout.com/pt/dictionary/logging/)
- [Observability](https://trescout.com/pt/dictionary/observability/)
- [Traces](https://trescout.com/pt/dictionary/traces/)
- [QA](https://trescout.com/pt/dictionary/qa/)
- [Session Replay](https://trescout.com/pt/dictionary/session-replay/)

## Ferramentas relacionadas

- [Sentry](https://trescout.com/pt/discover/sentry/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/error-tracking/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/error-tracking/
