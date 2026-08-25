# Motor de Busca Privado para Páginas e Arquivos Pessoais

Motor de busca privado com licença AGPLv3 para páginas visitadas e arquivos guardados pelo usuário. Oferece indexação full-text, filtros de consulta avançados e busca semântica opcional.

- ★ 2.620
- Go
- GitHub Trending · 2026-08-25

## O que esta ferramenta faz?
O Hister pode rodar localmente ou na infraestrutura que você controla; não exige serviço em nuvem ou telemetria obrigatória. Indexa páginas via extensões Chrome e Firefox, oferece opções de rastreamento de sites e importação do histórico do navegador. Se a busca semântica estiver ativada, o texto do documento é enviado ao endpoint de embeddings selecionado.

## Para quem é?
Quem quer consultar páginas web e arquivos pessoais em uma infraestrutura de busca sob seu controle.

## O que não esperar
Cenários que exigem serviço em nuvem obrigatório ou telemetria, ou fluxos de indexação do navegador que não permitem enviar conteúdo ao servidor Hister configurado.

## Destaques
- Opera localmente ou em infraestrutura controlada, sem telemetria ou serviço em nuvem obrigatório
- Consultas com full-text, filtros por campo, frases, curingas, negações e prioridades
- Busca opcional semântica com clientes web, terminal, TUI, CLI e MCP

## Primeiro fluxo de uso
- Baixe o binário apropriado para sua plataforma e torne-o executável no Linux ou macOS
- Inicie o servidor Hister em modo de escuta local
- Abra a interface web local
- Instale a extensão do Chrome ou Firefox e selecione as páginas a serem indexadas

## Início seguro

## Primeiro prompt
Abra a interface local, indexe as páginas selecionadas com a extensão do navegador e verifique as pesquisas usando filtros de consulta.

## Instalação
**Tornar o binário executável**

```
chmod +x hister
```


## Execução
**Iniciar o servidor hister**

```
./hister listen
```

**Acessar interface local**

```
http://127.0.0.1:4433
```


## Links
- Repositório no GitHub →
- Início rápido →
- README de privacidade e uso →
- Fluxo de uso →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/hister/
