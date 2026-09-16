# Analise aplicativos Android rapidamente

O ASC é uma interface de descompilador Android extremamente rápida, desenvolvida para pesquisadores de aplicativos móveis e agentes de inteligência artificial. Escrita em Python, esta ferramenta visa acelerar o processo de análise de arquivos de aplicativos complexos.

- ★ 1.336
- Python
- GitHub Trending · 2026-09-16

## O que você ganha
- Analisa arquivos de aplicativos grandes em segundos
- Realiza consultas diretamente no código sem sobrecarregar a memória
- Produz resultados rápidos sem pré-processamento desnecessário

## Instalação
**Instalação com gerenciador de pacotes**

```
pip install droidasc
```

**Instalação a partir do código-fonte**

```
pip install .
```


## Execução
**Abrir arquivo de aplicativo com interface visual**

```
droidasc app.apk --gui
```

**Exportar uma classe específica**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```


## Se você não programa
Aja como um pesquisador de aplicativos Android. Ajude-me a encontrar uma classe específica em um arquivo APK, analisar o arquivo AndroidManifest.xml ou pesquisar referências dentro do código usando a ferramenta Droid ASC. Ao criar os comandos, utilize os comandos getclass, getmanifest e findrefs da ferramenta com os parâmetros corretos e explique como devo interpretar as saídas.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/asc/
