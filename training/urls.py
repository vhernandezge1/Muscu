from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_home, name='training_home'),  # Route pour /training/
    path('tips/', views.training_tips, name='training_tips'),  # Route pour /training/tips/
]
