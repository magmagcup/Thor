from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .models import Question, Statistic, Topic, Answer
# Create your views here.

def index(request):
    #redirect players to the homepage index
    return HttpResponseRedirect(reverse("game:index"))

def form_page(request):
    form = QuestionForm()
    context = {'form': form}
    return render(request, 'game/form.html', context)

def page404(request, exception):
    return render(request, 'game/404.html')

def views_logout(request):
    logout(request)
    return redirect("game:home")

def home_page(request):
    return render(request, 'game/home.html')

def statistic_page(request):
    statistic = Statistic.objects.all()
    return render(request, 'game/statistic.html', {'stat':statistic})


def topic_page(request):
    topic = Topic.objects.all()
    return render(request, 'game/topic.html', {'topic':topic})

def question_page(request, topic_id):
    question = Question.objects.filter(topic_id=topic_id)
    return render(request, 'game/game.html', {'question':question})


@login_required
def get_stat(request):
    """Create statistic for each player include score"""
    user_id = request.user.id
    status = True
    check_id = Statistic.objects.filter(user_id=user_id)
    for check in check_id:
        print("check.id =  ", check)
        if check.user_id == user_id:
            status = False
    if User.is_authenticated and status == True:
        user = User.objects.get(pk=user_id)
        stat = Statistic(user=user)
        stat.save()
    return redirect('game:home')

def preview_form(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            topic = Topic.objects.get(topic_name=form.data.get('select_topic'))
            title = form.data.get('title')
            question = form.data.get('question')
            difficulty = form.data.get('select_difficulty')
            q = Question(topic_id=topic.id, question_title=title, question_text=question, difficulty=difficulty)
            q.save()
            assign_answer(question, q.id)
            return render(request, "game/preview_form.html", {'question':q})

def discard_form(request, question_id):
    check = Question.objects.filter(pk=question_id)
    if check:
        q = Question.objects.get(pk=question_id)
        q.delete()
        return redirect("game:form")
    else:
        return preview_form(request.POST)

def assign_answer(value,question_id):
    last_box_mark = 0
    while (']]' in value):
        start = value.find('[[', last_box_mark)
        if start < last_box_mark:
            break
        mid = value.find('|', last_box_mark)
        end = value.find(']]', last_box_mark)
        a = Answer(question_id=question_id, answer_text=value[start+2:mid], hint_text=value[mid+1:end])
        a.save()
        last_box_mark = end + 1

def get_topic(request):
    object_topic = Topic.objects.all()
    select_topic = [tuple([t,t]) for t in get_topic()]
    return select_topic
