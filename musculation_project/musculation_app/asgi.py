import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from musculation_app import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musculation_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # Gère les connexions WebSocket
        URLRouter({
            path("ws/musculation/", consumers.MusculationConsumer.as_asgi()),  # Route WebSocket
        })
    ),
})
