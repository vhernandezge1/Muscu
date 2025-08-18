from django.shortcuts import render

def home(request):
    """
    Vue pour la page d'accueil du projet principal.
    """
    return render(request, 'home.html')



