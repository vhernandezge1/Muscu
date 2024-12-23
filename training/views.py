from django.shortcuts import render
from .models import Exercise
from .models import NutritionTip

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'training/exercise_list.html', {'exercises': exercises})


def nutrition_list(request):
    tips = NutritionTip.objects.all()
    return render(request, 'training/nutrition_list.html', {'tips': tips})

def home(request):
    return render(request, 'index.html')  # Rendu du template 'index.html'
