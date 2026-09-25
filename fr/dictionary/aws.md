# Qu'est-ce qu' AWS ?

> Amazon Web Services

**Catégorie:** Dev  
**Dernière mise à jour:** 2026-09-22

AWS (Amazon Web Services) est la plateforme cloud d'Amazon fournissant à la demande des serveurs virtuels, du stockage, des bases de données et des infrastructures complètes sur Internet.

## Définition et étymologie
Plutôt que d'acheter et maintenir des serveurs physiques dans une salle informatique, les entreprises louent la puissance de calcul des centres de données d'Amazon. La capacité s'ajuste instantanément au trafic selon un modèle de paiement à l'usage. AWS constitue le socle technologique de la majorité des applications web contemporaines.

## Usage quotidien et contexte pratique
- **Sites web et applications mobiles :** Serveurs à mise à l'échelle automatique absorbant les pics de trafic.
- **Sauvegardes et archivage :** Stockage immuable et hautement disponible pour la conformité et la sécurité.
- **Diffusion vidéo :** Réseaux de diffusion de contenu (CDN) distribuant des médias à faible latence.
- **Startups :** Lancement instantané de produits sans investissement en matériel informatique.

## Profondeur technique et architecture
Services piliers d'AWS :- **EC2 :** Serveurs virtuels configurables à la demande.
- **S3 :** Stockage objet hautement résilient pour sauvegardes et fichiers statiques.
- **RDS :** Bases de données relationnelles entièrement gérées (Postgres, MySQL).
- **Lambda :** Exécution de code serverless déclenchée par des événements.

L'infrastructure s'articule autour de régions géographiques et de zones de disponibilité (AZ) indépendantes. Le modèle de responsabilité partagée stipule qu'Amazon sécurise le cloud, tandis que le client sécurise ses données et ses configurations.<div class="disc-cmd"><div class="disc-cmd-head"><span>Lister les instances EC2 actives via AWS CLI</span></div><pre><code>aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"</code></pre></div>

## Souvent confondu avec
Souvent confondu avec un simple hébergeur web. Un hébergeur traditionnel se contente de stocker des fichiers de site ; AWS offre plus de 200 services managés incluant intelligence artificielle, routage réseau mondial et conteneurs.

## Perspectives interdisciplinaires
- **Réseau électrique :** Se brancher sur une prise murale plutôt que construire sa propre centrale.
- **Entrepôt de stockage :** Louer un box selon le volume d'affaires sans acheter de hangar.
- **Taxi :** Se déplacer à la demande sans devoir financer l'achat d'un véhicule.

## Par analogie
C'est comme acheter de l'électricité au réseau public plutôt que de construire sa propre centrale : vous branchez vos appareils et ne payez que les kilowatts consommés.

## Questions fréquentes

**Pourquoi migrer vers AWS ?**  
Pour éliminer les investissements matériels lourds, déployer à l'international en quelques clics et adapter ses coûts au trafic réel.

**Est-il possible de démarrer gratuitement ?**  
Oui. L'offre AWS Free Tier propose des quotas gratuits pendant 12 mois pour découvrir les services de base sans facturation immédiate.

**Où sont stockées les données des utilisateurs ?**  
Elles demeurent exclusivement dans la région géographique choisie par l'administrateur, garantissant la conformité avec le RGPD.

**Comment maîtriser ses dépenses cloud ?**  
En configurant des alertes de budget AWS, en activant le balisage des ressources et en supprimant régulièrement les volumes de stockage inutilisés.

## Termes liés
- [Cloud Computing](/fr/dictionary/cloud-computing/)
- [IaaS](/fr/dictionary/iaas/)
- [PaaS](/fr/dictionary/paas/)

---
Source : Dictionnaire technique TreScout · https://trescout.com/fr/dictionary/aws/
