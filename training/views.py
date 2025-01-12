from django.shortcuts import render
from .models import TrainingTip

def training_list(request):
    tips = TrainingTip.objects.all()
    return render(request, 'training/training_list.html', {'tips': tips})
