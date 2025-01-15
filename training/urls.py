from django.urls import path
from . import api, views

urlpatterns = [
    path('tips/', views.training_tips, name='training_tips'),
    path('api/tips/', api.tips_api, name='tips_api'),
    path('api/tips/<int:pk>/', api.tip_detail_api, name='tip_detail_api'),
    path('register/', views.register, name='register'),
]
