from django.contrib import admin
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
