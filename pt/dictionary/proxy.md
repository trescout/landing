# O que é Proxy?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Proxy (em turco, servidor proxy) é o intermediário que transmite suas solicitações ao destino em seu nome.

## Definição e origem da palavra

"Proxy" significa proxy. Ele atua como uma proteção entre o seu computador e a Internet: você se conecta ao site por meio de um proxy, não diretamente. É usado para ocultação de identidade e gerenciamento de tráfego.

***Analogia:** É como se você transmitisse a mensagem por meio de seu amigo, e não diretamente; O comprador vê o intermediário, não você.*

## Como conhecer e usar no dia a dia?

**Empresa:** Controle do tráfego de saída.
**Segurança:** Ocultação de endereço.
**Acesso:** Excedência de restrições regionais.

## Profundidade Técnica e Arquitetura

Existem duas direções:

**avançar:** Esconda o cliente, saia.
**Reverter:** Ele protege o servidor e permite sua entrada. O Nginx faz esse trabalho.

Tipos: HTTP, HTTPS e SOCKS. Exemplo de variável de ambiente:

```
export https_proxy="http://vekil:8080"
```

Ele também mantém o cache: o conteúdo solicitado com frequência é entregue pelo proxy, a linha é relaxada.

## Coisas frequentemente misturadas

É considerada uma VPN. A VPN encapsula todo o dispositivo, enquanto o proxy geralmente opera no nível do aplicativo ou do navegador. A profundidade da privacidade varia.

## Use em diferentes disciplinas

**Amigo:** A pessoa que encaminha a mensagem em seu nome.
**Recepção:** O oficial que cumprimenta o visitante.
**Intérprete:** O meio que transmite a palavra.

## Perguntas Frequentes

**É seguro?**

Depende do proxy. Servidor não confiável pode monitorar o tráfego, então um provedor conhecido é escolhido.

**Por que é usado?**

Para controle, privacidade e acesso. Todos os três são necessidades separadas.

**O que é reverso?**

É a direção que distribui o que vem de fora para o servidor. Fornece balanceamento de carga e proteção.

**Isso acelera?**

No conteúdo em cache, sim, no tráfego criptografado e remoto geralmente fica lento.

## Termos relacionados

- [Self-Hosting](https://trescout.com/pt/dictionary/self-hosting/)
- [Offline](https://trescout.com/pt/dictionary/offline/)
- [VPN](https://trescout.com/pt/dictionary/vpn/)

## Ferramentas relacionadas

- [OmniRoute](https://trescout.com/pt/discover/omniroute/)
- [Litellm](https://trescout.com/pt/discover/litellm/)
- [FlClash](https://trescout.com/pt/discover/flclash/)
- [Nginx](https://trescout.com/pt/discover/nginx/)
- [Freellmapi](https://trescout.com/pt/discover/freellmapi/)
- [Headroom](https://trescout.com/pt/discover/headroom/)
- [User Scanner](https://trescout.com/pt/discover/user-scanner/)
- [OpenFlux](https://trescout.com/pt/discover/openflux/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/proxy/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/proxy/
