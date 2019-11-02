from django.db import models
# Create your models here.

class Question(models.Model):
    question_title = models.CharField(max_length=1000000)
    question_text = models.CharField(max_length=10000000)
    question_answer = models.CharField(max_length=1000000)
    answer_hint = models.CharField(max_length=1000000)

    def __str__(self):
        return self.question_title
