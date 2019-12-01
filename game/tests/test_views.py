from django.test import TestCase, Client
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic, Answer, Best_score, Statistic
from game.views import *

def discard_form(question_id):
    """Discard the Question Form."""
    check = Question.objects.filter(pk=question_id)
    if check:
        question = Question.objects.get(pk=question_id)
        question.delete()
        return True
    return False

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "111"
        self.password = "222"
        self.user = User.objects.create_user(self.username,password=self.password)
        self.check = Statistic.objects.filter(user=self.user.id)
        self.status = True
        self.topic = Topic.objects.create(topic_name="Topic")
        self.question = Question.objects.create(topic=self.topic, question_title='Hello', question_text="world", difficulty="Easy")
    
    def test_get_stat(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/stat/', follow=True)
        status = response.status_code
        self.assertEquals(status, 200)

        stat = Statistic.objects.create(user=self.user)
        self.assertTrue(self.check)

        if self.check:
            self.status = False
            self.assertFalse(self.status)

        self.assertEqual(stat.user.username, self.username)
        self.assertTrue(stat.user.password)
        self.assertTemplateUsed(response, 'game/base.html')
    
    def test_discard_form(self):
        get_question = Question.objects.get(pk=self.question.id)
        self.client.force_login(self.user)
        response = self.client.get(path=f'{get_question.id}', follow=True)
        status = response.status_code
        self.assertEquals(status, 200)

        self.assertTrue(get_question)
        delete = discard_form(get_question.id)
        self.assertTrue(delete)
        none_question = discard_form(get_question.id)
        self.assertFalse(none_question)
