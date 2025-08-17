from django.contrib.auth.models import AbstractUser
from django.db import models

<<<<<<< HEAD
class Exercise(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Facile'),
        ('medium', 'Moyenne'),
        ('hard', 'Difficile'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
=======
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('coach', 'Coach'),
        ('student', 'Élève'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


<<<<<<< HEAD
class NutritionTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
=======
class TrainingTip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='training_tips',
        limit_choices_to={'role': 'coach'},
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Ajout du champ
>>>>>>> 22d47467b6b2bad1ca72695fa94076d6d096d5c1

    def __str__(self):
        return self.title

