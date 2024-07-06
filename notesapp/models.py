from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title