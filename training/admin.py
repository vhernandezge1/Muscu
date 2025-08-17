from django.contrib import admin
<<<<<<< HEAD
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
=======
from .models import TrainingTip, CustomUser

@admin.register(TrainingTip)
class TrainingTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by')  
    list_filter = ('created_by',)
    search_fields = ('title', 'description')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email')
    list_filter = ('role',)
    search_fields = ('username', 'email')
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1
