from django.urls import path
from . import views

# Définition des URL de l'application 'nutrition'
urlpatterns = [
    # Page d'accueil de l'application Nutrition
    path('', views.home, name='nutrition_home'),

    # Exemple : page pour afficher les conseils nutritionnels
    path('tips/', views.nutrition_tips, name='nutrition_tips'),

    # Exemple : page pour un conseil spécifique (avec un ID dynamique)
    path('tips/<int:tip_id>/', views.tip_detail, name='tip_detail'),

    # Exemple : page pour ajouter un nouveau conseil
    path('tips/add/', views.add_tip, name='add_tip'),
]
