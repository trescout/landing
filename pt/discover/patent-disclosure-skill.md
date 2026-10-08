# Automatize descrições de invenções de patentes com inteligência artificial

O Patent Disclosure Skill baseado em Python analisa rascunhos de invenções técnicas para gerar descrições técnicas, reivindicações (claims) e comparações com o estado da técnica (prior art) em conformidade com o formato oficial de patentes.

- ★ 10.360
- Python
- GitHub Trending · 2026-08-31

## Atualizações

- **27 de setembro de 2026:** Estrelas 6,058 → 10,360.

## O que você ganha

- Geração de texto de patente estruturado: criação das seções de campo técnico, antecedentes, resumo e descrição detalhada da invenção em conformidade com as normas padrão de patentes.
- Árvore de reivindicações independentes e dependentes: Formulação automática de listas hierárquicas de reivindicações de patentes que maximizam o escopo da proteção legal.
- Análise de lacunas de técnica anterior (Prior Art): Ênfase clara nas diferenças técnicas e no nível inventivo entre as tecnologias existentes e a invenção.
- Acelerar a colaboração com agentes de patentes: economize tempo e custos transformando os rascunhos dos engenheiros em documentos técnicos organizados e prontos para os agentes de patentes.
- Suporte a terminologia de patentes multilíngue: conformidade com a terminologia em inglês, turco e de instituições internacionais de patentes (WIPO, EPO, USPTO).

## Instalação

**Clonando o repositório e instalando dependências**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```

## Execução

**Iniciar a análise de patentes e a geração de descrições**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```

## Arquitetura técnica e princípio de funcionamento

- Motor de Decomposição de Invenções Técnicas: Identifica as principais entradas, saídas e a metodologia em descrições de software, hardware ou processos químicos.
- Validador de Sintaxe de Reivindicações: Analisador de linguagem jurídica que verifica expressões vagas e erros formais em reivindicações.
- Exportação de Modelo e Markdown: Salvar o documento em formato Markdown com seções padronizadas para uso em pedidos oficiais de patente.

## Fluxos de trabalho de análise de patentes e preparação de reivindicações

- Transformar algoritmos de software em formato patenteável: derivar descrições de métodos e sistemas aceitáveis pelas autoridades de patentes a partir de códigos e diagramas de arquitetura.
- Defesa contra Office Actions: Criação de minutas de resposta que listam as características distintivas da invenção em face das objeções dos examinadores de patentes.
- Auditoria de Portfólio de Propriedade Intelectual: Mapeamento antecipado de etapas inventivas com potencial de patente em projetos tecnológicos internos.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Gostaria de preparar um documento formal de notificação de invenção para um algoritmo de cache de banco de dados distribuído que desenvolvi, utilizando a habilidade de patent disclosure. Você poderia explicar passo a passo como fornecer o fluxo do algoritmo como entrada e gerar as reivindicações independentes, o campo técnico da invenção e as diferenças em relação ao estado da técnica?

## Perguntas frequentes

- Esta ferramenta substitui um agente de patentes oficial? Não. O Patent Disclosure Skill é uma ferramenta de preparação e produtividade que ajuda engenheiros a organizar rascunhos de invenções e deixá-los prontos para os agentes; o depósito legal deve ser feito por um profissional.
- Com quais modelos de LLM funciona? Pode ser configurado para funcionar com Claude 3.5 Sonnet, GPT-4o ou modelos locais de pesos abertos (Qwen, Llama 3).
- Meus segredos técnicos confidenciais podem vazar na internet? Ao executar um LLM local (Ollama ou vLLM), todas as análises de patentes são feitas inteiramente no seu computador local e nenhum dado é enviado para fora.
- Consegue interpretar desenhos de patentes e fluxogramas? Quando modelos multimodais são conectados, o sistema também pode analisar arquiteturas e diagramas de blocos, transcrevendo-os para texto.

## Termos relacionados do glossário

- [Disclosure](https://trescout.com/pt/dictionary/disclosure/)
- [patent disclosure](https://trescout.com/pt/dictionary/patent-disclosure/)
- [Multimodal](https://trescout.com/pt/dictionary/multimodal/)
- [Markdown](https://trescout.com/pt/dictionary/markdown/)
- [Skill](https://trescout.com/pt/dictionary/skill/)
- [LLM](https://trescout.com/pt/dictionary/llm/)

- **Para quem é:** Agentes de patentes, gestores de propriedade intelectual, engenheiros de P&D e inventores.
- **Licença:** MIT (Özgür açık kaynak lisansı)
- **Framework:** Capacidade de Agente de Patentes Baseada em Python
- **Plataformas:** Linux, macOS, Windows

## Links

- [Repositório no GitHub →](https://github.com/handsomestWei/patent-disclosure-skill)
- [Ler em turco →](https://trescout.com/discover/patent-disclosure-skill/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-31: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/patent-disclosure-skill/
