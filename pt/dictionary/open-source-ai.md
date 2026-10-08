# O que é Open Source AI?

*Glossário · AI · Última atualização: 22 de setembro de 2026*

IA de código aberto (inteligência artificial de código aberto em turco) são modelos cujos pesos e códigos podem ser examinados e executados por qualquer pessoa.

## Definição e origem da palavra

Ao contrário dos modelos fechados, estes modelos são transparentes: qualquer pessoa que queira pode baixá-los, examiná-los com seus próprios dados e fazer alterações neles. Llama, Mistral e DeepSeek são exemplos conhecidos. É discutível que os dados de formação também devem ser abertos; A OSI conduz um estudo de definição separado sobre este assunto.

***Analogia:** Em vez de guardar a receita secreta de um prato, é como compartilhar a receita para que todos possam experimentar e melhorá-la.*

## Como conhecer e usar no dia a dia?

**Bate-papo local:** Assistente pessoal que funciona sem internet.
**Pesquisar:** Modelo básico testado.
**Institucional:** Solução interna sem transferência de dados.

## Profundidade Técnica e Arquitetura

Componentes:

**Pesos:** Os arquivos do modelo treinado são distribuídos pelo Hugging Face.
**Licença:** Apache e MIT são considerados permissivos. Algumas licenças comunitárias limitam o uso comercial, você precisará ler o texto.
**Quantização:** A versão reduzida do modelo (GGUF) funciona com pouca memória.
**Operando:** Ferramentas como o Ollama abrem modelos com um único comando:

```
ollama run llama3
```

Regra de hardware: À medida que o parâmetro aumenta, ele requer memória. Modelos menores rodam no laptop, os maiores rodam no servidor.

## Coisas frequentemente misturadas

Pode ser misturado com Pesos Abertos. Pesos Abertos são apenas os pesos abertos. A IA de código aberto, por outro lado, também inclui transparência de código e processo, seu escopo é mais amplo.

## Use em diferentes disciplinas

**Receita:** Receita compartilhada com ingredientes e medidas.
**Livro didático:** Código aberto que qualquer pessoa pode ler e editar.
**Banco de sementes:** Semente ancestral compartilhada pelos agricultores.

## Perguntas Frequentes

**Os modelos de código aberto são mais fracos?**

Antigamente era assim, mas hoje muitos modelos abertos competem com seus rivais fechados. Os modelos fechados estão à frente na corrida pelo topo, mas em questões práticas a diferença diminuiu.

**Por que devo usar código aberto?**

Para privacidade de dados, custo e integração total. Seus dados não são divulgados e você não paga taxa de licença.

**O uso comercial é permitido?**

Varia dependendo da licença. Apache e MIT são gratuitos, algumas licenças comunitárias impõem limites de número de usuários ou de receita.

**Por qual se deve começar?**

Comece localmente com modelos pequenos e quantizados. Se a necessidade aumentar, você o move para o servidor.

## Termos relacionados

- [Open Weights](https://trescout.com/pt/dictionary/open-weights/)
- [Self-Hosting](https://trescout.com/pt/dictionary/self-hosting/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/open-source-ai/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/open-source-ai/
