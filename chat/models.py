from django.db import models

class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
