from django.db import models

# Create your models here.

class Quotes(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.text} - {self.author}"