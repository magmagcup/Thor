from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import QuestionForm
from .models import Question
# Create your views here.

def index(request):
    #redirect players to the homepage index
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
            return redirect("game:form")
        
        else:
            form = QuestionForm()
    context = {'form': form, 'text': text}
    return render(request, 'form.html', context)
