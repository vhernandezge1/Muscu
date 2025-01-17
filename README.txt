Musculation - Application de gestion d'entraînements
Ce projet est une application web de gestion de conseils en musculation, incluant une API REST et une messagerie instantanée. 
L'objectif principal était de mettre en place une solution full stack avec Django en backend.


Prérequis
Python 3.11 ou version ultérieure
Django 5.1.4
Docker et Docker Compose (pour exécuter l'application dans un conteneur)
Installation


Créer un environnement virtuel:
python -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate

Installer les dépendances:
pip install -r requirements.txt

Appliquer les migrations:
python manage.py makemigrations
python manage.py migrate

Lancer le serveur:
python manage.py runserver
Avec Docker Compose

Cloner le dépôt:
git clone https://github.com/vhernandezge1/Muscu
cd <NOM_DU_DOSSIER>

Construire et démarrer les conteneurs:
docker-compose up --build

Accéder à l'application:
Application : http://localhost:8000
Admin Django : http://localhost:8000/admin/

Appliquer les migrations:
docker-compose exec web python manage.py migrate

Créer un superutilisateur:
docker-compose exec web python manage.py createsuperuser

Utilisation:
Accès aux pages principales
Page d'accueil : http://127.0.0.1:8000/
Conseils d'entraînement : http://127.0.0.1:8000/training/tips/
Interface admin : http://127.0.0.1:8000/admin/
Accès à l'API REST
Accueil de l'API : http://127.0.0.1:8000/api/
Liste des conseils : http://127.0.0.1:8000/api/tips/
Messages récents : http://127.0.0.1:8000/api/chat/

Exécuter les tests :
python manage.py test

Projet réalisé dans le cadre d'un TP fil rouge par Valentin Hernandez.