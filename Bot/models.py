from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

class UnansweredQuestion(models.Model):
    question = models.TextField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)