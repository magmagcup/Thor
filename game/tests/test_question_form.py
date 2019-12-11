from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.forms import QuestionForm

# Create your tests here.

class QuestionFormTest(TestCase):
    def setUp(self):
        self.username = "111"
        self.password = "222"
        self.user = User.objects.create_user(self.username,password=self.password)
        self.form = QuestionForm()
        self.post_form = QuestionForm(
            data={'topic':1,'difficulty':"Easy",'title':"1", 'question':"111"},
            initial={'topic':1}
            )

    def test_form(self):
        client = self.client
        client.force_login(self.user)
        response = client.get(path='/form/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_form_template(self):
        client = self.client
        client.force_login(self.user)
        response_form = client.get(path='/game/form/')
        self.assertTemplateUsed(response_form, 'game/form.html')

    def test_invalid_form(self):
        self.assertFalse(self.form.is_valid())
        self.assertFalse(QuestionForm({'topic':1,}).is_valid())
    
    def test_loading_template_form(self):
        self.assertTrue(self.form)
        self.assertTrue(self.post_form)