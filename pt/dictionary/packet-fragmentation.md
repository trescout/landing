# O que é Packet Fragmentation?

É o processo de divisão dos dados enviados pela Internet em pedaços menores de acordo com a capacidade de carga da rede.

## Definição
Ao enviar dados pela Internet, cada rede tem um tamanho máximo que pode transportar. Se os dados que você envia forem maiores que esse tamanho, o sistema os divide em pequenos pedaços, os entrega ao destino e os remonta lá.

## Como funciona
À medida que os dados são enviados, os dispositivos de rede verificam o tamanho do pacote. Se o limite for excedido, o pacote é fragmentado e cada fragmento recebe um 'número de sequência'. O dispositivo receptor analisa esses números e monta as peças na ordem correta.

## Onde é usado
Isso acontece constantemente em segundo plano durante protocolos de Internet e processos de rede.

## Costuma ser confundido com
Pode ser confundido com perda de dados, mas este é um processo de particionamento controlado.

## Perguntas frequentes
**O que acontece se peças forem perdidas?**
O dispositivo receptor percebe que faltam peças e pede ao remetente para reenviar essa peça.


## Termos relacionados
- [Networking Stack](/pt/dictionary/networking-stack/)
- [DNS Tunneling](/pt/dictionary/dns-tunneling/)

## Ferramentas relacionadas
- [Zapret Discord Youtube](/pt/discover/zapret-discord-youtube/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/packet-fragmentation/
