# Qu'est-ce que Cloud Computing ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Le cloud computing (informatique en nuage) est la mise à disposition de ressources informatiques telles que des serveurs, du stockage, des bases de données, des réseaux et des logiciels via Internet, à partir de centres de données distants et selon les besoins instantanés (on-demand), en remplacement d'infrastructures physiques locales.

## Définition, origine étymologique et naissance conceptuelle

Le cloud computing est un modèle informatique moderne qui permet aux entreprises et aux ingénieurs de louer en quelques secondes de la puissance de calcul, de la mémoire, de l'espace de stockage et des clusters de GPU d'intelligence artificielle via Internet, au lieu de construire leurs propres salles de serveurs et d'acheter du matériel physique.

Conceptuellement, ses racines remontent à 1961, lors d'un discours de John McCarthy, l'un des pères de l'intelligence artificielle, au MIT. McCarthy avait prédit qu'à l'avenir, la puissance informatique serait fournie comme un service public (utility), tout comme l'électricité et l'eau. L'intégration du mot "cloud" (nuage) dans ce secteur trouve son origine dans les télécommunications et l'ingénierie réseau : dans les années 1990, les architectes systèmes représentaient les centraux téléphoniques complexes et le cœur d'Internet dont ils voulaient masquer les détails par une "icône de nuage" dans leurs schémas. En 2006, avec le lancement par Amazon des services Simple Storage Service (S3) et Elastic Compute Cloud (EC2) à destination des développeurs, le modèle d'achat de serveurs axé sur les dépenses d'investissement (CapEx) a cédé la place au principe du paiement à l'usage (OpEx).

***Analogie :** C'est l'équivalent de se brancher directement sur le réseau électrique national au lieu d'installer une centrale hydroélectrique ou un générateur privé dans son jardin ou sa maison. Dès que vous branchez une prise, l'électricité circule ; peu importe la quantité d'énergie consommée par votre machine, vous ne payez à la fin du mois que cette consommation, sans avoir à vous soucier des pannes du générateur, du carburant ou de la maintenance du transformateur.*

## Modèles de service et de déploiement fondamentaux (IaaS, PaaS, SaaS, Serverless)

L'architecture du cloud computing se divise en quatre principaux modèles de service selon les niveaux d'abstraction :

1. IaaS (Infrastructure as a Service · Infrastructure as a Service) : Il s'agit du niveau le plus bas, composé de machines virtuelles brutes, de disques de stockage par blocs et de topologies de réseau virtuel. AWS EC2, Google Compute Engine et Azure VM appartiennent à cette catégorie. Le fournisseur de cloud gère le matériel et la couche de virtualisation ; le développeur est responsable de l'installation du système d'exploitation, des correctifs de sécurité et de la pile logicielle.
2. PaaS (Platform as a Service · Plateforme en tant que service) : Ce sont des plateformes qui libèrent le développeur des soucis de configuration de serveur, de système d'exploitation et d'environnement d'exécution (runtime). Vercel, Heroku et AWS Elastic Beanstalk en sont des exemples. L'ingénieur envoie uniquement son code source ; la mise à l'échelle, les certificats SSL et l'équilibrage de charge sont pris en charge automatiquement en arrière-plan.
3. SaaS (Software as a Service · Logiciel en tant que service) : logiciels clés en main auxquels l'utilisateur final accède directement via un navigateur Web ou une API, dont la maintenance est entièrement assurée par l'éditeur. Google Workspace, Slack, Salesforce et Figma sont les exemples les plus connus de ce modèle.
4. Serverless (FaaS · Fonction en tant que service) : architecture événementielle qui abstrait totalement le concept de serveur. Le code écrit sur AWS Lambda ou Cloudflare Workers ne s'exécute que lorsqu'une requête HTTP déclenchée ou un événement de base de données survient, fonctionne en millisecondes et s'arrête. Il génère un coût nul en l'absence de trafic.

Les modèles de déploiement sont quant à eux définis en fonction du lieu d'hébergement des données :

- Cloud public : Structure dans laquelle les ressources sont partagées en mode multi-locataire (multi-tenant) dans les centres de données mondiaux des grands fournisseurs.
- Cloud Privé : Environnement isolé exploité par des secteurs réglementés tels que la finance, la défense et la santé dans des centres de données qui leur sont exclusivement dédiés.
- Cloud Hybride (Hibrit Bulut) : Architecture hybride où les données client sensibles sont traitées sur des serveurs locaux dédiés (on-premise), tandis que la couche web, nécessitant un volume de traitement élevé, fonctionne sur le cloud public.
- Multi-cloud : configuration distribuée des systèmes sur AWS, Google Cloud et Azure à la fois afin d'éviter la dépendance à un seul fournisseur (vendor lock-in).

## Informatique et architecture des systèmes : Hyperviseur, conteneur et CAP

Le miracle technique sous-jacent du cloud computing est l'abstraction logicielle du matériel (virtualisation) :

- Couche Hyperviseur : C'est le logiciel de base qui fragmente les ressources processeur et RAM d'un seul serveur physique pour les partager entre des dizaines de machines virtuelles (VM) indépendantes. Les hyperviseurs de Type 1 Bare-metal (KVM, VMware ESXi) qui s'exécutent directement sur le matériel constituent l'épine dorsale des performances des fournisseurs de cloud.
- Conteneurs et orchestration : Pour s'affranchir de la charge liée à la duplication des systèmes d'exploitation des machines virtuelle, les conteneurs Docker ont vu le jour grâce aux fonctionnalités cgroups (limitation des ressources) et namespaces (isolation des processus) du noyau Linux. Quant au déploiement automatisé et à l'auto-réparation (self-healing) de milliers de conteneurs, ils sont assurés par les clusters Kubernetes.
- Théorème CAP et résilience distribuée : les infrastructures cloud mondiales fonctionnent dans les limites du théorème d'Eric Brewer. En cas de partitionnement réseau (Network Partition), un système doit privilégier soit la cohérence des données (Consistency), soit la haute disponibilité (Availability). Les architectes cloud mettent en œuvre des scénarios de reprise après sinistre grâce à des architectures géoredondantes (Multi-Region / Availability Zone).
- Modèle de responsabilité partagée (Shared Responsibility) : la sécurité dans le cloud se divise en deux. Le fournisseur est responsable de la sécurité des centres de données physiques, des serveurs, de l'hyperviseur et des câbles réseau (« Security OF the Cloud »). Le client est quant à lui responsable des mises à jour du système d'exploitation, du chiffrement, des rôles IAM (gestion des accès) et des vulnérabilités du code applicatif (« Security IN the Cloud »).

## Dimension économique, écologique et géopolitique

Le cloud computing n'est pas seulement une révolution technique, c'est aussi une rupture majeure dans l'allocation des ressources mondiales :

- Paradoxe de Jevons : le principe formulé au XIXe siècle par l'économiste William Stanley Jevons concernant la consommation de charbon s'applique également au cloud : à mesure que l'accès à la puissance informatique devient moins cher et plus facile, la consommation totale ne diminue pas, mais augmente au contraire de manière exponentielle. Aujourd'hui, la capacité d'entraîner des modèles d'intelligence artificielle dotés de centaines de milliards de paramètres est le résultat direct des économies d'échelle offertes par le cloud computing.
- Consommation d'énergie et d'eau : Les centres de données hyperscale consomment environ 1 à 2 % de l'électricité mondiale, et des millions de mètres cubes d'eau pure sont utilisés pour refroidir les grappes de GPU géantes. Cette situation a rendu obligatoire l'implantation des centres de données à proximité de sources d'énergie renouvelable et de climats froids.
- Souveraineté numérique et régimes juridiques : l'emplacement physique des données est une question géopolitique. Alors que la loi américaine CLOUD Act autorise les entreprises américaines à intervenir sur leurs serveurs situés à l'étranger, l'Union européenne, par le biais du RGPD et de l'initiative GAIA-X, ainsi que la Turquie, avec la législation KVKK, encouragent le maintien des données critiques à l'intérieur des frontières nationales.

## Souvent confondu avec

- Stockage Cloud vs Cloud Computing : Google Drive, iCloud ou Dropbox sont de simples services de stockage (storage), tandis que le cloud computing est un vaste écosystème qui, en plus du stockage, englobe une puissance de calcul dynamique, l'entraînement d'intelligences artificielles, la gestion de réseau et l'orchestration de bases de données.
- Serverless vs Vraiment Serverless : les serveurs physiques existent bien sûr dans l'architecture serverless ; le terme "sans serveur" indique que le développeur n'a plus à se soucier de configurer, de mettre à jour ou de surveiller un serveur, la gestion des serveurs étant rendue invisible par le fournisseur.

## Questions fréquentes

**Que signifie le cloud computing et quel est son équivalent en turc ?**

En turc, cela correspond à « bulut bilişim » (informatique en nuage). C'est un modèle où la puissance de calcul, les serveurs et les ressources de stockage sont loués à la demande via l'épine dorsale d'internet, au lieu d'utiliser des ordinateurs locaux.

**Quelle est la différence fondamentale entre les 3 principaux modèles de service du cloud computing (IaaS, PaaS, SaaS) ?**

Le IaaS est la location de matériel brut et de serveurs virtuels (AWS EC2), le PaaS est un environnement d'exécution et d'hébergement direct de code (Vercel), et le SaaS est un logiciel clé en main fourni à l'utilisateur final via le web (Google Docs).

**Que signifie le modèle de responsabilité partagée (Shared Responsibility Model) ?**

Il s'agit d'un partage des tâches en matière de sécurité, où le fournisseur de cloud est responsable de la protection de l'infrastructure physique, du centre de données et du matériel, tandis que l'utilisateur est responsable de la sécurité de ses propres applications, des autorisations des utilisateurs (IAM) et du chiffrement des données.

**Comment éviter la dépendance vis-à-vis d'un fournisseur de cloud (Vendor Lock-in) ?**

En utilisant des standards open source (conteneurs Docker, Kubernetes), des moteurs de bases de données indépendants (PostgreSQL) et des outils d'infrastructure en tant que code (Terraform / OpenTofu), les logiciels sont isolés des API propriétaires spécifiques à un fournisseur.

## Termes liés

- [SaaS](https://trescout.com/fr/dictionary/saas/)
- [PaaS](https://trescout.com/fr/dictionary/paas/)
- [IaaS](https://trescout.com/fr/dictionary/iaas/)
- [Personal Cloud](https://trescout.com/fr/dictionary/personal-cloud/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Network Stack](https://trescout.com/fr/dictionary/network-stack/)
- [Memory Management](https://trescout.com/fr/dictionary/memory-management/)

## Outils liés

- [DevOps-Interview-Guide](https://trescout.com/fr/discover/devops-interview-guide/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/cloud-computing/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/cloud-computing/
