from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),  # Route pour /chat/
    path('<str:room_name>/', views.room, name='room'),  # Route pour /chat/<room_name>/
]
