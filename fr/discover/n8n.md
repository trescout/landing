# Workflows visuels et automatisation avec l’IA

n8n associe un canvas visuel, du code personnalisé, des agents d’IA et des workflows dans une plateforme d’automatisation fair-code. La plateforme prend en charge un déploiement auto-hébergé ou cloud et plusieurs fournisseurs de modèles.

- ★ 202 576
- GitHub Trending · 2026-08-23

## Installation
**Créer le volume de données**

```
docker volume create n8n_data
```


## Exécution
**Démarrer le conteneur Docker n8n**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```


## Que fait cet outil ?
Avec n8n, vous pouvez créer des workflows sur un canvas visuel et les étendre avec JavaScript, Python et des paquets npm. Les sources officielles mentionnent la flexibilité entre les modèles OpenAI, Anthropic, Google et open source, ainsi que les validations humaines, l’observabilité, le contrôle d’accès par rôle et les pistes d’audit. La plateforme peut être auto-hébergée ou utilisée dans le cloud.

## Pour qui ?
Les équipes qui souhaitent combiner la conception visuelle de workflows avec du code personnalisé et des agents d’IA.

## À quoi ne faut-il pas s’attendre ?
Les personnes qui recherchent uniquement des produits sous licence propriétaire ou qui ne souhaitent pas étendre les workflows avec du code ou de la configuration.

## Points forts
- Associe canvas visuel, code personnalisé et agents d’IA dans les workflows.
- Peut être étendu avec JavaScript, Python et des paquets npm.
- Propose un déploiement auto-hébergé ou cloud.
- Mentionne les validations humaines, l’observabilité, le contrôle d’accès par rôle et les pistes d’audit.

## Premiers pas
- Suivez le démarrage rapide officiel avec Docker pour lancer n8n.
- Ouvrez l’éditeur dans votre navigateur sur le port 5678.
- Créez votre premier workflow sur le canvas visuel.
- Ajoutez du code personnalisé ou un fournisseur de modèles pris en charge selon vos besoins.

## Démarrage prudent

## Premier prompt
Aidez-moi à concevoir sur le canvas visuel un workflow qui reçoit une entrée, la traite avec un modèle d’IA et transmet le résultat à l’étape suivante.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Dépôt GitHub officiel de n8n →
- Documentation officielle de n8n →
- Dépôt de documentation n8n →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/n8n/
