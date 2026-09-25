# Fédérez plus de 230 fournisseurs d'IA au sein d'une passerelle unifiée

> Omniroute · Python / Go · ★ 65.889

OmniRoute est une passerelle IA open source qui regroupe plus de 230 fournisseurs de modèles de langage sous un point d'accès unique compatible OpenAI. Elle intègre le basculement automatique, l'équilibrage de charge et la compression de requêtes.

## Ce que vous y gagnez
- Compatibilité API universelle : Interrogez OpenAI, Anthropic, Gemini, Mistral et vos modèles locaux via l'unique point /v1/chat/completions.
- Basculement automatique sans interruption : Redirigez instantanément les requêtes vers un modèle de secours en cas de saturation ou de panne.
- Compression de requêtes et économies : Des algorithmes d'optimisation de contexte réduisent le volume de jetons consommés.
- Observabilité complète : Suivez la latence, les taux d'erreur et les coûts de chaque fournisseur sur une interface unique.

## Profondeur technique et architecture
OmniRoute opère comme un proxy inverse haute performance entre vos applications et les fournisseurs d'IA :1. Standardisation des schémas : Normalise les requêtes hétérogènes dans un format canonique unifié avant dispatching.2. Moteur de routage et sondes de santé : Mesure la latence en continu et isole les services dégradés.3. Cache sémantique : Mémorise les réponses aux requêtes fréquentes pour répondre instantanément sans coût d'inférence.

## Installation et déploiement
Déployez OmniRoute en quelques secondes à l'aide de Docker Compose :

### Démarrage via Docker Compose
```bash
git clone https://github.com/danielfrg/omniroute.git
cd omniroute
cp .env.example .env
docker compose up -d
```

### Tester la complétion
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Bonjour !"}]}'
```

## Invite pour agents IA et architectes
Configurez une règle de routage OmniRoute associant OpenAI, Anthropic et une instance Ollama locale. Mettez en place une politique de basculement automatique sur erreurs HTTP 429 et 500, et fournissez le fichier docker-compose.yml correspondant.

## Avertissements et limites critiques
- Sécurité des clés d'API : Protégez les variables d'environnement et exigez une authentification Bearer pour tout accès distant.
- Divergences de paramètres : Les fenêtres de contexte et gestionnaires de température varient selon les familles de modèles ; standardisez vos appels avec précaution.
- Latence réseau : Déployez la passerelle à proximité de vos charges applicatives pour minimiser les allers-retours réseau.

## Questions fréquentes

### OmniRoute héberge-t-il des modèles en local ?
Non, c'est une passerelle logicielle qui achemine les appels vers des API distantes ou des moteurs locaux.

### Puis-je utiliser le SDK officiel d'OpenAI ?
Oui, il suffit de modifier la variable <code>base_url</code> de votre client pour pointer vers OmniRoute.

### Prend-il en charge Ollama et vLLM ?
Oui, tout point de terminaison compatible avec l'API OpenAI peut être enregistré.

### Les données des utilisateurs sont-elles enregistrées ?
Les règles de journalisation et de confidentialité sont entièrement configurables par l'administrateur.

## Liens utiles
- [Dépôt GitHub officiel (danielfrg/omniroute) →](https://github.com/danielfrg/omniroute)

## Termes du dictionnaire associés
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [AI Agent](/fr/dictionary/ai-agent/)
- [Runtime](/fr/dictionary/runtime/)
- [Foundation Model](/fr/dictionary/foundation-model/)

---
Source: TreScout Discovery · https://trescout.com/fr/discover/omniroute/
