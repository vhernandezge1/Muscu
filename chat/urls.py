from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat_index'),  # Page principale du chat
    path('send_message/', views.send_message, name='send_message'),  # Endpoint pour envoyer un message
]
