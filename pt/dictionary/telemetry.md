# O que é Telemetry?

*Desenvolvimento · Última atualização: 22 de setembro de 2026*

Telemetria (medição remota em turco) é a coleta automática de informações de status de software e dispositivos e transmissão para o centro.

## Definição e origem da palavra

A palavra vem das raízes gregas tele (distante) e metron (medida). Os aplicativos enviam relatórios ao desenvolvedor sobre como o software está funcionando: qual recurso está sendo muito usado, onde o aplicativo está travando. É um fluxo de dados que flui silenciosamente em segundo plano para o usuário.

***Analogia:** É como os sensores dentro de um carro relatando constantemente a temperatura do motor e o nível de combustível ao painel do motorista.*

## Como conhecer e usar no dia a dia?

**Depuração:** Coleta automática de relatórios de falhas.
**Veredicto do produto:** Simplificação do botão menos utilizado.
**Desempenho:** Monitorando o tempo de inicialização de versão para versão.

## Profundidade Técnica e Arquitetura

Os três pilares da observabilidade:

**Registro:** Linhas de eventos ("pagamento iniciado", "pagamento finalizado").
**Métrica:** Métricas numéricas (número de solicitações, latência média).
**Rastreamento:** Um registro da jornada da solicitação entre os serviços.

Padrões abertos como OpenTelemetry são usados ​​para coleta. Duas regras são observadas: Em alto tráfego, enviar amostras (amostragem) ao invés de todas as solicitações e não registrar dados pessoais (e-mail, localização). Você pode ver quais dados estão sendo enviados e desligá-los na seção de configurações do aplicativo.

## Coisas frequentemente misturadas

Pode ser confundido com registro. Log é a única linha de evento. Uma métrica é um resumo numérico. Trace é a jornada do desejo. Telemetria é o nome da coleta e transmissão desses três.

## Use em diferentes disciplinas

**Hospital:** O monitor do paciente transmite o pulso para a tela da enfermeira.
**Aviação:** Armazenando dados de voo em uma caixa preta.
**Energia:** Os medidores informam o consumo ao centro.

## Perguntas Frequentes

**Afeta a minha privacidade?**

Geralmente são coletados dados anônimos e agregados. Você pode ver quais dados são enviados e desligá-los na seção de configurações do aplicativo.

**Qual é a diferença com Observabilidade?**

A telemetria coleta e transmite dados. Observabilidade é a capacidade de compreender o interior do sistema com os dados coletados. Um é o meio, o outro é o objetivo.

**Pode ser fechado?**

Na maioria dos aplicativos, sim, ele está desativado nas configurações. Os dispositivos corporativos podem permanecer abertos de acordo com a política.

**Isso tem um custo?**

Sim. Há uma taxa de transporte e armazenamento de dados. É por isso que a amostragem é feita em alto tráfego, alguns deles são enviados, não todos os eventos.

## Termos relacionados

- [Logs](https://trescout.com/pt/dictionary/logs/)
- [Observability](https://trescout.com/pt/dictionary/observability/)
- [Traces](https://trescout.com/pt/dictionary/traces/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/telemetry/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/telemetry/
