# Qu'est-ce qu'un Identity Provider ?

> Fournisseur d'Identité Numérique

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-22

Un Identity Provider (IdP / Fournisseur d'Identité) est un service d'authentification centralisé qui crée, gère et valide les identités numériques des utilisateurs sur de multiples applications.

## Définition et étymologie
Dans les architectures logicielles modernes, les applications ne doivent plus gérer de mots de passe en interne. L'IdP découple l'authentification de la logique métier, permettant aux utilisateurs de s'authentifier une seule fois pour accéder à plusieurs services via le Single Sign-On (SSO).

## Usage quotidien et contexte pratique
- **Connexion tierce :** Boutons 'Se connecter avec Google ou GitHub' intégrés dans les applications web.
- **Gestion d'entreprise :** Contrôle des accès et de la double authentification (MFA) via Okta ou Microsoft Entra ID.
- **Infrastructures auto-hébergées :** Déploiement de Keycloak ou Authentik pour sécuriser des parcs de microservices.

## Profondeur technique et architecture
Protocoles et briques de sécurité :- **OpenID Connect (OIDC) :** Couche d'identité reposant sur OAuth 2.0 fournissant des jetons JWT signés cryptographiquement.
- **SAML 2.0 :** Standard basé sur XML prédominant dans les systèmes d'information d'entreprise.
- **Authentification forte (MFA) :** Clés de sécurité physiques (FIDO2/WebAuthn) et applications d'authentification TOTP.

## Souvent confondu avec
Souvent confondu avec un fournisseur de service (Service Provider / SP). L'IdP répond à la question 'Qui êtes-vous ?' (authentification), tandis que le gestionnaire d'autorisations tranche 'Qu'avez-vous le droit de faire ?' (autorisation).

## Perspectives interdisciplinaires
- **Voyage :** L'administration délivrant un passeport officiel vs le visa d'entrée vérifié aux frontières.
- **Hôtellerie :** La réception d'un hôtel vérifiant une pièce d'identité et remettant une carte d'accès vs la serrure de la chambre.
- **Finance :** L'agence bancaire délivrant un moyen de paiement vs les terminaux de paiement commerçants.

## Par analogie
C'est l'équivalent de la réception d'un hôtel : vous montrez votre passeport à l'accueil pour obtenir une carte magnétique, qui vous ouvre ensuite les portes sans avoir à justifier de votre identité à chaque couloir.

## Questions fréquentes

**Quel est le principal avantage d'un fournisseur d'identité ?**  
Il évite de disperser les mots de passe dans des dizaines de bases distinctes et simplifie l'expérience grâce au SSO.

**Comment transmet-il les informations aux applications ?**  
Par l'émission de jetons chiffrés et signés (tokens JWT) attestant de l'identité vérifiée de l'utilisateur.

**Existe-t-il des IdP open source et auto-hébergeables ?**  
Oui, des solutions reconnues comme Keycloak, Authentik et Authelia permettent une maîtrise totale de ses identités.

**Que se passe-t-il en cas de panne de l'IdP ?**  
L'accès aux services connectés est bloqué ; la haute disponibilité et la mise en cache de jetons sont donc fondamentales.

## Termes liés
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [Endpoint](/fr/dictionary/endpoint/)
- [Application](/fr/dictionary/application/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/identity-provider/
