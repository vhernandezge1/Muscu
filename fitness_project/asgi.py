import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from training.consumers import ChatConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # Nous allons ajouter ici les routes pour les WebSockets
        )
    ),
})
