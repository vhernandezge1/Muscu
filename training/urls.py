from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_list, name='training_list'),
]
