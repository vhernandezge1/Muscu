# Musculation - Application de gestion d'entraînements

Ce projet est une application web de gestion de conseils en musculation, incluant une API REST et une messagerie instantanée. L'objectif principal était de mettre en place une solution full stack avec Django en backend.

---

## Fonctionnalités validées

### 1. **Gestion des conseils d'entraînement**
- **Consultation des conseils** : Les utilisateurs peuvent voir une liste de conseils d'entraînement disponibles.
- **API REST pour les conseils** : Endpoint `GET /api/tips/` qui retourne une liste des conseils au format JSON.

### 2. **Messagerie instantanée**
- **API REST pour le chat** : Endpoint `GET /api/chat/` qui retourne les messages récents.

### 3. **Modélisation ORM**
- Deux modèles principaux :
  - `TrainingTip` : Modèle pour les conseils d'entraînement avec les champs `title`, `description`, et `created_by`.
  - `Message` : Modèle pour les messages de chat avec les champs `content` et `timestamp`.

### 4. **Endpoints API REST**
- **Endpoint principal** :
  - `GET /api/` : Retourne un message d'accueil avec les informations sur les autres endpoints disponibles.
- **Endpoints additionnels** :
  - `GET /api/tips/` : Retourne une liste des conseils d'entraînement.
  - `GET /api/chat/` : Retourne une liste des messages récents du chat.

### 5. **Tests unitaires**
- Des tests unitaires ont été rédigés et validés pour :
  - Les endpoints de l'API (`/api/tips/` et `/api/chat/`).
  - La vérification du modèle `TrainingTip`.

### 6. **Gestion des utilisateurs**
- **CustomUser** : Un modèle utilisateur personnalisé avec un champ `role` (élève ou coach).
- **Système de connexion** : Fonctionnalité d'authentification par l'interface admin de Django.

---

## Prérequis

- **Python 3.11 ou version ultérieure**
- **Django 5.1.4**
- **SQLite** (par défaut pour le développement local)

---

## Installation

1. **Cloner le dépôt**
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

---

## Utilisation

### Accès aux pages principales

- **Page d'accueil** : `http://127.0.0.1:8000/`
- **Conseils d'entraînement** : `http://127.0.0.1:8000/training/tips/`
- **Interface admin** : `http://127.0.0.1:8000/admin/`

### Accès à l'API REST

- **Accueil de l'API** : `http://127.0.0.1:8000/api/`
- **Liste des conseils** : `http://127.0.0.1:8000/api/tips/`
- **Messages récents** : `http://127.0.0.1:8000/api/chat/`

---

## Tests

1. **Exécuter les tests**
   ```bash
   python manage.py test
   ```

2. **Couverture des tests**
   - Tests unitaires sur les endpoints API.
   - Tests sur les modèles pour valider les champs et les relations.

---

## Améliorations possibles

1. **Gestion des rôles et accès** : Limiter l'accès à certaines fonctionnalités selon les rôles.
2. **Front-end dynamique** : Ajouter des éléments adaptatifs en fonction du rôle de l'utilisateur connecté.
3. **Mise en production** : Ajouter des configurations pour déployer sur une plateforme cloud.

---

## Auteur

Projet réalisé dans le cadre d'un TP fil rouge.

