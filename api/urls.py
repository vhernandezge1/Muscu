from django.urls import path
from . import views
from .views import tips_api, chat_api

urlpatterns = [
    path('', views.api_home, name='api_home'),  # Endpoint de base pour l'API
    path('tips/', tips_api, name='api_tips'),  # Endpoint pour les conseils
    path('chat/', chat_api, name='api_chat'),  # Endpoint pour le chat
]
