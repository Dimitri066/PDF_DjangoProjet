# PDF_DjangoProjet

Ce projet est un projet de rattrapage PRO3600 à TelecomSudParis.
Il a pour but de créer un site avec Django qui permet de génerer des PDF à partir de templates personnalisés que l'admin fournira.

## Présentation
Cette application permet donc selon les consignes fourni de :

- Proposer à l'utilisateur la liste des templates disponibles
- Permettre à l'utilisateur de fournir les valeurs nécessaires dans un formulaire bootstrap (crispy forms)
- Une fois le formulaire rempli, générer le document demandé et le donner à l'utilisateur
- Proposer une interface d'administration à l'administrateur pour la création de templates
- Quelques tests unitaires sur la fonction qui génère un formulaire à partir des données contenues en base de données:
---
## Prérequis
- Python 3.12 ou plus

En termes de paquets python :
- Django
- Django Crispy Forms et crispy-bootstrap5 pour la génération de formulaires à partir de la classe Form de django
- Weasyprint pour la génération de fichiers PDFs à partir d'un template HTML
- django_extensions pour la génération des graphiques UML (documentation)

Pour les pages web :
- Bootstrap 5
---
## Utilisation du projet :

- Installer Python et les dépendances 
- Cloner le projet sur votre machine
- Creer un super utilisateur
- Lancer le serveur Django  
- Accéder à l'interface admin pour créer un template à l'aide d'un code HTML et de JSON.
- Choisir un template sur la page d'acceuil.
- Remplir le formulaire et recevoir automatiquement le PDF via votre navigateur.

## Exemple de Template simple
A copier dans les champs correspondant dans l'interface TemplateAdmin.
### CodeHTML:
```
<h1>Attestation de présence</h1>
<p>Je soussigné : <b>{nom_etudiant}</b></p>
<p>Certifie avoir été présent le : <b>{date}</b></p>
<p>Signature : ____________________________</p>`
```
### JSON
{"nom_etudiant": {"type": "str", "label": "Nom etudiant"},
  "date": {"type": "str", "label": "Date présence"} }
---
## Remarques :

- Le diagramme UML est disponible dans le dépôt sous le nom : Diagramme_UML.pdf
- Les tests unitaires portent uniquement sur la fonction generer_formulaire et n'ont généré aucune erreur.
- Tous les types de champs en JSON ne sont pas géré par le code par défaut c'est CharField.
---
## Notes d'ameliorations :

- Ajouter d’autres templates plus complexes.
- Gérer tous types de champs dans la fonction qui permet de générer des formulaires.
- Ajouter des tests unitaires sur toutes les fonctions et dans plus de cas.
- Améliorer l'interface graphique admin et utilisateur.
---
## Transparence de l'IA:
L'IA générative a été utilisée pour trouver, comprendre et tester différentes fonctions python.
De plus, elle a permi de générer du code HTML dont les squelettes des pages.
Tout ce qui a été généré par IA a été relu, adapté et modifié du mieux possible.
---

> Projet réalisé par Dimitri DYKIER élève de 2A à Telecom SudPAris
