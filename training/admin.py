from django.contrib import admin
from .models import TrainingTip

@admin.register(TrainingTip)
class TrainingTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
