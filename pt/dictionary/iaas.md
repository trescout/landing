# O que é IaaS?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> Infrastructure as a Service

IaaS (Infrastructure as a Service, infraestrutura como serviço) é o aluguel de hardware.

## Definição e origem da palavra

Quando o poder não é suficiente, partes são alugadas de um grande centro de dados. O sistema operacional e o software são seus, a responsabilidade pelo hardware é do provedor. A analogia de um terreno vazio é apropriada: a infraestrutura está pronta, o edifício é seu.

***Analogia:** Semelhante a alugar um terreno vazio; a infraestrutura está pronta, o edifício é seu.*

## Como conhecer e usar no dia a dia?

**Site:** Máquina de acordo com o tráfego.
**Backup:** Disco remoto.
**Teste:** Ambiente temporário.

## Profundidade Técnica e Arquitetura

Camadas:

**Máquina virtual:** Fatia de processador e memória.
**Armazenamento:** Espaço de bloco e objeto.
**Rede:** Rede virtual e endereço.

Máquina como código:

```
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}
```

Regra de custo: Máquina esquecida ligada gera cobrança. Disciplina de etiquetas e alarmes é essencial.

## Coisas frequentemente misturadas

Confunde-se com PaaS. IaaS fornece hardware, PaaS oferece ambiente pronto. Um é o terreno, o outro é o apartamento mobiliado.

## Use em diferentes disciplinas

**Terreno:** Terreno vazio com infraestrutura.
**Armazém:** Armazém com prateleiras prontas.
**Campo:** Aluguel de terra arada.

## Perguntas Frequentes

**O IaaS é seguro?**

A infraestrutura é segura, a segurança interna é sua responsabilidade. Disciplina de patches e acesso é essencial.

**Qual é a diferença do PaaS?**

IaaS fornece hardware, PaaS oferece um ambiente. Se você precisa de controle, escolha o primeiro; se deseja velocidade, escolha o segundo.

**Como manter os custos sob controle?**

Desligue o que não está em uso, escolha o tamanho correto e configure alertas.

**Quando escolher?**

Quando for necessário controle total e instalação personalizada. Para tarefas padrão, o PaaS é suficiente.

## Termos relacionados

- [SaaS](https://trescout.com/pt/dictionary/saas/)
- [PaaS](https://trescout.com/pt/dictionary/paas/)
- [Virtual Machines](https://trescout.com/pt/dictionary/virtual-machines/)

## Ferramentas relacionadas

- [Free for Dev](https://trescout.com/pt/discover/free-for-dev/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/iaas/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/iaas/
