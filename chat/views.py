from django.shortcuts import render
from django.http import JsonResponse

# Vue pour la page principale du chat
def index(request):
    return render(request, 'chat/index.html')

# Vue pour envoyer un message
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        # Tu peux ajouter ici une logique pour sauvegarder le message dans la base de données.
        return JsonResponse({'status': 'Message received', 'message': message})
    return JsonResponse({'error': 'Invalid request'}, status=400)
