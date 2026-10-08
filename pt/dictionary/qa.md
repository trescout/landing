# O que é QA?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

> Quality Assurance

QA (Quality Assurance - Garantia de Qualidade) é a disciplina sistemática de gestão da qualidade que visa prevenir defeitos antes que eles surjam em todas as fases do ciclo de vida de desenvolvimento de software, estabelecer padrões de engenharia e garantir a confiabilidade do produto final.

## Origem conceitual: Do ciclo de Deming e das linhas de produção para o software

O conceito de Garantia da Qualidade nasceu muito antes do software, em meados do século XX, na produção industrial. A Gestão da Qualidade Total (TQM), cujas bases foram lançadas por W. Edwards Deming e Walter Shewhart, e o ciclo PDCA (Plan-Do-Check-Act / Planejar-Fazer-Verificar-Agir), defendem que a qualidade não pode ser inspecionada posteriormente, mas sim construída diretamente no produto. O princípio Jidoka do Sistema de Produção Toyota (parar a linha imediatamente quando um produto defeituoso é fabricado) é também o ancestral da moderna integração contínua (CI) e da filosofia de QA de hoje.

No mundo do software, a famosa pesquisa "Economia da Engenharia de Software" de Barry Boehm provou que, enquanto o custo para corrigir um erro percebido na fase de design é de 1 unidade, o custo para corrigi-lo após ir para produção (production) pode subir até 100 vezes. O QA existe para evitar esse custo colossal e a perda de reputação.

***Analogia:** Depurar (debugging) é como intervir na mesa de cirurgia, enquanto fazer testes de software é realizar exames laboratoriais. Já o QA é um protocolo de saúde pública e medicina preventiva: visa eliminar o risco de adoecer desde o início, estabelecendo guias de alimentação saudável, calendários de vacinação e regras de higiene.*

## A distinção crítica: QA vs QC vs Testing

Embora esses três conceitos sejam frequentemente usados de forma intercambiável, existem limites metodológicos claros entre eles:

**Teste (Testing):** É a execução de cenários para encontrar erros concretos (bugs) em uma versão específica do software (é focado no produto e reativo).

**Controle de Qualidade (QC - Quality Control):** É o portão de auditoria que verifica se o produto está em conformidade com as especificações técnicas e critérios de aceitação determinados antes de ser lançado (é focado no produto e reativo).

**Garantia de Qualidade (QA - Quality Assurance):** É a disciplina abrangente que projeta metodologias de desenvolvimento, infraestrutura de testes, padrões de arquitetura e processos de CI/CD para garantir que os erros nunca ocorram (é orientada a processos e proativa).

## Paradigma de QA moderno: Shift-Left e Shift-Right

No modelo tradicional em cascata (waterfall), os desenvolvedores escreviam o código e depois o "jogavam por cima do muro" para o departamento de QA testar. No mundo ágil (Agile) e DevOps moderno, essa abordagem deu lugar a duas direções complementares:

**1. Shift-Left (Deslocamento para a Esquerda):** Move o controle de qualidade para o início do desenvolvimento. Enquanto escreve o código, o desenvolvedor aplica análise estática (ESLint, SonarQube), verificação de tipos (TypeScript), testes unitários (Jest, pytest) e TDD (Test-Driven Development). Aqui, o engenheiro de QA não é quem executa os testes, mas sim um arquiteto de plataforma que constrói a infraestrutura e os frameworks de teste.

**2. Shift-Right (Deslocamento para a Direita):** Consiste na manutenção da qualidade após o código entrar em produção (live). A experiência real do usuário é monitorada por meio de monitoramento sintético, implantações canary (kanarya dağıtımları), rastreamento de erros (Sentry), engenharia do caos (Chaos Engineering) e análise de tráfego em tempo real.

## Pirâmide de testes e camadas de automação

Uma arquitetura de QA sólida baseia-se no princípio da Pirâmide de Testes de Mike Cohn:

**Testes Unitários (Unit Tests):** Formam a base; testam funções independentes de forma isolada, executam em milissegundos e têm o menor custo.

**Testes de Integração e de Contrato (Integration & Contract Tests):** Valida o banco de dados, o cache e os contratos de API entre microsserviços (ex.: Pact).

**Testes de Ponta a Ponta (E2E Tests):** Simula as etapas de um usuário real no navegador com ferramentas como Cypress ou Playwright; tem escopo amplo, mas sua manutenção é mais custosa.

**Testes Não Funcionais:** Inclui testes de carga e de estresse (k6, Locust), varreduras de vulnerabilidade (SAST/DAST) e auditorias de acessibilidade (WCAG / a11y).

## QA na era da inteligência artificial e dos LLMs

Com a disseminação de sistemas probabilísticos (não determinísticos) como os grandes modelos de linguagem (LLMs), a disciplina de QA entrou em uma nova fase:

**Avaliações de LLM (Evals):** Auditorias automatizadas que pontuam as respostas do modelo quanto a alucinação, precisão, toxicidade e relevância (DeepEval, Ragas).

**Testes de Regressão Semântica:** Conjuntos de referência (benchmarks) que medem se uma alteração nos modelos de prompt prejudicou a qualidade das respostas anteriores.

**Geração de Testes Impulsionada por Inteligência Artificial:** Detecção automática de cenários de teste e diferenças de regressão de interface visual com modelos de inteligência artificial.

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

- [Unit Testing](https://trescout.com/pt/dictionary/unit-testing/)
- [End-to-End Testing](https://trescout.com/pt/dictionary/end-to-end-testing/)
- [Testing Framework](https://trescout.com/pt/dictionary/testing-framework/)
- [Production Pipeline](https://trescout.com/pt/dictionary/production-pipeline/)
- [Benchmarks](https://trescout.com/pt/dictionary/benchmark/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)

## Ferramentas relacionadas

- [Gstack](https://trescout.com/pt/discover/gstack/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/qa/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/qa/
