# Sistema de armazenamento de objetos de alto desempenho

O RustFS foi desenvolvido como um sistema de armazenamento de objetos de alto desempenho compatível com S3. Oferece suporte à interoperabilidade e migração de dados com outras plataformas compatíveis com S3, como MinIO e Ceph.

- ★ 33.264
- Rust
- GitHub Trending · 2026-09-19

## O que você ganha
- Proporciona alta velocidade e segurança de memória com a linguagem Rust
- Funciona perfeitamente com ferramentas existentes graças à sua estrutura compatível com S3
- Oferece uso comercial irrestrito com a licença Apache 2.0

## Instalação
**Iniciar com script de instalação**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Executar a versão mais recente com Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```


## Execução
**Iniciar o sistema usando Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```


## Se você não programa
Quero configurar um ambiente de armazenamento de objetos de alto desempenho usando o RustFS. Como posso gerenciar meus dados aproveitando a compatibilidade S3 do sistema e a que devo estar atento ao escalar em uma arquitetura distribuída? Oriente-me passo a passo sobre a instalação e as configurações básicas deste sistema licenciado sob Apache 2.0.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/rustfs/
