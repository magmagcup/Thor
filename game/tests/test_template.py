from django.test import TestCase, Client
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic, Answer, Best_score
from game.views import *

class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "111"
        self.password = "222"
        self.user = User.objects.create_user(self.username,password=self.password)
    
    def test_homepage(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/game/')
        status = response.status_code
        self.assertEquals(status, 200)