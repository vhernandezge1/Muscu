from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('nutrition/', views.nutrition_list, name='nutrition_list'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),
]

urlpatterns = [
    path('', views.home, name='home'), 
]
