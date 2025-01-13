import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat.consumers import ChatConsumer
from chat.routing import websocket_urlpatterns  # Importez vos routes WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
