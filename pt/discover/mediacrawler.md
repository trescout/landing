# Colete dados de mídia social automaticamente

O MediaCrawler coleta automaticamente postagens e comentários de usuários em plataformas populares de mídia social chinesa por meio de web scraping. Esta ferramenta baseada em Python oferece uma infraestrutura abrangente de rastreamento de dados para análise de conteúdo e processos de coleta de dados.

- ★ 59.631
- Python
- GitHub Trending · 2026-06-26

## Atualizar
- 2 de agosto de 2026: Estrela 53.062 → 59.631.

## O que você ganha
- Extraindo postagens e comentários de plataformas populares
- Login fácil com automação do navegador
- Suporta gravação em vários formatos de dados

## Instalação
**Instalando dependências**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Instalação do driver do scanner**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```


## Execução
**Iniciar extração de dados**

```
# 在 config/base_config.py 查看配置项目功能，写的有中文注释

# 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
uv run main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例，执行下面的命令查看
uv run main.py --help
```


## Se você não programa
Quero extrair dados de uma plataforma de mídia social especificada usando a ferramenta MediaCrawler. Deixe-me verificar as configurações no arquivo config/base_config.py e explicar passo a passo como devo configurar o comando uv run main.py para coletar informações de postagem e comentários fazendo pesquisa por palavra-chave para a plataforma xhs.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/mediacrawler/
