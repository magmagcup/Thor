from django.test import TestCase, Client
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic, Answer, Best_score, Statistic
from game.views import *

def get_best_score(topic_id, user_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    get_user = User.objects.get(pk=user_id)
    check_key = Best_score.objects.filter(key=topic.topic_name, user=user_id)
    if not check_key:
        s = Best_score(user=get_user, key=topic.topic_name, value=0)
        s.save()
        return True
    return False

def edit_form(question_id):
    check_key = Question.objects.filter(pk=question_id)
    if check_key:
        question = Question.objects.get(pk=question_id)
        topic = Topic.objects.get(pk=question.topic_id)
        form = QuestionForm(instance=question)
        question.delete()
        return True, form
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
        self.question = Question.objects.create(
            topic=self.topic, question_title='Hello',question_text="[[world|world]]", difficulty="Easy")
    
    def test_get_stat(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/stat/', data={'user_id':1}, follow=True)
        status = response.status_code
        self.assertEquals(status, 200)

        stat = Statistic.objects.create(user=self.user)
        self.assertTrue(self.check)

        self.assertEqual(stat.user.username, self.username)
        self.assertTrue(stat.user.password)
        self.assertTemplateUsed(response, 'game/base.html')
    
    def test_discard_form(self):
        get_question = Question.objects.get(pk=self.question.id)
        self.client.force_login(self.user)

        response = self.client.get(path=f'game/{get_question.id}', data={'question_id':get_question.id}, follow=True)
        status = response.status_code
        self.assertEquals(status, 200)
    
    def test_preview_form(self):
        self.client.force_login(self.user)
        get_question = Question.objects.get(pk=self.question.id)
        response = self.client.post(path=f'game/preview/', 
                                data={
                                    'topic':1, 
                                    'difficulty':"Easy",
                                    'title':"Hello", 
                                    'question':"[[Hello|]]"}, 
                                    follow=True)
        status = response.status_code
        self.assertEquals(status, 200)
    
    def test_receive_score(self):
        self.client.force_login(self.user)
        response = self.client.post(path=f'game/recieve/{self.topic.id}', 
                                    data={
                                    'topic':self.topic.id,
                                    'user_id':1,
                                    'score':100,},
                                    follow=True)
        status = response.status_code
        self.assertEquals(status, 200)
    
    def test_get_best_score(self):
        status = get_best_score(self.topic.id, self.user.id)
        self.assertTrue(status)
        Best_score.objects.create(user=self.user, key=self.topic.topic_name, value=0)
        status = get_best_score(self.topic.id, self.user.id)
        self.assertFalse(status)
    
    def test_edit_form(self):
        status = edit_form(self.question.id)
        self.assertTrue('<class "game.forms.QuestionForm">', type(status[1]))
        self.assertTrue(status)
        status = edit_form(self.question.id)
        self.assertFalse(status)
    
    def test_question_page(self):
        self.client.force_login(self.user)
        resources = question_page_resources(self.topic.id)
        response = self.client.post(path=f'game/{self.topic.id}',
                                    data={
                                        'q_title': resources["title"], 
                                        'q_text': resources["text"],
                                        'answer': resources["answer"], 
                                        'hint': resources["hint"],
                                        'q_diff': resources["diff"], 
                                        'topic_id': self.topic.id},
                                    follow=True)
        status = response.status_code
        self.assertEquals(status, 200)
    
    def test_answer_box(self):
        value = 'hello [[world|ruri]], python'
        boxed = create_answer_box(value)
        expect = 'hello <tr><th></th><td><input type="text" name="answer" id="answer" style="height: 28px; font-size: 22px; " size="5ch" maxlength="5" title="ruri" onblur="checkAnswer()" required></td></tr>, python'
        self.assertEqual(boxed, expect)
