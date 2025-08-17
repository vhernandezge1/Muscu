import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
<<<<<<< HEAD
from training.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')

django_asgi_app = get_asgi_application()
=======
from chat.consumers import ChatConsumer
from chat.routing import websocket_urlpatterns 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
<<<<<<< HEAD
        URLRouter([
            path("ws/chat/", ChatConsumer.as_asgi()),
        ])
=======
        URLRouter(websocket_urlpatterns)
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
    ),
})
