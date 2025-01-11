import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from training.consumers import ChatConsumer
from django.urls import path

# Définir les settings du projet Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')

# Définir les routes pour les WebSockets
websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),  # Route pour le chat WebSocket
]

# Configurer l'application ASGI avec les ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Pour gérer les requêtes HTTP classiques
    "websocket": AuthMiddlewareStack(  # Middleware d'authentification pour les WebSockets
        URLRouter(websocket_urlpatterns)  # Relier les routes WebSocket définies ci-dessus
    ),
})

