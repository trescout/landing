# Planification des ressources de l'entreprise open source

Odoo est une plateforme open source de planification des ressources de l'entreprise qui permet aux entreprises de gérer tous leurs processus opérationnels sous un même toit. Développé avec le langage Python, ce système offre une large gamme d'applications métiers modulaires allant de la vente à la comptabilité.

- ★ 52 082
- GitHub Trending · 2026-06-04

## Ce que ça vous apporte
- Il gère les processus commerciaux tels que les ventes, la comptabilité et l'entrepôt à partir d'un centre unique.
- Il propose des applications métiers modulaires et compatibles entre elles.
- Il fournit une infrastructure open source qui peut être personnalisée en fonction des besoins.

## Installation
****

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

****

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```


## Exécution
****

```
http://localhost:8069
```


## Pour commencer
- Source officielle →

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/odoo/
