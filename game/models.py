from django.db import models
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=10000000)