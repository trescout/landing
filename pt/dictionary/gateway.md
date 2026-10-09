# O que é Gateway?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Gateway (em português, porta de entrada), é o ponto de conexão que gerencia o tráfego entre diferentes redes.

## Definição e origem da palavra

"Gate" significa portão e "way" significa caminho. É a ponte que permite que duas redes se comuniquem: o dispositivo que conecta a internet da sua casa ao mundo exterior é o exemplo típico. Ele analisa os dados recebidos e decide para qual rede devem ser enviados.

***Analogia:** É como a porta de fronteira de um país; Ele controla as chegadas e garante que elas sigam na direção certa.*

## Como conhecer e usar no dia a dia?

**Modem doméstico:** Conecta sua casa à rede do provedor.
**Gateway corporativo:** Ponto de controle do tráfego do escritório.
**Nuvem:** A porta de entrada para redes virtuais.

## Profundidade Técnica e Arquitetura

Funções do gateway:

**Tradução de endereços (NAT):** Converte endereços internos para um único endereço externo.
**Filtragem:** Mantém o tráfego indesejado fora da porta.
**Roteamento:** Entrega o pacote à rede correta.

A informação da rota padrão é a seguinte:

```
default via 192.168.1.1 dev eth0
```

Esta linha indica que destinos não reconhecidos serão enviados através do modem. Já o API gateway está em uma camada diferente: ele gerencia solicitações de serviço, não de rede.

## Coisas frequentemente misturadas

Pode ser confundido com o API Gateway. O API Gateway gerencia serviços de software, enquanto o gateway de rede opera no nível de rede. Um é a porta da aplicação, o outro é a porta de caminho.

## Use em diferentes disciplinas

**Porta de fronteira:** Inspeção e direcionamento dos visitantes.
**Porto:** Desembaraço aduaneiro de navios.
**Recepção:** Direcionamento do visitante para o andar correto.

## Perguntas Frequentes

**É possível acessar a internet sem um gateway?**

Não. A rede local não consegue se conectar ao mundo exterior, permanecendo isolada.

**Qual é a diferença para um API gateway?**

O gateway transporta pacotes, o API gateway gerencia solicitações. Um é a camada de rede, o outro é a camada de aplicação.

**Qual é usado em casa?**

O gateway dentro do seu modem é suficiente. Não são necessárias configurações adicionais, o endereço é distribuído automaticamente.

**Duas redes podem ser mantidas separadas?**

Sim. Com regras de firewall, a passagem é bloqueada e as redes operam isoladas.

## Termos relacionados

- [API Gateway](https://trescout.com/pt/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Proxy](https://trescout.com/pt/dictionary/proxy/)

## Ferramentas relacionadas

- [OmniRoute](https://trescout.com/pt/discover/omniroute/)
- [Litellm](https://trescout.com/pt/discover/litellm/)
- [Fanqiang](https://trescout.com/pt/discover/fanqiang/)
- [Gitdiagram](https://trescout.com/pt/discover/gitdiagram/)
- [OpenWA](https://trescout.com/pt/discover/openwa/)
- [Grok2api](https://trescout.com/pt/discover/grok2api/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/gateway/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/gateway/
