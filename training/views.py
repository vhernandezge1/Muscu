<<<<<<< HEAD
from django.shortcuts import render
from .models import Exercise, NutritionTip

def home(request):
    return render(request, 'training/index.html')

def exercise_list(request):
    exercises = Exercise.objects.order_by('category', 'name')
    return render(request, 'training/exercise_list.html', {'exercises': exercises})

def nutrition_list(request):
    tips = NutritionTip.objects.order_by('category', '-created_at')
    return render(request, 'training/nutrition_list.html', {'tips': tips})
=======
from django.shortcuts import render , redirect
from .models import TrainingTip
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'training/register.html', {'form': form})

def is_coach(user):
    return user.role == 'coach'

@login_required
@user_passes_test(is_coach)
def coach_only_view(request):
    # Vue réservée aux coachs
    return render(request, 'training/coach_view.html')
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
