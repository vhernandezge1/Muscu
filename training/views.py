from django.shortcuts import render
from .models import Exercise, NutritionTip
from django.http import HttpResponse

def home(request):
    return render(request, "training/index.html")

def exercise_list(request):
    exercises = Exercise.objects.all().order_by("-created_at")
    return render(request, "training/exercise_list.html", {"exercises": exercises})

def nutrition_list(request):
    tips = NutritionTip.objects.all().order_by("-created_at")
    return render(request, "training/nutrition_list.html", {"tips": tips})



def test_error(request):
    1 / 0  # division par zéro => erreur 500
    return HttpResponse("Ceci ne s'affichera jamais")
