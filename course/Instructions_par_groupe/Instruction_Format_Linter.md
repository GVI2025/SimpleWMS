# Groupe X – Formatage du code, Linter et Normes

## Objectif
Mettre en place un formattage automatique du code Python, l’analyse syntaxique via un linter, et faire respecter une norme de style dans le cadre du projet de réservation.

## Travail attendu

### 1. Mise en place locale
- Choisir et configurer les outils suivants :
  - **Black** pour le formattage
  - **isort** pour le tri des imports
  - **Flake8** ou **Ruff** pour la vérification des normes PEP8
- Formater l’intégralité du code du projet

### 2. Intégration dans la CI
- Ajouter une **GitHub Action** dans `.github/workflows/` qui vérifie automatiquement le formatage et le lint à chaque push et pull request
- La CI doit échouer si le code n’est pas conforme

### 3. Présentation attendue
- Expliquer brièvement les rôles de Black, isort et Flake8/Ruff
- Montrer la CI et une pull request refusée à cause d’erreurs de style
- Montrer le diff Git d’un formattage automatique

---

**Livrables :**
- CI fonctionnelle
- Code formaté
- Capture ou démonstration prête pour la présentation