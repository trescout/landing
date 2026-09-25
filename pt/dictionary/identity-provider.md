# O que é um Identity Provider?

> Provedor de Identidade Digital

**Categoria:** Dev  
**Última atualização:** 2026-09-22

Um Identity Provider (IdP / Provedor de Identidade) é um sistema centralizado de autenticação que cria, gerencia e valida identidades de usuários em múltiplos aplicativos e serviços.

## Definição e etimologia
Na engenharia de software contemporânea, cada aplicação não deve guardar senhas de forma isolada. O IdP desacopla a segurança da lógica de negócios, permitindo que o usuário faça login uma única vez (Single Sign-On / SSO) para acessar todos os sistemas autorizados.

## Contexto cotidiano e uso prático
- **Login Social:** Botões de 'Entrar com Google ou Apple' encontrados em sites e aplicativos móveis.
- **Gestão Corporativa:** Controle unificado de acessos e políticas de MFA em empresas com Okta ou Azure AD.
- **Serviços Auto-hospedados:** Instalação de servidores Keycloak e Authentik para proteger microsserviços internos.

## Profundidade técnica e arquitetura
Protocolos e Padrões Arquiteturais:- **OpenID Connect (OIDC):** Camada de identidade construída sobre OAuth 2.0 que emite tokens JSON Web Token (JWT) assinados.
- **SAML 2.0:** Padrão federado baseado em XML muito empregado em infraestruturas legadas corporativas.
- **Múltiplo Fator (MFA):** Exigência de chaves de hardware FIDO2, biometria e aplicativos de códigos temporais (TOTP).

## Costuma ser confundido com
Frequentemente confundido com um Service Provider (SP) ou servidor de autorização. O IdP responde 'Quem é você?' (autenticação); o servidor de recursos decide 'O que você tem permissão para fazer?' (autorização).

## Perspectivas interdisciplinares
- **Diplomacia:** O cartório emitindo o passaporte cidadão vs fiscais de fronteira checando o visto de permanência.
- **Hotelaria:** A recepção conferindo documentos e emitindo a chave magnética vs a fechadura eletrônica do quarto.
- **Segurança:** O crachá emitido pela portaria central vs catracas de departamentos específicos.

## Por analogia
É comparável à recepção de um hotel: você valida sua identidade uma única vez no balcão, ganha um cartão magnético codificado e entra no seu quarto sem precisar mostrar o passaporte a cada porta.

## Perguntas frequentes

**Por que adotar um Identity Provider?**  
Reduz drasticamente os riscos de vazamento de senhas, centraliza revogações de acesso e oferece login único (SSO).

**Como o IdP avisa a aplicação que o usuário é legítimo?**  
Ele envia um token criptográfico assinado contendo dados verificados (claims) do usuário.

**Posso manter meu próprio IdP no meu servidor?**  
Sim, ferramentas abertas como Keycloak, Authentik e Authelia oferecem controle completo de dados on-premises.

**O que ocorre se o IdP sair do ar?**  
Novos acessos são impedidos; redundância, balanceamento de carga e caches de token são vitais.

## Termos relacionados
- [Cloud Computing](/pt/dictionary/cloud-computing/)
- [Endpoint](/pt/dictionary/endpoint/)
- [Application](/pt/dictionary/application/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/identity-provider/
