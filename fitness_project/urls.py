from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Pour l'administration
    path('', include('training.urls')),  # Inclure les URL de l'application training
]
