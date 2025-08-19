( Etant donné que j'ai oublié d'envoyer le ppt du 1er oral je le mets dans le dossier au cas où)

IMuscu est une application web développée avec Django 

Backend : Django 5, Django Channels
Frontend : HTML, CSS, JavaScript (dans les templates Django)
Base de données : SQLite
Serveur ASGI : Daphne (pour WebSockets)
Versionnement : Git & GitHub



Installation et exécution

1. Cloner le projet
git clone https://github.com/vhernandezge1/Muscu.git
cd Muscu/fitness_project


2.Créer et activer un environnement virtuel
python -m venv .venv

Pour  Windows (PowerShell)
.\.venv\Scripts\Activate

Pour Linux/Mac
source .venv/bin/activate


3. Installer les dépendances
pip install -r requirements.txt
pip install "django>=5.0,<6.0" channels daphne



4. Appliquer les migrations et insérer des données de démo
python manage.py migrate
python manage.py seed_demo



5. Lancer le serveur avec Daphne (pour WebSockets)
daphne -p 8000 fitness_project.asgi:application
    