from django.contrib import admin
from django.urls import path, include
from training import views

urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list'),  # Liste des exercices
    path('nutrition/', views.nutrition_list, name='nutrition_list'),  # Liste des conseils de nutrition
    path('', views.home, name='home'),  # Page d'accueil
]
