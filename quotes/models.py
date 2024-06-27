from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.text} - {self.author}"

class DailyQuote(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    day_of_year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"{self.quote} - Day {self.day_of_year}"