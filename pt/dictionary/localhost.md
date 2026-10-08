# O que é Localhost?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Localhost é o nome de rede especial que endereça o próprio computador. O equivalente a ele é o endereço 127.0.0.1.

## Definição e origem da palavra

"Local" significa local e "host" significa computador hospedeiro. O desenvolvedor não carrega o site imediatamente para a internet; primeiro, ele o testa neste endereço em seu próprio computador. O seu computador desempenha o papel de servidor por conta própria. Ninguém de fora pode ver, apenas você vê.

***Analogia:** É como ensaiar uma peça de teatro em uma sala vazia apenas com os atores antes de encná-la no palco; o público ainda não está lá.*

## Como conhecer e usar no dia a dia?

**Desenvolvimento web:** Endereço que abre no navegador após o npm run dev.
**Banco de dados:** Conexão com Postgres ou Redis instalada localmente.
**Teste de API:** Teste de endpoints que ainda não foram publicados.

## Profundidade Técnica e Arquitetura

O que você precisa saber:

**127.0.0.0/8:** Intervalo de loopback, geralmente 127.0.0.1 é utilizado.
**Porta:** O número da porta no mesmo computador. Se dois aplicativos ocuparem a mesma porta, haverá conflito.
**A diferença do 0.0.0.0:** O localhost está aberto apenas para você, enquanto o 0.0.0.0 escuta para todos na rede.

Exemplo de verificação de integridade:

```
curl http://localhost:3000/api/health
```

Se não houver resposta, o aplicativo não está rodando ou a porta está incorreta. O firewall geralmente permite o tráfego de localhost.

## Coisas frequentemente misturadas

Pensa-se que é um site da internet. No entanto, o localhost é exclusivo apenas para o seu computador, não exigindo nome de domínio nem publicação.

## Use em diferentes disciplinas

**Teatro:** Uma sala de ensaio sem público.
**Música:** Passagem de som antes da gravação.
**Culinária:** Degustação antes de servir.

## Perguntas Frequentes

**Por que usamos localhost?**

Para corrigir erros de forma segura em nosso próprio computador, sem expô-los à internet.

**O que é 127.0.0.1?**

É a representação numérica do nome localhost. Em cada computador, ele aponta para si mesmo.

**O que é uma porta e por que ela é necessária?**

É um número de porta que diferencia aplicativos no mesmo computador. Fica após os dois-pontos no endereço do navegador.

**É acessível externamente?**

Não. Para que outros vejam, são necessários publicação e um nome de domínio. Ferramentas de túnel são usadas para compartilhar conexões de teste.

## Termos relacionados

- [IDE](https://trescout.com/pt/dictionary/ide/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)

## Ferramentas relacionadas

- [Penpot](https://trescout.com/pt/discover/penpot/)
- [Project N.O.M.A.D](https://trescout.com/pt/discover/project-nomad/)
- [Freellmapi](https://trescout.com/pt/discover/freellmapi/)
- [Jenkins](https://trescout.com/pt/discover/jenkins/)
- [Omlx](https://trescout.com/pt/discover/omlx/)
- [OpenStock](https://trescout.com/pt/discover/openstock/)
- [Personal_AI_Infrastructure](https://trescout.com/pt/discover/personal-ai-infrastructure/)
- [Portless](https://trescout.com/pt/discover/portless/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/localhost/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/localhost/
