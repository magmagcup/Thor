from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.forms import AnswerForm

# Create your tests here.

class AnswerFormTest(TestCase):
    def setUp(self):
        self.answer = "repeatedly"
        self.answer_length = len(self.answer) 
        self.hint = "Do again and again <adv>"
        self.blank_form = AnswerForm(ans_length=self.answer_length,
                                     box_length=str(self.answer_length)+"ch", hint=self.hint)

    def test_html_answer_form_tag(self):
        self.assertEquals(str(self.blank_form),'<tr><th></th><td><input type="text" name="answer" id="answer" style="height: 28px; font-size: 22px; " size="10ch" maxlength="10" title="Do again and again &lt;adv&gt;" onblur="checkAnswer()" required></td></tr>')

