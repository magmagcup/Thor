from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .models import Question, Statistic, Topic, Best_score
# Create your views here.

def index(request):
    """redirect players to the homepage index"""
    return HttpResponseRedirect(reverse("game:index"))

def form_page(request):
    return render(request, 'game/form.html')

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
    return render(request, 'game/topic.html', {'topic': topic})


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

def get_best_score(request, topic_id):
    user_id = request.user.id
    topic = get_object_or_404(Topic, pk=topic_id)
    get_user = User.objects.get(pk=user_id)
    score_id = Statistic()
    check_key = Best_score.objects.filter(key=topic.topic_name, user=user_id)
    if check_key:
        s = Best_score.objects.get(key=topic.topic_name, user=user_id)
        if score_id.score > s.value:
            s.value += 1
            s.save()
        return redirect('game:home')
    s = Best_score(user=get_user, key=topic.topic_name, value=0)
    s.save()
    return redirect('game:home')

def cal_score_each_round(request):
    return 0


def get(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            title = form.data.get('title')
            question = form.data.get('question')
            answer = form.data.get('answer')
            hint = form.data.get('hint')
            q = Question(question_title=title, question_text=question, question_answer=answer, answer_hint=hint)
            q.save()
            return redirect("game:home")

        else:
            form = QuestionForm()
    context = {'form': form}
    return render(request, 'game/home.html', context)