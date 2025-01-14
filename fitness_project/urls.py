from django.contrib import admin
from django.urls import path, include
from . import views  # Import de la vue home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('training/', include('training.urls')),
    path('chat/', include('chat.urls')),
     path('api/', include('api.urls')),  # Routes pour l'API
]
