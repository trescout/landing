# Planification des ressources de l'entreprise open source

Odoo est une plateforme open source de planification des ressources de l'entreprise qui permet aux entreprises de gérer tous leurs processus opérationnels sous un même toit. Développé avec le langage Python, ce système offre une large gamme d'applications métiers modulaires allant de la vente à la comptabilité.

- ★ 54 692
- GitHub Trending · 2026-06-04

## Mises à jour

- **27 septembre 2026:** Étoiles 52,082 → 54,692.

## Ce que ça vous apporte

- Il gère les processus commerciaux tels que les ventes, la comptabilité et l'entrepôt à partir d'un centre unique.
- Il propose des applications métiers modulaires et compatibles entre elles.
- Il fournit une infrastructure open source qui peut être personnalisée en fonction des besoins.

## Installation

**Démarrer la base de données PostgreSQL**

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

**Démarrer Odoo connecté à la base de données**

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```

## Exécution

**Accéder à l'interface locale**

```
http://localhost:8069
```

## Pour commencer

- Source officielle →

## Termes liés du glossaire

- [Enterprise Resource Planning](https://trescout.com/fr/dictionary/enterprise-resource-planning/)

- **Pour qui:** Il convient aux entreprises qui souhaitent gérer tous leurs processus opérationnels sur une seule plateforme.

## Liens

- [Dépôt GitHub →](https://www.odoo.com)
- [Lire en turc →](https://trescout.com/discover/odoo/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-04 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/odoo/
