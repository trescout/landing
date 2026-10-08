# O que é OpenStreetMap?

*Glossário · Data · Última atualização: 22 de setembro de 2026*

OpenStreetMap (ou simplesmente OSM) é um mapa do mundo livre e aberto, desenhado de forma colaborativa por voluntários.

## Definição e origem da palavra

O projeto foi iniciado em 2004. Ao contrário dos mapas comerciais, os dados não são produzidos por uma empresa, mas por uma comunidade de voluntários: qualquer pessoa pode adicionar novas estradas, edifícios ou pontos de interesse, e corrigir erros. Os dados estão disponíveis para todos sob a licença ODbL. Isso significa que você pode usar os dados gratuitamente, mas deve citar a fonte ao compartilhá-los.

***Analogia:** É como a Wikipédia dos mapas; Qualquer um pode adicionar algo, corrigir bugs e ficar constantemente atualizado graças à comunidade.*

## Como conhecer e usar no dia a dia?

**Aplicativos de navegação:** Aplicativos como OsmAnd e MAPS.ME obtêm seus mapas a partir de dados do OSM.
**Logística:** Planejamento de rotas para empresas de distribuição.
**Ajuda em desastres:** Mapeamento rápido de zonas de crise por voluntários (por exemplo, a comunidade HOT).
**Planejamento urbano:** Análises de ciclovias e áreas verdes.

## Profundidade Técnica e Arquitetura

Os dados do OSM consistem em três blocos de construção:

**Nó (Node):** Um único ponto (por exemplo, a localização de uma farmácia).
**Via (Way):** Uma combinação de nós (rua, perímetro de um edifício).
**Relação (Relation):** Um grupo lógico de partes (linha de ônibus).

Cada elemento recebe uma etiqueta: pares de chave e valor como highway=residential. Para a edição, utiliza-se o editor iD no navegador ou a aplicação avançada JOSM.

A API Overpass é consultada para extrair dados específicos. Por exemplo, uma pequena consulta que encontra farmácias nas proximidades:

```
[out:json];
node["amenity"="pharmacy"](around:1000,41.0,29.0);
out;
```

Os dados brutos podem ser baixados do arquivo Planet.osm. As imagens do mapa são obtidas em partes a partir de servidores de blocos (tiles).

## Use em diferentes disciplinas

**Enciclopédia:** O modelo da Wikipedia, onde todos escrevem e corrigem.
**Software de código aberto:** O kernel Linux, que cresce com contribuições voluntárias.
**Ciência cidadã:** A coleta de registros de observação de aves em um banco de dados comum.

## Perguntas Frequentes

**É realmente gratuito?**

Os dados são gratuitos sob a licença ODbL. Se você os hospedar em seu próprio servidor, não pagará taxas adicionais. Empresas que oferecem serviços de blocos (tiles) prontos podem cobrar taxas separadamente.

**Qual é a diferença em relação ao Google Maps?**

No Google Maps, a empresa produz os dados e os vincula a cotas de API. No OSM, a comunidade produz os dados, e você pode baixar os dados brutos e processá-los sem limites.

**Como posso contribuir para o mapa?**

Você pode criar uma conta e começar com o editor iD no navegador. Adicionar uma loja que falta na sua rua é um bom primeiro passo.

**Posso usar no meu produto comercial?**

Sim, mas devido à ODbL, você deve fornecer a atribuição do OpenStreetMap de forma visível e compartilhar os dados derivados sob a mesma licença.

## Termos relacionados

- [Data Pipeline](https://trescout.com/pt/dictionary/data-pipeline/)
- [OSINT](https://trescout.com/pt/dictionary/osint/)
- [Graph-based Investigation](https://trescout.com/pt/dictionary/graph-based-investigation/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/openstreetmap/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/openstreetmap/
