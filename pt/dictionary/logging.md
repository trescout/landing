# O que é Logging?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Logging (em português, registro de eventos) é a gravação cronológica dos eventos de um programa.

## Definição e origem da palavra

Log significa registro ou histórico. Quando um programa apresenta um erro silenciosamente, é possível ler no registro o que ele estava fazendo até aquele momento. É como a caixa-preta de um avião: o primeiro lugar a ser verificado após um acidente.

***Analogia:** É como a caixa-preta que registra os dados de voo da aeronave; as ações do programa são registradas no log.*

## Como conhecer e usar no dia a dia?

**Apresentador:** Depuração.
**Produto:** Monitoramento de uso.
**Segurança:** Registro de eventos.

## Profundidade Técnica e Arquitetura

Níveis:

**DEBUG:** Detalhe do desenvolvedor.
**INFO:** Fluxo normal.
**AVISO:** Situação suspeita.
**ERRO:** Tarefa falha.

Regras:

**Registro estruturado:** Formato JSON, pesquisabilidade.
**Proibição de PII:** Senhas e identidades não entram no registro.
**Rotação:** O arquivo é arquivado quando cresce.

Exemplo:

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Ödeme alındı: sipariş=%s", siparis_id)
```

Muitos registros deixam o sistema lento, poucos registros deixam você cego. Em produção usa-se INFO, em caso de problemas ativa-se DEBUG.

## Coisas frequentemente misturadas

Acha-se que é observabilidade. No entanto, o registro (logging) é o seu bloco de construção: o log é a matéria-prima, a capacidade de observação é o produto.

## Use em diferentes disciplinas

**Caixa-preta:** Registro de dados de voo.
**Diário:** Notas em ordem cronológica.
**Gravação da câmera:** Arquivo de eventos.

## Perguntas Frequentes

**É bom guardar tudo?**

Não. O excesso torna o sistema lento e oculta o que é importante; o registro é mantido de forma equilibrada.

**O que é o nível?**

É a etiqueta de urgência do registro. Serve como filtro na busca.

**Onde os registros são gravados?**

Em um arquivo, sistema central ou serviço de nuvem. Em produção, recomenda-se a coleta centralizada.

**Por quanto tempo é armazenado?**

Depende da política. A depuração requer semanas, a auditoria requer anos.

## Termos relacionados

- [Observability](https://trescout.com/pt/dictionary/observability/)
- [Traces](https://trescout.com/pt/dictionary/traces/)
- [Logs](https://trescout.com/pt/dictionary/logs/)

## Ferramentas relacionadas

- [OmniRoute](https://trescout.com/pt/discover/omniroute/)
- [Spdlog](https://trescout.com/pt/discover/spdlog/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/logging/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/logging/
