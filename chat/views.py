from django.shortcuts import render

def chat_home(request):
    """
    Vue pour la page d'accueil de la messagerie.
    """
    return render(request, 'chat/home.html')

def room(request, room_name):
    """
    Vue pour afficher une salle de chat spécifique.
    """
    return render(request, 'chat/room.html', {'room_name': room_name})
