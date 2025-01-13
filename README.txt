Musculation Web App



Installation et Prérequis :

Python 3.10+

Django 5.1+

Django Channels

Un environnement virtuel Python (recommandé)



Étapes d'installation

Clonez le projet :

git clone https://github.com/vhernandezge1/Muscu.git
cd musculation-web-app

Créez un environnement virtuel et activez-le :

python -m venv venv
source venv/bin/activate  

# Sur Windows : venv\Scripts\activate

Installez les dépendances :

pip install -r requirements.txt

Appliquez les migrations :

python manage.py makemigrations
python manage.py migrate

Créez un superutilisateur :

python manage.py createsuperuser

Collectez les fichiers statiques :

python manage.py collectstatic

Lancement de l'application

Pour HTTP uniquement :

python manage.py runserver


Pour activer les WebSockets :

Lancez Daphne (nécessaire pour les WebSockets) :

daphne -p 8000 fitness_project.asgi:application


Accédez à l'application dans votre navigateur à l'adresse :

http://127.0.0.1:8000/

Structure du projet

fitness_project/ : Configuration principale de Django.

training/ : Application pour gérer les conseils d'entraînement.

chat/ : Application pour la messagerie instantanée.

templates/ : Contient les fichiers HTML pour l'interface utilisateur.

static/ : Contient les fichiers CSS et JavaScript.


Points importants

Les WebSockets ne fonctionneront correctement qu'avec Daphne ou un autre serveur ASGI.

Configurez votre fichier settings.py pour définir les valeurs appropriées de STATIC_URL et STATIC_ROOT.

Testez l'application en créant des conseils d'entraînement via l'interface d'administration ou en utilisant des données initiales.

Contribution

Les contributions sont les bienvenues !

Forkez le projet

Créez une branche pour votre fonctionnalité :

git checkout -b feature/nouvelle-fonctionnalite

Soumettez une Pull Request

Licence

Ce projet est sous licence MIT. Vous êtes libre de le modifier et de l'utiliser, à condition de mentionner l'auteur original.

Contact

Pour toute question ou problème, contactez-moi à :

Email : valentin.hernandez@ynov.com

GitHub : vhernandezge1

