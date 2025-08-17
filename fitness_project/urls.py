from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),  # routes de l'app
=======
from . import views  # Import de la vue home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('training/', include('training.urls')),
    path('chat/', include('chat.urls')),
     path('api/', include('api.urls')),  # Routes pour l'API
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
]
