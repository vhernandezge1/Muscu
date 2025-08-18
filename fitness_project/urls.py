from django.contrib import admin
from django.urls import path
from training import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("exercices/", views.exercise_list, name="exercices"),
    path("nutrition/", views.nutrition_list, name="nutrition"),
    path("test-error/", views.test_error, name="test_error"),
]
