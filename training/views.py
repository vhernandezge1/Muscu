from django.shortcuts import render
from .models import TrainingTip

def training_home(request):
    """
    Vue pour la page d'accueil de l'application Training.
    Accessible via : /training/
    """
    return render(request, 'training/home.html')

def training_tips(request):
    """
    Vue pour afficher la liste des conseils d'entraînement.
    Accessible via : /training/tips/
    """
    tips = TrainingTip.objects.all()  # Récupère tous les conseils dans la base de données
    return render(request, 'training/tips.html', {'tips': tips})
