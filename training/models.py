from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)  # Exemple: "Musculation", "Cardio", etc.
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Facile'), ('medium', 'Moyenne'), ('hard', 'Difficile')])

    def __str__(self):
        return self.name

class NutritionTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
