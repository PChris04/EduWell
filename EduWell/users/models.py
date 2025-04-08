from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    due_date = models.DateField()

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ('😞', 'Stressed'),
        ('😐', 'Neutral'),
        ('😊', 'Happy')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=2, choices=MOOD_CHOICES)
    date = models.DateField(auto_now_add=True)
    journal = models.TextField(blank=True)
