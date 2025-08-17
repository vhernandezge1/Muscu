from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercices/', views.exercise_list, name='exercices'),
    path('nutrition/', views.nutrition_list, name='nutrition'),
=======
from . import api, views

urlpatterns = [
    path('tips/', views.training_tips, name='training_tips'),
    path('api/tips/', api.tips_api, name='tips_api'),
    path('api/tips/<int:pk>/', api.tip_detail_api, name='tip_detail_api'),
    path('register/', views.register, name='register'),
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
]
