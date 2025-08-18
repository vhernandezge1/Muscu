from django.urls import path
from . import views
from .views import tips_api, chat_api

urlpatterns = [
    path('', views.api_home, name='api_home'),  
    path('tips/', tips_api, name='api_tips'),  
    path('chat/', chat_api, name='api_chat'),  
]
