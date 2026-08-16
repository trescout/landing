# Inteligência artificial de código aberto na área da saúde

OpenMed é uma plataforma que reúne modelos de inteligência artificial de código aberto e conjuntos de dados utilizados na área da saúde. Desenvolvida para aplicações voltadas para a área médica, esta biblioteca baseada em Python visa padronizar os processos de processamento de dados de saúde.

- ★ 5.015
- Python
- GitHub Trending · 2026-06-10

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
Quero analisar textos médicos usando a biblioteca OpenMed. Tenho o Python instalado no meu dispositivo. Em primeiro lugar, concluí a instalação com o comando pip install “openmed[hf]”. Agora, quais funções devo chamar em meu código Python para analisar minhas notas clínicas e detectar termos médicos ou dados pessoais (PII) nelas? Por favor, crie-me um bloco de código de amostra simples na seleção do modelo e na impressão dos resultados.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openmed/
