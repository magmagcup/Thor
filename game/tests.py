from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User, AnonymousUser
from .models import Question, Answer, Topic
from .forms import QuestionForm

# Create your tests here.

class FormTest(TestCase):
    def setUp(self):
        self.question = "Binary Search: Search a sorted array by [[repeatedly|Do again and again <adv>)]]"
        self.title = "Binary Search"
        self.answer = "repeatedly"
        self.hint = "Do again and again <adv>"
        self.difficulty = "easy"
        self.topic = "Algorithm"
        self.form = QuestionForm()
        self.form_data = {
                            'select_topic':self.topic, 
                            'select_difficulty':self.difficulty, 
                            'title':self.title, 
                            'question':self.question
                        }
        self.post_form = QuestionForm(self.form_data)
    
    def test_form(self):
        client = self.client
        response = client.get(path='/form/')
        status = response.status_code
        self.assertEqual(status, 200)
    
    def test_form_template(self):
        client = self.client
        response_form = client.get(path='/game/form/')
        self.assertTemplateUsed(response_form, 'game/form.html')
    
    def test_valid_form(self):
        self.assertTrue(self.post_form.is_valid())

    
    def test_invalid_form(self):
        self.assertTrue(self.post_form.is_valid())
        self.assertFalse(self.form.is_valid())