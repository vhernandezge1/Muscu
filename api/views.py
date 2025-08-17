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

def tips_api(request):
    tips = [
        {"id": 1, "title": "Hydratez-vous régulièrement", "description": "Buvez au moins 2 litres d'eau par jour."},
        {"id": 2, "title": "Variez vos exercices", "description": "Travaillez différents groupes musculaires pour un développement équilibré."},
    ]
    return JsonResponse(tips, safe=False)

def chat_api(request):
    messages = [
        {"id": 1, "user": "Coach1", "message": "Bienvenue sur le chat de musculation !"},
        {"id": 2, "user": "Élève1", "message": "Merci ! J'ai une question sur les séries d'exercices."},
    ]
    return JsonResponse(messages, safe=False)