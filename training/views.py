from django.shortcuts import render
from .models import Exercise, NutritionTip

def home(request):
    return render(request, "training/index.html")

def exercise_list(request):
    exercises = Exercise.objects.all().order_by("-created_at")
    return render(request, "training/exercise_list.html", {"exercises": exercises})

def nutrition_list(request):
    tips = NutritionTip.objects.all().order_by("-created_at")
    return render(request, "training/nutrition_list.html", {"tips": tips})
