from django.test import TestCase, Client
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic, Answer, Best_score, Statistic
from game.views import *

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "111"
        self.password = "222"
        self.user = User.objects.create_user(self.username,password=self.password)
        self.check = Statistic.objects.filter(user=self.user.id)
        self.status = True
    
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

