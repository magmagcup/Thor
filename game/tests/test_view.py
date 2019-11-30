from django.test import TestCase, Client
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic, Answer, Best_score
from game.views import *

class HomepageViewTest(TestCase):
    def setUp(self):
        self.user = Client()