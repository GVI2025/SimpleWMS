# Groupe X – Scan de sécurité automatisé (Bandit)

## Objectif
Intégrer un outil de détection de failles de sécurité dans le projet Python en utilisant **Bandit**, et rendre l’analyse automatique via GitHub Actions.

## Travail attendu

### 1. Mise en place locale
- Installer Bandit via pip ou poetry
- Lancer une analyse de sécurité sur le projet :
  ```bash
  bandit -r app/
  ```
- Corriger les problèmes de sécurité identifiés (si justifié)

### 2. Intégration dans la CI
- Ajouter une **GitHub Action** qui lance automatiquement Bandit à chaque push / pull request
- La CI doit échouer si des vulnérabilités critiques sont détectées

### 3. Présentation attendue
- Démonstration d’une analyse Bandit
- Exemple de fail dans la CI sur une faille simple (ex: `subprocess`)
- Explication de la correction

---

**Livrables :**
- GitHub Action fonctionnelle
- Corrections effectuées
- Capture ou démonstration de cas d’erreur + correctif
