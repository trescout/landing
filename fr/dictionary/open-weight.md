# Qu'est-ce que l'Open Weight ?

> Poids de Modèle en Accès Public

**Catégorie:** AI  
**Dernière mise à jour:** 2026-09-22

L'open weight désigne les modèles d'intelligence artificielle dont les paramètres entraînés (les poids) sont téléchargeables librement, permettant leur exécution et leur réentraînement sur du matériel privé.

## Définition et étymologie
Par opposition aux fournisseurs d'API fermées qui facturent chaque jeton, les modèles à poids ouverts confient les tenseurs du réseau neuronal directement aux développeurs. Cela garantit la souveraineté des données et supprime la dépendance envers des serveurs tiers.

## Usage quotidien et contexte pratique
- **Exécution locale sans connexion :** Faire tourner des modèles sur un ordinateur portable ou un serveur interne sans connexion Internet.
- **Confidentialité des données d'entreprise :** Empêcher toute fuite de secrets industriels ou de données médicales.
- **Économies d'échelle :** Supprimer les coûts d'abonnement récurrents en rentabilisant son propre matériel informatique.

## Profondeur technique et architecture
Architecture technique des poids ouverts :- **Formats de tenseurs :** Distribution au format Safetensors ou GGUF, avec quantification en 4 ou 8 bits.
- **Moteurs d'inférence dédiés :** Prise en charge par des frameworks ultra-rapides comme vLLM, Ollama et llama.cpp.
- **Adaptation par adaptateurs LoRA :** Personnalisation ciblée sans réentraîner la totalité des milliards de paramètres de base.

## Souvent confondu avec
Souvent confondu avec l'open source intégral. L'open source exige de fournir aussi le code et les données brutes d'entraînement ; l'open weight livre principalement les matrices numériques finales résultant du calcul.

## Perspectives interdisciplinaires
- **Boulangerie :** Acheter un mélange de farines prêt à l'emploi et cuire son pain chez soi vs acheter une baguette industrielle emballée.
- **Logiciel :** Télécharger un binaire exécutable autonome vs souscrire à un abonnement logiciel SaaS distant.
- **Musique :** Posséder les pistes d'enregistrement multipistes pour faire ses mixages vs écouter un flux radio protégé.

## Par analogie
C'est comme recevoir la préparation et les ingrédients pour cuire et assaisonner le plat dans votre propre cuisine comme vous l'entendez.

## Questions fréquentes

**Que peut-on faire avec un modèle open-weight ?**  
On peut l'héberger chez soi, le quantifier pour qu'il consomme moins de mémoire, lui appliquer un fine-tuning LoRA et l'utiliser hors ligne.

**En quoi est-ce différent d'une API commerciale ?**  
Une API est une boîte noire externe payante au jeton ; les poids ouverts vous appartiennent et tournent sur vos propres puces.

**Quel équipement faut-il pour faire tourner un modèle 8B ?**  
Un ordinateur équipé de 16 Go de mémoire unifiée ou une carte graphique de 8 à 12 Go de VRAM suffit pour un modèle quantifié en 4 bits.

**L'usage commercial est-il autorisé ?**  
La plupart des modèles phares (Llama, Mistral, Qwen) autorisent l'utilisation commerciale dans les limites de leurs licences respectives.

## Termes liés
- [Open Source AI](/fr/dictionary/open-source-ai/)
- [Foundation Model](/fr/dictionary/foundation-model/)
- [SLM](/fr/dictionary/slm/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/open-weight/
