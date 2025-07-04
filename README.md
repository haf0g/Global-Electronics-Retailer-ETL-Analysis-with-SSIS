# Projet Business Intelligence - Global Electronics Retailer

## Contexte
Ce projet a été réalisé dans le cadre d'un module de Business Intelligence à l'ENSA en mai 2025. Il simule la mise en place d'un système décisionnel pour un détaillant mondial de produits électroniques, utilisant des technologies Microsoft (SQL Server, SSIS, Power BI) pour analyser les performances commerciales.

## Objectifs
- Concevoir un entrepôt de données avec un schéma en étoile.
- Développer un processus ETL avec SSIS pour intégrer des sources hétérogènes (CSV, Excel, JSON, SQL).
- Créer des tableaux de bord interactifs et automatisés avec Power BI.

## Architecture
- **Entrepôt de données** : `GlobalRetailerDWH` avec les tables :
  - Fait : `FactSales`
  - Dimensions : `DimCustomer`, `DimStore`, `DimProduct`, `DimDate`
- **Sources** : Fichiers CSV (ventes), Excel (produits), JSON (taux de change), et base SQL (clients/magasins).

![image](https://github.com/user-attachments/assets/3f7ce3a9-c3f6-4348-b53a-7187c3497e39)

## Conception du Data Warehouse
![image](https://github.com/user-attachments/assets/6882610c-e966-438c-a824-05bf8e5e8497)

## Processus ETL (SSIS)
1. **Extraction** : Téléchargement des taux de change via API, lecture des fichiers CSV/Excel/SQL.
2. **Transformation** : Calculs (`TotalSales`), conversions de données, gestion des valeurs manquantes.
3. **Chargement** : Insertion dans les tables de dimensions et de faits.

## Tableaux de bord Power BI
- **KPIs** : Chiffre d'affaires (2,42 milliards USD), nombre de commandes (26 000).
- **Visualisations** :
  - Évolution MoM des ventes.
  - Répartition par catégorie de produits.
  - Analyse hiérarchique (pays, sous-catégories).
  - Top 5 des produits performants.

  ### Dashboard développé :
![image](https://github.com/user-attachments/assets/8244326e-0ab4-4f75-8fbd-5a26eec77939)

## Automatisation
- Exécution quotidienne via SQL Server Agent.
- Vidage des tables de staging avant chaque chargement.

## Livrables
- Modèles conceptuel et physique de l'entrepôt.
- Packages SSIS et rapports Power BI (.pbix).
- Documentation complète (PDF).

## Auteur
- **Hafid GARHOUM**

---

*Ce projet illustre la maîtrise des outils BI pour la consolidation et l'analyse de données commerciales.*
