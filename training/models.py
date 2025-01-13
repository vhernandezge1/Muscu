from django.db import models

class TrainingTip(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", default="Pas de description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return self.title
