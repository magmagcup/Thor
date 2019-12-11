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
    
    difficulty = models.CharField(max_length=10)

    question_title = models.CharField(max_length=256,
    verbose_name='Title')
    question_text = models.TextField(verbose_name='Question')



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

    def __str__(self):
        return self.user.username


class UserPicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=10000)


def save_picture(backend, user, response, details,*args,**kwargs):
    if not UserPicture.objects.filter(user=user):
        new_user_pic = UserPicture(user=user, profile_photo=response['picture'])
        new_user_pic.save()

class Best_score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.key
