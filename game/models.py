import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'game_topic'

    def __str__(self):
        return self.topic_name

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    question_title = models.CharField(max_length=1000000)
    question_text = models.CharField(max_length=10000000)

    difficulty = models.CharField(max_length=10)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    hint_text = models.CharField(max_length=1000000)

    def __str__(self):
        return self.answer_text

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    best_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
