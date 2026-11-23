# Ferramenta de avaliação de capacidades de agentes de inteligência artificial

Desenvolvido pela NVIDIA, o SkillEvaluator é um framework multilocal que avalia as capacidades dos agentes de inteligência artificial por meio de métodos como controle de qualidade, detecção de sobreposição semântica e geração de dados sintéticos. Esta ferramenta oferece processos de avaliação em tempo real para medir os impactos nos comportamentos dos agentes.

- ★ 4.449
- Python
- GitHub Trending · 2026-11-16

## Atualizações

- **23 de novembro de 2026:** Estrelas 4,448 → 4,449, versão mais recente v1.0.1 (18 de novembro de 2026).
- **23 de novembro de 2026:** Estrelas 3,655 → 4,448, versão mais recente v1.1.0 (23 de novembro de 2026).
- **18 de novembro de 2026:** Estrelas 2,913 → 3,655, versão mais recente v1.0.1 (18 de novembro de 2026).
- **17 de novembro de 2026:** Estrelas 1,912 → 2,913, versão mais recente v0.9.0 (13 de novembro de 2026).

## O que você ganha

- Verifica a qualidade das capacidades dos agentes de inteligência artificial
- Mede o impacto das habilidades dos agentes nos resultados das tarefas
- Oferece relatórios detalhados com um framework em camadas

## Instalação

**Instale o pacote**

```
pip install skillevaluator
```

## Execução

**Realizar controle de qualidade**

```
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero avaliar as capacidades do agente de inteligência artificial. Para este propósito, conclua a instalação executando o comando pip install skillevaluator no terminal e, em seguida, execute o comando uv run --python 3.13 skillevaluator quality-check \
src/skillevaluator/tier3/reference_skills/text-analyzer \
-r cli -r json -o reports/first-quality para o teste de controle de qualidade de exemplo.

Repositório: https://github.com/NVIDIA/SkillEvaluator. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Framework](https://trescout.com/pt/dictionary/framework/)
- [Terminal](https://trescout.com/pt/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores que criam agentes de inteligência artificial e desejam testar o desempenho das habilidades desses agentes.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/NVIDIA/SkillEvaluator)
- [Ler em turco →](https://trescout.com/discover/skillevaluator/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/skillevaluator/
