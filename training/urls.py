from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercices/', views.exercise_list, name='exercices'),
    path('nutrition/', views.nutrition_list, name='nutrition'),
]
