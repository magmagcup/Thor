from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from game.forms import QuestionForm, AnswerForm
from game.models import Question, Answer, Topic