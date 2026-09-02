# Baixe vídeos da internet em seu próprio servidor

Desenvolvido por Averygan, o Reclip é uma ferramenta leve e auto-hospedável para baixar vídeos de quase todos os sites da internet. Ele permite que você salve arquivos de mídia em seu dispositivo local por meio de uma interface web simples.

- ★ 7.951
- HTML
- GitHub Trending · 2026-09-02

## O que você ganha
- Baixa arquivos de vídeo e áudio de mais de 1000 sites, como YouTube e Instagram.
- Salva os arquivos baixados no formato de vídeo MP4 ou áudio MP3.
- Oferece uma interface simples e rápida que funciona através do navegador web.

## Instalação
**Instalação padrão**

```
brew install yt-dlp ffmpeg    # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Instalação com Docker**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```


## Execução
**Acesso à interface**

```
http://localhost:8899
```


## Se você não programa
Desejo usar a ferramenta Reclip para baixar links de vídeos da internet para o meu dispositivo local nos formatos MP4 ou MP3. Para iniciar o processo de download, preciso colar os links na caixa de entrada, selecionar o formato, clicar no botão Fetch para carregar as informações do vídeo e, em seguida, usar o botão Download. Nesse processo, posso realizar downloads em lote e ajustar a resolução do vídeo de acordo com minhas preferências.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/reclip/
