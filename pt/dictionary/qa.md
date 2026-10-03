# O que é QA?

> Quality Assurance

QA (Quality Assurance - Garantia de Qualidade) é a disciplina sistemática de gestão da qualidade que visa prevenir defeitos antes que eles surjam em todas as fases do ciclo de vida de desenvolvimento de software, estabelecer padrões de engenharia e garantir a confiabilidade do produto final.

## Origem conceitual: Do ciclo de Deming e das linhas de produção para o software
O conceito de Garantia da Qualidade nasceu muito antes do software, em meados do século XX, na produção industrial. A Gestão da Qualidade Total (TQM), cujas bases foram lançadas por W. Edwards Deming e Walter Shewhart, e o ciclo PDCA (Plan-Do-Check-Act / Planejar-Fazer-Verificar-Agir), defendem que a qualidade não pode ser inspecionada posteriormente, mas sim construída diretamente no produto. O princípio Jidoka do Sistema de Produção Toyota (parar a linha imediatamente quando um produto defeituoso é fabricado) é também o ancestral da moderna integração contínua (CI) e da filosofia de QA de hoje.

## A distinção crítica: QA vs QC vs Testing
Embora esses três conceitos sejam frequentemente usados de forma intercambiável, existem limites metodológicos claros entre eles:

## Paradigma de QA moderno: Shift-Left e Shift-Right
No modelo tradicional em cascata (waterfall), os desenvolvedores escreviam o código e depois o "jogavam por cima do muro" para o departamento de QA testar. No mundo ágil (Agile) e DevOps moderno, essa abordagem deu lugar a duas direções complementares:

## Pirâmide de testes e camadas de automação
Uma arquitetura de QA sólida baseia-se no princípio da Pirâmide de Testes de Mike Cohn:

## QA na era da inteligência artificial e dos LLMs
Com a disseminação de sistemas probabilísticos (não determinísticos) como os grandes modelos de linguagem (LLMs), a disciplina de QA entrou em uma nova fase:

## Perguntas frequentes
**O que significa QA e qual é a sua sigla?**
É a abreviação de Quality Assurance; em português, significa Garantia de Qualidade. É a disciplina de engenharia que garante que os processos de software funcionem sem erros do início ao fim.

**Qual é a diferença entre QA, QC (Controle de Qualidade) e Teste?**
O Teste e o QC são etapas reativas focadas em encontrar erros no código existente. Já o QA é um processo proativo que projeta os processos de desenvolvimento, padrões e ferramentas para evitar que os erros ocorram desde o início.

**O que significam as abordagens de teste Shift-Left e Shift-Right?**
Shift-Left significa puxar os processos de teste para o início do desenvolvimento (no momento da escrita do código); Shift-Right refere-se ao monitoramento em tempo real da saúde do sistema e do comportamento do usuário no ambiente de produção.

**Como o QA é realizado em aplicativos baseados em inteligência artificial e LLM?**
Além dos testes tradicionais, são utilizadas estruturas de avaliação (evals) especiais que medem taxas de alucinação, similaridade semântica, regressão de prompt e métricas de precisão de RAG.


## Termos relacionados
- [Unit Testing](/pt/dictionary/unit-testing/)
- [End-to-End Testing](/pt/dictionary/end-to-end-testing/)
- [Testing Framework](/pt/dictionary/testing-framework/)
- [Production Pipeline](/pt/dictionary/production-pipeline/)
- [Benchmarks](/pt/dictionary/benchmark/)
- [Runtime](/pt/dictionary/runtime/)

## Ferramentas relacionadas
- [Gstack](/pt/discover/gstack/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/qa/
