from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.models import Question, Topic


class QuestionModelTest(TestCase):

    def setUp(self):
        self.question = "Did the Main Character Dies?"
        self.title = "Spoil Hello World"
        self.difficulty = "Hardcore"
        self.topic_object = Topic(topic_name="Hello World")
        self.question_object = Question(topic=self.topic_object, 
                                        question_text=self.question, 
                                        question_title=self.title, 
                                        difficulty=self.difficulty)
    
    def test_question_object(self):
        self.assertTrue(self.question_object)
        self.assertEquals(str(self.question_object),self.title)
        self.assertEquals(self.question_object.question_title,self.title)
        self.assertEquals(self.question_object.question_text,self.question)
        self.assertEquals(self.question_object.difficulty,self.difficulty)
        self.assertEquals(self.question_object.topic,self.topic_object)
