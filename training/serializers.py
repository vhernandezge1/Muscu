from rest_framework import serializers
from .models import TrainingTip

class TrainingTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTip
        fields = '__all__'  # Inclut tous les champs du modèle TrainingTip
