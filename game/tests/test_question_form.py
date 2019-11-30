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
        self.question = "Binary Search: Search a sorted array by [[repeatedly|Do again and again <adv>)]]"
        self.title = "Binary Search"
        self.difficulty = "easy"
        self.topic = "Algorithm"
        self.form = QuestionForm()
        self.post_form = QuestionForm({
                            'topic':self.topic, 
                            'difficulty':self.difficulty, 
                            'title':self.title, 
                            'question':self.question
                        })
        self.html_tag_question_form = '<tr><th><label for="id_topic">Topic:</label></th><td><select name="topic" id="id_topic">\n  <option value="Naval History of WWII">Naval History of WWII</option>\n\n  <option value="Algorithm">Algorithm</option>\n\n  <option value="1">1</option>\n\n</select></td></tr>\n<tr><th><label for="id_difficulty">Difficulty:</label></th><td><select name="difficulty" id="id_difficulty">\n  <option value="easy">Easy</option>\n\n  <option value="normal">Normal</option>\n\n  <option value="hard">Hard</option>\n\n  <option value="extreme">Extreme</option>\n\n</select></td></tr>\n<tr><th><label for="title">Title</br>:</label></th><td><textarea name="title" cols="40" rows="10" id="title" style="height: 50px; font-size: 22px" class="mt-5" maxlength="100000" required>\n</textarea></td></tr>\n<tr><th><label for="question">Question</br>:</label></th><td><textarea name="question" cols="40" rows="10" id="question" style="height: 400px; font-size: 22px" class="mt-5" maxlength="100000" required>\n</textarea></td></tr>'

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

    def test_valid_form(self):
        self.assertTrue(self.post_form.is_valid())

    def test_invalid_form(self):
        self.assertTrue(self.post_form.is_valid())
        self.assertFalse(self.form.is_valid())
        self.assertFalse(QuestionForm({'topic':self.topic,}).is_valid())
    
    def test_question_form_tag_html(self):
        self.assertTrue(self.form)
        self.assertTrue(self.post_form)
        self.assertEquals(str(self.form),self.html_tag_question_form)