from django.shortcuts import render
from django.http import HttpResponse

# Vue pour la page d'accueil de l'application Nutrition
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de Nutrition !")

# Vue pour afficher tous les conseils nutritionnels
def nutrition_tips(request):
    # Exemple : liste de conseils statiques
    tips = [
        "Mangez des protéines à chaque repas.",
        "Buvez au moins 2 litres d'eau par jour.",
        "Évitez les aliments transformés."
    ]
    # Rendu dans un template HTML
    return render(request, 'nutrition/nutrition_tips.html', {'tips': tips})

# Vue pour afficher les détails d’un conseil spécifique
def tip_detail(request, tip_id):
    # Exemple : conseils statiques pour simuler un détail
    tips = {
        1: "Les protéines sont essentielles pour la croissance musculaire.",
        2: "L'eau améliore la récupération et les performances.",
        3: "Les aliments transformés contiennent souvent des sucres et des graisses cachées."
    }
    tip = tips.get(tip_id, "Conseil non trouvé.")  # Message si l'ID n'existe pas
    return render(request, 'nutrition/tip_detail.html', {'tip_id': tip_id, 'tip': tip})

# Vue pour ajouter un nouveau conseil nutritionnel
def add_tip(request):
    if request.method == 'POST':
        # Simuler la réception des données d'un formulaire
        new_tip = request.POST.get('tip', 'Aucun conseil soumis.')
        return HttpResponse(f"Nouveau conseil ajouté : {new_tip}")
    # Si la méthode n'est pas POST, afficher un formulaire fictif
    return render(request, 'nutrition/add_tip.html')
