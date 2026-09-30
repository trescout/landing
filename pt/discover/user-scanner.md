# Análise de usuários OSINT em mais de 465 plataformas

O User-Scanner baseado em Python realiza varredura de inteligência de código aberto (OSINT) em mais de 465 redes sociais, fóruns e repositórios de código a partir de um único nome de usuário ou e-mail.

- ★ 5.007
- Python
- GitHub Trending · 2026-08-31

## O que você ganha
- Ampla cobertura da plataforma: verifique a presença da conta no GitHub, Reddit, Twitter, Steam, Telegram e mais de 465 sites de uma só vez.
- Verificação assíncrona de alta velocidade: consulta paralela de centenas de alvos em segundos com arquitetura baseada em assíncrono e aiohttp.
- Filtragem de falso positivo: Mecanismo de detecção inteligente que verifica textos de erro no corpo da resposta, bem como códigos de status HTTP.
- Exportação de relatórios JSON e CSV: Salvando resultados de análises em formatos configurados para uso em relatórios forenses e de segurança.
- Privacidade e execução local: Possibilidade de executar quaisquer consultas inteiramente a partir da máquina local, sem enviá-las para servidores de terceiros.

## Instalação
**Clonando o repositório e instalando dependências**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```


## Execução
**Verificar nome de usuário e e-mail de destino**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```


## Arquitetura técnica e princípio de funcionamento
- Modelos de banco de dados (manifestos de site JSON): configuração modular contendo padrões de URL, códigos de erro e expressões regulares de perfil para mais de 465 plataformas.
- Pool de solicitações simultâneas: usando a largura de banda da rede de maneira mais eficiente, armazenando em cache resoluções DNS e soquetes TCP.
- Cabeçalhos HTTP personalizados e rotação de agente de usuário: simulação realista de cabeçalhos de navegador para evitar WAF e obstruções de limite de taxa.

## Cenários de investigação OSINT e análise de dados
- Violação e rastreamento de dados pessoais: mapeie em quais canais sociais os perfis vazados estão ativos com correlação de nome de usuário.
- Auditorias de Segurança Corporativa: Determine se os funcionários da empresa abrem contas em plataformas externas com seus endereços de e-mail corporativos.
- Defesa de engenharia social: identifique antecipadamente contas de imitação não autorizadas contra ataques de spear phishing.

## Se você não programa
Você pode explicar passo a passo como posso verificar mais de 465 plataformas usando um único nome de usuário usando a ferramenta User-Scanner em uma auditoria de segurança, exportar as descobertas no formato JSON e listar perfis suspeitos?

## Perguntas frequentes
- É legal usar o User-Scanner? Sim. O User-Scanner consulta apenas o status de presença da conta publicamente visível em páginas da web públicas; Ele não fornece acesso não autorizado ao sistema ou quebra de senhas.
- Existe suporte para Tor ou proxy? Sim. Você pode mascarar seu endereço IP e evitar limites de velocidade roteando solicitações por meio de cadeias de proxy SOCKS5 ou HTTP.
- Quanto tempo leva para concluir os resultados? Graças à sua arquitetura assíncrona, a verificação de mais de 465 plataformas normalmente é concluída em 20 a 45 segundos, dependendo da sua conexão com a Internet.
- Como funciona a pesquisa de e-mail? No modo de e-mail, os sinais de autenticação pública são examinados nos pontos finais de redefinição de senha ou de registro de conta dos serviços suportados.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/user-scanner/
