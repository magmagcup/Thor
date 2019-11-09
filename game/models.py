import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from social_django import models as oauth_model_user

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class Question(models.Model):
    question_title = models.CharField(max_length=1000000)
    question_text = models.CharField(max_length=10000000)
    question_answer = models.CharField(max_length=1000000)
    answer_hint = models.CharField(max_length=1000000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.question_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    best_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
