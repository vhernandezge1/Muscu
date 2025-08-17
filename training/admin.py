from django.contrib import admin
from .models import Exercise, NutritionTip

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "difficulty", "created_at")
    list_filter = ("category", "difficulty")
    search_fields = ("name", "description", "category")

@admin.register(NutritionTip)
class NutritionTipAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "content", "category")
