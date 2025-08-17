from rest_framework import serializers
from .models import TrainingTip

class TrainingTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTip
        fields = ['id', 'title', 'description']
