# O que é Amazon Web Services?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> Amazon Web Services

AWS (Amazon Web Services) é uma plataforma em nuvem onde você aluga serviços de TI como servidores, armazenamento e bancos de dados pela internet.

## Definição e origem da palavra

Em vez de construir seu próprio servidor físico, você aluga data centers da Amazon. Quando a necessidade aumenta, a capacidade aumenta, e quando o trabalho é concluído, ela diminui. Funciona com o modelo de pagamento que aumenta conforme você o utiliza. Quase todos os aplicativos modernos possuem esse tipo de infraestrutura em nuvem em segundo plano.

***Analogia:** É como comprar eletricidade da rede em vez de construir a sua própria central elétrica; Você só paga pelo que usa.*

## Como conhecer e usar no dia a dia?

**Site:** Servidores que crescem de acordo com o tráfego.
**Backup:** Um cofre de arquivos aparentemente interminável.
**Vídeo:** Conteúdo distribuído à medida que é assistido.
**Startup:** Não vá ao ar sem montar uma sala de servidores.

## Profundidade Técnica e Arquitetura

Serviços básicos:

**EC2:** Servidor virtual para alugar.
**P3:** Armazenamento de objetos, backup e cofre de arquivos estáticos.
**RDS:** Banco de dados relacional gerenciado.
**Lambada:** Função sem servidor que é executada quando ocorre um evento.

Conceitos:

**Região e zona de acesso:** Localização física de dados e redundância.
**Responsabilidade compartilhada:** A segurança da nuvem é responsabilidade da Amazon, a segurança dos dados nela contidos é sua.
**Nível gratuito:** Uso gratuito limitado para novas contas.

Para listar servidores em execução:

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

É recomendável definir um alarme orçamentário para evitar surpresas nas faturas, pois recursos abertos e esquecidos continuam sendo cobrados.

## Coisas frequentemente misturadas

Pensa-se que seja apenas um serviço de hospedagem de sites. Porém, é uma plataforma de infraestrutura completa que abrange banco de dados, inteligência artificial, rede e camadas de segurança com mais de 200 serviços.

## Use em diferentes disciplinas

**Rede elétrica:** Desconectar em vez de instalar um quadro elétrico.
**Armazém para alugar:** Alugando quantas prateleiras forem necessárias.
**Táxi:** Viajar sem possuir veículo.

## Perguntas Frequentes

**Por que devo usar AWS?**

Você tem acesso instantâneo à infraestrutura corporativa sem fazer nenhum investimento em hardware. Se o tráfego estiver flutuante, o escalonamento e os serviços prontos economizam tempo.

**Posso começar de graça?**

Sim. O plano gratuito, os termos de crédito e de prazo para novas contas podem mudar com o tempo; Antes de começar, você deve verificar os limites atuais na página do nível gratuito da AWS.

**Onde meus dados são mantidos?**

Ele é mantido na região que você escolher. Para regulamentações como KVKK, você deve selecionar a região e a criptografia de acordo com sua política.

**Como manter a conta sob controle?**

Com alertas de orçamento, limpeza de recursos não utilizados e dimensionamento correto. Rotular a disciplina é essencial em equipes pequenas.

## Termos relacionados

- [Cloud Computing](https://trescout.com/pt/dictionary/cloud-computing/)
- [IaaS](https://trescout.com/pt/dictionary/iaas/)
- [PaaS](https://trescout.com/pt/dictionary/paas/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/aws/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/aws/
