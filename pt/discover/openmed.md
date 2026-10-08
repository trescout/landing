# Inteligência artificial de código aberto na área da saúde

OpenMed é uma plataforma que reúne modelos de inteligência artificial de código aberto e conjuntos de dados utilizados na área da saúde. Desenvolvida para aplicações voltadas para a área médica, esta biblioteca baseada em Python visa padronizar os processos de processamento de dados de saúde.

- ★ 5.329
- Python
- GitHub Trending · 2026-06-10

## Atualizações

- **16 de setembro de 2026:** Estrelas 5,217 → 5,329, versão mais recente v2.5.0 (15 de setembro de 2026).
- **5 de setembro de 2026:** Estrelas 5,076 → 5,217, versão mais recente v2.3.0 (4 de setembro de 2026).
- **21 de agosto de 2026:** Estrelas 5,015 → 5,076, versão mais recente v2.2.0 (21 de agosto de 2026).
- **15 de agosto de 2026:** Estrelas 4,793 → 5,015, versão mais recente v2.1.0 (12 de agosto de 2026).

## O que você ganha

- Extrai insights médicos estruturados de textos clínicos.
- Anonimiza dados pessoais de saúde no dispositivo.
- Ele executa mais de 1.000 modelos médicos de IA offline.

## Instalação

**Configuração básica**

```
pip install "openmed[hf]"
```

**Suporte Apple Silicon (MLX)**

```
pip install "openmed[mlx]"
```

## Execução

**Análise Simples com Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero analisar textos médicos usando a biblioteca OpenMed. Tenho o Python instalado no meu dispositivo. Em primeiro lugar, concluí a instalação com o comando pip install “openmed[hf]”. Agora, quais funções devo chamar em meu código Python para analisar minhas notas clínicas e detectar termos médicos ou dados pessoais (PII) nelas? Por favor, crie-me um bloco de código de amostra simples na seleção do modelo e na impressão dos resultados.

## Termos relacionados do glossário

- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a profissionais de saúde e desenvolvedores de software que desejam realizar análises orientadas para a privacidade em seu próprio hardware, sem enviar seus dados médicos para serviços em nuvem.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/maziyarpanahi/openmed)
- [Ler em turco →](https://trescout.com/discover/openmed/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-10: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openmed/
