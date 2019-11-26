from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question, Statistic, Topic, Answer
from random import sample

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

def question_difficulty(value, topic_id, difficulty):
    return [q for q in value.objects.filter(topic_id=topic_id, difficulty=difficulty)]

def random_question_list(value, topic_id):
    easy = sample(question_difficulty(value, topic_id, 'easy'), 3)
    normal = sample(question_difficulty(value, topic_id, 'normal'), 3)
    hard = sample(question_difficulty(value, topic_id, 'hard'), 3)
    extreme = sample(question_difficulty(value, topic_id, 'extreme'), 1)
    return easy + normal + hard + extreme

def question_page(request, topic_id):
    question = random_question_list(Question, topic_id)
    q_title = [q.question_title for q in question]
    q_text = [q.question_text for q in question]
    ans,hint = [], []
    for q in question:
        answer_set = list(Answer.objects.filter(question_id=q.id, topic_id=topic_id))
        ans.append([a.answer_text for a in answer_set])
        hint.append([a.hint_text for a in answer_set])
    return render(request, 'game/game.html', {'q_title':q_title, 'q_text':q_text, 'answer':ans, 'hint':hint})

def create_answer_box(value):
    while (']]' in value):
        start = value.find('[[')
        mid = value.find('|')
        end = value.find(']]')
        ans_length = mid - start - 2
        box_length = ans_length
        if box_length < 1:
            box_length = 1
        hint = value[mid+1:end]
        replacement = str(AnswerForm(ans_length=ans_length,
                                     box_length=str(box_length)+"ch", hint=hint))
        value = value[:start] + replacement + value[end+2:]
    return value


def assign_answer(value, question_id, topic_id):
    last_box_mark = 0
    while (']]' in value):
        start = value.find('[[', last_box_mark)
        if start < last_box_mark:
            break
        mid = value.find('|', last_box_mark)
        end = value.find(']]', last_box_mark)
        a = Answer(question_id=question_id, topic_id=topic_id,
                   answer_text=value[start+2:mid], hint_text=value[mid+1:end])
        a.save()
        last_box_mark = end + 1

@login_required
def get_stat(request):
    """Create statistic for each player include score"""
    user_id = request.user.id
    status = True
    check_id = Statistic.objects.filter(user_id=user_id)
    if check_id:
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
            topic = Topic.objects.get(topic_name=form.data.get('topic'))
            title = form.data.get('title')
            raw_question = form.data.get('question')
            question = create_answer_box(raw_question)
            difficulty = form.data.get('difficulty')
            q = Question(topic_id=topic.id, question_title=title, question_text=question, difficulty=difficulty)
            q.save()
            assign_answer(raw_question, q.id, topic.id)
            return render(request, "game/preview_form.html", {'question':q})

def discard_form(request, question_id):
    check = Question.objects.filter(pk=question_id)
    if check:
        q = Question.objects.get(pk=question_id)
        q.delete()
        return redirect("game:form")
    else:
        return preview_form(request.POST)

def receive_score(request):
    user_id = request.user.id
    score = request.GET.get('result_score')
    profile = Statistic.objects.get(user=user_id)
    if int(profile.best_score) < int(score):
        profile.best_score = int(score)
        profile.save()
    return render(request, "game/home.html")
