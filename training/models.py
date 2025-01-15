from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('coach', 'Coach'),
        ('student', 'Élève'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


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

    def __str__(self):
        return self.title

