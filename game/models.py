import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from collections import OrderedDict
from dictionaryfield import DictionaryField
from picklefield.fields import PickledObjectField
# from social_django import models as oauth_model_user

# Create your models here.

class Question(models.Model):
    question_title = models.CharField(max_length=1000000)
    question_text = models.CharField(max_length=10000000)
    question_answer = models.CharField(max_length=1000000)
    answer_hint = models.CharField(max_length=1000000)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.question_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Best_score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return  self.key

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __add__(self, num):
        return self.score + num

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name
