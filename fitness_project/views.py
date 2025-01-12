from django.shortcuts import render

def home(request):
    # Rendu du template 'home.html'
    return render(request, 'home.html')
    