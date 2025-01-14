from django.http import JsonResponse

def api_home(request):
    data = {
        "message": "Bienvenue sur l'API de Musculation !",
        "endpoints": {
            "GET /api/tips/": "Liste des conseils d'entraînement",
            "GET /api/chat/": "Messages récents du chat",
        },
    }
    return JsonResponse(data)
